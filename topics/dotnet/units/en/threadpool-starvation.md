# ThreadPool starvation and blocking waits

[Русский](../threadpool-starvation.md) · [English](threadpool-starvation.md)

[Home](../../../../README.en.md) · [Module](../../en/threadpool-scheduling.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/threadpool-starvation)

> Explain occupied workers and the source of queue growth.

## Definition

ThreadPool starvation delays queued work when workers are unavailable. Thread.Sleep blocks one worker per executing delegate; Task.Delay does not reserve a worker during the timer wait.

## Internal mechanics

1. Task.Run(() => Thread.Sleep(...)) queues a delegate on the ThreadPool.
2. While executing Sleep, the worker is blocked although not consuming CPU on computation.
3. The pool may add OS worker threads, but their count and growth rate depend on runtime and workload.
4. Monitor dotnet.thread_pool.thread.count and queue.length; low CPU with long queues is a useful indicator.

## Resources

Task.Delay: timer registration and Task; Thread.Sleep: occupied worker stack and queued delegates.

## Pitfalls and constraints

Do not claim exact OS thread counts or allocated bytes without measuring the specific runtime.

## Example

```csharp
await Task.Delay(5000); // timer, no blocked worker
await Task.Run(() => Thread.Sleep(5000)); // blocked worker
```

## Review questions

- [Q-009: What happens to the ThreadPool when 10,000 Task.Delay(5000) operations run versus 10,000 Task.Run(() => Thread.Sleep(5000)) operations?](../../../../questions/dotnet/en/Q-009-task-delay-vs-thread-sleep.md)
- [Q-011: What does it mean when the ThreadPool creates an additional thread, and why do 10,000 Tasks not imply 10,000 threads?](../../../../questions/dotnet/en/Q-011-threadpool-worker-creation.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[← Previous](os-vs-runtime-scheduler.md) · [Русский](../threadpool-starvation.md) · [English](threadpool-starvation.md)
