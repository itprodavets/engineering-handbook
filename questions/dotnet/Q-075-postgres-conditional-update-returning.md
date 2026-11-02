# Q-075 — PostgreSQL conditional UPDATE

[Русский](./Q-075-postgres-conditional-update-returning.md) · [English](en/Q-075-postgres-conditional-update-returning.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-075) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-074-postgres-read-committed-check-act.md)

## Вопрос

Как одним SQL statement защитить последний товар через UPDATE ... RETURNING?

## Фрагмент .NET / C# — попробуйте предсказать результат

```sql
UPDATE inventory SET available=available-1 WHERE sku='IPHONE-17' AND available>0 RETURNING available;
```

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

UPDATE ... SET available=available-1 WHERE sku=$1 AND available>0 RETURNING available: второй UPDATE после recheck не обновит строк.

</details>

### Документация и исходники

[https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)

---

[Русский](./Q-075-postgres-conditional-update-returning.md) · [English](en/Q-075-postgres-conditional-update-returning.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-075) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-074-postgres-read-committed-check-act.md)
