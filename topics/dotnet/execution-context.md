# Continuation и контексты

[Русский](execution-context.md) · [English](en/execution-context.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/execution-context)

SynchronizationContext, TaskScheduler, AsyncLocal и ConfigureAwait.

## Определение

Операция await может захватывать контекст продолжения. ExecutionContext переносит логический контекст (например, AsyncLocal), в отличие от ThreadStatic. ConfigureAwait(false) не отменяет ExecutionContext.

## Механизм: от языка и runtime до ОС

1. AsyncLocal<T> течёт через стандартный ExecutionContext, который Task.Run обычно захватывает.
2. ConfigureAwait(false) не пытается вернуться в захваченный SynchronizationContext или нестандартный TaskScheduler.
3. TaskCompletionSource может выполнить continuations inline; RunContinuationsAsynchronously избегает их синхронного встраивания.
4. Continuation может выполняться на другом worker; физическая идентичность потока не гарантирована.

## Ресурсы

- **Память:** Состояние ExecutionContext, Task и continuation удерживает ссылки; реальные аллокации зависят от пути.
- **Worker threads:** Task.Run использует ThreadPool, но ConfigureAwait(false) не создаёт worker самостоятельно.

## Ограничения и риски

- Синхронное выполнение continuation под lock может вызвать reentrancy и lock inversion.
- ThreadStatic и AsyncLocal семантически различны даже если вывод при одном запуске совпал.

## Вопросы для проверки

- [Q-002: Всегда ли совпадают Environment.CurrentManagedThreadId до и после await ToListAsync()? Если они разные, создал ли await новый поток?](../../questions/dotnet/Q-002-thread-id-after-await.md)
- [Q-017: Что именно меняет ConfigureAwait(false)? Подавляет ли он ExecutionContext?](../../questions/dotnet/Q-017-configureawait-and-context.md)
- [Q-022: Почему SetResult под lock может вызвать неожиданный код и как помогает RunContinuationsAsynchronously?](../../questions/dotnet/Q-022-taskcompletionsource-continuations.md)
- [Q-023: Почему AsyncLocal<T> сохраняет значение при Task.Run на другом потоке, а ThreadStatic — нет?](../../questions/dotnet/Q-023-asynclocal-executioncontext.md)

## Закрепление на коде

- [Q-031: Что напечатает Task.Run — X или null?](../../questions/dotnet/Q-031-asynclocal-flow.md)
- [Q-032: Изменится ли managed thread id на await CompletedTask.ConfigureAwait(false)?](../../questions/dotnet/Q-032-configureawait-thread-id.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions)

---

[Русский](execution-context.md) · [English](en/execution-context.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/execution-context)
