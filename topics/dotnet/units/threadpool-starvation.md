# ThreadPool starvation и блокирующие ожидания

[Русский](threadpool-starvation.md) · [English](en/threadpool-starvation.md)

[Главная](../../../README.md) · [Модуль](../threadpool-scheduling.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/threadpool-starvation)

> Объяснять, какие workers заняты и почему растёт очередь.

## Определение

ThreadPool starvation — задержка готовых work items из-за нехватки доступных workers. Блокирующий Thread.Sleep занимает один worker на каждую исполняемую задачу; Task.Delay не резервирует worker для ожидания таймера.

## Внутренний механизм

1. Task.Run(() => Thread.Sleep(...)) добавляет делегат в очередь ThreadPool.
2. Когда worker выполняет Sleep, он заблокирован, хотя не расходует CPU на вычисления.
3. Пул может создать дополнительные ОС-потоки, но их точное число и скорость роста зависят от реализации и условий.
4. Отслеживай dotnet.thread_pool.thread.count и queue.length; низкий CPU при большой очереди — полезный сигнал.

## Потребляемые ресурсы

Task.Delay: timer registration и Task; Thread.Sleep: занятый worker stack и очередь ожидающих делегатов.

## Ошибки и ограничения

Не обещай фиксированное количество OS threads или байтов аллокаций без измерения на конкретном runtime.

## Пример

```csharp
await Task.Delay(5000); // timer, no blocked worker
await Task.Run(() => Thread.Sleep(5000)); // blocked worker
```

## Вопросы для закрепления

- [Q-009: Что произойдёт с ThreadPool, если одновременно запустить 10 000 Task.Delay(5000) и 10 000 Task.Run(() => Thread.Sleep(5000))?](../../../questions/dotnet/Q-009-task-delay-vs-thread-sleep.md)
- [Q-011: Что означает «ThreadPool может создать дополнительный поток» при вызове Task.Run и почему это не означает 10 000 потоков для 10 000 Task?](../../../questions/dotnet/Q-011-threadpool-worker-creation.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[← Назад](os-vs-runtime-scheduler.md) · [Русский](threadpool-starvation.md) · [English](en/threadpool-starvation.md)
