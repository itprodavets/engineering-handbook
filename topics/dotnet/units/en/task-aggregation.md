# WhenAll and WhenAny completion semantics

[Русский](../task-aggregation.md) · [English](task-aggregation.md)

[Home](../../../../README.en.md) · [Module](../../en/task-composition.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/task-aggregation)

> Distinguish waiting for all tasks from receiving the first completion.

## Definition

Task.WhenAll produces an aggregate task that completes after all inputs. Task.WhenAny yields the first completed task regardless of its state; the others are not automatically canceled.

## Internal mechanics

1. WhenAny returns Task<Task>; the outer task succeeds even if the winning task faulted.
2. To observe the winner’s exception, await the returned inner Task.
3. WhenAll preserves failures of all faulted input tasks in its AggregateException.
4. A normal await of WhenAll rethrows one exception; inspect all.Exception.InnerExceptions for the full set.

## Resources

Aggregate Task and continuations; no dedicated threads per wait.

## Pitfalls and constraints

WhenAll neither synchronizes shared memory nor bounds parallelism.

## Example

```csharp
Task all = Task.WhenAll(first, second);
try { await all; } catch { Console.WriteLine(all.Exception); }
```

## Review questions

- [Q-014: Does awaiting Task.WhenAny throw the winning task's exception or cancel the other tasks?](../../../../questions/dotnet/en/Q-014-whenany-faulted-task.md)
- [Q-015: How does Task.WhenAll handle several faulted tasks and what does await throw?](../../../../questions/dotnet/en/Q-015-whenall-multiple-exceptions.md)
- [Q-026: What does it print, and does awaiting WhenAny throw the winning task's exception?](../../../../questions/dotnet/en/Q-026-whenany-faulted-output.md)
- [Q-027: How many exceptions are stored by WhenAll when two input Tasks fault?](../../../../questions/dotnet/en/Q-027-whenall-exceptions-count.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)

---

[Next →](startnew-nested-tasks.md) · [Русский](../task-aggregation.md) · [English](task-aggregation.md)
