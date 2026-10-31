# ValueTask<T> и правила потребления

[Русский](valuetask-ivaluetasksource.md) · [English](en/valuetask-ivaluetasksource.md)

[Главная](../../../README.md) · [Модуль](../valuetask.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/valuetask-ivaluetasksource)

> Понять, почему struct не гарантирует нулевые аллокации.

## Определение

ValueTask<T> — value type, представляющий готовый результат, Task<T> или IValueTaskSource<T>. Некоторые источники поддерживают только однократное потребление, поэтому многократный await без контракта некорректен.

## Внутренний механизм

1. При частом синхронном завершении API может вернуть результат без отдельного Task<T>-объекта.
2. При незавершённой операции источник может быть пулом IValueTaskSource с token/version.
3. Повторный await или AsTask в неподходящий момент может нарушить контракт источника.
4. Выбирай ValueTask после профилирования; Task<T> зачастую проще в композиции.

## Потребляемые ресурсы

Размер struct и возможные underlying allocations; точная экономия требует benchmark/профиля.

## Ошибки и ограничения

ValueTask<T> нельзя считать «всегда быстрее Task<T>»; измерение нужно на конкретном пути.

## Пример

```csharp
ValueTask<int> GetAsync() => ValueTask.FromResult(42);
int result = await GetAsync();
```

## Вопросы для закрепления

- [Q-019: Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память?](../../../questions/dotnet/Q-019-valuetask-consumption.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012)

---

[Русский](valuetask-ivaluetasksource.md) · [English](en/valuetask-ivaluetasksource.md)
