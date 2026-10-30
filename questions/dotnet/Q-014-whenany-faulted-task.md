# Q-014 — Task.WhenAny / faults

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-013-completed-await-and-scheduling.md) · [Следующий →](Q-015-whenall-multiple-exceptions.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Task.WhenAny

## Вопрос (RU)

Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные?

## Question (EN)

Does awaiting Task.WhenAny throw the winning task's exception or cancel the other tasks?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Нет. WhenAny возвращает успешно завершённую Task<Task>, результат которой — первая завершившаяся задача, в том числе faulted. Для ошибки нужен await возвращённой внутренней Task; остальные задачи продолжаются, если не отменены отдельно.

### EN — concise interview answer

No. WhenAny completes successfully with the first completed task, even if it faulted. Await that inner task to observe its exception; the remaining tasks continue unless canceled separately.

</details>

**Terminology / Термины:** WhenAny; winner; faulted; cancellation

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-013-completed-await-and-scheduling.md) · [Следующий →](Q-015-whenall-multiple-exceptions.md)
