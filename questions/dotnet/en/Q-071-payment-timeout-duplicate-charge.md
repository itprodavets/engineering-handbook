# Q-071 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-071-payment-timeout-duplicate-charge.md) · [English](./Q-071-payment-timeout-duplicate-charge.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-071) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-070-three-pods-provider-quota.md) · [Next →](Q-072-outbox-not-charge-idempotency.md)

## Question

Can retrying ChargeAsync after a lost bank reply charge twice?

<details>
<summary>Model answer — reveal after your attempt</summary>

Yes. Timeout does not prove rollback; retry the same logical attempt with a stable provider-enforced idempotency key and reconciliation.

</details>

### Documentation and source

[https://stripe.com/blog/idempotency](https://stripe.com/blog/idempotency)

---

[Русский](../Q-071-payment-timeout-duplicate-charge.md) · [English](./Q-071-payment-timeout-duplicate-charge.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-071) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-070-three-pods-provider-quota.md) · [Next →](Q-072-outbox-not-charge-idempotency.md)
