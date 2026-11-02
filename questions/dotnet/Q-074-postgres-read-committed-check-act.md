# Q-074 — PostgreSQL isolation

[Русский](./Q-074-postgres-read-committed-check-act.md) · [English](en/Q-074-postgres-read-committed-check-act.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-074) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-073-remote-timeout-not-rollback.md) · [Следующий →](Q-075-postgres-conditional-update-returning.md)

## Вопрос

Могут ли два Pod под READ COMMITTED прочитать available=1 и затем безусловными UPDATE получить -1?

## Фрагмент .NET / C# — попробуйте предсказать результат

```sql
BEGIN;
SELECT available FROM inventory WHERE sku='IPHONE-17';
UPDATE inventory SET available=available-1 WHERE sku='IPHONE-17';
COMMIT;
```

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Да. Второй UPDATE ждёт row lock, затем уменьшает новую версию 0→-1, так как WHERE проверяет только sku.

</details>

### Документация и исходники

[https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)

---

[Русский](./Q-074-postgres-read-committed-check-act.md) · [English](en/Q-074-postgres-read-committed-check-act.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-074) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-073-remote-timeout-not-rollback.md) · [Следующий →](Q-075-postgres-conditional-update-returning.md)
