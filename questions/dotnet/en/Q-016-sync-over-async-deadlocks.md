# Q-016 — Blocking and sync-over-async

[Русский](../Q-016-sync-over-async-deadlocks.md) · [English](./Q-016-sync-over-async-deadlocks.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-016) · [Canonical lesson](../../../topics/dotnet/en/sync-over-async.md) · [← Previous](Q-015-whenall-multiple-exceptions.md) · [Next →](Q-017-configureawait-and-context.md)

## Question

Why are .Result and .Wait() dangerous in ASP.NET Core? Is a deadlock guaranteed?

<details>
<summary>Model answer — reveal after your attempt</summary>

They block the caller and can cause ThreadPool starvation. Deadlock is not inevitable: the classic case involves a single-threaded SynchronizationContext, which standard ASP.NET Core does not install.

</details>

---

[Русский](../Q-016-sync-over-async-deadlocks.md) · [English](./Q-016-sync-over-async-deadlocks.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-016) · [Canonical lesson](../../../topics/dotnet/en/sync-over-async.md) · [← Previous](Q-015-whenall-multiple-exceptions.md) · [Next →](Q-017-configureawait-and-context.md)
