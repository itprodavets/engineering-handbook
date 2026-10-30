# Q-005 — CPU vs I/O

[Русский](./Q-005-cpu-during-io.md) · [English](en/Q-005-cpu-during-io.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-005) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-004-async-postgres-pipeline.md) · [Следующий →](Q-006-hundred-threads-eight-cores.md)

## Вопрос

PostgreSQL выполняет SQL 5 секунд. Что делает ядро CPU нашего .NET-сервера при await ToListAsync()?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Ядро CPU не привязано к ожидающему запросу: ОС может выполнять другие потоки или оставить его простаивать. CPU расходуется до ожидания на подготовку/отправку SQL и после него на приём, чтение и материализацию данных.

</details>

---

[Русский](./Q-005-cpu-during-io.md) · [English](en/Q-005-cpu-during-io.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-005) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-004-async-postgres-pipeline.md) · [Следующий →](Q-006-hundred-threads-eight-cores.md)
