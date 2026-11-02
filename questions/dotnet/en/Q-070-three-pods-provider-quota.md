# Q-070 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-070-three-pods-provider-quota.md) · [English](./Q-070-three-pods-provider-quota.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-070) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-069-network-await-permit-lifetime.md) · [Next →](Q-071-payment-timeout-duplicate-charge.md)

## Question

How many concurrent payment calls with three Pods each using SemaphoreSlim(5,5)?

<details>
<summary>Model answer — reveal after your attempt</summary>

Up to 15: each concurrency limit is local to its Pod.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

---

[Русский](../Q-070-three-pods-provider-quota.md) · [English](./Q-070-three-pods-provider-quota.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-070) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-069-network-await-permit-lifetime.md) · [Next →](Q-071-payment-timeout-duplicate-charge.md)
