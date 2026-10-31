# Async/Await — runnable labs

[Русский](README.md) · [English](README.en.md)

[Learning module](../../../topics/dotnet/en/async-lifecycle.md) · [Home](../../../README.en.md)

These are **reproducible experiments**, not a substitute for emitted IL inspection or profiling. .NET 10 SDK required.

| Lab | Mechanism | Run |
|---|---|---|
| 01 | Completed vs pending await | `dotnet run --file labs/dotnet/async-internals/01-await-control-flow.cs` |
| 02 | AsyncStateMachineAttribute and IAsyncStateMachine | `dotnet run --file labs/dotnet/async-internals/02-state-machine-reflection.cs` |
| 03 | Real asynchronous TCP on loopback | `dotnet run --file labs/dotnet/async-internals/03-socket-simulation.cs` |
| 04 | Current-thread managed allocations | `dotnet run --file labs/dotnet/async-internals/04-allocations.cs` |
| 05 | ThreadPool threads/queued work during blocking | `dotnet run --file labs/dotnet/async-internals/05-queue-diagnostics.cs` |

**Limits:** 04–05 report *observations*, not normative thread counts or allocated bytes. Do not assume different machines produce equal results.

Inspect emitted IL in ILSpy or SharpLab; investigate runtime events using dotnet-trace/dotnet-counters.

[Interview methodology](../../../docs/engineering-interview.en.md)
