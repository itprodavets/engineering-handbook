# PostgreSQL READ COMMITTED: stock races and conditional UPDATE

[Русский](../postgres-read-committed-stock.md) · [English](postgres-read-committed-stock.md)

[Home](../../../../README.en.md) · [Module](../../en/microservices-concurrency.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/postgres-read-committed-stock)

> Prove one-SKU correctness across two transactions using MVCC and row locks.

## Definition

At READ COMMITTED two Pods can both read available=1 with ordinary SELECT. Both later performing UPDATE SET available=available-1 WHERE sku=... can produce -1: the second UPDATE waits for the row lock then applies to the updated zero value. A conditional UPDATE ... WHERE available>0 RETURNING available rechecks the predicate and prevents negative stock.

## Internal mechanics

1. Both independent SELECTs may observe available=1.
2. The first UPDATE obtains the row lock, writes zero and commits.
3. The second UPDATE waits and then decrements the current 0→-1 row version if WHERE only filters sku.
4. Place WHERE available>0 inside the UPDATE; PostgreSQL rechecks it after a concurrent update.
5. If the second statement updates zero rows, the item is out of stock. A CHECK available>=0 adds defense against other writers.

## Step-by-step explanation

### SELECT + unconditional UPDATE leaves a race

Two SELECTs read 1. The first UPDATE writes 0. The second waits for the row lock and after the first commits updates the new version 0→-1, because its WHERE lacks available>0. Row locks serialize physical writes but cannot enforce a predicate checked earlier in a separate statement.

```sql
BEGIN;
SELECT available FROM inventory WHERE sku='IPHONE-17';
UPDATE inventory SET available=available-1 WHERE sku='IPHONE-17';
COMMIT;
```

### Conditional UPDATE and RETURNING

Put SET available=available-1 and WHERE available>0 into one statement. Under READ COMMITTED a competing UPDATE waits then rechecks WHERE on the updated row version: after the first decrements to zero the second updates zero rows. RETURNING yields the new value only for the winner; CHECK available>=0 is useful defense in depth.

```sql
UPDATE inventory SET available=available-1
WHERE sku='IPHONE-17' AND available>0
RETURNING available;
```

### Reservation is separate from payment

Reservation can be a short atomic transaction, while the provider is outside PostgreSQL. A complete checkout needs reservation IDs, orderId deduplication, expiration/release, a payment workflow and compensation for partial failures; this is a deeper follow-up topic.


## Resources

PostgreSQL MVCC row versions, row locks, transactions and connections; business state is outside Pod processes.

## Pitfalls and constraints

READ COMMITTED is not SERIALIZABLE. SELECT FOR UPDATE in a proper transaction can protect read-then-update, but holding a row lock over a remote ChargeAsync is risky. One-SKU SQL does not make Payment/Order part of a single ACID transaction.

## Example

```sql
UPDATE inventory
SET available=available-1
WHERE sku='IPHONE-17' AND available>0
RETURNING available;
```

## Review questions

- [Q-074: Can two Pods under READ COMMITTED both read available=1 and then reach -1 via unconditional UPDATE?](../../../../questions/dotnet/en/Q-074-postgres-read-committed-check-act.md)
- [Q-075: How can one UPDATE ... RETURNING statement protect the last item?](../../../../questions/dotnet/en/Q-075-postgres-conditional-update-returning.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

What does READ COMMITTED mean for two SELECT statements?

<details>
<summary>Answer criteria</summary>

Each statement sees its own committed snapshot.

</details>

### 2. Explain

Why can the second UPDATE cause -1 despite row locking?

<details>
<summary>Answer criteria</summary>

After waiting it uses the updated row version with no available>0 predicate.

</details>

### 3. Predict

What does the second UPDATE ... WHERE available>0 RETURNING return?

<details>
<summary>Answer criteria</summary>

Zero updated rows after predicate recheck.

</details>

### 4. Diagnose

What to inspect for oversell after scale-out?

<details>
<summary>Answer criteria</summary>

SQL WHERE, isolation, row waits, missing CHECK and retries.

</details>

### 5. Design

How to reserve SKU without Redis locks or a transaction spanning payment?

<details>
<summary>Answer criteria</summary>

Short conditional UPDATE, reservation idempotency and separate payment workflow.

</details>


## References

- [https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)
- [https://www.postgresql.org/docs/current/sql-update.html](https://www.postgresql.org/docs/current/sql-update.html)

---

[← Previous](payment-timeout-idempotency-outbox.md) · [Русский](../postgres-read-committed-stock.md) · [English](postgres-read-committed-stock.md)
