# The async/await execution lifecycle

[Русский](../async-lifecycle.md) · [English](async-lifecycle.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/async-lifecycle)

From a C# method call to I/O completion and continuation.

## Definition

async/await composes incomplete operations without requiring the caller’s thread to block. It does not create parallelism or make PostgreSQL run faster. Awaiting a completed operation may not suspend at all.

## Mechanics: C# to OS

1. Roslyn lowers the async method into a state machine with MoveNext, awaiters, and saved state.
2. Execution starts on the calling thread until an await encounters an incomplete operation.
3. A continuation is registered; no worker must remain dedicated to that wait. .NET and the OS kernel manage the socket.
4. After I/O becomes ready, continuation code decodes and materializes results using CPU time; the thread and core may differ.

## Resources

- **Threads:** No dedicated blocked worker thread for a properly asynchronous pending wait.
- **CPU:** Needed before the wait and when processing the result; the core can run other threads meanwhile.
- **Memory:** Operation state, continuation, and network buffers; exact bytes depend on the implementation.

## Constraints and pitfalls

- Do not assume every await switches threads or always allocates a distinct Task.
- Async APIs do not remove database connection-pool, dataset, or throughput limits.

## Review questions

- [Q-001: Why does ToListAsync() scale better than Task.Run(() => ToList()) under 1,000 concurrent HTTP requests?](../../../questions/dotnet/en/Q-001-async-io-scalability.md)
- [Q-003: What does I/O stand for, and what kind of I/O occurs when querying PostgreSQL?](../../../questions/dotnet/en/Q-003-what-is-io.md)
- [Q-004: What happens inside .NET, the OS kernel and CPU between sending an asynchronous SQL query and receiving the result?](../../../questions/dotnet/en/Q-004-async-postgres-pipeline.md)
- [Q-005: PostgreSQL takes five seconds to execute a query. What does the .NET server's CPU core do while awaiting ToListAsync()?](../../../questions/dotnet/en/Q-005-cpu-during-io.md)
- [Q-012: Does calling an async Task method start a new thread or run synchronously at first?](../../../questions/dotnet/en/Q-012-async-starts-synchronously.md)
- [Q-013: Does await always suspend, allocate a worker, or switch threads?](../../../questions/dotnet/en/Q-013-completed-await-and-scheduling.md)

## Reinforcement challenges

- [Q-024: What is the output and why? The awaited Task is already complete.](../../../questions/dotnet/en/Q-024-completed-await-output.md)
- [Q-025: What is the output? The method awaits an incomplete TaskCompletionSource.](../../../questions/dotnet/en/Q-025-incomplete-await-output.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)
- [https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)

---

[Русский](../async-lifecycle.md) · [English](async-lifecycle.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/async-lifecycle)
