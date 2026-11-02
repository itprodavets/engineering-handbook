# Monitor, SemaphoreSlim and asynchronous deadlocks

[Русский](../mutual-exclusion-and-semaphores.md) · [English](mutual-exclusion-and-semaphores.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/mutual-exclusion-and-semaphores)

> Distinguish Monitor thread ownership, SemaphoreSlim permits, async deadlocks and cancellation errors.

## Definition

Monitor is thread-affine: Exit must run on the thread that entered. Manual Monitor.Enter across await compiles but may throw on cross-thread Exit. SemaphoreSlim(2,2) represents two permits, not two threads; WaitAsync need not block a worker. Nested waiting on one SemaphoreSlim(1,1) can deadlock asynchronously without blocked workers.

## Internal mechanics

1. Monitor.Enter acquires a monitor that await does not release.
2. Monitor.Exit from another worker throws SynchronizationLockException; await inside normal C# lock is prohibited.
3. SemaphoreSlim.WaitAsync with no available permit yields an incomplete Task; the worker can do other work.
4. While a Task.Delay or network operation is awaited, the acquired permit remains held until Release.
5. Outer awaits Inner; Inner awaits Outer’s permit: a circular asynchronous deadlock.
6. After a canceled WaitAsync no permit was acquired; unconditional Release in a finally around the wait corrupts the count.

## Step-by-step explanation

### Monitor.Enter across await

Monitor belongs to the thread that called Enter. After a real suspension, the continuation may run on another worker; Monitor.Exit then throws SynchronizationLockException. finally does not transfer ownership. The compiler disallows await inside normal lock, but manual Enter/Exit bypass that protection.

```csharp
Monitor.Enter(gate);
try { await Task.Delay(100); }
finally { Monitor.Exit(gate); } // unsafe
```

### Two permits are not two workers

SemaphoreSlim(2,2) permits two holders at once. While both await Task.Delay, both permits remain held but no dedicated worker is blocked. Further WaitAsync calls are pending when count is zero; Wait() would block. FIFO admission is not guaranteed.

### Async deadlock without blocked threads

OuterAsync acquires the sole permit, prints Outer entered and awaits InnerAsync. InnerAsync waits on that permit before reaching Inner entered, while Outer cannot finally-release before Inner completes. This is deadlock even with free workers. The lab cancels the pending wait to avoid hanging CI.

### Cancellation does not grant a release right

If WaitAsync(ct) is canceled before acquisition, awaiting it throws OperationCanceledException. A try/finally wrapping the wait still releases, inflating the count. Place await WaitAsync before try/finally or track acquisition explicitly.

```csharp
await sem.WaitAsync(ct);
try { await WorkAsync(); }
finally { sem.Release(); }
```


## Resources

Monitor thread affinity; SemaphoreSlim permits, wait queues, Task continuations and CPU when executing. Pending await does not require a dedicated blocked worker.

## Pitfalls and constraints

Do not hold Monitor across await. SemaphoreSlim is not reentrant, promises no FIFO and is not a distributed lock. Await acquisition before try/finally; Release only after successful acquisition.

## Example

```csharp
await semaphore.WaitAsync(ct);
try { await WorkAsync(ct); }
finally { semaphore.Release(); }
```

## Runnable experiments

- [Q-064.cs](../../../../labs/dotnet/Q-064.cs) — `dotnet run --file labs/dotnet/Q-064.cs`
- [Q-065.cs](../../../../labs/dotnet/Q-065.cs) — `dotnet run --file labs/dotnet/Q-065.cs`
- [Q-066.cs](../../../../labs/dotnet/Q-066.cs) — `dotnet run --file labs/dotnet/Q-066.cs`
- [Q-067.cs](../../../../labs/dotnet/Q-067.cs) — `dotnet run --file labs/dotnet/Q-067.cs`

## Review questions

- [Q-020: Why is await prohibited inside lock, and how does SemaphoreSlim.WaitAsync differ?](../../../../questions/dotnet/en/Q-020-await-inside-lock.md)
- [Q-029: Does lock(new object()) protect counter from concurrent increments?](../../../../questions/dotnet/en/Q-029-lock-new-object.md)
- [Q-034: What does second.IsCompleted print after another WaitAsync without Release?](../../../../questions/dotnet/en/Q-034-semaphore-waitasync.md)
- [Q-064: Why does Monitor.Exit after await on another thread throw?](../../../../questions/dotnet/en/Q-064-monitor-exit-after-await.md)
- [Q-065: What does SemaphoreSlim(2,2) mean with two pending delays and two additional tasks?](../../../../questions/dotnet/en/Q-065-semaphore-permits-vs-threads.md)
- [Q-066: What if Outer holds SemaphoreSlim(1,1) and awaits Inner, which also awaits it?](../../../../questions/dotnet/en/Q-066-semaphore-nested-async-deadlock.md)
- [Q-067: Why can finally Release after a canceled WaitAsync corrupt the count?](../../../../questions/dotnet/en/Q-067-semaphore-canceled-wait-overrelease.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

How do Monitor thread ownership and SemaphoreSlim permits differ?

<details>
<summary>Answer criteria</summary>

Monitor.Exit requires the owning thread; SemaphoreSlim Release does not check owner but must be balanced.

</details>

### 2. Explain

Why is a permit held while the worker is free during Task.Delay?

<details>
<summary>Answer criteria</summary>

Permit stays until Release; pending Task does not block a worker.

</details>

### 3. Predict

What prints for nested OuterAsync/InnerAsync on one SemaphoreSlim(1,1)?

<details>
<summary>Answer criteria</summary>

Only Outer entered, then a pending deadlock.

</details>

### 4. Diagnose

Why did CurrentCount increase after WaitAsync cancellation?

<details>
<summary>Answer criteria</summary>

finally Release ran without acquiring a permit.

</details>

### 5. Design

How should CancellationToken, WaitAsync and finally be composed?

<details>
<summary>Answer criteria</summary>

await WaitAsync(ct) before try; Release in finally only after successful acquisition.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor](https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit](https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
- [https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/](https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/)

---

[← Previous](compare-exchange-cas-loop.md) · [Next →](parallel-foreach-async-void.md) · [Русский](../mutual-exclusion-and-semaphores.md) · [English](mutual-exclusion-and-semaphores.md)
