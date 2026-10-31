# I/O-bound and CPU-bound work

[Русский](../io-vs-cpu-bound.md) · [English](io-vs-cpu-bound.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/io-vs-cpu-bound)

> Distinguish computation, network waiting, and physical resources.

## Definition

I/O-bound work is limited by external I/O latency or throughput; CPU-bound work by instruction execution. Querying PostgreSQL includes both CPU activity and network waiting.

## Internal mechanics

1. Before sending SQL, CPU time is spent in EF Core/Npgsql and request serialization.
2. During a pending asynchronous wait, no worker is dedicated to that request; the OS may schedule other threads.
3. After data arrives, CPU work resumes for reading, decoding, materialization, and the HTTP response.
4. Async does not make PostgreSQL faster: connection pools, database throughput, and result size remain limiting factors.

## Step-by-step explanation

### Elapsed waiting is not CPU time

Elapsed request time includes client computation, network/database waits and response processing. A five-second SQL query does not consume five seconds of ASP.NET Core CPU: during pending asynchronous I/O, the worker can execute other work. EF Core and the provider still use CPU to prepare SQL, transfer bytes, decode values and materialize objects.

### Awaiting an operation does not release a specific CPU core

A .NET worker is an OS thread placed on a logical CPU by the OS scheduler. `await` does not release a named core: for an incomplete operation the async method registers a continuation and returns control. The worker can process other jobs; the OS chooses its logical CPU. An already completed Task may not suspend at all.

### What actually limits throughput

For 1,000 HTTP requests distinguish request count, active database connections, executing SQL commands, blocked workers and pending Tasks. The PostgreSQL connection pool can limit concurrent queries before the ThreadPool is stressed. `ToListAsync()` also materializes results in memory; projection and pagination remain important.

### What can be verified

Observe CPU time, `dotnet.thread_pool.thread.count`, `dotnet.thread_pool.queue.length`, DB connections and p95/p99 latency. These measure different resources. Low CPU with a growing queue is a diagnostic signal, not by itself proof of starvation.


## Resources

CPU time before/after waiting; socket and buffers during I/O; zero dedicated blocked workers for properly asynchronous pending reads.

## Pitfalls and constraints

Do not treat database I/O as a separate hardware channel: a remote PostgreSQL query usually uses network I/O on the client.

## Example

```csharp
var orders = await db.Orders.AsNoTracking().ToListAsync(ct);
```

## Runnable experiments

- [01-await-control-flow.cs](../../../../labs/dotnet/async-internals/01-await-control-flow.cs) — `dotnet run --file labs/dotnet/async-internals/01-await-control-flow.cs`

## Review questions

- [Q-003: What does I/O stand for, and what kind of I/O occurs when querying PostgreSQL?](../../../../questions/dotnet/en/Q-003-what-is-io.md)
- [Q-005: PostgreSQL takes five seconds to execute a query. What does the .NET server's CPU core do while awaiting ToListAsync()?](../../../../questions/dotnet/en/Q-005-cpu-during-io.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Define I/O-bound work and name two specific bottlenecks for a PostgreSQL request.

<details>
<summary>Answer criteria</summary>

Mentions I/O latency/throughput and concrete examples such as network, connection-pool capacity or DB throughput; distinguishes CPU work.

</details>

### 2. Explain

Explain CPU execution before, during and after awaiting ToListAsync().

<details>
<summary>Answer criteria</summary>

Before: preparation/send; pending wait: no worker held by this request; after: read/materialize/respond. Avoid claiming the CPU is always idle.

</details>

### 3. Predict

If SQL takes five seconds, does the HTTP worker remain blocked for those five seconds with true async I/O?

<details>
<summary>Answer criteria</summary>

No for a truly pending asynchronous wait. A synchronous completion is possible; CPU is still used while handling results.

</details>

### 4. Diagnose

At 1,000 requests CPU=25% and p99 latency rises. Why can’t you assume ThreadPool starvation? What would you inspect?

<details>
<summary>Answer criteria</summary>

Check pool threads, pending work and stacks, DB connections, query plans and downstream latency. Low CPU alone is ambiguous.

</details>

### 5. Design

How would you bound concurrent database queries without blocking worker threads?

<details>
<summary>Answer criteria</summary>

Use async SemaphoreSlim.WaitAsync or bounded Channel, Release in finally, cancellation, timeouts and metrics; avoid synchronous waits.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Next →](awaiter-completion-path.md) · [Русский](../io-vs-cpu-bound.md) · [English](io-vs-cpu-bound.md)
