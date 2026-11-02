# Q-074 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-074-postgres-read-committed-check-act.md) · [English](./Q-074-postgres-read-committed-check-act.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-074) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-073-remote-timeout-not-rollback.md) · [Next →](Q-075-postgres-conditional-update-returning.md)

## Question

Can two Pods under READ COMMITTED both read available=1 and then reach -1 via unconditional UPDATE?

## .NET / C# challenge — predict the outcome first

```sql
BEGIN;
SELECT available FROM inventory WHERE sku='IPHONE-17';
UPDATE inventory SET available=available-1 WHERE sku='IPHONE-17';
COMMIT;
```

<details>
<summary>Model answer — reveal after your attempt</summary>

Yes. The second UPDATE waits for the row lock and then decrements the new row version 0→-1 because WHERE only filters sku.

</details>

### Documentation and source

[https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)

---

[Русский](../Q-074-postgres-read-committed-check-act.md) · [English](./Q-074-postgres-read-committed-check-act.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-074) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-073-remote-timeout-not-rollback.md) · [Next →](Q-075-postgres-conditional-update-returning.md)
