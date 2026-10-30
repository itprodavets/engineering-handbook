# Q-003 — Основы I/O

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-002-thread-id-after-await.md) · [Следующий →](Q-004-async-postgres-pipeline.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** I/O fundamentals

## Вопрос (RU)

Что означает аббревиатура I/O и какой вид I/O происходит при обращении к PostgreSQL?

## Question (EN)

What does I/O stand for, and what kind of I/O occurs when querying PostgreSQL?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

I/O = Input/Output (ввод/вывод), обмен с сетью, диском или устройством. Обращение к PostgreSQL обычно включает сетевой I/O по TCP; асинхронное ожидание ответа не требует блокировать worker.

### EN — concise interview answer

I/O stands for Input/Output: exchanging data with networks, storage or devices. A PostgreSQL call typically involves network I/O over TCP, and an asynchronous wait does not require a blocked worker thread.

</details>

**Terminology / Термины:** Input/Output; network I/O; TCP socket

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-002-thread-id-after-await.md) · [Следующий →](Q-004-async-postgres-pipeline.md)
