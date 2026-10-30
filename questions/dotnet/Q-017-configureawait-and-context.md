# Q-017 — ConfigureAwait / contexts

[Русский](./Q-017-configureawait-and-context.md) · [English](en/Q-017-configureawait-and-context.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-017) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-016-sync-over-async-deadlocks.md) · [Следующий →](Q-018-cancellationtoken-taskrun.md)

## Вопрос

Что именно меняет ConfigureAwait(false)? Подавляет ли он ExecutionContext?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Для обычного Task-await он отключает возврат continuation в захваченный SynchronizationContext/нестандартный TaskScheduler. Он не создаёт поток и не отключает распространение ExecutionContext или AsyncLocal.

</details>

---

[Русский](./Q-017-configureawait-and-context.md) · [English](en/Q-017-configureawait-and-context.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-017) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-016-sync-over-async-deadlocks.md) · [Следующий →](Q-018-cancellationtoken-taskrun.md)
