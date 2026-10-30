# Q-009 — ThreadPool and the OS scheduler

[Русский](../Q-009-task-delay-vs-thread-sleep.md) · [English](./Q-009-task-delay-vs-thread-sleep.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-009) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-008-task-vs-thread.md) · [Next →](Q-010-task-whenall-execution.md)

## Question

What happens to the ThreadPool when 10,000 Task.Delay(5000) operations run versus 10,000 Task.Run(() => Thread.Sleep(5000)) operations?

<details>
<summary>Model answer — reveal after your attempt</summary>

10,000 Task.Delay operations require zero dedicated blocked worker threads while their timers are pending. Task.Run queues 10,000 delegates; each executing Thread.Sleep blocks one worker for five seconds. The ThreadPool may reuse idle workers or create additional ones; the exact count is workload-dependent.

</details>

---

[Русский](../Q-009-task-delay-vs-thread-sleep.md) · [English](./Q-009-task-delay-vs-thread-sleep.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-009) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-008-task-vs-thread.md) · [Next →](Q-010-task-whenall-execution.md)
