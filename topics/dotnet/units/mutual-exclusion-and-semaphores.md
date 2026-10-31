# Monitor lock и SemaphoreSlim

[Русский](mutual-exclusion-and-semaphores.md) · [English](en/mutual-exclusion-and-semaphores.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/mutual-exclusion-and-semaphores)

> Различать блокировку потока и асинхронное ожидание разрешения.

## Определение

lock обеспечивает взаимное исключение между потоками, захватывающими один и тот же объект. SemaphoreSlim.WaitAsync позволяет асинхронно ждать разрешение, не блокируя вызывающий worker на время ожидания.

## Внутренний механизм

1. lock(new object()) создаёт отдельный объект для каждого исполнения и не защищает общую переменную.
2. Компилятор запрещает await внутри тела lock (CS1996), потому что блокировка привязана к синхронной критической секции.
3. SemaphoreSlim уменьшает счётчик при WaitAsync, а Release возвращает разрешение; это не рекурсивная блокировка.
4. Release размещай в finally, чтобы исключения и отмена после успешного захвата не приводили к утечке разрешения.

## Потребляемые ресурсы

Lock contention и очереди ожидания; заблокированные Monitor workers vs async-ожидание семафора.

## Ошибки и ограничения

Повторный WaitAsync(1,1) без Release может навсегда остановить данную операцию.

## Пример

```csharp
using var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();
try { /* protected async work */ }
finally { semaphore.Release(); }
```

## Вопросы для закрепления

- [Q-020: Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?](../../../questions/dotnet/Q-020-await-inside-lock.md)
- [Q-029: Защищает ли lock(new object()) переменную counter от гонки?](../../../questions/dotnet/Q-029-lock-new-object.md)
- [Q-034: Что напечатает second.IsCompleted после повторного WaitAsync без Release?](../../../questions/dotnet/Q-034-semaphore-waitasync.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)

---

[← Назад](compare-exchange-cas-loop.md) · [Далее →](parallel-foreach-async-void.md) · [Русский](mutual-exclusion-and-semaphores.md) · [English](en/mutual-exclusion-and-semaphores.md)
