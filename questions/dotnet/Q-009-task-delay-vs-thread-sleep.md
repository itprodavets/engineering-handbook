# Q-009 — Task.Delay / Thread.Sleep

[Русский](./Q-009-task-delay-vs-thread-sleep.md) · [English](en/Q-009-task-delay-vs-thread-sleep.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-009) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-008-task-vs-thread.md) · [Следующий →](Q-010-task-whenall-execution.md)

## Вопрос

Что произойдёт с ThreadPool, если одновременно запустить 10 000 Task.Delay(5000) и 10 000 Task.Run(() => Thread.Sleep(5000))?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Task.Delay создаёт 10 000 ожидающих операций с таймерами, но 0 рабочих потоков блокируется специально ради этих задержек. Task.Run помещает 10 000 делегатов в очередь; каждый выполняемый Thread.Sleep блокирует 1 worker на 5 секунд. ThreadPool может использовать существующие или создавать дополнительные потоки; точное число не фиксировано.

</details>

---

[Русский](./Q-009-task-delay-vs-thread-sleep.md) · [English](en/Q-009-task-delay-vs-thread-sleep.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-009) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-008-task-vs-thread.md) · [Следующий →](Q-010-task-whenall-execution.md)
