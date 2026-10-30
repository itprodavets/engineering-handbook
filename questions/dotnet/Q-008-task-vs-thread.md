# Q-008 — Task / Thread

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-007-threadpool-vs-os-scheduler.md) · [Следующий →](Q-009-task-delay-vs-thread-sleep.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Task / Thread

## Вопрос (RU)

Чем Task отличается от Thread? Создаёт ли Task новый поток и что делает await?

## Question (EN)

What is the difference between Task and Thread in .NET? Does a Task create a new thread, and what does await do?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Thread — планируемый ОС поток исполнения. Task — объект, представляющий завершение операции (и результат в Task<T>); он не обязан иметь собственный поток. Task.Run обычно запускает работу на ThreadPool, а await при незавершённом I/O приостанавливает метод без блокировки рабочего потока.

### EN — concise interview answer

A Thread is an OS-scheduled execution path. A Task represents an operation's completion (and a result with Task<T>), not a dedicated thread. Task.Run usually queues work to the ThreadPool; awaiting incomplete asynchronous I/O suspends the method without blocking its worker.

</details>

**Terminology / Термины:** Task; Task<T>; Thread; Task.Run; await; ThreadPool

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-007-threadpool-vs-os-scheduler.md) · [Следующий →](Q-009-task-delay-vs-thread-sleep.md)
