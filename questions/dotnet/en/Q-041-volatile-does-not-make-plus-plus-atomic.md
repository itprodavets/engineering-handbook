# Q-041 — Shared memory and synchronization

[Русский](../Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-041) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-040-lost-update-two-task-run.md) · [Next →](Q-042-interlocked-increment-ref.md)

## Question

Why does volatile int Value not make Value++ atomic, and what ordering does C# volatile provide?

## .NET / C# challenge — predict the outcome first

```csharp
sealed class Counter { public volatile int Value; }
// Two concurrent Value++ operations can both read 5 and write 6.
```

<details>
<summary>Model answer — reveal after your attempt</summary>

`volatile`/`Volatile.Read` provide acquire reads; `volatile`/`Volatile.Write` provide release writes. These constrain memory ordering, not composite-operation atomicity. `Value++` consists logically of read → add → write: two workers may both read 5 and write 6 (lost update). `volatile` neither promises the chronologically newest value on every read nor establishes a global total order.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)

---

[Русский](../Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-041) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-040-lost-update-two-task-run.md) · [Next →](Q-042-interlocked-increment-ref.md)
