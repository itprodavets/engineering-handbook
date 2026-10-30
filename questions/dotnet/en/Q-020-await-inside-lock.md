# Q-020 — Shared memory and synchronization

[Русский](../Q-020-await-inside-lock.md) · [English](./Q-020-await-inside-lock.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-020) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-019-valuetask-consumption.md) · [Next →](Q-021-volatile-vs-interlocked.md)

## Question

Why is await prohibited inside lock, and how does SemaphoreSlim.WaitAsync differ?

<details>
<summary>Model answer — reveal after your attempt</summary>

The compiler reports CS1996 for await inside lock. SemaphoreSlim.WaitAsync awaits a permit without blocking a worker; release it in finally. SemaphoreSlim is not automatically reentrant.

</details>

---

[Русский](../Q-020-await-inside-lock.md) · [English](./Q-020-await-inside-lock.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-020) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-019-valuetask-consumption.md) · [Next →](Q-021-volatile-vs-interlocked.md)
