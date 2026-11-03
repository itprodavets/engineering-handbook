# Q-048 — Shared memory and synchronization

[Русский](../Q-048-safe-publication-acquire-release.md) · [English](./Q-048-safe-publication-acquire-release.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-048) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-047-cas-loop-five-buyers.md) · [Next →](Q-049-release-before-data-allows-zero.md)

## Question

Why does data=42 before release-store and acquire-reading ready safely publish 42?

## .NET / C# challenge — predict the outcome first

```csharp
int data = 0, ready = 0;
// Producer: data = 42; Volatile.Write(ref ready, 1);
// Consumer: if (Volatile.Read(ref ready) == 1) Console.WriteLine(data);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-048.cs
```

[Q-048.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-048.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Assuming initial `data=ready=0` and no interfering writers, producer writes `data=42` before `Volatile.Write(ref ready,1)` (release). If the consumer's `Volatile.Read(ref ready)` (acquire) observes this publication, a subsequent `data` read observes 42. Release covers preceding stores; acquire prevents moving subsequent data reads before the flag read. `Interlocked.Increment` is unnecessary: this is safe publication, not a counter update. No bounded waiting time is promised.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](../Q-048-safe-publication-acquire-release.md) · [English](./Q-048-safe-publication-acquire-release.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-048) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-047-cas-loop-five-buyers.md) · [Next →](Q-049-release-before-data-allows-zero.md)
