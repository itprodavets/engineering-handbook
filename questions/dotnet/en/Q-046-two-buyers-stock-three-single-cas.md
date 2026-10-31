# Q-046 — Shared memory and synchronization

[Русский](../Q-046-two-buyers-stock-three-single-cas.md) · [English](./Q-046-two-buyers-stock-three-single-cas.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-046) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-045-two-buyers-single-item-cas.md) · [Next →](Q-047-cas-loop-five-buyers.md)

## Question

If stock=3 and two threads perform CompareExchange(ref stock,2,3), how many succeed and what do the calls return?

## .NET / C# challenge — predict the outcome first

```csharp
int previous=Interlocked.CompareExchange(ref stock,2,3);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-046.cs
```

[Q-046.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-046.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Exactly one 3→2 transition succeeds; stock=2. Winner receives old value 3, loser gets 2. Loser must reread stock and retry with expected=2 to buy another item.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](../Q-046-two-buyers-stock-three-single-cas.md) · [English](./Q-046-two-buyers-stock-three-single-cas.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-046) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-045-two-buyers-single-item-cas.md) · [Next →](Q-047-cas-loop-five-buyers.md)
