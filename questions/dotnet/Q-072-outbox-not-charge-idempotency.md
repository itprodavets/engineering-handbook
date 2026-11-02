# Q-072 — Outbox vs idempotency

[Русский](./Q-072-outbox-not-charge-idempotency.md) · [English](en/Q-072-outbox-not-charge-idempotency.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-072) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-071-payment-timeout-duplicate-charge.md) · [Следующий →](Q-073-remote-timeout-not-rollback.md)

## Вопрос

Почему Transactional Outbox не заменяет идемпотентность платежного провайдера?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Outbox атомарно сохраняет событие с локальным состоянием, но relay допускает повторы; consumer/provider должны дедуплицировать.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)

---

[Русский](./Q-072-outbox-not-charge-idempotency.md) · [English](en/Q-072-outbox-not-charge-idempotency.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-072) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-071-payment-timeout-duplicate-charge.md) · [Следующий →](Q-073-remote-timeout-not-rollback.md)
