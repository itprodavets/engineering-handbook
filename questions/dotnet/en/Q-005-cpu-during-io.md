# Q-005 — The async/await execution lifecycle

[Русский](../Q-005-cpu-during-io.md) · [English](./Q-005-cpu-during-io.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-005) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-004-async-postgres-pipeline.md) · [Next →](Q-006-hundred-threads-eight-cores.md)

## Question

PostgreSQL takes five seconds to execute a query. What does the .NET server's CPU core do while awaiting ToListAsync()?

<details>
<summary>Model answer — reveal after your attempt</summary>

The CPU core is not reserved for the waiting request: the OS may run other threads or leave it idle. CPU time is still required before the wait to prepare/send SQL and afterwards to read and materialize the result.

</details>

---

[Русский](../Q-005-cpu-during-io.md) · [English](./Q-005-cpu-during-io.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-005) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-004-async-postgres-pipeline.md) · [Next →](Q-006-hundred-threads-eight-cores.md)
