# Q-018 — CancellationToken

[Русский](./Q-018-cancellationtoken-taskrun.md) · [English](en/Q-018-cancellationtoken-taskrun.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-018) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-017-configureawait-and-context.md) · [Следующий →](Q-019-valuetask-consumption.md)

## Вопрос

Прерывает ли CancellationToken выполняющуюся Task.Run и автоматически ли попадает в делегат?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. Отмена кооперативная; Task.Run(token) может не допустить запуск, если задача ещё не началась, но не останавливает уже выполняющийся код и не передаёт token в делегат автоматически.

</details>

---

[Русский](./Q-018-cancellationtoken-taskrun.md) · [English](en/Q-018-cancellationtoken-taskrun.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-018) · [Основная тема](../../topics/dotnet/cancellation.md) · [← Предыдущий](Q-017-configureawait-and-context.md) · [Следующий →](Q-019-valuetask-consumption.md)
