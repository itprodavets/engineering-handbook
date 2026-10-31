# What the compiler generates for async/await

[Русский](../async-state-machine.md) · [English](async-state-machine.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-state-machine)

> Understand MoveNext, awaiters and the IsCompleted fast path.

## Definition

Roslyn lowers an async method into a state machine with saved state and a MoveNext() method. The async keyword does not start a thread.

## Internal mechanics

1. Calling an async Task method starts executing on the caller thread until an incomplete awaitable is reached.
2. Awaiter.IsCompleted=true permits synchronous continuation via GetResult(), without a mandatory thread switch.
3. When IsCompleted=false, the state machine stores its position, registers a continuation, and returns a Task to its caller.
4. After completion, MoveNext resumes execution; heap allocations depend on the path and implementation.

## Resources

State fields and awaiter; possible continuation/Task allocations; no automatically created OS thread.

## Pitfalls and constraints

Do not equate await with Task.Run: awaiting a completed Task need not suspend at all.

## Example

```csharp
async Task Example() { Console.Write("A"); await Task.CompletedTask; Console.Write("B"); }
```

## Review questions

- [Q-012: Does calling an async Task method start a new thread or run synchronously at first?](../../../../questions/dotnet/en/Q-012-async-starts-synchronously.md)
- [Q-013: Does await always suspend, allocate a worker, or switch threads?](../../../../questions/dotnet/en/Q-013-completed-await-and-scheduling.md)
- [Q-024: What is the output and why? The awaited Task is already complete.](../../../../questions/dotnet/en/Q-024-completed-await-output.md)
- [Q-025: What is the output? The method awaits an incomplete TaskCompletionSource.](../../../../questions/dotnet/en/Q-025-incomplete-await-output.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Previous](io-vs-cpu-bound.md) · [Next →](async-socket-pipeline.md) · [Русский](../async-state-machine.md) · [English](async-state-machine.md)
