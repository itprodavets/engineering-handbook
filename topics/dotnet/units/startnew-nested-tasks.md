# Вложенные Task и StartNew(Func<Task>)

[Русский](startnew-nested-tasks.md) · [English](en/startnew-nested-tasks.md)

[Главная](../../../README.md) · [Модуль](../task-composition.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/startnew-nested-tasks)

> Отличать завершение outer Task от реальной асинхронной работы.

## Определение

Task.Factory.StartNew с async-делегатом может возвращать Task<Task>. Внешняя Task завершается при возврате внутренней Task, а не после завершения внутренней операции.

## Внутренний механизм

1. Компилятор преобразует async-лямбду в функцию, возвращающую Task.
2. StartNew планирует выполнение делегата и возвращает Task<TResult>, где TResult тоже является Task.
3. await outer возвращает inner; для полной операции нужен await inner или Unwrap().
4. Task.Run(Func<Task>) умеет разворачивать полученный Task, поэтому часто удобнее для async-делегата.

## Потребляемые ресурсы

Два Task-объекта/представления и операции продолжения; возможны скрытые ошибки внутренней Task.

## Ошибки и ограничения

Один await outer не гарантирует, что inner закончился; иначе теряется контроль жизненного цикла и исключений.

## Пример

```csharp
Task<Task> outer = Task.Factory.StartNew<Task>(async () => await Task.Delay(100));
Task inner = await outer;
await inner;
```

## Вопросы для закрепления

- [Q-033: Каков тип задачи и ждёт ли один await outer завершения внутренней асинхронной операции?](../../../questions/dotnet/Q-033-startnew-nested-task.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskextensions.unwrap)

---

[← Назад](task-aggregation.md) · [Русский](startnew-nested-tasks.md) · [English](en/startnew-nested-tasks.md)
