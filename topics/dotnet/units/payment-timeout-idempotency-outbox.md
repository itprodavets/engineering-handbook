# Потерянный ответ платежа: Outbox и идемпотентность

[Русский](payment-timeout-idempotency-outbox.md) · [English](en/payment-timeout-idempotency-outbox.md)

[Главная](../../../README.md) · [Модуль](../microservices-concurrency.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/payment-timeout-idempotency-outbox)

> Объяснять частичные отказы и защищать финансовые операции от повторов.

## Определение

Timeout после ChargeAsync не доказывает отката: удалённый банк мог списать деньги до потери ответа. Повтор с новым ключом может списать ещё раз. Стабильный idempotency key должен обрабатываться на стороне провайдера. Transactional Outbox обеспечивает локальную атомарность состояния+события, но допускает повторную доставку.

## Внутренний механизм

1. OrderService посылает ChargeAsync внешнему провайдеру.
2. Провайдер делает списание, но ответ теряется по сети.
3. Timeout оставляет outcome неизвестным; CancellationToken не отменяет уже выполненный удалённый эффект.
4. Повторы одной логической попытки используют тот же сохранённый idempotency key.
5. Outbox записывает локальный факт и событие в одной транзакции, relay может отправить его повторно, потребитель обязан дедуплицировать.
6. Неизвестный результат нужно сверять через provider status API/webhook и журнал попыток.

## Последовательное объяснение

### Списание совершено, но ответ не дошёл

Transport timeout сигнализирует о неудаче получения ответа, а не об откате платежа. Провайдер мог завершить side effect. Локальный CancellationToken не способен атомарно откатить удалённую транзакцию. Храни paymentAttemptId, состояния Unknown/Pending/Succeeded/Failed и сверяй результат, а не запускай новый независимый charge.

### Один платёж — один стабильный ключ для повторов

Создай идентификатор для одной логической попытки и храни его устойчиво. При сетевых повторах передавай тот же key и те же параметры. Принимающая сторона должна атомарно дедуплицировать. Лаборатория Q-071 — последовательная in-memory симуляция; она не демонстрирует сетевую или межпроцессную дедупликацию банка.

### Outbox гарантирует сохранение события, не уникальность платежа

Transactional Outbox сохраняет изменение локального Order и запись outbox в одной транзакции. Relay может опубликовать событие, упасть до отметки delivered и опубликовать его повторно. Для PaymentRequested требуется inbox/deduplication, а для внешнего платежа — provider idempotency key и reconciliation.


## Потребляемые ресурсы

Внешние соединения, идемпотентные ключи, payment attempt ID, outbox/inbox таблицы и доставка событий.

## Ошибки и ограничения

Локальный SemaphoreSlim не сохраняет состояние после рестарта и не координирует Pod. Outbox не гарантирует exactly once у платёжного API; semantics и TTL ключа зависят от контракта провайдера.

## Пример

```csharp
await provider.ChargeAsync(orderId, amount, stableIdempotencyKey, ct);
```

## Запускаемые эксперименты

- [Q-071.cs](../../../labs/dotnet/Q-071.cs) — `dotnet run --file labs/dotnet/Q-071.cs`

## Вопросы для закрепления

- [Q-071: Может ли при потерянном ответе банка повторный ChargeAsync списать деньги дважды?](../../../questions/dotnet/Q-071-payment-timeout-duplicate-charge.md)
- [Q-072: Почему Transactional Outbox не заменяет идемпотентность платежного провайдера?](../../../questions/dotnet/Q-072-outbox-not-charge-idempotency.md)
- [Q-073: Означает ли gRPC DeadlineExceeded или локальный CancellationToken откат успешно списанного платежа?](../../../questions/dotnet/Q-073-remote-timeout-not-rollback.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Почему timeout не доказывает, что банк не списал деньги?

<details>
<summary>Критерии ответа</summary>

Ответ может потеряться после успешного списания.

</details>

### 2. Explain

Чем Outbox отличается от provider idempotency key?

<details>
<summary>Критерии ответа</summary>

Outbox — локальная атомарность события и state; ключ — дедуп удалённого side effect.

</details>

### 3. Predict

Может ли повтор с новым ключом привести к двум списаниям?

<details>
<summary>Критерии ответа</summary>

Да, при неопределённом результате исходного платежа.

</details>

### 4. Diagnose

Как установить факт платежа после timeout?

<details>
<summary>Критерии ответа</summary>

Payment attempt ID, provider status API/webhook, telemetry, audit.

</details>

### 5. Design

Как спроектировать Order→Payment при повторной доставке Outbox?

<details>
<summary>Критерии ответа</summary>

Outbox+Inbox, стабильный provider key, сохранение попыток, reconciliation.

</details>


## Источники

- [https://stripe.com/blog/idempotency](https://stripe.com/blog/idempotency)
- [https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
- [https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[← Назад](remote-io-permit-lifetime.md) · [Далее →](postgres-read-committed-stock.md) · [Русский](payment-timeout-idempotency-outbox.md) · [English](en/payment-timeout-idempotency-outbox.md)
