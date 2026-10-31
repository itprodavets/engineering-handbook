# Q-041 — Shared memory and synchronization

[Русский](../Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-041) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-040-lost-update-two-task-run.md) · [Next →](Q-042-interlocked-increment-ref.md)

## Question

Why does volatile int Value not make Value++ atomic, and what ordering does C# volatile provide?

## .NET / C# challenge — predict the outcome first

```csharp
sealed class Counter { public volatile int Value; }
// Two unsynchronized Value++ operations can lose an update.
```

<details>
<summary>Model answer — reveal after your attempt</summary>

Volatile reads have acquire, writes have release semantics. This is not a single global sequential order or an atomic composite read-modify-write: both workers may write 1 rather than 2.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)

---

[Русский](../Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-041) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-040-lost-update-two-task-run.md) · [Next →](Q-042-interlocked-increment-ref.md)
