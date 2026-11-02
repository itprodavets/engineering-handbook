# Q-073 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-073-remote-timeout-not-rollback.md) · [English](./Q-073-remote-timeout-not-rollback.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-073) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-072-outbox-not-charge-idempotency.md) · [Next →](Q-074-postgres-read-committed-check-act.md)

## Question

Does gRPC DeadlineExceeded or local CancellationToken roll back an already committed payment?

<details>
<summary>Model answer — reveal after your attempt</summary>

No. The remote side effect may have committed before network failure; use status APIs/webhooks and reconciliation.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[Русский](../Q-073-remote-timeout-not-rollback.md) · [English](./Q-073-remote-timeout-not-rollback.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-073) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-072-outbox-not-charge-idempotency.md) · [Next →](Q-074-postgres-read-committed-check-act.md)
