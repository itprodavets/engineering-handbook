# Q-047 — Shared memory and synchronization

[Русский](../Q-047-cas-loop-five-buyers.md) · [English](./Q-047-cas-loop-five-buyers.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-047) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-046-two-buyers-stock-three-single-cas.md)

## Question

How does a CAS loop behave with stock=3/two buyers and stock=1/five buyers?

## .NET / C# challenge — predict the outcome first

```csharp
while (true) {
  int current=Volatile.Read(ref stock);
  if (current<=0) return false;
  if (Interlocked.CompareExchange(ref stock,current-1,current)==current) return true;
}
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-047.cs
```

[Q-047.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-047.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

With stock=3/two buyers both succeed and stock=1; a failed CAS rereads the actual value. With stock=1/five buyers one returns true, four false and stock=0. Each iteration checks current<=0; the invariant holds if all writers follow this protocol.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](../Q-047-cas-loop-five-buyers.md) · [English](./Q-047-cas-loop-five-buyers.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-047) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-046-two-buyers-stock-three-single-cas.md)
