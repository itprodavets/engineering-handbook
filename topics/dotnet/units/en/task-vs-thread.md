# Thread, Task and Task.Run are distinct

[Русский](../task-vs-thread.md) · [English](task-vs-thread.md)

[Home](../../../../README.en.md) · [Module](../../en/threadpool-scheduling.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/task-vs-thread)

> Separate OS execution units from operation completion objects.

## Definition

A Thread is an OS-scheduled execution context with a stack; a Task represents completion of an operation. Task.Run queues a delegate to the ThreadPool, not necessarily creating a new Thread.

## Internal mechanics

1. A Task can remain pending on I/O without holding a dedicated worker.
2. Task.Run uses an available worker to execute its delegate; the worker later becomes reusable.
3. Task.WhenAll observes completion of supplied tasks and does not start them again.
4. An OS thread has its own stack; a Task does not intrinsically own an OS thread stack.

## Resources

Thread: OS stack and scheduling structures; Task: managed state and continuations.

## Pitfalls and constraints

‘10,000 Tasks = 10,000 Threads’ is false; distinguish queued work from active workers.

## Example

```csharp
var task = Task.Run(() => Compute());
var result = await task;
```

## Review questions

- [Q-008: What is the difference between Task and Thread in .NET? Does a Task create a new thread, and what does await do?](../../../../questions/dotnet/en/Q-008-task-vs-thread.md)
- [Q-010: Does Task.WhenAll create threads or start the tasks passed to it?](../../../../questions/dotnet/en/Q-010-task-whenall-execution.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool](https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool)

---

[Next →](os-vs-runtime-scheduler.md) · [Русский](../task-vs-thread.md) · [English](task-vs-thread.md)
