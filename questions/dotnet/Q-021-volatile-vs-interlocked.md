# Q-021 — volatile / atomicity

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../computer-science/concurrency/memory-model.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-020-await-inside-lock.md) · [Следующий →](Q-022-taskcompletionsource-continuations.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Memory ordering

## Вопрос (RU)

Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?

## Question (EN)

Why is volatile counter++ unsafe, and how do Interlocked.Increment and lock differ?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

volatile управляет доступом/упорядочиванием чтений и записей, но ++ остаётся read-modify-write. Interlocked.Increment выполняет атомарное изменение одного значения, а lock защищает произвольную критическую секцию.

### EN — concise interview answer

volatile affects memory access and ordering but does not make read-modify-write atomic. Interlocked.Increment atomically changes one variable; lock protects a critical section.

</details>

**Terminology / Термины:** volatile; Interlocked; atomicity; critical section

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../computer-science/concurrency/memory-model.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../computer-science/concurrency/memory-model.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-020-await-inside-lock.md) · [Следующий →](Q-022-taskcompletionsource-continuations.md)
