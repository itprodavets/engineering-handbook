# Q-022 — TaskCompletionSource / continuation

[Русский](./Q-022-taskcompletionsource-continuations.md) · [English](en/Q-022-taskcompletionsource-continuations.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-022) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-021-volatile-vs-interlocked.md) · [Следующий →](Q-023-asynclocal-executioncontext.md)

## Вопрос

Почему SetResult под lock может вызвать неожиданный код и как помогает RunContinuationsAsynchronously?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Продолжения Task могут выполняться синхронно при SetResult, включая код под удерживаемой вызывающим потоком блокировкой. TaskCreationOptions.RunContinuationsAsynchronously исключает синхронное встраивание продолжений, помогая уменьшить опасность lock inversion/reentrancy.

</details>

---

[Русский](./Q-022-taskcompletionsource-continuations.md) · [English](en/Q-022-taskcompletionsource-continuations.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-022) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-021-volatile-vs-interlocked.md) · [Следующий →](Q-023-asynclocal-executioncontext.md)
