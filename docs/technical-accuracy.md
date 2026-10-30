# Technical accuracy policy / Стандарт инженерной точности

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](internals-reference.md) · [Запуск / Run](execution.md)

Каждая новая тема или вопрос описывается по следующим аспектам:

1. **Определение:** что конструкция означает и чем не является.
2. **Компиляция:** что делает Roslyn, какие IL и state machines появляются.
3. **Runtime:** что делают CLR, JIT, GC и API библиотек.
4. **OS / hardware:** какие потоки, системные вызовы, виртуальная память и CPU задействованы.
5. **Ресурсы:** heap allocations (bytes), Task count, OS thread count, stack reservation/commit, очередь, CPU time, handles, sockets, locks.
6. **Failure modes:** race, deadlock, contention, starvation, false sharing, resource exhaustion.
7. **Verifiability:** sample code, expected and allowed output, docs/source URL, runtime/platform and diagnostics.

## Evidence levels

- **Language/API contract:** гарантировано спецификацией или документацией.
- **Implementation:** верно для конкретной версии runtime/провайдера/ОС; может измениться.
- **Measurement:** точное значение зависит от среды и нагрузки, проверять BenchmarkDotNet, dotnet-counters, dotnet-trace, ETW/perf.

**Avoid:** «значительно больше памяти», «await создаёт поток», «всегда переключается», «каждая Task — новый OS thread», «ровно N CPU%» без конкретных условий.

**Prefer:** «каждый запущенный `Thread.Sleep` удерживает один ThreadPool worker на интервал сна», «у каждого таймера нет отдельного заблокированного worker», «число созданных ThreadPool потоков динамически выбирается runtime». 

## Sources and verification

- [Microsoft async internals](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)
- [Microsoft ThreadPool](https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool)
- [Microsoft starvation diagnostics](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)
- [21 mechanisms and resource profiles](internals-reference.md)
- [Run 12 reproducible experiments](../labs/README.md)

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](internals-reference.md) · [Запуск / Run](execution.md)
