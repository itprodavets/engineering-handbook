# ExecutionContext и AsyncLocal<T>

[Русский](executioncontext-asynclocal.md) · [English](en/executioncontext-asynclocal.md)

[Главная](../../../README.md) · [Модуль](../execution-context.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/executioncontext-asynclocal)

> Понять логический контекст, не привязанный к ОС-потоку.

## Определение

ExecutionContext хранит логический контекст выполнения, включая AsyncLocal<T>, и обычно распространяется при асинхронных переходах. ThreadStatic хранит значение, привязанное к конкретному потоку.

## Внутренний механизм

1. При Task.Run runtime обычно захватывает и передаёт ExecutionContext делегату.
2. Continuation может выполняться на другом worker, но AsyncLocal.Value сохраняет логическое значение.
3. ExecutionContext.SuppressFlow отключает перенос контекста в новой асинхронной работе, но требует аккуратного использования.
4. ConfigureAwait(false) сам по себе не подавляет ExecutionContext.

## Потребляемые ресурсы

Context capture/restore overhead и удерживаемые ссылки внутри AsyncLocal.

## Ошибки и ограничения

Не путай AsyncLocal с ThreadLocal/ThreadStatic: переход потока не равен потере логического контекста.

## Пример

```csharp
var trace = new AsyncLocal<string>();
trace.Value = "X";
await Task.Run(() => Console.Write(trace.Value));
```

## Вопросы для закрепления

- [Q-023: Почему AsyncLocal<T> сохраняет значение при Task.Run на другом потоке, а ThreadStatic — нет?](../../../questions/dotnet/Q-023-asynclocal-executioncontext.md)
- [Q-031: Что напечатает Task.Run — X или null?](../../../questions/dotnet/Q-031-asynclocal-flow.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)

---

[Далее →](synchronizationcontext-configureawait.md) · [Русский](executioncontext-asynclocal.md) · [English](en/executioncontext-asynclocal.md)
