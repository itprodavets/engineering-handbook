# Q-002 — Continuations and execution contexts

[Русский](../Q-002-thread-id-after-await.md) · [English](./Q-002-thread-id-after-await.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-002) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-001-async-io-scalability.md) · [Next →](Q-003-what-is-io.md)

## Question

Must Environment.CurrentManagedThreadId be the same before and after await ToListAsync()? If not, did await create a new thread?

<details>
<summary>Model answer — reveal after your attempt</summary>

No. In ASP.NET Core, the continuation may execute on a different ThreadPool thread. await neither creates a thread nor guarantees a thread switch; an already completed task may continue synchronously.

</details>

---

[Русский](../Q-002-thread-id-after-await.md) · [English](./Q-002-thread-id-after-await.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-002) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-001-async-io-scalability.md) · [Next →](Q-003-what-is-io.md)
