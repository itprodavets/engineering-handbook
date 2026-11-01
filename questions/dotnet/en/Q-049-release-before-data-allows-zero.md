# Q-049 — Shared memory and synchronization

[Русский](../Q-049-release-before-data-allows-zero.md) · [English](./Q-049-release-before-data-allows-zero.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-049) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-048-safe-publication-acquire-release.md) · [Next →](Q-050-nonvolatile-loop-jit-hoisting.md)

## Question

Can the consumer see zero if producer publishes ready before writing data?

## .NET / C# challenge — predict the outcome first

```csharp
Volatile.Write(ref ready,1);
data=42; // consumer might read old data
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-049.cs
```

[Q-049.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-049.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Yes. The consumer can observe flag 1 and read data before the later data store. Release does not publish subsequent writes. The lab forces that order.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](../Q-049-release-before-data-allows-zero.md) · [English](./Q-049-release-before-data-allows-zero.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-049) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-048-safe-publication-acquire-release.md) · [Next →](Q-050-nonvolatile-loop-jit-hoisting.md)
