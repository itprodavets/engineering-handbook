# From PostgreSQL to epoll/IOCP and continuations

[Русский](../async-socket-pipeline.md) · [English](async-socket-pipeline.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-socket-pipeline)

> Trace SQL, sockets, the OS kernel, and resumption in C#.

## Definition

Npgsql sends a query over a socket. A pending asynchronous receive waits for I/O readiness/completion through runtime and OS mechanisms, not one blocked worker per query.

## Internal mechanics

1. EF Core translates LINQ into a command; Npgsql acquires a connection, forms protocol messages, and sends bytes.
2. On Linux, socket readiness may be observed via epoll; on Windows, completion-based I/O uses IOCP.
3. The network stack receives data; the runtime resumes reads and EF Core materializes rows.
4. A large response may interleave multiple reads, CPU processing and waits; one await need not mean one network receive.

## Step-by-step explanation

### The EF Core → Npgsql → Socket boundary

EF Core translates LINQ, Npgsql handles the PostgreSQL protocol and connection, and Socket/NetworkStream use OS APIs. SQL latency includes work on the database server; the client does not dedicate one CPU or worker for the entire remote wait.

### What the OS kernel actually does

On Linux .NET can use epoll-based socket polling; Windows socket I/O uses IOCP. They differ in implementation but both avoid a dedicated blocked worker per pending read. Runtime I/O event threads may exist: zero dedicated workers per wait does not mean zero threads in the process.

### Why one result may require multiple reads

As packets arrive, the kernel updates socket readiness, the runtime resumes read operations, Npgsql decodes protocol messages and EF Core materializes rows. Large results can alternate between I/O readiness and CPU decoding; ToListAsync does not mean the OS kernel constructs the entire C# list.

### Connection pools, timeouts and backpressure

When fewer database connections are available than incoming HTTP requests, some operations wait for a free connection. Task count does not equal active SQL count. Use cancellation, connection timeouts, bounded concurrency and DB connection metrics.


## Resources

Socket/descriptor, connection pool, network buffers, managed objects, CPU while processing responses.

## Pitfalls and constraints

The database can bottleneck despite idle workers. Do not assume 1,000 requests imply 1,000 connections.

## Example

```csharp
await using var connection = new NpgsqlConnection(connectionString);
await connection.OpenAsync(ct);
```

## Runnable experiments

- [03-socket-simulation.cs](../../../../labs/dotnet/async-internals/03-socket-simulation.cs) — `dotnet run --file labs/dotnet/async-internals/03-socket-simulation.cs`

## Review questions

- [Q-001: Why does ToListAsync() scale better than Task.Run(() => ToList()) under 1,000 concurrent HTTP requests?](../../../../questions/dotnet/en/Q-001-async-io-scalability.md)
- [Q-004: What happens inside .NET, the OS kernel and CPU between sending an asynchronous SQL query and receiving the result?](../../../../questions/dotnet/en/Q-004-async-postgres-pipeline.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Name the responsibilities of EF Core, Npgsql, Socket APIs and the OS kernel.

<details>
<summary>Answer criteria</summary>

EF Core handles query/materialization, Npgsql the protocol/connection, Socket/OS network bytes, not SQL objects.

</details>

### 2. Explain

How can a pending network read avoid a dedicated blocked worker on Linux/Windows?

<details>
<summary>Answer criteria</summary>

Linux epoll readiness or Windows IOCP completion; runtime resumes the continuation, with CPU used for callbacks and decoding.

</details>

### 3. Predict

If 1,000 HTTP requests await PostgreSQL with a pool limit of 100 connections, do all 1,000 SQL queries execute at once?

<details>
<summary>Answer criteria</summary>

No; connection pool/application limits prevent that. At most 100 connections from that pool, active SQL may be fewer.

</details>

### 4. Diagnose

p99 rises, client CPU is low, ThreadPool queue stable and DB pool waits grow. Which layer is more likely the bottleneck?

<details>
<summary>Answer criteria</summary>

The connection pool/DB, not proven starvation. Inspect SQL duration, pool occupancy, plans and network.

</details>

### 5. Design

For a heavy API, choose unlimited ToListAsync, synchronous Task.Run or bounded async with pagination. Why?

<details>
<summary>Answer criteria</summary>

Bounded asynchronous I/O with pagination/projection, timeouts and monitoring based on actual DB pool capacity.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Previous](async-state-machine.md) · [Next →](async-memory-and-allocations.md) · [Русский](../async-socket-pipeline.md) · [English](async-socket-pipeline.md)
