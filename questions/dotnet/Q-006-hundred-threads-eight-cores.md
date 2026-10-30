# Q-006 — OS Scheduler

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-005-cpu-during-io.md) · [Следующий →](Q-007-threadpool-vs-os-scheduler.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** OS Scheduler

## Вопрос (RU)

Как 8 физических ядер CPU могут выполнять работу 100 готовых к исполнению потоков?

## Question (EN)

How can eight physical CPU cores handle 100 runnable threads?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Планировщик ОС распределяет процессорное время и может вытеснить незавершённый поток, сохранив его контекст, чтобы выполнить другой. Без SMT одновременно выполняются максимум 8 потоков, но 100 могут продвигаться по очереди.

### EN — concise interview answer

The OS scheduler shares CPU time among runnable threads. It can preempt an unfinished thread, save its execution context and run another. Without SMT, up to eight threads execute simultaneously, but all 100 can make progress over time.

</details>

**Terminology / Термины:** OS Scheduler; preemption; context switch; SMT; concurrency

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-005-cpu-during-io.md) · [Следующий →](Q-007-threadpool-vs-os-scheduler.md)
