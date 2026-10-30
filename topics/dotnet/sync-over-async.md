# Блокировки и sync-over-async

[Русский](sync-over-async.md) · [English](en/sync-over-async.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/sync-over-async)

Почему .Result и .Wait() опасны и откуда берётся deadlock.

## Определение

Синхронное ожидание Task блокирует вызывающий поток, даже если незавершённая операция — асинхронный I/O. В серверных приложениях блокирование worker-потоков сокращает доступную ёмкость ThreadPool.

## Механизм: от языка и runtime до ОС

1. Task.Wait и Task.Result удерживают текущий поток до завершения, исключения или отмены.
2. Если продолжение должно выполниться в контексте, который заблокирован этим же ожиданием, возможен deadlock.
3. Стандартный ASP.NET Core не устанавливает SynchronizationContext старого однопоточного типа, но starvation остаётся.
4. Используй сквозное async/await и ограничивай конкурентность на уровне ресурсов.

## Ресурсы

- **Потоки:** 1 заблокированный worker на каждый выполняющийся синхронный Wait/Result.
- **Очереди:** Continuation может ждать свободного worker, увеличивая задержки.

## Ограничения и риски

- Отсутствие deadlock не означает отсутствие деградации пропускной способности.
- Task.Run(() => SomeAsync().Result) переносит блокировку, но не делает I/O неблокирующим.

## Вопросы для проверки

- [Q-016: Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock?](../../questions/dotnet/Q-016-sync-over-async-deadlocks.md)

## Закрепление на коде

—

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[Русский](sync-over-async.md) · [English](en/sync-over-async.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/sync-over-async)
