# Q-007 — ThreadPool and the OS scheduler

[Русский](../Q-007-threadpool-vs-os-scheduler.md) · [English](./Q-007-threadpool-vs-os-scheduler.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-007) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-006-hundred-threads-eight-cores.md) · [Next →](Q-008-task-vs-thread.md)

## Question

What is the difference between the .NET ThreadPool and the OS scheduler? Who decides which CPU core runs a thread?

<details>
<summary>Model answer — reveal after your attempt</summary>

The ThreadPool manages queued work and .NET worker threads. The OS scheduler assigns runnable OS threads to logical processors and may preempt or migrate them. A Task is not a Thread.

</details>

---

[Русский](../Q-007-threadpool-vs-os-scheduler.md) · [English](./Q-007-threadpool-vs-os-scheduler.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-007) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-006-hundred-threads-eight-cores.md) · [Next →](Q-008-task-vs-thread.md)
