# Q-004 — CLR / ОС / сеть

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-003-what-is-io.md) · [Следующий →](Q-005-cpu-during-io.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** CLR / OS / networking

## Вопрос (RU)

Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата?

## Question (EN)

What happens inside .NET, the OS kernel and CPU between sending an asynchronous SQL query and receiving the result?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Npgsql отправляет SQL через сокет. Если ответ не готов, await сохраняет continuation и освобождает worker; ОС отслеживает готовность сокета (например, epoll на Linux). При получении данных .NET возобновляет обработку, а Npgsql/EF Core читают и материализуют объекты с использованием CPU.

### EN — concise interview answer

Npgsql sends SQL over a socket. If the response is pending, await suspends the method and frees the worker while the OS monitors socket readiness (for example, epoll on Linux). Once data arrives, .NET resumes processing and Npgsql/EF Core read and materialize the result using CPU time.

</details>

**Terminology / Термины:** Npgsql; socket; epoll; continuation; materialization

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-003-what-is-io.md) · [Следующий →](Q-005-cpu-during-io.md)
