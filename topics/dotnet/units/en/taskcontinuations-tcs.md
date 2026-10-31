# TaskCompletionSource and inline continuations

[Русский](../taskcontinuations-tcs.md) · [English](taskcontinuations-tcs.md)

[Home](../../../../README.en.md) · [Module](../../en/execution-context.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/taskcontinuations-tcs)

> Understand reentrancy and why SetResult under lock can be risky.

## Definition

TaskCompletionSource completes a Task programmatically. Depending on configuration, continuations may run inline on the SetResult caller; RunContinuationsAsynchronously prevents such inline execution.

## Internal mechanics

1. The completion implementation processes registered continuation callbacks.
2. If SetResult runs inside a lock, an inline continuation may invoke external code while the lock is held.
3. This can cause reentrancy, lock inversion, and unexpected latency.
4. RunContinuationsAsynchronously changes continuation scheduling, not one new thread per continuation.

## Resources

Continuation objects/queue entries and execution cost, potentially lock contention.

## Pitfalls and constraints

Avoid synchronous arbitrary continuations under long-held locks.

## Example

```csharp
var gate = new TaskCompletionSource<int>(TaskCreationOptions.RunContinuationsAsynchronously);
gate.SetResult(42);
```

## Review questions

- [Q-022: Why can SetResult under a lock run unexpected code, and what does RunContinuationsAsynchronously change?](../../../../questions/dotnet/en/Q-022-taskcompletionsource-continuations.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions)

---

[← Previous](synchronizationcontext-configureawait.md) · [Русский](../taskcontinuations-tcs.md) · [English](taskcontinuations-tcs.md)
