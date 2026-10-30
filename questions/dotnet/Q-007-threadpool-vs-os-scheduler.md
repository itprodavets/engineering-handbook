# Q-007 — ThreadPool / Scheduler

[Русский](./Q-007-threadpool-vs-os-scheduler.md) · [English](en/Q-007-threadpool-vs-os-scheduler.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-007) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-006-hundred-threads-eight-cores.md) · [Следующий →](Q-008-task-vs-thread.md)

## Вопрос

Чем отличается .NET ThreadPool от планировщика ОС? Кто решает, на каком ядре выполняется поток?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

ThreadPool управляет очередями задач и количеством рабочих потоков .NET. Планировщик ОС назначает готовые ОС-потоки логическим процессорам, может вытеснять и переносить их между ядрами. Task — не то же самое, что Thread.

</details>

---

[Русский](./Q-007-threadpool-vs-os-scheduler.md) · [English](en/Q-007-threadpool-vs-os-scheduler.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-007) · [Основная тема](../../topics/dotnet/threadpool-scheduling.md) · [← Предыдущий](Q-006-hundred-threads-eight-cores.md) · [Следующий →](Q-008-task-vs-thread.md)
