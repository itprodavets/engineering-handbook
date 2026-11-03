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

Without `volatile` or another synchronization mechanism, reading `ready` is not an acquire operation and does not establish safe publication of prior `data` writes. Observing ordinary `ready==1` is not a valid release/acquire proof that a following `data` read sees 42. In `while(ready==0)`, JIT may hoist a normal load where permitted, but a particular optimization is not required. Typical behavior on x86 or in one test run is not a C#/.NET memory-model guarantee.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](../Q-050-nonvolatile-loop-jit-hoisting.md) · [English](./Q-050-nonvolatile-loop-jit-hoisting.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-050) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-049-release-before-data-allows-zero.md) · [Next →](Q-051-thread-yield-is-not-memory-fence.md)
