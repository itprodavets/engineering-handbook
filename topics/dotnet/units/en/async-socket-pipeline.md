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

## Resources

Socket/descriptor, connection pool, network buffers, managed objects, CPU while processing responses.

## Pitfalls and constraints

The database can bottleneck despite idle workers. Do not assume 1,000 requests imply 1,000 connections.

## Example

```csharp
await using var connection = new NpgsqlConnection(connectionString);
await connection.OpenAsync(ct);
```

## Review questions

- [Q-001: Why does ToListAsync() scale better than Task.Run(() => ToList()) under 1,000 concurrent HTTP requests?](../../../../questions/dotnet/en/Q-001-async-io-scalability.md)
- [Q-004: What happens inside .NET, the OS kernel and CPU between sending an asynchronous SQL query and receiving the result?](../../../../questions/dotnet/en/Q-004-async-postgres-pipeline.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Previous](async-state-machine.md) · [Русский](../async-socket-pipeline.md) · [English](async-socket-pipeline.md)
