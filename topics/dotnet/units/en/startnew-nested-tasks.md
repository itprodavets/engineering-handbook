# Nested Tasks and StartNew(Func<Task>)

[Русский](../startnew-nested-tasks.md) · [English](startnew-nested-tasks.md)

[Home](../../../../README.en.md) · [Module](../../en/task-composition.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/startnew-nested-tasks)

> Separate completion of the outer Task from the inner async operation.

## Definition

Task.Factory.StartNew with an async delegate can produce Task<Task>. The outer Task completes when the delegate returns the inner Task, not when the inner async operation finishes.

## Internal mechanics

1. The compiler lowers the async lambda into a function returning Task.
2. StartNew schedules the delegate and returns Task<TResult>, where TResult is itself a Task.
3. Awaiting outer returns inner; use await inner or Unwrap() for full completion.
4. Task.Run(Func<Task>) unwraps the returned Task and is often preferable for async delegates.

## Resources

Two task representations and continuations; unobserved inner failures are possible.

## Pitfalls and constraints

One await of outer does not guarantee inner completion, causing lifecycle and exception-handling bugs.

## Example

```csharp
Task<Task> outer = Task.Factory.StartNew<Task>(async () => await Task.Delay(100));
Task inner = await outer;
await inner;
```

## Review questions

- [Q-033: What is the task type, and does awaiting outer once wait for the inner async operation?](../../../../questions/dotnet/en/Q-033-startnew-nested-task.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap)

---

[← Previous](task-aggregation.md) · [Русский](../startnew-nested-tasks.md) · [English](startnew-nested-tasks.md)
