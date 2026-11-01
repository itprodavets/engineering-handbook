# Q-050 — Shared memory and synchronization

[Русский](../Q-050-nonvolatile-loop-jit-hoisting.md) · [English](./Q-050-nonvolatile-loop-jit-hoisting.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-050) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-049-release-before-data-allows-zero.md) · [Next →](Q-051-thread-yield-is-not-memory-fence.md)

## Question

Does while(ready==0) without volatile necessarily terminate after another thread writes ready=1?

## .NET / C# challenge — predict the outcome first

```csharp
while (ready == 0) { } // ordinary unsynchronized read
```

<details>
<summary>Model answer — reveal after your attempt</summary>

No. Ordinary reads do not establish synchronization; optimizations such as load hoisting may be permitted. A particular JIT need not do so; do not run unbounded unsafe loops in CI.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](../Q-050-nonvolatile-loop-jit-hoisting.md) · [English](./Q-050-nonvolatile-loop-jit-hoisting.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-050) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-049-release-before-data-allows-zero.md) · [Next →](Q-051-thread-yield-is-not-memory-fence.md)
