# Shared memory and synchronization

[Русский](../shared-memory.md) · [English](shared-memory.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/shared-memory)

Races, atomicity, locks, Interlocked and SemaphoreSlim.

## Definition

Concurrent Tasks can mutate the same object. Task.WhenAll only waits for completion; it does not make operations atomic. Synchronization protects shared-state invariants, not a particular “thread”.

## Mechanics: C# to OS

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

## Reinforcement challenges

- [Q-028: Is counter always 10,000? Why or why not?](../../../questions/dotnet/en/Q-028-lost-update-race.md)
- [Q-029: Does lock(new object()) protect counter from concurrent increments?](../../../questions/dotnet/en/Q-029-lock-new-object.md)
- [Q-034: What does second.IsCompleted print after another WaitAsync without Release?](../../../questions/dotnet/en/Q-034-semaphore-waitasync.md)
- [Q-035: Does Parallel.ForEach wait for async lambda continuations, and what output is guaranteed?](../../../questions/dotnet/en/Q-035-parallel-foreach-async-void.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)
- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

---

[Русский](../shared-memory.md) · [English](shared-memory.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/shared-memory)
