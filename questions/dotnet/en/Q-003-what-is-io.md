# Q-003 — The async/await execution lifecycle

[Русский](../Q-003-what-is-io.md) · [English](./Q-003-what-is-io.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-003) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-002-thread-id-after-await.md) · [Next →](Q-004-async-postgres-pipeline.md)

## Question

What does I/O stand for, and what kind of I/O occurs when querying PostgreSQL?

<details>
<summary>Model answer — reveal after your attempt</summary>

I/O stands for Input/Output: exchanging data with networks, storage or devices. A PostgreSQL call typically involves network I/O over TCP, and an asynchronous wait does not require a blocked worker thread.

</details>

---

[Русский](../Q-003-what-is-io.md) · [English](./Q-003-what-is-io.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-003) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-002-thread-id-after-await.md) · [Next →](Q-004-async-postgres-pipeline.md)
