# Runnable C# labs / Запускаемые примеры

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](../languages/csharp/README.md) · [Запуск / Run](../docs/execution.md)

**Requires .NET 10 SDK.** Each lab is a standalone file-based application. No external NuGet dependencies or project scaffolding are required.

| ID | Challenge | CLI command | Expected / allowed output |
|---|---|---|---|
| [Q-024](../questions/dotnet/Q-024-completed-await-output.md) | Completed await | `dotnet run --file labs/dotnet/Q-024.cs` | `ABC` |
| [Q-025](../questions/dotnet/Q-025-incomplete-await-output.md) | Incomplete await gate | `dotnet run --file labs/dotnet/Q-025.cs` | `ACB` |
| [Q-026](../questions/dotnet/Q-026-whenany-faulted-output.md) | WhenAny faulted | `dotnet run --file labs/dotnet/Q-026.cs` | `True` |
| [Q-027](../questions/dotnet/Q-027-whenall-exceptions-count.md) | WhenAll exceptions | `dotnet run --file labs/dotnet/Q-027.cs` | `2` |
| [Q-028](../questions/dotnet/Q-028-lost-update-race.md) | Lost update | `dotnet run --file labs/dotnet/Q-028.cs` | `1..10000` |
| [Q-029](../questions/dotnet/Q-029-lock-new-object.md) | Wrong lock object | `dotnet run --file labs/dotnet/Q-029.cs` | `1..10000` |
| [Q-030](../questions/dotnet/Q-030-cancellation-after-start.md) | Cancellation after start | `dotnet run --file labs/dotnet/Q-030.cs` | `DONE` |
| [Q-031](../questions/dotnet/Q-031-asynclocal-flow.md) | AsyncLocal flow | `dotnet run --file labs/dotnet/Q-031.cs` | `X` |
| [Q-032](../questions/dotnet/Q-032-configureawait-thread-id.md) | ConfigureAwait(false) | `dotnet run --file labs/dotnet/Q-032.cs` | `True` |
| [Q-033](../questions/dotnet/Q-033-startnew-nested-task.md) | StartNew nested Task | `dotnet run --file labs/dotnet/Q-033.cs` | `Outer awaited\nInner awaited` |
| [Q-034](../questions/dotnet/Q-034-semaphore-waitasync.md) | Semaphore nonreentrant | `dotnet run --file labs/dotnet/Q-034.cs` | `False` |
| [Q-035](../questions/dotnet/Q-035-parallel-foreach-async-void.md) | Parallel.ForEach async void | `dotnet run --file labs/dotnet/Q-035.cs` | `AXXX` |

Run an individual example:

```bash
./scripts/run-lab.sh Q-024
# or: dotnet run --file labs/dotnet/Q-024.cs
```

**Q-028 and Q-029:** output is nondeterministic; the range is a property to check, not a promise that a race occurs on every run.

**Q-035:** the lab adds a completion gate to prevent the process from exiting before outstanding `async void` continuations complete. This preserves the trap while making the demonstration reproducible.

[Run in Codespaces or GitHub Actions](../docs/execution.md) · [Accuracy and verification rules](../docs/technical-accuracy.md)

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](../languages/csharp/README.md) · [Запуск / Run](../docs/execution.md)
