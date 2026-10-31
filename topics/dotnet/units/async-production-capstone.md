# Production-разбор: p99 latency и ThreadPool starvation

[Русский](async-production-capstone.md) · [English](en/async-production-capstone.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-production-capstone)

> Научиться подтверждать причину задержек и проектировать исправление.

## Определение

Высокая latency при низком CPU — симптом, а не диагноз. Причиной могут быть sync-over-async, очередь ThreadPool, ограничение пула DB-соединений, медленные SQL, сетевые таймауты или downstream backpressure.

## Внутренний механизм

1. Сформулируй гипотезы: ThreadPool, DB pool, SQL duration, network, lock contention.
2. Собери metrics: p50/p95/p99, pool threads, pending work items, CPU time, DB connections, rates/errors.
3. Используй dotnet-stack/dotnet-trace, чтобы найти занятые workers и sync-over-async stacks.
4. Исправь причину, установи bounded concurrency, timeout/cancellation, проверь нагрузочным тестом.

## Последовательное объяснение

### Шаг 1: конкурирующие гипотезы

Сценарий: 1 000 HTTP-запросов одновременно, CPU=20%, p99=12 секунд, количество worker threads растёт. Это совместимо с ThreadPool starvation, но также с блокировками на уровне DB pool. Если ThreadPool queue.length растёт и stack traces показывают `Task.Wait`/`.Result` — появляются доказательства sync-over-async. Если очередь пула стабильна, а DB pool waits растут — основной предел, вероятно, БД.

### Шаг 2: измерение без угадывания

Смотри `dotnet.thread_pool.thread.count` (сколько threads существует), `dotnet.thread_pool.queue.length` (сколько work items ждёт), CPU time, количество активных DB-соединений, HTTP latency p99. Ни одна метрика отдельно не даёт полный диагноз. Команда `dnx dotnet-counters monitor -p <PID>` доступна в .NET 10; не запускай сбор в production без понимания накладных расходов.

### Шаг 3: исправление и компромиссы

Убери `.Result`/`.Wait()` из async code path, не оборачивай синхронный I/O в Task.Run. Ограничь одновременную работу с БД через async SemaphoreSlim/Channel, но помни: ограничение на уровне каждого инстанса не равно глобальному. Примени projection, pagination и CancellationToken. Увеличение ThreadPool min threads может замаскировать симптом, но не исправляет корневой блокирующий код.

### Шаг 4: доказательство исправления

Проведи одинаковый load test до и после: throughput, latency distributions, errors, thread count, queue length, DB pool occupancy и CPU. Укажи версии .NET, количество CPU и pool limits; не делай вывод из одного разового прогона. Если рецидивы краткие, собери trace со stack samples.


## Потребляемые ресурсы

ThreadPool workers/queues, DB connection pool, network sockets, memory, CPU, retries; только измеренный контекст позволяет оценить пределы.

## Ошибки и ограничения

Нельзя делать вывод «ThreadPool starvation» только по CPU=20%. Ограничение пула подключений может выглядеть похоже; замена на Task.Run часто ухудшает ситуацию.

## Пример

```csharp
await semaphore.WaitAsync(ct);
try { return await db.Orders.AsNoTracking().Take(100).ToListAsync(ct); }
finally { semaphore.Release(); }
```

## Запускаемые эксперименты

- [05-queue-diagnostics.cs](../../../labs/dotnet/async-internals/05-queue-diagnostics.cs) — `dotnet run --file labs/dotnet/async-internals/05-queue-diagnostics.cs`

## Вопросы для закрепления


## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Назови два основных наблюдаемых признака возможного ThreadPool starvation.

<details>
<summary>Критерии ответа</summary>

Рост thread count/queue length вместе с задержками и возможно низким CPU; это признаки, не доказательство.

</details>

### 2. Explain

Почему .Result блокирует worker, даже если внутри выполняется асинхронное I/O?

<details>
<summary>Критерии ответа</summary>

Синхронное ожидание удерживает вызывающий поток до завершения Task, которая может ждать I/O и continuation.

</details>

### 3. Predict

Что произойдёт при Task.Run(() => DbQueryAsync().Result) под нагрузкой?

<details>
<summary>Критерии ответа</summary>

Worker блокируется на .Result, очередь/число workers могут расти; это не делает I/O неблокирующим.

</details>

### 4. Diagnose

CPU=20%, p99 растёт, ThreadPool queue=0, но DB pool waits растут. Куда смотреть сначала?

<details>
<summary>Критерии ответа</summary>

Пул соединений/длительность SQL и downstream DB, при этом проверить другие данные; CPU alone не диагноз.

</details>

### 5. Design

Предложи исправление для 1 000 запросов с 100 DB connections и объясни компромиссы bounded concurrency.

<details>
<summary>Критерии ответа</summary>

Async end-to-end, pagination, max concurrency ниже/равно лимита на нужном уровне, backpressure, timeouts, cancellation; следить за очередями и p99.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)
- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime)

---

[← Назад](async-memory-and-allocations.md) · [Далее →](async-before-await.md) · [Русский](async-production-capstone.md) · [English](en/async-production-capstone.md)
