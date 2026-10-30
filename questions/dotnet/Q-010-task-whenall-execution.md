# Q-010 — Task.WhenAll / execution

[Русский](./Q-010-task-whenall-execution.md) · [English](en/Q-010-task-whenall-execution.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-010) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-009-task-delay-vs-thread-sleep.md) · [Следующий →](Q-011-threadpool-worker-creation.md)

## Вопрос

Создаёт ли Task.WhenAll новые потоки и запускает ли сам переданные ему задачи?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. Task.WhenAll создаёт задачу, которая завершается, когда завершились все переданные задачи; потоки он не создаёт. Task.Delay запускает таймер при вызове, Task.Run ставит делегат в очередь при вызове; при ленивом Select эти вызовы выполняются при перечислении Task.WhenAll.

</details>

---

[Русский](./Q-010-task-whenall-execution.md) · [English](en/Q-010-task-whenall-execution.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-010) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-009-task-delay-vs-thread-sleep.md) · [Следующий →](Q-011-threadpool-worker-creation.md)
