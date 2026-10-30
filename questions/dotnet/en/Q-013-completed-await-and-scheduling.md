# Q-013 — The async/await execution lifecycle

[Русский](../Q-013-completed-await-and-scheduling.md) · [English](./Q-013-completed-await-and-scheduling.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-013) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-012-async-starts-synchronously.md) · [Next →](Q-014-whenany-faulted-task.md)

## Question

Does await always suspend, allocate a worker, or switch threads?

<details>
<summary>Model answer — reveal after your attempt</summary>

No. An already completed awaitable continues synchronously. An incomplete await registers a continuation and suspends the method; await itself does not create a thread.

</details>

---

[Русский](../Q-013-completed-await-and-scheduling.md) · [English](./Q-013-completed-await-and-scheduling.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-013) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-012-async-starts-synchronously.md) · [Next →](Q-014-whenany-faulted-task.md)
