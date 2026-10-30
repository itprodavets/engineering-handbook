# Q-008 — ThreadPool and the OS scheduler

[Русский](../Q-008-task-vs-thread.md) · [English](./Q-008-task-vs-thread.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-008) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-007-threadpool-vs-os-scheduler.md) · [Next →](Q-009-task-delay-vs-thread-sleep.md)

## Question

What is the difference between Task and Thread in .NET? Does a Task create a new thread, and what does await do?

<details>
<summary>Model answer — reveal after your attempt</summary>

A Thread is an OS-scheduled execution path. A Task represents an operation's completion (and a result with Task<T>), not a dedicated thread. Task.Run usually queues work to the ThreadPool; awaiting incomplete asynchronous I/O suspends the method without blocking its worker.

</details>

---

[Русский](../Q-008-task-vs-thread.md) · [English](./Q-008-task-vs-thread.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-008) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-007-threadpool-vs-os-scheduler.md) · [Next →](Q-009-task-delay-vs-thread-sleep.md)
