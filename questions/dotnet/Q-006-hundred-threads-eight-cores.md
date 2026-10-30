# Q-006 — OS Scheduler

[Русский](./Q-006-hundred-threads-eight-cores.md) · [English](en/Q-006-hundred-threads-eight-cores.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-006) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-005-cpu-during-io.md) · [Следующий →](Q-007-threadpool-vs-os-scheduler.md)

## Вопрос

Как 8 физических ядер CPU могут выполнять работу 100 готовых к исполнению потоков?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Планировщик ОС распределяет процессорное время и может вытеснить незавершённый поток, сохранив его контекст, чтобы выполнить другой. Без SMT одновременно выполняются максимум 8 потоков, но 100 могут продвигаться по очереди.

</details>

---

[Русский](./Q-006-hundred-threads-eight-cores.md) · [English](en/Q-006-hundred-threads-eight-cores.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-006) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-005-cpu-during-io.md) · [Следующий →](Q-007-threadpool-vs-os-scheduler.md)
