# Q-021 — Shared memory and synchronization

[Русский](../Q-021-volatile-vs-interlocked.md) · [English](./Q-021-volatile-vs-interlocked.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-021) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-020-await-inside-lock.md) · [Next →](Q-022-taskcompletionsource-continuations.md)

## Question

Why is volatile counter++ unsafe, and how do Interlocked.Increment and lock differ?

<details>
<summary>Model answer — reveal after your attempt</summary>

volatile affects memory access and ordering but does not make read-modify-write atomic. Interlocked.Increment atomically changes one variable; lock protects a critical section.

</details>

---

[Русский](../Q-021-volatile-vs-interlocked.md) · [English](./Q-021-volatile-vs-interlocked.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-021) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-020-await-inside-lock.md) · [Next →](Q-022-taskcompletionsource-continuations.md)
