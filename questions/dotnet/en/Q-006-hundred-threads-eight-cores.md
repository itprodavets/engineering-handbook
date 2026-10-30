# Q-006 — ThreadPool and the OS scheduler

[Русский](../Q-006-hundred-threads-eight-cores.md) · [English](./Q-006-hundred-threads-eight-cores.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-006) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-005-cpu-during-io.md) · [Next →](Q-007-threadpool-vs-os-scheduler.md)

## Question

How can eight physical CPU cores handle 100 runnable threads?

<details>
<summary>Model answer — reveal after your attempt</summary>

The OS scheduler shares CPU time among runnable threads. It can preempt an unfinished thread, save its execution context and run another. Without SMT, up to eight threads execute simultaneously, but all 100 can make progress over time.

</details>

---

[Русский](../Q-006-hundred-threads-eight-cores.md) · [English](./Q-006-hundred-threads-eight-cores.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-006) · [Canonical lesson](../../../topics/dotnet/en/threadpool-scheduling.md) · [← Previous](Q-005-cpu-during-io.md) · [Next →](Q-007-threadpool-vs-os-scheduler.md)
