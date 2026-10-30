# Основные темы C# / .NET

[Русский](README.md) · [English](en/README.md)

Основные механизмы объясняются ровно один раз. Дополнительные вопросы — примеры для закрепления.

- [Жизненный цикл async/await](async-lifecycle.md) — От вызова C#-метода до сетевого события и продолжения.
- [ThreadPool и планировщик ОС](threadpool-scheduling.md) — Кто планирует work item и кто назначает поток на CPU.
- [Композиция Task и ошибки](task-composition.md) — WhenAny, WhenAll, nested Task, наблюдаемость ошибок.
- [Разделяемая память и синхронизация](shared-memory.md) — Гонки, атомарность, lock, Interlocked и SemaphoreSlim.
- [Continuation и контексты](execution-context.md) — SynchronizationContext, TaskScheduler, AsyncLocal и ConfigureAwait.
- [Отмена асинхронных операций](cancellation.md) — Что реально делает CancellationToken и чего он не делает.
- [ValueTask<T> и стоимость ожидания](valuetask.md) — Точная область применения без правил вроде «всегда быстрее».
- [Блокировки и sync-over-async](sync-over-async.md) — Почему .Result и .Wait() опасны и откуда берётся deadlock.
