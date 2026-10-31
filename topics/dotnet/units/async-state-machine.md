# Что компилятор генерирует для async/await

[Русский](async-state-machine.md) · [English](en/async-state-machine.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-state-machine)

> Понимать MoveNext, awaiter и ветвление IsCompleted.

## Определение

Roslyn понижает async-метод в машину состояний с полями для сохранения состояния и методом MoveNext(). Само ключевое слово async не запускает поток.

## Внутренний механизм

1. Вызов async Task-метода начинает исполнение на вызывающем потоке до await незавершённого awaitable.
2. Awaiter.IsCompleted=true означает синхронное продолжение через GetResult(), без обязательного переключения.
3. При IsCompleted=false state machine сохраняет позицию, регистрирует continuation и возвращает Task вызывающему коду.
4. После завершения операции MoveNext продолжает выполнение; количество heap-аллокаций зависит от пути и реализации.

## Потребляемые ресурсы

Поля состояния и awaiter; возможные continuation и Task allocations; нет обязательного нового ОС-потока.

## Ошибки и ограничения

Нельзя приравнивать await к Task.Run: завершённая Task не обязана приводить даже к приостановке метода.

## Пример

```csharp
async Task Example() { Console.Write("A"); await Task.CompletedTask; Console.Write("B"); }
```

## Вопросы для закрепления

- [Q-012: Запускает ли вызов async Task-метода новый поток или начинает работу синхронно?](../../../questions/dotnet/Q-012-async-starts-synchronously.md)
- [Q-013: Всегда ли await приостанавливает метод, выделяет worker или переключает поток?](../../../questions/dotnet/Q-013-completed-await-and-scheduling.md)
- [Q-024: Какой вывод и почему? async-метод содержит await уже завершённой Task.](../../../questions/dotnet/Q-024-completed-await-output.md)
- [Q-025: Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource.](../../../questions/dotnet/Q-025-incomplete-await-output.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Назад](io-vs-cpu-bound.md) · [Далее →](async-socket-pipeline.md) · [Русский](async-state-machine.md) · [English](en/async-state-machine.md)
