# Deadlocks and starvation with .Result/.Wait()

[Русский](../sync-over-async.md) · [English](sync-over-async.md)

[Home](../../../../README.en.md) · [Module](../../en/sync-over-async.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/sync-over-async)

> Distinguish a blocked worker, cyclic waits, and lack of progress.

## Definition

Task.Result/Wait block the caller until Task completion. Under load this reduces ThreadPool capacity; a classic deadlock requires a specific wait cycle, such as a captured single-threaded context.

## Internal mechanics

1. A worker starts async work and then blocks in .Result.
2. The continuation needs execution elsewhere; if workers are exhausted it waits in a queue.
3. In a UI SynchronizationContext, the continuation may require the blocked UI thread, creating deadlock.
4. Standard ASP.NET Core lacks that UI-style context, but ThreadPool starvation remains a risk.

## Resources

One blocked worker per executing .Result/.Wait(); queued work and possible additional worker threads.

## Pitfalls and constraints

Avoiding deadlock does not guarantee scalability. Do not wrap async I/O as Task.Run(() => io.Result).

## Example

```csharp
var orders = await GetOrdersAsync(); // no synchronous .Result
```

## Review questions

- [Q-016: Why are .Result and .Wait() dangerous in ASP.NET Core? Is a deadlock guaranteed?](../../../../questions/dotnet/en/Q-016-sync-over-async-deadlocks.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[Русский](../sync-over-async.md) · [English](sync-over-async.md)
