# Q-007 — ThreadPool / Scheduler

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-006-hundred-threads-eight-cores.md) · [Следующий →](Q-008-task-vs-thread.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** ThreadPool / Scheduler

## Вопрос (RU)

Чем отличается .NET ThreadPool от планировщика ОС? Кто решает, на каком ядре выполняется поток?

## Question (EN)

What is the difference between the .NET ThreadPool and the OS scheduler? Who decides which CPU core runs a thread?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

ThreadPool управляет очередями задач и количеством рабочих потоков .NET. Планировщик ОС назначает готовые ОС-потоки логическим процессорам, может вытеснять и переносить их между ядрами. Task — не то же самое, что Thread.

### EN — concise interview answer

The ThreadPool manages queued work and .NET worker threads. The OS scheduler assigns runnable OS threads to logical processors and may preempt or migrate them. A Task is not a Thread.

</details>

**Terminology / Термины:** ThreadPool; OS Scheduler; Task vs Thread

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-006-hundred-threads-eight-cores.md) · [Следующий →](Q-008-task-vs-thread.md)
