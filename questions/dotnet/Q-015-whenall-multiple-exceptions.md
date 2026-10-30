# Q-015 — Task.WhenAll / exceptions

[Русский](./Q-015-whenall-multiple-exceptions.md) · [English](en/Q-015-whenall-multiple-exceptions.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-015) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-014-whenany-faulted-task.md) · [Следующий →](Q-016-sync-over-async-deadlocks.md)

## Вопрос

Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

WhenAll завершается Faulted и хранит исключения всех упавших задач в aggregate Exception.InnerExceptions. Обычный await выбрасывает одно исключение; для полного набора надо изучить свойство Exception у общей Task.

</details>

---

[Русский](./Q-015-whenall-multiple-exceptions.md) · [English](en/Q-015-whenall-multiple-exceptions.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-015) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-014-whenany-faulted-task.md) · [Следующий →](Q-016-sync-over-async-deadlocks.md)
