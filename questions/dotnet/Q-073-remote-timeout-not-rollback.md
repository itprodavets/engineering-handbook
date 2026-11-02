# Q-073 — Remote partial failure

[Русский](./Q-073-remote-timeout-not-rollback.md) · [English](en/Q-073-remote-timeout-not-rollback.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-073) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-072-outbox-not-charge-idempotency.md) · [Следующий →](Q-074-postgres-read-committed-check-act.md)

## Вопрос

Означает ли gRPC DeadlineExceeded или локальный CancellationToken откат успешно списанного платежа?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. Удалённый side effect мог состояться до сетевого сбоя; нужен status API/webhook и reconciliation.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[Русский](./Q-073-remote-timeout-not-rollback.md) · [English](en/Q-073-remote-timeout-not-rollback.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-073) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-072-outbox-not-charge-idempotency.md) · [Следующий →](Q-074-postgres-read-committed-check-act.md)
