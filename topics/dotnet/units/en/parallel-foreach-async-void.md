# Why Parallel.ForEach(async ...) is dangerous

[Русский](../parallel-foreach-async-void.md) · [English](parallel-foreach-async-void.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/parallel-foreach-async-void)

> Explain why async void continuations escape loop completion.

## Definition

Parallel.ForEach accepts a synchronous Action<T>. An async lambda converted to Action<T> becomes async void, so the loop does not wait for continuations after the first incomplete await.

## Internal mechanics

1. After an incomplete await, async void returns control to the Action caller.
2. Parallel.ForEach considers the synchronous invocation complete even while async code is waiting.
3. Exceptions from async void are not observed through Task.WhenAll and may terminate the process.
4. Use Parallel.ForEachAsync with a ValueTask delegate, or Task.WhenAll with explicit async Tasks.

## Resources

Continuations and ThreadPool, with risk of unbounded external operations.

## Pitfalls and constraints

‘Loop completed => async operations completed’ is false.

## Example

```csharp
await Parallel.ForEachAsync(items, async (item, ct) => {
    await HandleAsync(item, ct);
});
```

## Review questions

- [Q-035: Does Parallel.ForEach wait for async lambda continuations, and what output is guaranteed?](../../../../questions/dotnet/en/Q-035-parallel-foreach-async-void.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.parallel.foreachasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.parallel.foreachasync)

---

[← Previous](mutual-exclusion-and-semaphores.md) · [Русский](../parallel-foreach-async-void.md) · [English](parallel-foreach-async-void.md)
