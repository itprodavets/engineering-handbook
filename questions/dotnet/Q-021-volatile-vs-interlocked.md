# Q-021 — volatile / atomicity

[Русский](./Q-021-volatile-vs-interlocked.md) · [English](en/Q-021-volatile-vs-interlocked.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-021) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-020-await-inside-lock.md) · [Следующий →](Q-022-taskcompletionsource-continuations.md)

## Вопрос

Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

volatile управляет доступом/упорядочиванием чтений и записей, но ++ остаётся read-modify-write. Interlocked.Increment выполняет атомарное изменение одного значения, а lock защищает произвольную критическую секцию.

</details>

---

[Русский](./Q-021-volatile-vs-interlocked.md) · [English](en/Q-021-volatile-vs-interlocked.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-021) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-020-await-inside-lock.md) · [Следующий →](Q-022-taskcompletionsource-continuations.md)
