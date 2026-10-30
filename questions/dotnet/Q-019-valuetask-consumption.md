# Q-019 — ValueTask / reuse

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-018-cancellationtoken-taskrun.md) · [Следующий →](Q-020-await-inside-lock.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** ValueTask

## Вопрос (RU)

Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память?

## Question (EN)

Why isn't it always safe to await ValueTask<T> twice, and does it always save memory?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

ValueTask<T> — struct, который может хранить готовый результат, Task или IValueTaskSource. Источник может допускать только одно потребление; выгода по аллокациям зависит от частоты синхронного завершения и использования API.

### EN — concise interview answer

ValueTask<T> is a struct that can wrap a result, Task, or IValueTaskSource. A source may support only one consumption; allocation savings depend on synchronous completions and usage patterns.

</details>

**Terminology / Термины:** ValueTask<T>; IValueTaskSource; AsTask

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-018-cancellationtoken-taskrun.md) · [Следующий →](Q-020-await-inside-lock.md)
