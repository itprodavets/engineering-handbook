# Q-043 — Shared memory and synchronization

[Русский](../Q-043-check-then-act-stock-negative.md) · [English](./Q-043-check-then-act-stock-negative.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-043) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-042-interlocked-increment-ref.md) · [Next →](Q-044-compareexchange-returns-prior.md)

## Question

Can stock become -1 after a volatile positive check and an Interlocked.Decrement when starting at stock=1?

## .NET / C# challenge — predict the outcome first

```csharp
if (Volatile.Read(ref stock)>0)
    Interlocked.Decrement(ref stock);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-043.cs
```

[Q-043.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-043.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Yes. Both buyers may read 1 before either decrements. Their individually atomic decrements produce 1→0→-1. The check and act are not atomic together, violating stock>=0.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.decrement](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.decrement)

---

[Русский](../Q-043-check-then-act-stock-negative.md) · [English](./Q-043-check-then-act-stock-negative.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-043) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-042-interlocked-increment-ref.md) · [Next →](Q-044-compareexchange-returns-prior.md)
