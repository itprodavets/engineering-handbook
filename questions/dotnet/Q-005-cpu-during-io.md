# Q-005 — CPU vs I/O

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-004-async-postgres-pipeline.md) · [Следующий →](Q-006-hundred-threads-eight-cores.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** CPU vs I/O

## Вопрос (RU)

PostgreSQL выполняет SQL 5 секунд. Что делает ядро CPU нашего .NET-сервера при await ToListAsync()?

## Question (EN)

PostgreSQL takes five seconds to execute a query. What does the .NET server's CPU core do while awaiting ToListAsync()?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Ядро CPU не привязано к ожидающему запросу: ОС может выполнять другие потоки или оставить его простаивать. CPU расходуется до ожидания на подготовку/отправку SQL и после него на приём, чтение и материализацию данных.

### EN — concise interview answer

The CPU core is not reserved for the waiting request: the OS may run other threads or leave it idle. CPU time is still required before the wait to prepare/send SQL and afterwards to read and materialize the result.

</details>

**Terminology / Термины:** CPU-bound; I/O-bound; OS Scheduler

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-004-async-postgres-pipeline.md) · [Следующий →](Q-006-hundred-threads-eight-cores.md)
