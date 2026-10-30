# Q-010 — ThreadPool and the OS scheduler

[Русский](../Q-010-task-whenall-execution.md) · [English](./Q-010-task-whenall-execution.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-010) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-009-task-delay-vs-thread-sleep.md) · [Next →](Q-011-threadpool-worker-creation.md)

## Question

Does Task.WhenAll create threads or start the tasks passed to it?

<details>
<summary>Model answer — reveal after your attempt</summary>

No. Task.WhenAll returns an aggregate Task that completes when all supplied tasks finish; it neither creates threads nor starts existing tasks. Task.Delay schedules its timer when invoked; Task.Run queues its delegate when invoked. With lazy Select, those calls occur as WhenAll enumerates the sequence.

</details>

---

[Русский](../Q-010-task-whenall-execution.md) · [English](./Q-010-task-whenall-execution.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-010) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-009-task-delay-vs-thread-sleep.md) · [Next →](Q-011-threadpool-worker-creation.md)
