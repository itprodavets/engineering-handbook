# Q-022 — Continuations and execution contexts

[Русский](../Q-022-taskcompletionsource-continuations.md) · [English](./Q-022-taskcompletionsource-continuations.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-022) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-021-volatile-vs-interlocked.md) · [Next →](Q-023-asynclocal-executioncontext.md)

## Question

Why can SetResult under a lock run unexpected code, and what does RunContinuationsAsynchronously change?

<details>
<summary>Model answer — reveal after your attempt</summary>

Task continuations may run inline when SetResult completes the task, including while the caller holds a lock. RunContinuationsAsynchronously prevents inline execution of continuations and mitigates reentrancy or lock-inversion hazards.

</details>

---

[Русский](../Q-022-taskcompletionsource-continuations.md) · [English](./Q-022-taskcompletionsource-continuations.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-022) · [Canonical lesson](../../../topics/dotnet/en/execution-context.md) · [← Previous](Q-021-volatile-vs-interlocked.md) · [Next →](Q-023-asynclocal-executioncontext.md)
