# Q-019 — ValueTask / reuse

[Русский](./Q-019-valuetask-consumption.md) · [English](en/Q-019-valuetask-consumption.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-019) · [Основная тема](../../topics/dotnet/valuetask.md) · [← Предыдущий](Q-018-cancellationtoken-taskrun.md) · [Следующий →](Q-020-await-inside-lock.md)

## Вопрос

Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

ValueTask<T> — struct, который может хранить готовый результат, Task или IValueTaskSource. Источник может допускать только одно потребление; выгода по аллокациям зависит от частоты синхронного завершения и использования API.

</details>

---

[Русский](./Q-019-valuetask-consumption.md) · [English](en/Q-019-valuetask-consumption.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-019) · [Основная тема](../../topics/dotnet/valuetask.md) · [← Предыдущий](Q-018-cancellationtoken-taskrun.md) · [Следующий →](Q-020-await-inside-lock.md)
