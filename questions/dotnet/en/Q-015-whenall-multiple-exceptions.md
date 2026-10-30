# Q-015 — Task composition and exceptions

[Русский](../Q-015-whenall-multiple-exceptions.md) · [English](./Q-015-whenall-multiple-exceptions.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-015) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-014-whenany-faulted-task.md) · [Next →](Q-016-sync-over-async-deadlocks.md)

## Question

How does Task.WhenAll handle several faulted tasks and what does await throw?

<details>
<summary>Model answer — reveal after your attempt</summary>

The aggregate task is Faulted and preserves all task failures in Exception.InnerExceptions. A regular await throws one exception; inspect the aggregate task for the complete set.

</details>

---

[Русский](../Q-015-whenall-multiple-exceptions.md) · [English](./Q-015-whenall-multiple-exceptions.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-015) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-014-whenany-faulted-task.md) · [Next →](Q-016-sync-over-async-deadlocks.md)
