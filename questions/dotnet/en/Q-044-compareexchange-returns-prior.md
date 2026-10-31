# Q-044 — Shared memory and synchronization

[Русский](../Q-044-compareexchange-returns-prior.md) · [English](./Q-044-compareexchange-returns-prior.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-044) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-043-check-then-act-stock-negative.md) · [Next →](Q-045-two-buyers-single-item-cas.md)

## Question

Starting from stock=1, what does CompareExchange(ref stock,0,1) return and what is stock afterward?

## .NET / C# challenge — predict the outcome first

```csharp
int stock=1;
int previous=Interlocked.CompareExchange(ref stock,0,1);
Console.WriteLine($"{previous} {stock}");
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-044.cs
```

[Q-044.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-044.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Returns the old value 1 while atomically writing 0 because stock matched expected=1. Arguments: ref location, newValue, expectedValue. For stock=10/current=10, CAS(current-3,current) returns previous=10 and leaves current=10, stock=7.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](../Q-044-compareexchange-returns-prior.md) · [English](./Q-044-compareexchange-returns-prior.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-044) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-043-check-then-act-stock-negative.md) · [Next →](Q-045-two-buyers-single-item-cas.md)
