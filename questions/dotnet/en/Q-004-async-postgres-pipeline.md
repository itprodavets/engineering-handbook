# Q-004 — The async/await execution lifecycle

[Русский](../Q-004-async-postgres-pipeline.md) · [English](./Q-004-async-postgres-pipeline.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-004) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-003-what-is-io.md) · [Next →](Q-005-cpu-during-io.md)

## Question

What happens inside .NET, the OS kernel and CPU between sending an asynchronous SQL query and receiving the result?

<details>
<summary>Model answer — reveal after your attempt</summary>

Npgsql sends SQL over a socket. If the response is pending, await suspends the method and frees the worker while the OS monitors socket readiness (for example, epoll on Linux). Once data arrives, .NET resumes processing and Npgsql/EF Core read and materialize the result using CPU time.

</details>

---

[Русский](../Q-004-async-postgres-pipeline.md) · [English](./Q-004-async-postgres-pipeline.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-004) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-003-what-is-io.md) · [Next →](Q-005-cpu-during-io.md)
