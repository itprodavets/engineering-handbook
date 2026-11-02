# Shared memory and synchronization

[Русский](../shared-memory.md) · [English](shared-memory.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/shared-memory)

Races, atomicity, locks, Interlocked and SemaphoreSlim.

## Definition

Concurrent Tasks can mutate the same object. Task.WhenAll only waits for completion; it does not make operations atomic. Synchronization protects shared-state invariants, not a particular “thread”.

## Mechanics: language/runtime to OS

1. counter++ reads, computes, and writes; competing threads can lose an update.
2. Interlocked.Increment atomically changes one value; lock enforces mutual exclusion over a critical section.
3. lock(new object()) creates distinct monitors and does not protect shared state.
4. SemaphoreSlim.WaitAsync asynchronously waits for a permit but is not a reentrant mutex.

## Resources

- **Shared memory:** Shared mutable objects require consistently synchronized access.
- **Synchronization:** Monitors, atomic read–modify–write, and/or asynchronous waiter queues.
- **CPU:** Contention and retries can consume CPU; locks can increase latency.

## Constraints and pitfalls

- volatile does not make counter++ atomic.
- Lock ordering and retained permits can cause deadlock or long waits.

## Review questions

- [Q-020: Why is await prohibited inside lock, and how does SemaphoreSlim.WaitAsync differ?](../../../questions/dotnet/en/Q-020-await-inside-lock.md)
- [Q-021: Why is volatile counter++ unsafe, and how do Interlocked.Increment and lock differ?](../../../questions/dotnet/en/Q-021-volatile-vs-interlocked.md)
- [Q-039: How do race conditions differ from data races, and can a logical race occur without a data race?](../../../questions/dotnet/en/Q-039-race-condition-vs-data-race.md)
- [Q-041: Why does volatile int Value not make Value++ atomic, and what ordering does C# volatile provide?](../../../questions/dotnet/en/Q-041-volatile-does-not-make-plus-plus-atomic.md)
- [Q-050: Does while(ready==0) without volatile necessarily terminate after another thread writes ready=1?](../../../questions/dotnet/en/Q-050-nonvolatile-loop-jit-hoisting.md)
- [Q-051: Why does Thread.Yield in an ordinary polling loop not replace Volatile.Read?](../../../questions/dotnet/en/Q-051-thread-yield-is-not-memory-fence.md)

## Reinforcement challenges

- [Q-028: Is counter always 10,000? Why or why not?](../../../questions/dotnet/en/Q-028-lost-update-race.md)
- [Q-029: Does lock(new object()) protect counter from concurrent increments?](../../../questions/dotnet/en/Q-029-lock-new-object.md)
- [Q-034: What does second.IsCompleted print after another WaitAsync without Release?](../../../questions/dotnet/en/Q-034-semaphore-waitasync.md)
- [Q-035: Does Parallel.ForEach wait for async lambda continuations, and what output is guaranteed?](../../../questions/dotnet/en/Q-035-parallel-foreach-async-void.md)
- [Q-040: What outcomes are possible after two Task.Run(() => state.Value++) and awaiting Task.WhenAll, starting at Value=0?](../../../questions/dotnet/en/Q-040-lost-update-two-task-run.md)
- [Q-042: What does Interlocked.Increment(ref int) guarantee, and why is ref unrelated to Counter being a reference type?](../../../questions/dotnet/en/Q-042-interlocked-increment-ref.md)
- [Q-043: Can stock become -1 after a volatile positive check and an Interlocked.Decrement when starting at stock=1?](../../../questions/dotnet/en/Q-043-check-then-act-stock-negative.md)
- [Q-044: Starting from stock=1, what does CompareExchange(ref stock,0,1) return and what is stock afterward?](../../../questions/dotnet/en/Q-044-compareexchange-returns-prior.md)
- [Q-045: Can both threads successfully execute CompareExchange(ref stock,0,1) when stock starts at 1?](../../../questions/dotnet/en/Q-045-two-buyers-single-item-cas.md)
- [Q-046: If stock=3 and two threads perform CompareExchange(ref stock,2,3), how many succeed and what do the calls return?](../../../questions/dotnet/en/Q-046-two-buyers-stock-three-single-cas.md)
- [Q-047: How does a CAS loop behave with stock=3/two buyers and stock=1/five buyers?](../../../questions/dotnet/en/Q-047-cas-loop-five-buyers.md)
- [Q-048: Why does data=42 before release-store and acquire-reading ready safely publish 42?](../../../questions/dotnet/en/Q-048-safe-publication-acquire-release.md)
- [Q-049: Can the consumer see zero if producer publishes ready before writing data?](../../../questions/dotnet/en/Q-049-release-before-data-allows-zero.md)
- [Q-064: Why does Monitor.Exit after await on another thread throw?](../../../questions/dotnet/en/Q-064-monitor-exit-after-await.md)
- [Q-065: What does SemaphoreSlim(2,2) mean with two pending delays and two additional tasks?](../../../questions/dotnet/en/Q-065-semaphore-permits-vs-threads.md)
- [Q-066: What if Outer holds SemaphoreSlim(1,1) and awaits Inner, which also awaits it?](../../../questions/dotnet/en/Q-066-semaphore-nested-async-deadlock.md)
- [Q-067: Why can finally Release after a canceled WaitAsync corrupt the count?](../../../questions/dotnet/en/Q-067-semaphore-canceled-wait-overrelease.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)
- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

---

[Русский](../shared-memory.md) · [English](shared-memory.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/shared-memory)
