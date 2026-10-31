# Production case: p99 latency and ThreadPool starvation

[Русский](../async-production-capstone.md) · [English](async-production-capstone.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-production-capstone)

> Learn to prove the cause of latency and design a justified fix.

## Definition

High latency with low CPU is a symptom, not a diagnosis. Causes include sync-over-async, ThreadPool queues, database connection-pool limits, slow SQL, network timeouts or downstream backpressure.

## Internal mechanics

1. List competing hypotheses: ThreadPool, DB pool, SQL latency, network and lock contention.
2. Collect metrics: p50/p95/p99, pool thread count, pending work, CPU, DB connections, rates and errors.
3. Use dotnet-stack/dotnet-trace to identify blocked workers and sync-over-async stacks.
4. Fix the root cause, apply bounded concurrency and timeouts/cancellation, verify under a load test.

## Step-by-step explanation

### Step 1: competing hypotheses

Scenario: 1,000 concurrent requests, CPU=20%, p99=12 seconds and rising worker count. This is compatible with ThreadPool starvation but may also involve DB pool contention. Rising ThreadPool queue length and stacks in Task.Wait/.Result support a sync-over-async hypothesis. Stable ThreadPool queue with growing DB pool waits points toward the DB layer.

### Step 2: measure rather than guess

Observe dotnet.thread_pool.thread.count (existing threads), dotnet.thread_pool.queue.length (pending work items), CPU time, active DB connections and HTTP p99. No single metric is a full diagnosis. .NET 10 can run `dnx dotnet-counters monitor -p <PID>`; account for diagnostic overhead in production.

### Step 3: remediation and trade-offs

Remove .Result/.Wait() from async paths; do not wrap synchronous I/O in Task.Run. Bound DB operations with async SemaphoreSlim/Channel, remembering that per-instance limits are not global. Apply projection, pagination and CancellationToken. Raising ThreadPool minimum threads may mask symptoms rather than fixing the blocking code.

### Step 4: prove improvement

Run comparable before/after load tests: throughput, latency percentiles, errors, thread count, queue length, DB pool occupancy and CPU. Record .NET version, CPU count and pool limits; avoid drawing conclusions from one run. Capture a trace for intermittent issues.


## Resources

ThreadPool workers/queues, DB connections, sockets, memory, CPU and retries; capacity limits require measurement.

## Pitfalls and constraints

CPU=20% alone does not prove ThreadPool starvation. Connection-pool contention can look similar; wrapping in Task.Run can make it worse.

## Example

```csharp
await semaphore.WaitAsync(ct);
try { return await db.Orders.AsNoTracking().Take(100).ToListAsync(ct); }
finally { semaphore.Release(); }
```

## Runnable experiments

- [05-queue-diagnostics.cs](../../../../labs/dotnet/async-internals/05-queue-diagnostics.cs) — `dotnet run --file labs/dotnet/async-internals/05-queue-diagnostics.cs`

## Review questions


## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Name two observable signs of possible ThreadPool starvation.

<details>
<summary>Answer criteria</summary>

Growing thread count/queued work and latency, potentially low CPU; clues, not proof.

</details>

### 2. Explain

Why does .Result block a worker even if the inner I/O is asynchronous?

<details>
<summary>Answer criteria</summary>

Synchronous wait occupies the caller until the Task completes, even if inner I/O uses continuations.

</details>

### 3. Predict

What happens under load with Task.Run(() => DbQueryAsync().Result)?

<details>
<summary>Answer criteria</summary>

A worker blocks in Result; work queues/thread count may grow; this does not make I/O nonblocking.

</details>

### 4. Diagnose

CPU=20%, p99 increases, ThreadPool queue=0, DB pool waits increase. Where do you investigate first?

<details>
<summary>Answer criteria</summary>

Investigate DB pool occupancy, SQL duration and downstream DB first, corroborating with other evidence.

</details>

### 5. Design

Design a fix for 1,000 requests with 100 DB connections and explain bounded concurrency trade-offs.

<details>
<summary>Answer criteria</summary>

Async end-to-end, pagination, concurrency bound relative to the relevant pool, backpressure, timeouts and cancellation; monitor queue depth and p99.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)
- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime)

---

[← Previous](async-memory-and-allocations.md) · [Русский](../async-production-capstone.md) · [English](async-production-capstone.md)
