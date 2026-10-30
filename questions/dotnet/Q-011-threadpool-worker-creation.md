# Q-011 — ThreadPool / создание потоков

[Русский](./Q-011-threadpool-worker-creation.md) · [English](en/Q-011-threadpool-worker-creation.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-011) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-010-task-whenall-execution.md) · [Следующий →](Q-012-async-starts-synchronously.md)

## Вопрос

Что означает «ThreadPool может создать дополнительный поток» при вызове Task.Run и почему это не означает 10 000 потоков для 10 000 Task?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

ThreadPool сначала использует имеющиеся свободные worker-потоки. Если работы в очереди больше, чем могут обработать доступные workers, пул может создать дополнительные ОС-потоки в рамках своих ограничений. Task.Delay не выделяет отдельный заблокированный поток на каждый таймер; конкретное число новых потоков зависит от нагрузки и состояния пула.

</details>

---

[Русский](./Q-011-threadpool-worker-creation.md) · [English](en/Q-011-threadpool-worker-creation.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-011) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-010-task-whenall-execution.md) · [Следующий →](Q-012-async-starts-synchronously.md)
