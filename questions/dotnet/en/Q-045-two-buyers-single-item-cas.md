# Q-045 — Shared memory and synchronization

[Русский](../Q-045-two-buyers-single-item-cas.md) · [English](./Q-045-two-buyers-single-item-cas.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-045) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-044-compareexchange-returns-prior.md) · [Next →](Q-046-two-buyers-stock-three-single-cas.md)

## Question

Can both threads successfully execute CompareExchange(ref stock,0,1) when stock starts at 1?

## .NET / C# challenge — predict the outcome first

```csharp
if (Interlocked.CompareExchange(ref stock,0,1)==1)
    Console.WriteLine("Purchased");
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-045.cs
```

[Q-045.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-045.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No. Only one CAS can atomically replace 1→0 and return previous=1. The other sees 0 and returns previous=0; Purchased occurs once and stock ends at 0.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](../Q-045-two-buyers-single-item-cas.md) · [English](./Q-045-two-buyers-single-item-cas.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-045) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-044-compareexchange-returns-prior.md) · [Next →](Q-046-two-buyers-stock-three-single-cas.md)
