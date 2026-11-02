# Q-072 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-072-outbox-not-charge-idempotency.md) · [English](./Q-072-outbox-not-charge-idempotency.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-072) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-071-payment-timeout-duplicate-charge.md) · [Next →](Q-073-remote-timeout-not-rollback.md)

## Question

Why does Transactional Outbox not replace payment-provider idempotency?

<details>
<summary>Model answer — reveal after your attempt</summary>

Outbox atomically saves event and local state, but relay may deliver duplicates; consumers/providers must deduplicate.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)

---

[Русский](../Q-072-outbox-not-charge-idempotency.md) · [English](./Q-072-outbox-not-charge-idempotency.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-072) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-071-payment-timeout-duplicate-charge.md) · [Next →](Q-073-remote-timeout-not-rollback.md)
