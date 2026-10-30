# ThreadPool and the OS scheduler

[Русский](../threadpool-scheduling.md) · [English](threadpool-scheduling.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/threadpool-scheduling)

Who schedules work items and who selects CPU cores.

## Definition

A Task represents an operation; a Thread is an OS-scheduled execution context with a stack. The ThreadPool schedules work items on workers, while the OS scheduler assigns threads to logical CPUs. Task.Run does not imply thread creation.

## Mechanics: language/runtime to OS

1. Task.Run queues a delegate through TaskScheduler.Default / ThreadPool; an existing worker may execute it.
2. If workers are insufficient, the ThreadPool can add them according to runtime heuristics and limits.
3. The OS kernel schedules runnable threads on logical CPUs, preempts them, and may migrate them.
4. Thread.Sleep blocks its worker; Task.Delay uses timer machinery rather than reserving a worker for the wait.

## Resources

- **OS threads:** Additional workers require OS stacks, thread metadata and virtual address space.
- **Queues:** Task.Run queues delegates; 10,000 Tasks do not mean 10,000 simultaneously executing delegates.
- **CPU:** A sleeping worker does not perform CPU calculations, but cannot process other pool work.

## Constraints and pitfalls

- ThreadPool starvation can occur with queued work and few available workers even when CPU usage is low.
- The number of Tasks does not determine the exact number of OS threads created.

## Review questions

- [Q-006: How can eight physical CPU cores handle 100 runnable threads?](../../../questions/dotnet/en/Q-006-hundred-threads-eight-cores.md)
- [Q-007: What is the difference between the .NET ThreadPool and the OS scheduler? Who decides which CPU core runs a thread?](../../../questions/dotnet/en/Q-007-threadpool-vs-os-scheduler.md)
- [Q-008: What is the difference between Task and Thread in .NET? Does a Task create a new thread, and what does await do?](../../../questions/dotnet/en/Q-008-task-vs-thread.md)
- [Q-009: What happens to the ThreadPool when 10,000 Task.Delay(5000) operations run versus 10,000 Task.Run(() => Thread.Sleep(5000)) operations?](../../../questions/dotnet/en/Q-009-task-delay-vs-thread-sleep.md)
- [Q-010: Does Task.WhenAll create threads or start the tasks passed to it?](../../../questions/dotnet/en/Q-010-task-whenall-execution.md)
- [Q-011: What does it mean when the ThreadPool creates an additional thread, and why do 10,000 Tasks not imply 10,000 threads?](../../../questions/dotnet/en/Q-011-threadpool-worker-creation.md)

## Reinforcement challenges

—

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool](https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool)
- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[Русский](../threadpool-scheduling.md) · [English](threadpool-scheduling.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/threadpool-scheduling)
