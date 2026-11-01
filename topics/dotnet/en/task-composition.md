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
- [Q-052: Why does reading data after await producer yield 42 without volatile?](../../../questions/dotnet/en/Q-052-await-producer-publishes-data.md)
- [Q-053: Can Consumer print zero even if the caller later awaits Task.WhenAll(producer,consumer)?](../../../questions/dotnet/en/Q-053-whenall-does-not-order-producer-consumer.md)
- [Q-054: Why does awaiting Task.Delay(100) not establish producer completion or visibility?](../../../questions/dotnet/en/Q-054-task-delay-is-not-synchronization.md)
- [Q-055: If Task.Delay wins WhenAny, must producer still be incomplete when the continuation executes?](../../../questions/dotnet/en/Q-055-whenany-winner-vs-continuation-time.md)
- [Q-056: Does awaiting WhenAny throw the winner's exception? What does awaiting the returned Task do?](../../../questions/dotnet/en/Q-056-whenany-faulted-winner-exception.md)
- [Q-057: How many InnerExceptions are stored for two faulted tasks, and what does await combined propagate?](../../../questions/dotnet/en/Q-057-whenall-multiple-exceptions-await-one.md)
- [Q-058: What status does WhenAll(Faulted,Canceled) have, and what does await propagate?](../../../questions/dotnet/en/Q-058-whenall-faulted-priority-over-canceled.md)
- [Q-059: Does WhenAny cancel losing tasks and what happens to them?](../../../questions/dotnet/en/Q-059-whenany-does-not-cancel-loser.md)
- [Q-060: If one input task is already Faulted and another is pending, does WhenAll complete immediately?](../../../questions/dotnet/en/Q-060-whenall-waits-not-fail-fast.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany)

---

[Русский](../task-composition.md) · [English](task-composition.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/task-composition)
