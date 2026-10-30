# Q-013 — Await / completed task

[Русский](./Q-013-completed-await-and-scheduling.md) · [English](en/Q-013-completed-await-and-scheduling.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-013) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-012-async-starts-synchronously.md) · [Следующий →](Q-014-whenany-faulted-task.md)

## Вопрос

Всегда ли await приостанавливает метод, выделяет worker или переключает поток?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. Для уже завершённого awaitable GetAwaiter().IsCompleted позволяет продолжить выполнение синхронно. Незавершённый await регистрирует continuation; новый поток при этом не создаётся самим await.

</details>

---

[Русский](./Q-013-completed-await-and-scheduling.md) · [English](en/Q-013-completed-await-and-scheduling.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-013) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-012-async-starts-synchronously.md) · [Следующий →](Q-014-whenany-faulted-task.md)
