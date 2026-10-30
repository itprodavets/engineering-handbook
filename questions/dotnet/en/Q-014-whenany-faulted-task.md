# Q-014 — Task composition and exceptions

[Русский](../Q-014-whenany-faulted-task.md) · [English](./Q-014-whenany-faulted-task.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-014) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-013-completed-await-and-scheduling.md) · [Next →](Q-015-whenall-multiple-exceptions.md)

## Question

Does awaiting Task.WhenAny throw the winning task's exception or cancel the other tasks?

<details>
<summary>Model answer — reveal after your attempt</summary>

No. WhenAny completes successfully with the first completed task, even if it faulted. Await that inner task to observe its exception; the remaining tasks continue unless canceled separately.

</details>

---

[Русский](../Q-014-whenany-faulted-task.md) · [English](./Q-014-whenany-faulted-task.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-014) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-013-completed-await-and-scheduling.md) · [Next →](Q-015-whenall-multiple-exceptions.md)
