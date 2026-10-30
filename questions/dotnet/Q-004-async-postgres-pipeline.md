# Q-004 — CLR / ОС / сеть

[Русский](./Q-004-async-postgres-pipeline.md) · [English](en/Q-004-async-postgres-pipeline.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-004) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-003-what-is-io.md) · [Следующий →](Q-005-cpu-during-io.md)

## Вопрос

Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Npgsql отправляет SQL через сокет. Если ответ не готов, await сохраняет continuation и освобождает worker; ОС отслеживает готовность сокета (например, epoll на Linux). При получении данных .NET возобновляет обработку, а Npgsql/EF Core читают и материализуют объекты с использованием CPU.

</details>

---

[Русский](./Q-004-async-postgres-pipeline.md) · [English](en/Q-004-async-postgres-pipeline.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-004) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-003-what-is-io.md) · [Следующий →](Q-005-cpu-during-io.md)
