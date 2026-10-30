# Q-020 — lock / async mutex

[Русский](./Q-020-await-inside-lock.md) · [English](en/Q-020-await-inside-lock.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-020) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-019-valuetask-consumption.md) · [Следующий →](Q-021-volatile-vs-interlocked.md)

## Вопрос

Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Компилятор выдаёт CS1996: нельзя приостановить async-метод внутри lock. SemaphoreSlim.WaitAsync даёт ожидаемое без блокировки потока получение разрешения; Release обязателен, обычно в finally. SemaphoreSlim не обеспечивает автоматической рекурсивности.

</details>

---

[Русский](./Q-020-await-inside-lock.md) · [English](en/Q-020-await-inside-lock.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-020) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-019-valuetask-consumption.md) · [Следующий →](Q-021-volatile-vs-interlocked.md)
