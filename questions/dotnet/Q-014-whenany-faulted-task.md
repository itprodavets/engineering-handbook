# Q-014 — Task.WhenAny / faults

[Русский](./Q-014-whenany-faulted-task.md) · [English](en/Q-014-whenany-faulted-task.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-014) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-013-completed-await-and-scheduling.md) · [Следующий →](Q-015-whenall-multiple-exceptions.md)

## Вопрос

Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. WhenAny возвращает успешно завершённую Task<Task>, результат которой — первая завершившаяся задача, в том числе faulted. Для ошибки нужен await возвращённой внутренней Task; остальные задачи продолжаются, если не отменены отдельно.

</details>

---

[Русский](./Q-014-whenany-faulted-task.md) · [English](en/Q-014-whenany-faulted-task.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-014) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-013-completed-await-and-scheduling.md) · [Следующий →](Q-015-whenall-multiple-exceptions.md)
