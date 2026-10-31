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

## Resources

CPU time before/after waiting; socket and buffers during I/O; zero dedicated blocked workers for properly asynchronous pending reads.

## Pitfalls and constraints

Do not treat database I/O as a separate hardware channel: a remote PostgreSQL query usually uses network I/O on the client.

## Example

```csharp
var orders = await db.Orders.AsNoTracking().ToListAsync(ct);
```

## Review questions

- [Q-003: What does I/O stand for, and what kind of I/O occurs when querying PostgreSQL?](../../../../questions/dotnet/en/Q-003-what-is-io.md)
- [Q-005: PostgreSQL takes five seconds to execute a query. What does the .NET server's CPU core do while awaiting ToListAsync()?](../../../../questions/dotnet/en/Q-005-cpu-during-io.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Next →](async-state-machine.md) · [Русский](../io-vs-cpu-bound.md) · [English](io-vs-cpu-bound.md)
