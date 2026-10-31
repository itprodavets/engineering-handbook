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

Atomic read-modify-write of one int: two completed increments from 0 result in 2. ref passes the variable location even for a local value-type int. It does not acquire a C# Monitor over an entire section; runtime typically uses CPU atomic instructions.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)

---

[Русский](../Q-042-interlocked-increment-ref.md) · [English](./Q-042-interlocked-increment-ref.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-042) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Next →](Q-043-check-then-act-stock-negative.md)
