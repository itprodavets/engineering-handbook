# Deep-dive learning units

[Русский](../README.md) · [English](README.md)

One mechanism, one canonical explanation; questions reinforce it.

## [The async/await execution lifecycle](../../en/async-lifecycle.md)

- [I/O-bound and CPU-bound work](io-vs-cpu-bound.md) — Distinguish computation, network waiting, and physical resources.
- [The awaiter contract and synchronous completion](awaiter-completion-path.md) — Understand GetAwaiter/IsCompleted/GetResult and why await may not suspend.
- [What the compiler generates for async/await](async-state-machine.md) — Understand MoveNext, awaiters and the IsCompleted fast path.
- [From PostgreSQL to epoll/IOCP and continuations](async-socket-pipeline.md) — Trace SQL, sockets, the OS kernel, and resumption in C#.
- [Memory, state machines and async allocation cost](async-memory-and-allocations.md) — Measure real async costs without inventing object sizes.
- [Production case: p99 latency and ThreadPool starvation](async-production-capstone.md) — Learn to prove the cause of latency and design a justified fix.

## [ThreadPool and the OS scheduler](../../en/threadpool-scheduling.md)

- [Thread, Task and Task.Run are distinct](task-vs-thread.md) — Separate OS execution units from operation completion objects.
- [The OS scheduler, CPU cores and ThreadPool](os-vs-runtime-scheduler.md) — Understand CPU time, preemption and .NET work queues.
- [ThreadPool starvation and blocking waits](threadpool-starvation.md) — Explain occupied workers and the source of queue growth.

## [Task composition and exceptions](../../en/task-composition.md)

- [WhenAll and WhenAny completion semantics](task-aggregation.md) — Distinguish waiting for all tasks from receiving the first completion.
- [Nested Tasks and StartNew(Func<Task>)](startnew-nested-tasks.md) — Separate completion of the outer Task from the inner async operation.

## [Shared memory and synchronization](../../en/shared-memory.md)

- [Atomicity, volatile and Interlocked](atomicity-and-memory-visibility.md) — Understand read-modify-write and memory visibility.
- [Monitor locks and SemaphoreSlim](mutual-exclusion-and-semaphores.md) — Distinguish thread blocking from asynchronous permit waiting.
- [Why Parallel.ForEach(async ...) is dangerous](parallel-foreach-async-void.md) — Explain why async void continuations escape loop completion.

## [Continuations and execution contexts](../../en/execution-context.md)

- [ExecutionContext and AsyncLocal<T>](executioncontext-asynclocal.md) — Understand logical context detached from OS thread identity.
- [SynchronizationContext and ConfigureAwait(false)](synchronizationcontext-configureawait.md) — Understand context capture and why thread switching is not guaranteed.
- [TaskCompletionSource and inline continuations](taskcontinuations-tcs.md) — Understand reentrancy and why SetResult under lock can be risky.

## [Cancellation of asynchronous work](../../en/cancellation.md)

- [CancellationToken is cooperative cancellation](cancellation-tokens.md) — Distinguish cancellation requests from forced thread termination.

## [ValueTask<T> and allocation trade-offs](../../en/valuetask.md)

- [ValueTask<T> and consumption contracts](valuetask-ivaluetasksource.md) — Understand why being a struct does not guarantee zero allocations.

## [Blocking and sync-over-async](../../en/sync-over-async.md)

- [Deadlocks and starvation with .Result/.Wait()](sync-over-async.md) — Distinguish a blocked worker, cyclic waits, and lack of progress.
