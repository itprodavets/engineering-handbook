# Deep engineering interview preparation: method and rubric

[Русский](engineering-interview.md) · [English](engineering-interview.en.md)

[Home](../README.en.md) · [Async/Await module](../topics/dotnet/en/async-lifecycle.md) · [Knowledge checks](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-state-machine)

## Principle

Interview competence is not a collection of memorized one-liners. For each mechanism complete five skill checks. Self-ratings are not certifications: validate capabilities with unseen code, emitted IL, runtime measurements and production reasoning.

| Level | Demonstrate | Suggested evaluation |
|---|---|---|
| **Recall** | Exact definitions and limitations | 30–60 seconds without hints |
| **Explain** | C# → Roslyn → IL/JIT → CLR → OS | 2–3 minutes with a clear sequence |
| **Predict** | Behavior of unfamiliar C# | Predict before running, then reproduce |
| **Diagnose** | Root cause of a failure or slowdown | Hypotheses, metrics/traces/stacks |
| **Design** | Justified production decisions | Resource bounds and trade-offs |

## Reference module: Async/Await

Follow [I/O-bound](../topics/dotnet/units/en/io-vs-cpu-bound.md) → [awaiter](../topics/dotnet/units/en/awaiter-completion-path.md) → [async state machine](../topics/dotnet/units/en/async-state-machine.md) → [socket I/O](../topics/dotnet/units/en/async-socket-pipeline.md) → [allocation](../topics/dotnet/units/en/async-memory-and-allocations.md) → [production diagnostics](../topics/dotnet/units/en/async-production-capstone.md).

Write explanations before revealing the evaluation rubric. Run related [labs](../labs/dotnet/async-internals/README.en.md) and record **runtime version, CPU, OS, connection limit and measured values**. Measurements are not language guarantees.

## Errors → spaced repetition

Grades of "Not yet" or "Partially" create a review card targeting that exact weak skill. A card links to the original lesson instead of duplicating the theory. Existing question cards become eligible after studying their canonical unit.

Self-ratings, typed answers and review schedules remain in the browser's localStorage and are not uploaded to public GitHub. No automatic semantic grading of written explanations is claimed; a human interviewer can verify the evidence.

## A strong explanation

Use exact terms and an ordered mechanism, while separating **API/language guarantees**, **implementation details**, and **observations**. For load-related questions, identify the resource bottleneck, its limits, instrumentation and falsifiable hypotheses.

A concise interview answer should survive detailed follow-up questions.
