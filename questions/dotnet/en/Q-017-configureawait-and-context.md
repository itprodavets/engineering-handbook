# Q-017 — Continuations and execution contexts

[Русский](../Q-017-configureawait-and-context.md) · [English](./Q-017-configureawait-and-context.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-017) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-016-sync-over-async-deadlocks.md) · [Next →](Q-018-cancellationtoken-taskrun.md)

## Question

What exactly does ConfigureAwait(false) change? Does it suppress ExecutionContext?

<details>
<summary>Model answer — reveal after your attempt</summary>

For standard Task awaiting it avoids capturing SynchronizationContext or a non-default TaskScheduler for the continuation. It neither creates a thread nor suppresses ExecutionContext or AsyncLocal flow.

</details>

---

[Русский](../Q-017-configureawait-and-context.md) · [English](./Q-017-configureawait-and-context.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-017) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-016-sync-over-async-deadlocks.md) · [Next →](Q-018-cancellationtoken-taskrun.md)
