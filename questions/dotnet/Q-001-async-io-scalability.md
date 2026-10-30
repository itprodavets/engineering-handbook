# Q-001 — Async / I/O

[Русский](./Q-001-async-io-scalability.md) · [English](en/Q-001-async-io-scalability.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-001) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [Следующий →](Q-002-thread-id-after-await.md)

## Вопрос

Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

ToListAsync() использует асинхронный I/O: при незавершённом чтении await сохраняет продолжение и освобождает рабочий поток. Task.Run() отправляет синхронный ToList() в ThreadPool, где поток блокируется при ожидании БД; возможен ThreadPool starvation.

</details>

---

[Русский](./Q-001-async-io-scalability.md) · [English](en/Q-001-async-io-scalability.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-001) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [Следующий →](Q-002-thread-id-after-await.md)
