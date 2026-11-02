# Асинхронный сетевой await удерживает permit, но не worker

[Русский](remote-io-permit-lifetime.md) · [English](en/remote-io-permit-lifetime.md)

[Главная](../../../README.md) · [Модуль](../microservices-concurrency.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/remote-io-permit-lifetime)

> Разделять удержание семафора, Task, socket и физический поток.

## Определение

После Gate.WaitAsync() permit остаётся занятым до Release даже в течение пяти секунд внешнего HTTPS/gRPC await. Истинно асинхронное pending I/O не удерживает отдельный заблокированный worker, но сохраняет Task, permit, сетевые ресурсы и очередь следующих Checkout.

## Внутренний механизм

1. Gate.WaitAsync приобретает permit и уменьшает CurrentCount.
2. ChargeAsync запускает сетевой I/O; при незавершённом await метод приостанавливается.
3. Worker может выполнять другую работу, permit остаётся занятым до Release.
4. Следующий Checkout того же Pod ждёт WaitAsync; другой Pod независим.
5. Лимиты concurrency должны соответствовать downstream, учитывать timeout/backpressure и суммарные реплики.

## Последовательное объяснение

### Await может освободить worker, но не permit

Пятсекундный pending await внешнего API не означает пять секунд CPU time на ASP.NET Core. Однако CurrentCount у Gate остаётся нулевым, пока не отработает finally. В лаборатории Q-069 незавершённый TaskCompletionSource моделирует сетевое ожидание и демонстрирует удержание permit без настоящей сети.

### Локальные квоты суммируются

Три Pod с SemaphoreSlim(5,5) могут вместе отправить 15 вызовов провайдеру. Глобальная квота требует согласованной координации или очереди. Внутренняя gRPC сеть и внешний HTTPS имеют разные задержки и ограничения, но обе подвержены timeout и частичным сбоям.

### Изолируй лимит по downstream

Общий gate вокруг ReserveAsync+ChargeAsync сериализует весь checkout одного Pod, даже если узким местом является только внешний провайдер. Узкий bounded concurrency limiter на конкретном downstream, CancellationToken, таймауты и метрики очереди лучше описывают нагрузку.


## Потребляемые ресурсы

Semaphore permit, pending Task, continuation, connection pools и сетевые буферы. CPU не занят постоянно во время истинного pending I/O.

## Ошибки и ограничения

Task.Run над синхронным сетевым I/O удерживает worker. Большая критическая секция создаёт очередь и растущий p99 даже при низком CPU; локальный лимит не является глобальной квотой.

## Пример

```csharp
await Gate.WaitAsync(ct);
try { await payments.ChargeAsync(orderId, ct); }
finally { Gate.Release(); }
```

## Запускаемые эксперименты

- [Q-069.cs](../../../labs/dotnet/Q-069.cs) — `dotnet run --file labs/dotnet/Q-069.cs`

## Вопросы для закрепления

- [Q-069: Что удерживает CheckoutAsync во время 5-секундного await ChargeAsync: worker или permit?](../../../questions/dotnet/Q-069-network-await-permit-lifetime.md)
- [Q-070: Сколько одновременно запросов к payment provider при 3 Pod × SemaphoreSlim(5,5)?](../../../questions/dotnet/Q-070-three-pods-provider-quota.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Что удерживается при async ChargeAsync?

<details>
<summary>Критерии ответа</summary>

Permit, Task и сетевое состояние; worker не обязан блокироваться.

</details>

### 2. Explain

Почему при низком CPU может расти очередь Checkout?

<details>
<summary>Критерии ответа</summary>

Permit держится во время внешнего I/O; следующие операции ожидают.

</details>

### 3. Predict

Сколько вызовов при 3 Pod × Gate(5,5)?

<details>
<summary>Критерии ответа</summary>

До 15.

</details>

### 4. Diagnose

Как найти bottleneck при высоком p99 и пустом CurrentCount?

<details>
<summary>Критерии ответа</summary>

Очередь WaitAsync, latency provider, пула соединений и retries.

</details>

### 5. Design

Где ограничить платёжный API?

<details>
<summary>Критерии ответа</summary>

У клиента конкретного downstream; для глобальной квоты отдельная координация.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)
- [https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[← Назад](replica-local-semaphore-scope.md) · [Далее →](payment-timeout-idempotency-outbox.md) · [Русский](remote-io-permit-lifetime.md) · [English](en/remote-io-permit-lifetime.md)
