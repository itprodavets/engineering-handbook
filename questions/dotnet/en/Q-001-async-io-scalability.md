# Q-001 — The async/await execution lifecycle

[Русский](../Q-001-async-io-scalability.md) · [English](./Q-001-async-io-scalability.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-001) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [Next →](Q-002-thread-id-after-await.md)

## Question

Why does ToListAsync() scale better than Task.Run(() => ToList()) under 1,000 concurrent HTTP requests?

<details>
<summary>Model answer — reveal after your attempt</summary>

ToListAsync() uses asynchronous I/O: when data is not ready, await suspends the method and releases the worker. Task.Run() queues synchronous I/O onto the ThreadPool, keeping a worker blocked and increasing the risk of thread pool starvation.

</details>

---

[Русский](../Q-001-async-io-scalability.md) · [English](./Q-001-async-io-scalability.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-001) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [Next →](Q-002-thread-id-after-await.md)
