# Q-011 — ThreadPool / создание потоков

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-010-task-whenall-execution.md) · [Следующий →](Q-012-async-starts-synchronously.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** ThreadPool / worker creation

## Вопрос (RU)

Что означает «ThreadPool может создать дополнительный поток» при вызове Task.Run и почему это не означает 10 000 потоков для 10 000 Task?

## Question (EN)

What does it mean when the ThreadPool creates an additional thread, and why do 10,000 Tasks not imply 10,000 threads?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

ThreadPool сначала использует имеющиеся свободные worker-потоки. Если работы в очереди больше, чем могут обработать доступные workers, пул может создать дополнительные ОС-потоки в рамках своих ограничений. Task.Delay не выделяет отдельный заблокированный поток на каждый таймер; конкретное число новых потоков зависит от нагрузки и состояния пула.

### EN — concise interview answer

The ThreadPool first reuses available workers. If queued work exceeds available worker capacity, it may create additional OS threads within its limits. A Task.Delay timer does not reserve a blocked worker per delay; the number of new workers depends on the workload and current pool state.

</details>

**Terminology / Термины:** Worker thread; OS thread creation; work queue; thread reuse

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-010-task-whenall-execution.md) · [Следующий →](Q-012-async-starts-synchronously.md)
