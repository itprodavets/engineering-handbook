# Q-023 — Continuations and execution contexts

[Русский](../Q-023-asynclocal-executioncontext.md) · [English](./Q-023-asynclocal-executioncontext.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-023) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-022-taskcompletionsource-continuations.md) · [Next →](Q-024-completed-await-output.md)

## Question

Why does AsyncLocal<T> flow through Task.Run to another thread while ThreadStatic does not?

<details>
<summary>Model answer — reveal after your attempt</summary>

AsyncLocal<T> belongs to the logical ExecutionContext, which normally flows through async work and Task.Run. ThreadStatic is tied to a specific physical thread and does not follow thread changes.

</details>

---

[Русский](../Q-023-asynclocal-executioncontext.md) · [English](./Q-023-asynclocal-executioncontext.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-023) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-022-taskcompletionsource-continuations.md) · [Next →](Q-024-completed-await-output.md)
