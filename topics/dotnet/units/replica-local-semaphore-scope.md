# SemaphoreSlim локален для Pod, а остаток общий

[Русский](replica-local-semaphore-scope.md) · [English](en/replica-local-semaphore-scope.md)

[Главная](../../../README.md) · [Модуль](../microservices-concurrency.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/replica-local-semaphore-scope)

> Объяснять область действия static и причину гонок между репликами.

## Определение

Три Kubernetes Pod имеют три независимые копии static SemaphoreSlim(1,1): три checkout-запроса могут одновременно пройти локальные gates. Общий инвариант остатка нужно атомарно защищать в InventoryService/PostgreSQL, а не в OrderService.

## Внутренний механизм

1. Каждый Pod имеет отдельный процесс CLR и собственные static поля.
2. Все три Gate могут независимо перейти 1→0 при WaitAsync.
3. Все три Checkout могут одновременно вызвать общий InventoryService.ReserveAsync.
4. Только владелец общего состояния может защитить SKU атомарным SQL и идемпотентностью брони.

## Последовательное объяснение

### Три Pod — три разрешения

В Pod A, B, C каждый `static Gate` существует в отдельном адресном пространстве. Три вызова могут независимо войти в критическую секцию и одновременно вызвать ReserveAsync. Q-068 воспроизводит независимые Gate в одном процессе; это демонстрация области действия, а не настоящий Kubernetes/сетевой тест.

### Инвариант на стороне InventoryService

Именно InventoryService/PostgreSQL владеет `available` и должен атомарно решить, кому достался последний товар. Локальный SemaphoreSlim можно оставить для ограничения нагрузки на один экземпляр, но он не координирует реплики и не обеспечивает exactly-once бронирование.

### Почему Redis lock не автоматически безопаснее

Аренда распределённого lock может истечь при паузе, network partition или длительной операции. Старый владелец иногда продолжает работать после получения lock новым участником; поэтому необходимы атомарные проверки на стороне данных и при необходимости fencing tokens.


## Потребляемые ресурсы

Три локальных счётчика, ThreadPool и Task state; общая строка PostgreSQL и её транзакции.

## Ошибки и ограничения

Слово static не делает объект cluster-global. Redis lease lock тоже имеет срок действия/fencing риски и не заменяет атомарный бизнес-предикат.

## Пример

```csharp
private static readonly SemaphoreSlim Gate = new(1, 1); // one per process
```

## Запускаемые эксперименты

- [Q-068.cs](../../../labs/dotnet/Q-068.cs) — `dotnet run --file labs/dotnet/Q-068.cs`

## Вопросы для закрепления

- [Q-068: Защитит ли static SemaphoreSlim(1,1) последний SKU от трёх Pod?](../../../questions/dotnet/Q-068-static-semaphore-three-pods.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Сколько static SemaphoreSlim в трёх Pod?

<details>
<summary>Критерии ответа</summary>

Три, каждый process-local.

</details>

### 2. Explain

Почему три запроса могут одновременно вызвать ReserveAsync?

<details>
<summary>Критерии ответа</summary>

Разрешения независимы, общего Gate нет.

</details>

### 3. Predict

Защищает ли Gate(1,1) внутри OrderService последний SKU?

<details>
<summary>Критерии ответа</summary>

Нет, только локальный Pod.

</details>

### 4. Diagnose

Почему oversell возник после scale-out?

<details>
<summary>Критерии ответа</summary>

Проверять local locks, SQL check-then-act и дубли.

</details>

### 5. Design

Где расположить глобальную проверку остатка?

<details>
<summary>Критерии ответа</summary>

InventoryService/PostgreSQL conditional update + business idempotency.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
- [https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)

---

[Далее →](remote-io-permit-lifetime.md) · [Русский](replica-local-semaphore-scope.md) · [English](en/replica-local-semaphore-scope.md)
