# Q-010 — Task.WhenAll / execution

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-009-task-delay-vs-thread-sleep.md) · [Следующий →](Q-011-threadpool-worker-creation.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Task.WhenAll / execution

## Вопрос (RU)

Создаёт ли Task.WhenAll новые потоки и запускает ли сам переданные ему задачи?

## Question (EN)

Does Task.WhenAll create threads or start the tasks passed to it?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Нет. Task.WhenAll создаёт задачу, которая завершается, когда завершились все переданные задачи; потоки он не создаёт. Task.Delay запускает таймер при вызове, Task.Run ставит делегат в очередь при вызове; при ленивом Select эти вызовы выполняются при перечислении Task.WhenAll.

### EN — concise interview answer

No. Task.WhenAll returns an aggregate Task that completes when all supplied tasks finish; it neither creates threads nor starts existing tasks. Task.Delay schedules its timer when invoked; Task.Run queues its delegate when invoked. With lazy Select, those calls occur as WhenAll enumerates the sequence.

</details>

**Terminology / Термины:** Task.WhenAll; IEnumerable; deferred execution; TaskScheduler

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-009-task-delay-vs-thread-sleep.md) · [Следующий →](Q-011-threadpool-worker-creation.md)
