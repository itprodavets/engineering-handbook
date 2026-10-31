# SynchronizationContext и ConfigureAwait(false)

[Русский](synchronizationcontext-configureawait.md) · [English](en/synchronizationcontext-configureawait.md)

[Главная](../../../README.md) · [Модуль](../execution-context.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/synchronizationcontext-configureawait)

> Понять захват контекста и отсутствие гарантии переключения потока.

## Определение

SynchronizationContext определяет, куда можно отправить продолжение. ConfigureAwait(false) при стандартном Task-await не требует возврата в захваченный SynchronizationContext/нестандартный TaskScheduler, но не запускает новый поток.

## Внутренний механизм

1. В UI-приложениях контекст может требовать возобновления на конкретном UI-потоке.
2. Обычный ASP.NET Core не устанавливает такой SynchronizationContext для HTTP-запроса.
3. Если Task завершена к моменту await, продолжение часто выполняется синхронно на прежнем потоке.
4. CurrentManagedThreadId до и после незавершённого await может отличаться, но не обязан.

## Потребляемые ресурсы

Состояние continuation, контексты и потенциальные переключения, но 0 автоматически созданных потоков await.

## Ошибки и ограничения

ConfigureAwait(false) не является «переключателем на ThreadPool» и не подавляет AsyncLocal.

## Пример

```csharp
int id = Environment.CurrentManagedThreadId;
await Task.CompletedTask.ConfigureAwait(false);
Console.WriteLine(id == Environment.CurrentManagedThreadId);
```

## Вопросы для закрепления

- [Q-002: Всегда ли совпадают Environment.CurrentManagedThreadId до и после await ToListAsync()? Если они разные, создал ли await новый поток?](../../../questions/dotnet/Q-002-thread-id-after-await.md)
- [Q-017: Что именно меняет ConfigureAwait(false)? Подавляет ли он ExecutionContext?](../../../questions/dotnet/Q-017-configureawait-and-context.md)
- [Q-032: Изменится ли managed thread id на await CompletedTask.ConfigureAwait(false)?](../../../questions/dotnet/Q-032-configureawait-thread-id.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)

---

[← Назад](executioncontext-asynclocal.md) · [Далее →](taskcontinuations-tcs.md) · [Русский](synchronizationcontext-configureawait.md) · [English](en/synchronizationcontext-configureawait.md)
