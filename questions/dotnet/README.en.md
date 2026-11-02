# .NET / C# questions and exercises

[Русский](README.md) · [English](README.en.md)

[Home](../../README.en.md) · [Interactive learning](https://itprodavets.github.io/engineering-handbook/#/en/home)

Each question belongs to exactly one canonical lesson; related code challenges serve as reinforcement rather than repeated theory. Model answers are hidden until you attempt the question.

## The async/await execution lifecycle

[Canonical lesson](../../topics/dotnet/en/async-lifecycle.md)

- [Q-001](en/Q-001-async-io-scalability.md): Why does ToListAsync() scale better than Task.Run(() => ToList()) under 1,000 concurrent HTTP requests?
- [Q-003](en/Q-003-what-is-io.md): What does I/O stand for, and what kind of I/O occurs when querying PostgreSQL?
- [Q-004](en/Q-004-async-postgres-pipeline.md): What happens inside .NET, the OS kernel and CPU between sending an asynchronous SQL query and receiving the result?
- [Q-005](en/Q-005-cpu-during-io.md): PostgreSQL takes five seconds to execute a query. What does the .NET server's CPU core do while awaiting ToListAsync()?
- [Q-012](en/Q-012-async-starts-synchronously.md): Does calling an async Task method start a new thread or run synchronously at first?
- [Q-013](en/Q-013-completed-await-and-scheduling.md): Does await always suspend, allocate a worker, or switch threads?
- [Q-024](en/Q-024-completed-await-output.md): What is the output and why? The awaited Task is already complete. — reinforcement
- [Q-025](en/Q-025-incomplete-await-output.md): What is the output? The method awaits an incomplete TaskCompletionSource. — reinforcement
- [Q-036](en/Q-036-apm-eap-tap-history.md): How was asynchronous I/O performed before async/await, and when did APM, EAP and TAP appear? — reinforcement
- [Q-037](en/Q-037-apm-vs-taskrun-read.md): Why can NetworkStream.BeginRead scale better than Task.Run(() => stream.Read(...))?
- [Q-038](en/Q-038-inline-apm-callback-captured-result.md): What does a callback print if invoked inline before assigning result = BeginRead(...)? — reinforcement

## ThreadPool and the OS scheduler

[Canonical lesson](../../topics/dotnet/en/threadpool-scheduling.md)

- [Q-006](en/Q-006-hundred-threads-eight-cores.md): How can eight physical CPU cores handle 100 runnable threads?
- [Q-007](en/Q-007-threadpool-vs-os-scheduler.md): What is the difference between the .NET ThreadPool and the OS scheduler? Who decides which CPU core runs a thread?
- [Q-008](en/Q-008-task-vs-thread.md): What is the difference between Task and Thread in .NET? Does a Task create a new thread, and what does await do?
- [Q-009](en/Q-009-task-delay-vs-thread-sleep.md): What happens to the ThreadPool when 10,000 Task.Delay(5000) operations run versus 10,000 Task.Run(() => Thread.Sleep(5000)) operations?
- [Q-010](en/Q-010-task-whenall-execution.md): Does Task.WhenAll create threads or start the tasks passed to it?
- [Q-011](en/Q-011-threadpool-worker-creation.md): What does it mean when the ThreadPool creates an additional thread, and why do 10,000 Tasks not imply 10,000 threads?

## Task composition and exceptions

[Canonical lesson](../../topics/dotnet/en/task-composition.md)

- [Q-014](en/Q-014-whenany-faulted-task.md): Does awaiting Task.WhenAny throw the winning task's exception or cancel the other tasks?
- [Q-015](en/Q-015-whenall-multiple-exceptions.md): How does Task.WhenAll handle several faulted tasks and what does await throw?
- [Q-026](en/Q-026-whenany-faulted-output.md): What does it print, and does awaiting WhenAny throw the winning task's exception? — reinforcement
- [Q-027](en/Q-027-whenall-exceptions-count.md): How many exceptions are stored by WhenAll when two input Tasks fault? — reinforcement
- [Q-033](en/Q-033-startnew-nested-task.md): What is the task type, and does awaiting outer once wait for the inner async operation? — reinforcement
- [Q-052](en/Q-052-await-producer-publishes-data.md): Why does reading data after await producer yield 42 without volatile? — reinforcement
- [Q-053](en/Q-053-whenall-does-not-order-producer-consumer.md): Can Consumer print zero even if the caller later awaits Task.WhenAll(producer,consumer)? — reinforcement
- [Q-054](en/Q-054-task-delay-is-not-synchronization.md): Why does awaiting Task.Delay(100) not establish producer completion or visibility? — reinforcement
- [Q-055](en/Q-055-whenany-winner-vs-continuation-time.md): If Task.Delay wins WhenAny, must producer still be incomplete when the continuation executes? — reinforcement
- [Q-056](en/Q-056-whenany-faulted-winner-exception.md): Does awaiting WhenAny throw the winner's exception? What does awaiting the returned Task do? — reinforcement
- [Q-057](en/Q-057-whenall-multiple-exceptions-await-one.md): How many InnerExceptions are stored for two faulted tasks, and what does await combined propagate? — reinforcement
- [Q-058](en/Q-058-whenall-faulted-priority-over-canceled.md): What status does WhenAll(Faulted,Canceled) have, and what does await propagate? — reinforcement
- [Q-059](en/Q-059-whenany-does-not-cancel-loser.md): Does WhenAny cancel losing tasks and what happens to them? — reinforcement
- [Q-060](en/Q-060-whenall-waits-not-fail-fast.md): If one input task is already Faulted and another is pending, does WhenAll complete immediately? — reinforcement

## Shared memory and synchronization

[Canonical lesson](../../topics/dotnet/en/shared-memory.md)

- [Q-020](en/Q-020-await-inside-lock.md): Why is await prohibited inside lock, and how does SemaphoreSlim.WaitAsync differ?
- [Q-021](en/Q-021-volatile-vs-interlocked.md): Why is volatile counter++ unsafe, and how do Interlocked.Increment and lock differ?
- [Q-028](en/Q-028-lost-update-race.md): Is counter always 10,000? Why or why not? — reinforcement
- [Q-029](en/Q-029-lock-new-object.md): Does lock(new object()) protect counter from concurrent increments? — reinforcement
- [Q-034](en/Q-034-semaphore-waitasync.md): What does second.IsCompleted print after another WaitAsync without Release? — reinforcement
- [Q-035](en/Q-035-parallel-foreach-async-void.md): Does Parallel.ForEach wait for async lambda continuations, and what output is guaranteed? — reinforcement
- [Q-039](en/Q-039-race-condition-vs-data-race.md): How do race conditions differ from data races, and can a logical race occur without a data race?
- [Q-040](en/Q-040-lost-update-two-task-run.md): What outcomes are possible after two Task.Run(() => state.Value++) and awaiting Task.WhenAll, starting at Value=0? — reinforcement
- [Q-041](en/Q-041-volatile-does-not-make-plus-plus-atomic.md): Why does volatile int Value not make Value++ atomic, and what ordering does C# volatile provide?
- [Q-042](en/Q-042-interlocked-increment-ref.md): What does Interlocked.Increment(ref int) guarantee, and why is ref unrelated to Counter being a reference type? — reinforcement
- [Q-043](en/Q-043-check-then-act-stock-negative.md): Can stock become -1 after a volatile positive check and an Interlocked.Decrement when starting at stock=1? — reinforcement
- [Q-044](en/Q-044-compareexchange-returns-prior.md): Starting from stock=1, what does CompareExchange(ref stock,0,1) return and what is stock afterward? — reinforcement
- [Q-045](en/Q-045-two-buyers-single-item-cas.md): Can both threads successfully execute CompareExchange(ref stock,0,1) when stock starts at 1? — reinforcement
- [Q-046](en/Q-046-two-buyers-stock-three-single-cas.md): If stock=3 and two threads perform CompareExchange(ref stock,2,3), how many succeed and what do the calls return? — reinforcement
- [Q-047](en/Q-047-cas-loop-five-buyers.md): How does a CAS loop behave with stock=3/two buyers and stock=1/five buyers? — reinforcement
- [Q-048](en/Q-048-safe-publication-acquire-release.md): Why does data=42 before release-store and acquire-reading ready safely publish 42? — reinforcement
- [Q-049](en/Q-049-release-before-data-allows-zero.md): Can the consumer see zero if producer publishes ready before writing data? — reinforcement
- [Q-050](en/Q-050-nonvolatile-loop-jit-hoisting.md): Does while(ready==0) without volatile necessarily terminate after another thread writes ready=1?
- [Q-051](en/Q-051-thread-yield-is-not-memory-fence.md): Why does Thread.Yield in an ordinary polling loop not replace Volatile.Read?
- [Q-064](en/Q-064-monitor-exit-after-await.md): Why does Monitor.Exit after await on another thread throw? — reinforcement
- [Q-065](en/Q-065-semaphore-permits-vs-threads.md): What does SemaphoreSlim(2,2) mean with two pending delays and two additional tasks? — reinforcement
- [Q-066](en/Q-066-semaphore-nested-async-deadlock.md): What if Outer holds SemaphoreSlim(1,1) and awaits Inner, which also awaits it? — reinforcement
- [Q-067](en/Q-067-semaphore-canceled-wait-overrelease.md): Why can finally Release after a canceled WaitAsync corrupt the count? — reinforcement

## Continuations and execution contexts

[Canonical lesson](../../topics/dotnet/en/execution-context.md)

- [Q-002](en/Q-002-thread-id-after-await.md): Must Environment.CurrentManagedThreadId be the same before and after await ToListAsync()? If not, did await create a new thread?
- [Q-017](en/Q-017-configureawait-and-context.md): What exactly does ConfigureAwait(false) change? Does it suppress ExecutionContext?
- [Q-022](en/Q-022-taskcompletionsource-continuations.md): Why can SetResult under a lock run unexpected code, and what does RunContinuationsAsynchronously change?
- [Q-023](en/Q-023-asynclocal-executioncontext.md): Why does AsyncLocal<T> flow through Task.Run to another thread while ThreadStatic does not?
- [Q-031](en/Q-031-asynclocal-flow.md): Does Task.Run print X or null? — reinforcement
- [Q-032](en/Q-032-configureawait-thread-id.md): Does awaiting CompletedTask.ConfigureAwait(false) change the managed thread ID? — reinforcement

## Cancellation of asynchronous work

[Canonical lesson](../../topics/dotnet/en/cancellation.md)

- [Q-018](en/Q-018-cancellationtoken-taskrun.md): Can CancellationToken forcibly stop a running Task.Run, and is it passed to the delegate automatically?
- [Q-030](en/Q-030-cancellation-after-start.md): Will the program print DONE when the token is canceled after the delegate starts? — reinforcement
- [Q-061](en/Q-061-fromexception-oce-vs-fromcanceled.md): Why is Task.FromException(OCE) Faulted but Task.FromCanceled(token) Canceled? — reinforcement
- [Q-062](en/Q-062-async-task-oce-builder-canceled.md): Why is async Task throwing OCE Canceled while Task.FromException(OCE) is Faulted? — reinforcement
- [Q-063](en/Q-063-async-task-throws-after-completed-await.md): Does calling TestAsync synchronously throw InvalidOperationException if its body awaits CompletedTask then throws? — reinforcement

## ValueTask<T> and allocation trade-offs

[Canonical lesson](../../topics/dotnet/en/valuetask.md)

- [Q-019](en/Q-019-valuetask-consumption.md): Why isn't it always safe to await ValueTask<T> twice, and does it always save memory?

## Blocking and sync-over-async

[Canonical lesson](../../topics/dotnet/en/sync-over-async.md)

- [Q-016](en/Q-016-sync-over-async-deadlocks.md): Why are .Result and .Wait() dangerous in ASP.NET Core? Is a deadlock guaranteed?

## Microservices: concurrency, networking, payments and PostgreSQL

[Canonical lesson](../../topics/dotnet/en/microservices-concurrency.md)

- [Q-068](en/Q-068-static-semaphore-three-pods.md): Does static SemaphoreSlim(1,1) protect a last-item SKU across three Pods? — reinforcement
- [Q-069](en/Q-069-network-await-permit-lifetime.md): During a five-second await ChargeAsync, does CheckoutAsync hold a worker or a permit? — reinforcement
- [Q-070](en/Q-070-three-pods-provider-quota.md): How many concurrent payment calls with three Pods each using SemaphoreSlim(5,5)?
- [Q-071](en/Q-071-payment-timeout-duplicate-charge.md): Can retrying ChargeAsync after a lost bank reply charge twice? — reinforcement
- [Q-072](en/Q-072-outbox-not-charge-idempotency.md): Why does Transactional Outbox not replace payment-provider idempotency?
- [Q-073](en/Q-073-remote-timeout-not-rollback.md): Does gRPC DeadlineExceeded or local CancellationToken roll back an already committed payment?
- [Q-074](en/Q-074-postgres-read-committed-check-act.md): Can two Pods under READ COMMITTED both read available=1 and then reach -1 via unconditional UPDATE?
- [Q-075](en/Q-075-postgres-conditional-update-returning.md): How can one UPDATE ... RETURNING statement protect the last item?
