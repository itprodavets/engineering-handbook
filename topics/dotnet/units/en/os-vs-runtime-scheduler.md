# The OS scheduler, CPU cores and ThreadPool

[Русский](../os-vs-runtime-scheduler.md) · [English](os-vs-runtime-scheduler.md)

[Home](../../../../README.en.md) · [Module](../../en/threadpool-scheduling.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/os-vs-runtime-scheduler)

> Understand CPU time, preemption and .NET work queues.

## Definition

The OS scheduler assigns runnable threads to logical processors. The .NET ThreadPool manages workers and work queues but does not select their CPU cores.

## Internal mechanics

1. With eight logical CPUs, at most eight software threads execute instructions simultaneously, one per hardware execution context.
2. The OS can preempt an unfinished thread and run another; that is a context switch.
3. 100 runnable threads can make progress concurrently by time-sharing but cannot all execute in parallel.
4. The ThreadPool schedules work items on workers; the OS scheduler maps those workers onto processors.

## Resources

CPU time for execution and switching; cache misses after migration; stacks and kernel bookkeeping per thread.

## Pitfalls and constraints

Low CPU use with growing HTTP latency may indicate I/O waits, blocking or starvation.

## Example

```csharp
Console.WriteLine(Environment.CurrentManagedThreadId);
```

## Review questions

- [Q-006: How can eight physical CPU cores handle 100 runnable threads?](../../../../questions/dotnet/en/Q-006-hundred-threads-eight-cores.md)
- [Q-007: What is the difference between the .NET ThreadPool and the OS scheduler? Who decides which CPU core runs a thread?](../../../../questions/dotnet/en/Q-007-threadpool-vs-os-scheduler.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading](https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading)

---

[← Previous](task-vs-thread.md) · [Next →](threadpool-starvation.md) · [Русский](../os-vs-runtime-scheduler.md) · [English](os-vs-runtime-scheduler.md)
