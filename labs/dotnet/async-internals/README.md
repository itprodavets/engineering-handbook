# Async/Await — лаборатории / Labs

[Русский](README.md) · [English](README.en.md)

[Учебный модуль](../../../topics/dotnet/async-lifecycle.md) · [Главная](../../../README.md)

Это **воспроизводимые эксперименты**, а не замена сгенерированного IL и профилирования. Для всех требуется .NET 10 SDK.

| Пример | Механизм | Команда |
|---|---|---|
| 01 | Завершённый и незавершённый await | `dotnet run --file labs/dotnet/async-internals/01-await-control-flow.cs` |
| 02 | AsyncStateMachineAttribute и IAsyncStateMachine | `dotnet run --file labs/dotnet/async-internals/02-state-machine-reflection.cs` |
| 03 | Реальный async TCP I/O на loopback | `dotnet run --file labs/dotnet/async-internals/03-socket-simulation.cs` |
| 04 | Выделения managed-памяти на текущем потоке | `dotnet run --file labs/dotnet/async-internals/04-allocations.cs` |
| 05 | ThreadPool threads / work items под небольшим блокированием | `dotnet run --file labs/dotnet/async-internals/05-queue-diagnostics.cs` |

**Ограничение:** 04–05 выводят *наблюдения*, а не нормативные числа потоков и байтов. Не сравнивай измерения на разных машинах как идентичные.

Для реального IL: собери код, изучи state machine в ILSpy или SharpLab. Для runtime events используй dotnet-trace / dotnet-counters.

[Методика проверки на собеседовании](../../../docs/engineering-interview.md)
