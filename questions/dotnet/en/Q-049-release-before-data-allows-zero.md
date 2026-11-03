# Q-049 — Shared memory and synchronization

[Русский](../Q-049-release-before-data-allows-zero.md) · [English](./Q-049-release-before-data-allows-zero.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-049) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-048-safe-publication-acquire-release.md) · [Next →](Q-050-nonvolatile-loop-jit-hoisting.md)

## Question

Can the consumer see zero if producer publishes ready before writing data?

## .NET / C# challenge — predict the outcome first

```csharp
int data = 0, ready = 0;
// Producer: Volatile.Write(ref ready, 1); data = 42;
// Consumer may observe ready==1 while data is still 0.
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-049.cs
```

[Q-049.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-049.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Yes: zero is possible even with no JIT/CPU reordering. Valid interleaving: producer release-stores `ready=1` → consumer observes 1 → reads old `data=0` → producer later writes `data=42`. Release does not publish future stores. Fix the protocol by writing data first, then release-storing the flag; consumer acquire-reads the flag. The lab deterministically reproduces this ordering.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](../Q-049-release-before-data-allows-zero.md) · [English](./Q-049-release-before-data-allows-zero.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-049) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-048-safe-publication-acquire-release.md) · [Next →](Q-050-nonvolatile-loop-jit-hoisting.md)
