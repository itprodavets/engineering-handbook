# Engineering Handbook

**RU / EN • Languages, runtimes, distributed systems, databases, infrastructure and system design.**

> Техническая база знаний: от C#-синтаксиса и IL/JIT до потоков ОС, CPU, конкурентного доступа к памяти и распределённых систем. Each question includes a concise Russian and English reference answer.

**Статус:** первый модуль — C#/.NET; Go, Kafka и прочие разделы предусмотрены структурой и будут наполняться без искусственно сгенерированных «готовых» уроков.

## Навигация / Navigation

| Раздел | Содержимое |
|---|---|
| [C# / .NET — 35 interview questions](questions/dotnet/README.md) | Теория, ответы RU/EN и задания с подвохом |
| [C# / .NET language internals](languages/csharp/README.md) | async/await, Task, ValueTask, контексты |
| [CLR / JIT / ThreadPool](runtimes/clr/README.md) | Граница CLR ↔ OS Scheduler ↔ CPU |
| [Concurrency & memory model](computer-science/concurrency/README.md) | Race condition, volatile, Interlocked, lock |
| [Mechanics & resources](docs/internals-reference.md) | 21 подробное определение RU/EN по слоям |
| [Terminology / Глоссарий](docs/glossary.md) | 31 термин RU/EN |
| [Runnable labs / Примеры](labs/README.md) | 12 запускаемых C# 14 / .NET 10 файлов |
| [How to run code](docs/execution.md) | Codespaces, CLI, Actions |
| [Technical accuracy rules](docs/technical-accuracy.md) | Гарантии, ресурсы, риски, профилирование |
| [Go](languages/go/README.md) | Скелет будущего раздела |
| [Kafka](distributed-systems/kafka/README.md) | Скелет будущего раздела |
| [PostgreSQL](databases/postgresql/README.md) | Скелет будущего раздела |
| [Linux / OS](infrastructure/linux/README.md) | Скелет будущего раздела |
| [System design](system-design/README.md) | Скелет будущего раздела |

## Запустить код / Run a snippet

GitHub Markdown не исполняет fenced code blocks. Поэтому **каждый сложный пример имеет отдельный `.cs`**, пригодный для запуска через .NET 10 SDK.

```bash
dotnet --version   # requires .NET 10 SDK or later
dotnet run --file labs/dotnet/Q-024.cs  # prints ABC
./scripts/run-lab.sh Q-025            # prints ACB
```

**Без установки на компьютер:** открой репозиторий в GitHub → **Code → Codespaces → Create codespace**, перейди к соответствующему `.cs` и запусти `dotnet run --file ...` в терминале Codespaces. Или открой **Actions → Run one lab** и выбери ID задания (после публикации репозитория).

[Подробная инструкция / Execution guide](docs/execution.md) · [Microsoft: .NET 10 file-based apps](https://learn.microsoft.com/en-us/dotnet/core/sdk/file-based-apps)

## Interview questions / Содержание по ID

| ID | Тема / Topic | ID | Тема / Topic |
|---|---|---|---|
| [Q-001](questions/dotnet/Q-001-async-io-scalability.md) | Async / I/O | [Q-002](questions/dotnet/Q-002-thread-id-after-await.md) | Async / потоки |
| [Q-003](questions/dotnet/Q-003-what-is-io.md) | Основы I/O | [Q-004](questions/dotnet/Q-004-async-postgres-pipeline.md) | CLR / ОС / сеть |
| [Q-005](questions/dotnet/Q-005-cpu-during-io.md) | CPU vs I/O | [Q-006](questions/dotnet/Q-006-hundred-threads-eight-cores.md) | OS Scheduler |
| [Q-007](questions/dotnet/Q-007-threadpool-vs-os-scheduler.md) | ThreadPool / Scheduler | [Q-008](questions/dotnet/Q-008-task-vs-thread.md) | Task / Thread |
| [Q-009](questions/dotnet/Q-009-task-delay-vs-thread-sleep.md) | Task.Delay / Thread.Sleep | [Q-010](questions/dotnet/Q-010-task-whenall-execution.md) | Task.WhenAll / execution |
| [Q-011](questions/dotnet/Q-011-threadpool-worker-creation.md) | ThreadPool / создание потоков | [Q-012](questions/dotnet/Q-012-async-starts-synchronously.md) | Async / first await |
| [Q-013](questions/dotnet/Q-013-completed-await-and-scheduling.md) | Await / completed task | [Q-014](questions/dotnet/Q-014-whenany-faulted-task.md) | Task.WhenAny / faults |
| [Q-015](questions/dotnet/Q-015-whenall-multiple-exceptions.md) | Task.WhenAll / exceptions | [Q-016](questions/dotnet/Q-016-sync-over-async-deadlocks.md) | Sync-over-async / blocking |
| [Q-017](questions/dotnet/Q-017-configureawait-and-context.md) | ConfigureAwait / contexts | [Q-018](questions/dotnet/Q-018-cancellationtoken-taskrun.md) | CancellationToken |
| [Q-019](questions/dotnet/Q-019-valuetask-consumption.md) | ValueTask / reuse | [Q-020](questions/dotnet/Q-020-await-inside-lock.md) | lock / async mutex |
| [Q-021](questions/dotnet/Q-021-volatile-vs-interlocked.md) | volatile / atomicity | [Q-022](questions/dotnet/Q-022-taskcompletionsource-continuations.md) | TaskCompletionSource / continuation |
| [Q-023](questions/dotnet/Q-023-asynclocal-executioncontext.md) | AsyncLocal / ExecutionContext | [Q-024](questions/dotnet/Q-024-completed-await-output.md) | Completed await |
| [Q-025](questions/dotnet/Q-025-incomplete-await-output.md) | Incomplete await gate | [Q-026](questions/dotnet/Q-026-whenany-faulted-output.md) | WhenAny faulted |
| [Q-027](questions/dotnet/Q-027-whenall-exceptions-count.md) | WhenAll exceptions | [Q-028](questions/dotnet/Q-028-lost-update-race.md) | Lost update |
| [Q-029](questions/dotnet/Q-029-lock-new-object.md) | Wrong lock object | [Q-030](questions/dotnet/Q-030-cancellation-after-start.md) | Cancellation after start |
| [Q-031](questions/dotnet/Q-031-asynclocal-flow.md) | AsyncLocal flow | [Q-032](questions/dotnet/Q-032-configureawait-thread-id.md) | ConfigureAwait(false) |
| [Q-033](questions/dotnet/Q-033-startnew-nested-task.md) | StartNew nested Task | [Q-034](questions/dotnet/Q-034-semaphore-waitasync.md) | Semaphore nonreentrant |
| [Q-035](questions/dotnet/Q-035-parallel-foreach-async-void.md) | Parallel.ForEach async void | — | — |

## Principles

- **Точность вместо расплывчатых сравнений:** отдельно считать Task, worker threads, OS threads, heap allocations, timer registrations, очереди и соединения.
- **Контракт vs реализация:** гарантии C#/.NET не смешивать с эвристиками ThreadPool, JIT/GC и результатами бенчмарков.
- **Source-first:** ссылки на .NET source / Microsoft Learn; фиксировать версию runtime для экспериментов.
- **Safe to publish:** личные ответы, оценки и история обучения остаются в приватном Google Sheets, **в GitHub записаны только учебные задачи и эталонные ответы**.

[Contributing / Формат новых вопросов](CONTRIBUTING.md) · [Стандарт доказательности](docs/technical-accuracy.md)
