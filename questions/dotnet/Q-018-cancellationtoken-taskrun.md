# Q-018 — CancellationToken

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-017-configureawait-and-context.md) · [Следующий →](Q-019-valuetask-consumption.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Cancellation

## Вопрос (RU)

Прерывает ли CancellationToken выполняющуюся Task.Run и автоматически ли попадает в делегат?

## Question (EN)

Can CancellationToken forcibly stop a running Task.Run, and is it passed to the delegate automatically?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Нет. Отмена кооперативная; Task.Run(token) может не допустить запуск, если задача ещё не началась, но не останавливает уже выполняющийся код и не передаёт token в делегат автоматически.

### EN — concise interview answer

No. Cancellation is cooperative. Task.Run(token) can prevent execution before a task starts, but does not interrupt running code or automatically pass the token into the delegate.

</details>

**Terminology / Термины:** CancellationToken; cooperative; Task.Run

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../languages/csharp/async-await.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/async-await.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-017-configureawait-and-context.md) · [Следующий →](Q-019-valuetask-consumption.md)
