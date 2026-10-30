# Engineering Handbook — software engineering learning

[Русский](README.md) · [English](README.en.md)

**Interactive course:** [Open the learning app](https://itprodavets.github.io/engineering-handbook/#/en/home).

A technical learning handbook covering languages, runtimes, concurrency, infrastructure, and distributed systems. One canonical lesson per concept, with separate reinforcement exercises.

## Curriculum

- [The async/await execution lifecycle](topics/dotnet/en/async-lifecycle.md) — 8 questions and exercises
- [ThreadPool and the OS scheduler](topics/dotnet/en/threadpool-scheduling.md) — 6 questions and exercises
- [Task composition and exceptions](topics/dotnet/en/task-composition.md) — 5 questions and exercises
- [Shared memory and synchronization](topics/dotnet/en/shared-memory.md) — 6 questions and exercises
- [Continuations and execution contexts](topics/dotnet/en/execution-context.md) — 6 questions and exercises
- [Cancellation of asynchronous work](topics/dotnet/en/cancellation.md) — 2 questions and exercises
- [ValueTask<T> and allocation trade-offs](topics/dotnet/en/valuetask.md) — 1 questions and exercises
- [Blocking and sync-over-async](topics/dotnet/en/sync-over-async.md) — 1 questions and exercises

## Practical challenges and code

- [Questions and answers](questions/dotnet/README.en.md)
- [Runnable C# labs](labs/README.en.md)
- [Open Codespaces](https://codespaces.new/itprodavets/engineering-handbook)
- [Run a selected lab through Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml)

## Running C#

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

GitHub Pages does not compile C#. Use Codespaces or GitHub Actions for actual execution; in-browser answer checking compares your prediction against the reference, not executed C#.

## Planned learning tracks

Go, Kafka, PostgreSQL, Kubernetes, Linux, and system design. These tracks will be filled with actual lessons, without duplicating theory.

## Learning progress

Personal answers and scores remain in the private Google Sheet, not in this repository. The browser app saves progress only on your device. GitHub Pages may be publicly reachable even when the repository is private.

[Contributing](CONTRIBUTING.en.md)
