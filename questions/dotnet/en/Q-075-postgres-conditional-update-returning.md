# Q-075 — Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../Q-075-postgres-conditional-update-returning.md) · [English](./Q-075-postgres-conditional-update-returning.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-075) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-074-postgres-read-committed-check-act.md)

## Question

How can one UPDATE ... RETURNING statement protect the last item?

## .NET / C# challenge — predict the outcome first

```sql
UPDATE inventory SET available=available-1 WHERE sku='IPHONE-17' AND available>0 RETURNING available;
```

<details>
<summary>Model answer — reveal after your attempt</summary>

UPDATE ... SET available=available-1 WHERE sku=$1 AND available>0 RETURNING available: the second UPDATE affects zero rows after predicate recheck.

</details>

### Documentation and source

[https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)

---

[Русский](../Q-075-postgres-conditional-update-returning.md) · [English](./Q-075-postgres-conditional-update-returning.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-075) · [Canonical lesson](../../../topics/dotnet/en/microservices-concurrency.md) · [← Previous](Q-074-postgres-read-committed-check-act.md)
