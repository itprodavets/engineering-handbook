# Q-016 — Sync-over-async / blocking

[Русский](./Q-016-sync-over-async-deadlocks.md) · [English](en/Q-016-sync-over-async-deadlocks.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-016) · [Основная тема](../../topics/dotnet/sync-over-async.md) · [← Предыдущий](Q-015-whenall-multiple-exceptions.md) · [Следующий →](Q-017-configureawait-and-context.md)

## Вопрос

Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

.Result и .Wait() блокируют вызывающий поток до завершения Task, увеличивая риск ThreadPool starvation. Deadlock не гарантирован: классический случай связан с однопоточным SynchronizationContext; стандартный ASP.NET Core его не устанавливает.

</details>

---

[Русский](./Q-016-sync-over-async-deadlocks.md) · [English](en/Q-016-sync-over-async-deadlocks.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-016) · [Основная тема](../../topics/dotnet/sync-over-async.md) · [← Предыдущий](Q-015-whenall-multiple-exceptions.md) · [Следующий →](Q-017-configureawait-and-context.md)
