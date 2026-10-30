# Blocking and sync-over-async

[Русский](../sync-over-async.md) · [English](sync-over-async.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/sync-over-async)

Why .Result and .Wait() are risky and where deadlocks come from.

## Definition

Synchronously waiting for a Task blocks the caller even if the pending operation is asynchronous I/O. In servers, blocked workers reduce ThreadPool capacity.

## Mechanics: C# to OS

1. Task.Wait and Task.Result keep the calling thread blocked until completion, failure or cancellation.
2. Deadlock is possible when a continuation requires the same context that the synchronous wait is blocking.
3. Standard ASP.NET Core does not install the old single-threaded SynchronizationContext, but starvation remains.
4. Prefer async all the way and bound concurrency at the resource boundary.

## Resources

- **Threads:** One blocked worker per actively executing synchronous Wait/Result.
- **Queues:** Continuations may wait for available workers, increasing latency.

## Constraints and pitfalls

- No deadlock does not imply good throughput.
- Task.Run(() => SomeAsync().Result) merely moves the blocking work; it does not make I/O nonblocking.

## Review questions

- [Q-016: Why are .Result and .Wait() dangerous in ASP.NET Core? Is a deadlock guaranteed?](../../../questions/dotnet/en/Q-016-sync-over-async-deadlocks.md)

## Reinforcement challenges

—

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[Русский](../sync-over-async.md) · [English](sync-over-async.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/sync-over-async)
