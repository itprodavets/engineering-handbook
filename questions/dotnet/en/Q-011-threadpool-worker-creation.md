# Q-011 — ThreadPool and the OS scheduler

[Русский](../Q-011-threadpool-worker-creation.md) · [English](./Q-011-threadpool-worker-creation.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-011) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-010-task-whenall-execution.md) · [Next →](Q-012-async-starts-synchronously.md)

## Question

What does it mean when the ThreadPool creates an additional thread, and why do 10,000 Tasks not imply 10,000 threads?

<details>
<summary>Model answer — reveal after your attempt</summary>

The ThreadPool first reuses available workers. If queued work exceeds available worker capacity, it may create additional OS threads within its limits. A Task.Delay timer does not reserve a blocked worker per delay; the number of new workers depends on the workload and current pool state.

</details>

---

[Русский](../Q-011-threadpool-worker-creation.md) · [English](./Q-011-threadpool-worker-creation.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-011) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-010-task-whenall-execution.md) · [Next →](Q-012-async-starts-synchronously.md)
