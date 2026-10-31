# CancellationToken — кооперативная отмена

[Русский](cancellation-tokens.md) · [English](en/cancellation-tokens.md)

[Главная](../../../README.md) · [Модуль](../cancellation.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/cancellation-tokens)

> Отличать запрос на отмену от принудительной остановки потока.

## Определение

CancellationToken сообщает о запросе отмены. Он не прерывает исполняемый поток и не останавливает уже начавшийся Task.Run автоматически; операция должна проверять token либо передать его в поддерживающее отмену API.

## Внутренний механизм

1. CancellationTokenSource.Cancel устанавливает состояние отмены и выполняет зарегистрированные callbacks.
2. Task.Run(token) может отмениться до начала исполнения; уже начавшийся делегат не прерывается принудительно.
3. Для I/O передавай token в метод драйвера, но конкретная поддержка отмены зависит от API.
4. После проверки token обычно ThrowIfCancellationRequested формирует OperationCanceledException.

## Потребляемые ресурсы

CancellationTokenSource registrations/callbacks; никакого гарантированного освобождения worker по сигналу отмены.

## Ошибки и ограничения

Не предполагай, что Cancel завершил все операции; при отмене нужно дождаться их фактического завершения.

## Пример

```csharp
using var cts = new CancellationTokenSource();
await Task.Delay(1000, cts.Token);
```

## Вопросы для закрепления

- [Q-018: Прерывает ли CancellationToken выполняющуюся Task.Run и автоматически ли попадает в делегат?](../../../questions/dotnet/Q-018-cancellationtoken-taskrun.md)
- [Q-030: Выведет ли программа DONE, если отменить token после запуска делегата?](../../../questions/dotnet/Q-030-cancellation-after-start.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads)

---

[Русский](cancellation-tokens.md) · [English](en/cancellation-tokens.md)
