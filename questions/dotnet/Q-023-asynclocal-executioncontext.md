# Q-023 — AsyncLocal / ExecutionContext

[Русский](./Q-023-asynclocal-executioncontext.md) · [English](en/Q-023-asynclocal-executioncontext.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-023) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-022-taskcompletionsource-continuations.md) · [Следующий →](Q-024-completed-await-output.md)

## Вопрос

Почему AsyncLocal<T> сохраняет значение при Task.Run на другом потоке, а ThreadStatic — нет?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

AsyncLocal<T> хранится в логическом ExecutionContext, который по умолчанию распространяется через асинхронные переходы и Task.Run. ThreadStatic привязан к конкретному потоку ОС/CLR, поэтому при смене потока значение не переносится.

</details>

---

[Русский](./Q-023-asynclocal-executioncontext.md) · [English](en/Q-023-asynclocal-executioncontext.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-023) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-022-taskcompletionsource-continuations.md) · [Следующий →](Q-024-completed-await-output.md)
