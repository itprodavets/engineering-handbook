# Task composition and exceptions

[Русский](../task-composition.md) · [English](task-composition.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/task-composition)

WhenAny, WhenAll, nested Tasks, and observing failures.

## Definition

Task.WhenAll represents the joint completion of supplied tasks; WhenAny yields the first completed Task regardless of its status. Task<Task> requires separating outer and inner completion.

## Mechanics: language/runtime to OS

1. Task.WhenAny returns the winning Task; await the winner to observe its exception.
2. Task.WhenAll becomes Faulted if one or more input tasks fault.
3. A normal await rethrows one exception; inspect the combined Task.Exception for all failures.
4. Task.Factory.StartNew(Func<Task>) produces a nested Task; Unwrap or a second await waits for the inner task.

## Resources

- **Task instances:** Aggregate Tasks and continuations; WhenAll/WhenAny need no dedicated new threads.
- **Exceptions:** Faulted Tasks retain exception information while those objects remain reachable.

## Constraints and pitfalls

- WhenAny does not automatically cancel losing operations.
- Multiple faults may be missed in diagnostics if you inspect only the exception rethrown by await.

## Review questions

- [Q-014: Does awaiting Task.WhenAny throw the winning task's exception or cancel the other tasks?](../../../questions/dotnet/en/Q-014-whenany-faulted-task.md)
- [Q-015: How does Task.WhenAll handle several faulted tasks and what does await throw?](../../../questions/dotnet/en/Q-015-whenall-multiple-exceptions.md)

## Reinforcement challenges

- [Q-026: What does it print, and does awaiting WhenAny throw the winning task's exception?](../../../questions/dotnet/en/Q-026-whenany-faulted-output.md)
- [Q-027: How many exceptions are stored by WhenAll when two input Tasks fault?](../../../questions/dotnet/en/Q-027-whenall-exceptions-count.md)
- [Q-033: What is the task type, and does awaiting outer once wait for the inner async operation?](../../../questions/dotnet/en/Q-033-startnew-nested-task.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany)

---

[Русский](../task-composition.md) · [English](task-composition.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/task-composition)
