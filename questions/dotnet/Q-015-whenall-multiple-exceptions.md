# Q-015 — Task.WhenAll / exceptions

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-014-whenany-faulted-task.md) · [Следующий →](Q-016-sync-over-async-deadlocks.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Task.WhenAll

## Вопрос (RU)

Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await?

## Question (EN)

How does Task.WhenAll handle several faulted tasks and what does await throw?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

WhenAll завершается Faulted и хранит исключения всех упавших задач в aggregate Exception.InnerExceptions. Обычный await выбрасывает одно исключение; для полного набора надо изучить свойство Exception у общей Task.

### EN — concise interview answer

The aggregate task is Faulted and preserves all task failures in Exception.InnerExceptions. A regular await throws one exception; inspect the aggregate task for the complete set.

</details>

**Terminology / Термины:** WhenAll; AggregateException; faulted; await

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-014-whenany-faulted-task.md) · [Следующий →](Q-016-sync-over-async-deadlocks.md)
