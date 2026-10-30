# Q-002 — Async / потоки

[Русский](./Q-002-thread-id-after-await.md) · [English](en/Q-002-thread-id-after-await.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-002) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-001-async-io-scalability.md) · [Следующий →](Q-003-what-is-io.md)

## Вопрос

Всегда ли совпадают Environment.CurrentManagedThreadId до и после await ToListAsync()? Если они разные, создал ли await новый поток?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. В ASP.NET Core продолжение после await может выполняться на другом ThreadPool-потоке. await сам по себе не создаёт поток и не гарантирует переключение; завершённая операция может продолжиться синхронно.

</details>

---

[Русский](./Q-002-thread-id-after-await.md) · [English](en/Q-002-thread-id-after-await.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-002) · [Основная тема](../../topics/dotnet/execution-context.md) · [← Предыдущий](Q-001-async-io-scalability.md) · [Следующий →](Q-003-what-is-io.md)
