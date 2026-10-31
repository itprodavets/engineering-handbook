# Deadlock и starvation при .Result/.Wait()

[Русский](sync-over-async.md) · [English](en/sync-over-async.md)

[Главная](../../../README.md) · [Модуль](../sync-over-async.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/sync-over-async)

> Различать заблокированный поток, цикл ожидания и отсутствие прогресса.

## Определение

Task.Result/Wait блокируют вызывающий поток до завершения Task. При высокой нагрузке это уменьшает доступный ThreadPool; classic deadlock требует конкретного цикла ожидания, например захваченного однопоточного контекста.

## Внутренний механизм

1. Рабочий поток вызывает async-операцию, затем .Result и остаётся заблокирован.
2. Continuation должен выполниться где-то ещё; при нехватке workers он задерживается в очереди.
3. В UI SynchronizationContext continuation может требовать именно заблокированный UI thread, формируя deadlock.
4. Стандартный ASP.NET Core не имеет такого контекста, но ThreadPool starvation остаётся реальным риском.

## Потребляемые ресурсы

Один заблокированный worker на исполняемый .Result/.Wait(); work queue и возможно новые worker threads.

## Ошибки и ограничения

Отсутствие deadlock не гарантирует масштабируемости. Не заменяй async I/O конструкцией Task.Run(() => io.Result).

## Пример

```csharp
var orders = await GetOrdersAsync(); // no synchronous .Result
```

## Вопросы для закрепления

- [Q-016: Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock?](../../../questions/dotnet/Q-016-sync-over-async-deadlocks.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[Русский](sync-over-async.md) · [English](en/sync-over-async.md)
