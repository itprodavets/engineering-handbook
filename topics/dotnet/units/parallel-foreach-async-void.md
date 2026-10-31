# Почему Parallel.ForEach(async ...) опасен

[Русский](parallel-foreach-async-void.md) · [English](en/parallel-foreach-async-void.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/parallel-foreach-async-void)

> Объяснять потерю управления продолжениями async void.

## Определение

Parallel.ForEach принимает Action<T> — синхронный делегат. Async-лямбда, приведённая к Action<T>, становится async void, поэтому Parallel.ForEach не ждёт её продолжения после первого незавершённого await.

## Внутренний механизм

1. После await незавершённой операции async void возвращает управление вызывающему Action.
2. Parallel.ForEach считает соответствующую синхронную итерацию выполненной, пока асинхронный код ещё ждёт.
3. Исключения async void не наблюдаются через Task.WhenAll и могут завершить процесс.
4. Используй Parallel.ForEachAsync с ValueTask-делегатом, либо Task.WhenAll с явными async Task.

## Потребляемые ресурсы

Продолжения и ThreadPool, риск неконтролируемого числа внешних операций.

## Ошибки и ограничения

Вывод «цикл завершился => async-операции завершились» неверен.

## Пример

```csharp
await Parallel.ForEachAsync(items, async (item, ct) => {
    await HandleAsync(item, ct);
});
```

## Вопросы для закрепления

- [Q-035: Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован?](../../../questions/dotnet/Q-035-parallel-foreach-async-void.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.parallel.foreachasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.parallel.foreachasync)

---

[← Назад](mutual-exclusion-and-semaphores.md) · [Русский](parallel-foreach-async-void.md) · [English](en/parallel-foreach-async-void.md)
