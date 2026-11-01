# Q-051 — Shared memory and synchronization

[Русский](../Q-051-thread-yield-is-not-memory-fence.md) · [English](./Q-051-thread-yield-is-not-memory-fence.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-051) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-050-nonvolatile-loop-jit-hoisting.md) · [Next →](Q-052-await-producer-publishes-data.md)

## Question

Why does Thread.Yield in an ordinary polling loop not replace Volatile.Read?

## .NET / C# challenge — predict the outcome first

```csharp
while (ready == 0) { Thread.Yield(); }
```

<details>
<summary>Model answer — reveal after your attempt</summary>

Yield affects OS scheduling; it is neither an acquire read nor a happens-before protocol. A particular runtime may happen to terminate the loop, but synchronization is not guaranteed.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0)

---

[Русский](../Q-051-thread-yield-is-not-memory-fence.md) · [English](./Q-051-thread-yield-is-not-memory-fence.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-051) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-050-nonvolatile-loop-jit-hoisting.md) · [Next →](Q-052-await-producer-publishes-data.md)
