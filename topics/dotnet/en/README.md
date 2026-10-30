# Canonical .NET / C# lessons

[Русский](../README.md) · [English](README.md)

Core mechanisms have one home; related challenges reinforce them instead of repeating the theory.

- [The async/await execution lifecycle](async-lifecycle.md) — From a C# method call to I/O completion and continuation.
- [ThreadPool and the OS scheduler](threadpool-scheduling.md) — Who schedules work items and who selects CPU cores.
- [Task composition and exceptions](task-composition.md) — WhenAny, WhenAll, nested Tasks, and observing failures.
- [Shared memory and synchronization](shared-memory.md) — Races, atomicity, locks, Interlocked and SemaphoreSlim.
- [Continuations and execution contexts](execution-context.md) — SynchronizationContext, TaskScheduler, AsyncLocal and ConfigureAwait.
- [Cancellation of asynchronous work](cancellation.md) — What CancellationToken actually does and does not do.
- [ValueTask<T> and allocation trade-offs](valuetask.md) — When it helps—and why it is not always faster.
- [Blocking and sync-over-async](sync-over-async.md) — Why .Result and .Wait() are risky and where deadlocks come from.
