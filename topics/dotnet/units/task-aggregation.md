# WhenAll и WhenAny — семантика завершения

[Русский](task-aggregation.md) · [English](en/task-aggregation.md)

[Главная](../../../README.md) · [Модуль](../task-composition.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/task-aggregation)

> Различать ожидание всех задач и получение первой завершившейся.

## Определение

Task.WhenAll создаёт агрегирующую Task, завершение которой зависит от всех входных. Task.WhenAny возвращает завершившуюся первой Task независимо от её статуса; оставшиеся задачи не отменяются автоматически.

## Внутренний механизм

1. WhenAny возвращает Task<Task>, у внешней задачи статус успеха даже если winner завершился Faulted.
2. Для исключения победителя отдельно await саму возвращённую Task.
3. WhenAll сохраняет ошибки всех faulted входных задач в своей AggregateException.
4. Обычный await WhenAll выбрасывает одно исключение; изучи all.Exception.InnerExceptions для полного набора.

## Потребляемые ресурсы

Агрегирующие Task и продолжения; не выделяются специальные потоки на каждое ожидание.

## Ошибки и ограничения

WhenAll не даёт сериализации доступа к общей памяти и не ограничивает параллелизм.

## Пример

```csharp
Task all = Task.WhenAll(first, second);
try { await all; } catch { Console.WriteLine(all.Exception); }
```

## Вопросы для закрепления

- [Q-014: Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные?](../../../questions/dotnet/Q-014-whenany-faulted-task.md)
- [Q-015: Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await?](../../../questions/dotnet/Q-015-whenall-multiple-exceptions.md)
- [Q-026: Что напечатает код и выбросит ли await Task.WhenAny исключение?](../../../questions/dotnet/Q-026-whenany-faulted-output.md)
- [Q-027: Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task?](../../../questions/dotnet/Q-027-whenall-exceptions-count.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)

---

[Далее →](startnew-nested-tasks.md) · [Русский](task-aggregation.md) · [English](en/task-aggregation.md)
