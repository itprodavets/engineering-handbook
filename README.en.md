# Engineering Handbook — software engineering learning

[Русский](README.md) · [English](README.en.md)

**Interactive course:** [Open the learning app](https://itprodavets.github.io/engineering-handbook/#/en/home).

A technical learning handbook covering languages, runtimes, concurrency, infrastructure, and distributed systems. One canonical lesson per concept, with separate reinforcement exercises.

## Curriculum

| Area | Topics |
|---|---|
| [Programming languages](catalog/en/programming-languages.md) | C# / .NET, Go, Python, TypeScript / JavaScript, Rust, Java |
| [Databases and storage](catalog/en/databases.md) | PostgreSQL, SQL / query optimization, Redis, SQLite, Search / Elasticsearch, Vector databases |
| [AI, LLM, and RAG](catalog/en/ai-llm-rag.md) | LLMs and transformers, Retrieval-Augmented Generation, AI agents, Embeddings and retrieval, Model Context Protocol, LLM evaluation |
| [Messaging and streaming](catalog/en/messaging-streaming.md) | Apache Kafka, RabbitMQ, NATS, Stream processing |
| [Distributed systems](catalog/en/distributed-systems.md) | Distributed algorithms, gRPC / Protocol Buffers, Consistency, Retry, backpressure, circuit breaker |
| [Runtimes, OS, and memory](catalog/en/runtimes-systems.md) | CLR / JIT / GC, Go runtime, JVM, OS and virtual memory |
| [Software architecture and system design](catalog/en/software-architecture.md) | System design, DDD / Clean Architecture, Design patterns, API design |
| [Infrastructure and operations](catalog/en/infrastructure.md) | Linux, Docker / OCI, Kubernetes, Cloud / networking, CI/CD, OpenTelemetry / observability |
| [Algorithms and computer science](catalog/en/computer-science.md) | Algorithms, Data structures, Concurrency and memory, Performance engineering |
| [Security and quality](catalog/en/security-quality.md) | Testing / property-based testing, OWASP / application security, Cryptography, Load / chaos testing |

[Full catalog](catalog/README.en.md)

### .NET / C#

- [The async/await execution lifecycle](topics/dotnet/en/async-lifecycle.md) — 11 questions and exercises
- [ThreadPool and the OS scheduler](topics/dotnet/en/threadpool-scheduling.md) — 6 questions and exercises
- [Task composition and exceptions](topics/dotnet/en/task-composition.md) — 5 questions and exercises
- [Shared memory and synchronization](topics/dotnet/en/shared-memory.md) — 15 questions and exercises
- [Continuations and execution contexts](topics/dotnet/en/execution-context.md) — 6 questions and exercises
- [Cancellation of asynchronous work](topics/dotnet/en/cancellation.md) — 2 questions and exercises
- [ValueTask<T> and allocation trade-offs](topics/dotnet/en/valuetask.md) — 1 questions and exercises
- [Blocking and sync-over-async](topics/dotnet/en/sync-over-async.md) — 1 questions and exercises


## Deep-dive learning and flashcards

- [C# / .NET deep-dive units](topics/dotnet/units/en/README.md)
- [Know / Don't know flashcards](https://itprodavets.github.io/engineering-handbook/#/en/cards)
- [Spaced-repetition method](docs/learning-method.en.md)

## Practical challenges and code

- [.NET / C# — Questions](questions/dotnet/README.en.md)
- [Runnable C# labs](labs/README.en.md)
- [Open Codespaces](https://codespaces.new/itprodavets/engineering-handbook)
- [Run a selected lab through Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml)

## Running C#

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

GitHub Pages does not compile C#. Use Codespaces or GitHub Actions for actual execution; in-browser answer checking compares your prediction against the reference, not executed C#.

## Planned learning tracks

Go, Kafka, PostgreSQL, Kubernetes, Linux, System Design. New tracks are added when their first verified canonical lesson is ready.

## Learning progress

Personal answers and scores remain in the private Google Sheet, not in this repository. The browser app saves progress only on your device. GitHub Pages may be publicly reachable even when the repository is private.

[Add topics from ChatGPT](docs/chat-authoring.en.md) · [Contributing](CONTRIBUTING.en.md)

[Repository layout](docs/repository-layout.en.md) · [Why no SQLite](docs/storage.en.md) · [Benchmarks](benchmarks/README.en.md)
