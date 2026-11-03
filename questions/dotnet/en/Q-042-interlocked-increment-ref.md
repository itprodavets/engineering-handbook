# Q-042 — Shared memory and synchronization

[Русский](../Q-042-interlocked-increment-ref.md) · [English](./Q-042-interlocked-increment-ref.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-042) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Next →](Q-043-check-then-act-stock-negative.md)

## Question

What does Interlocked.Increment(ref int) guarantee, and why is ref unrelated to Counter being a reference type?

## .NET / C# challenge — predict the outcome first

```csharp
int counter = 0;
Interlocked.Increment(ref counter);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-042.cs
```

[Q-042.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-042.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

`Interlocked.Increment(ref value)` is an atomic read-modify-write on one addressable `int`, returning the updated value. `ref` passes the variable itself, irrespective of whether its container is a class. Ten workers each making 1,000 increments yield 10,000 from zero if there are no other writes or relevant overflow. It also provides memory-ordering guarantees, but cannot protect other fields or a separate check-then-act sequence; it is not a C# `Monitor` critical section.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)

---

[Русский](../Q-042-interlocked-increment-ref.md) · [English](./Q-042-interlocked-increment-ref.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-042) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Next →](Q-043-check-then-act-stock-negative.md)
