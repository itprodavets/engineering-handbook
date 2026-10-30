# Q-012 — Async / first await

[Русский](./Q-012-async-starts-synchronously.md) · [English](en/Q-012-async-starts-synchronously.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-012) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-011-threadpool-worker-creation.md) · [Следующий →](Q-013-completed-await-and-scheduling.md)

## Вопрос

Запускает ли вызов async Task-метода новый поток или начинает работу синхронно?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Вызов начинает исполнять тело на текущем потоке до первого await незавершённой операции. Компилятор генерирует state machine, но async не означает запуск в ThreadPool.

</details>

---

[Русский](./Q-012-async-starts-synchronously.md) · [English](en/Q-012-async-starts-synchronously.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-012) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-011-threadpool-worker-creation.md) · [Следующий →](Q-013-completed-await-and-scheduling.md)
