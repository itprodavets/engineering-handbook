# Monitor locks and SemaphoreSlim

[Русский](../mutual-exclusion-and-semaphores.md) · [English](mutual-exclusion-and-semaphores.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/mutual-exclusion-and-semaphores)

> Distinguish thread blocking from asynchronous permit waiting.

## Definition

lock enforces mutual exclusion only for threads synchronizing on the same object. SemaphoreSlim.WaitAsync can await a permit without blocking the caller thread while pending.

## Internal mechanics

1. lock(new object()) creates a distinct object for each execution and does not protect shared state.
2. The compiler disallows await inside lock (CS1996) because that lock scopes a synchronous critical section.
3. SemaphoreSlim decrements the permit count on WaitAsync, and Release returns a permit; it is not a reentrant mutex.
4. Place Release in finally so exceptions or cancellation after acquisition do not leak permits.

## Resources

Lock contention and waiter queues; blocked Monitor workers versus asynchronous semaphore waits.

## Pitfalls and constraints

A second WaitAsync(1,1) without Release can stall the same flow indefinitely.

## Example

```csharp
using var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();
try { /* protected async work */ }
finally { semaphore.Release(); }
```

## Review questions

- [Q-020: Why is await prohibited inside lock, and how does SemaphoreSlim.WaitAsync differ?](../../../../questions/dotnet/en/Q-020-await-inside-lock.md)
- [Q-029: Does lock(new object()) protect counter from concurrent increments?](../../../../questions/dotnet/en/Q-029-lock-new-object.md)
- [Q-034: What does second.IsCompleted print after another WaitAsync without Release?](../../../../questions/dotnet/en/Q-034-semaphore-waitasync.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[← Previous](atomicity-and-memory-visibility.md) · [Next →](parallel-foreach-async-void.md) · [Русский](../mutual-exclusion-and-semaphores.md) · [English](mutual-exclusion-and-semaphores.md)
