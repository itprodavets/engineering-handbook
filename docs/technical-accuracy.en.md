# Technical accuracy standard

[Русский](technical-accuracy.md) · [English](technical-accuracy.en.md)

[Home](../README.en.md) · [Curriculum](../topics/dotnet/en/README.md)

Every mechanism has **one canonical explanation**. Questions and runnable labs link back to that lesson instead of restating its theory.

## Every technical claim distinguishes

1. **Language/API contract:** what the C# specification or .NET API actually guarantees.
2. **Implementation detail:** behavior of a specific Roslyn, CLR, JIT or library version.
3. **Resource usage:** CPU, managed heap, OS thread, stack, queues, timers and connections independently.
4. **Concurrency risks:** conditions for deadlock, races, contention and starvation.
5. **Verification:** diagnostics, benchmarks, measurable outputs and experiment limitations.

Avoid imprecise claims such as “uses more memory”, “is faster” or “creates a thread.” Never invent thread counts, allocation sizes or elapsed time; measure them under declared conditions.

## Reproducibility

Runnable source files are under [labs/](../labs/README.en.md). Nondeterministic cases must be checked against valid properties rather than one observed output. The learning interface clearly separates prediction checking from actual C# execution.
