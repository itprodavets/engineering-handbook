# Композиция Task и ошибки

[Русский](task-composition.md) · [English](en/task-composition.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/task-composition)

WhenAny, WhenAll, nested Task, наблюдаемость ошибок.

## Определение

Task.WhenAll создаёт агрегирующее завершение уже переданных задач; WhenAny возвращает первую завершившуюся Task независимо от её статуса. Task<Task> требует понимания внешнего и внутреннего ожидания.

## Механизм: от C# до ОС

1. Task.WhenAny возвращает победившую Task; исключение внутри неё станет видно при её await.
2. Task.WhenAll становится Faulted, если одна или больше входных задач завершились ошибкой.
3. Обычный await общей задачи выбрасывает одно исключение; полную совокупность ошибок смотри через Task.Exception.
4. Task.Factory.StartNew(Func<Task>) даёт вложенную Task; Unwrap или второй await позволяют дождаться внутренней.

## Ресурсы

- **Task-объекты:** Агрегирующие Task и связанные продолжения; новые потоки специально для WhenAll/WhenAny не требуются.
- **Исключения:** Faulted Task удерживает исключения до освобождения соответствующих объектов.

## Ограничения и риски

- WhenAny не отменяет проигравшие операции автоматически.
- Ошибки нескольких запросов могут быть потеряны в диагностике, если смотреть только исключение из await.

## Вопросы для проверки

- [Q-014: Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные?](../../questions/dotnet/Q-014-whenany-faulted-task.md)
- [Q-015: Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await?](../../questions/dotnet/Q-015-whenall-multiple-exceptions.md)

## Закрепление на коде

- [Q-026: Что напечатает код и выбросит ли await Task.WhenAny исключение?](../../questions/dotnet/Q-026-whenany-faulted-output.md)
- [Q-027: Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task?](../../questions/dotnet/Q-027-whenall-exceptions-count.md)
- [Q-033: Каков тип задачи и ждёт ли один await outer завершения внутренней асинхронной операции?](../../questions/dotnet/Q-033-startnew-nested-task.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany)

---

[Русский](task-composition.md) · [English](en/task-composition.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/task-composition)
