# TaskCompletionSource и встроенные continuation

[Русский](taskcontinuations-tcs.md) · [English](en/taskcontinuations-tcs.md)

[Главная](../../../README.md) · [Модуль](../execution-context.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/taskcontinuations-tcs)

> Понимать reentrancy и опасность SetResult под lock.

## Определение

TaskCompletionSource вручную переводит Task в завершённое состояние. В зависимости от настроек некоторые продолжения могут выполниться прямо в вызывающем SetResult потоке; RunContinuationsAsynchronously предотвращает такое синхронное встраивание.

## Внутренний механизм

1. Реализация completion обрабатывает зарегистрированные continuation callbacks.
2. Если SetResult вызывается внутри lock, синхронное continuation может выполнить чужой код при удерживаемой блокировке.
3. Это может приводить к reentrancy, lock inversion и неожиданной latency.
4. RunContinuationsAsynchronously изменяет способ планирования; это не означает создания отдельного потока для каждого continuation.

## Потребляемые ресурсы

Continuation objects/queue entries и стоимость их исполнения, возможные lock contention.

## Ошибки и ограничения

Не вызывай пользовательские продолжения синхронно под долгоживущими блокировками без необходимости.

## Пример

```csharp
var gate = new TaskCompletionSource<int>(TaskCreationOptions.RunContinuationsAsynchronously);
gate.SetResult(42);
```

## Вопросы для закрепления

- [Q-022: Почему SetResult под lock может вызвать неожиданный код и как помогает RunContinuationsAsynchronously?](../../../questions/dotnet/Q-022-taskcompletionsource-continuations.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions)

---

[← Назад](synchronizationcontext-configureawait.md) · [Русский](taskcontinuations-tcs.md) · [English](en/taskcontinuations-tcs.md)
