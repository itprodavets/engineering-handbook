# Q-008 — Task / Thread

[Русский](./Q-008-task-vs-thread.md) · [English](en/Q-008-task-vs-thread.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-008) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-007-threadpool-vs-os-scheduler.md) · [Следующий →](Q-009-task-delay-vs-thread-sleep.md)

## Вопрос

Чем Task отличается от Thread? Создаёт ли Task новый поток и что делает await?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Thread — планируемый ОС поток исполнения. Task — объект, представляющий завершение операции (и результат в Task<T>); он не обязан иметь собственный поток. Task.Run обычно запускает работу на ThreadPool, а await при незавершённом I/O приостанавливает метод без блокировки рабочего потока.

</details>

---

[Русский](./Q-008-task-vs-thread.md) · [English](en/Q-008-task-vs-thread.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-008) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-007-threadpool-vs-os-scheduler.md) · [Следующий →](Q-009-task-delay-vs-thread-sleep.md)
