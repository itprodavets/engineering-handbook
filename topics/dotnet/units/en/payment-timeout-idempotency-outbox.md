# Lost payment responses: Outbox and idempotency

[Русский](../payment-timeout-idempotency-outbox.md) · [English](payment-timeout-idempotency-outbox.md)

[Home](../../../../README.en.md) · [Module](../../en/microservices-concurrency.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/payment-timeout-idempotency-outbox)

> Explain partial failures and protect financial operations against duplicate effects.

## Definition

A ChargeAsync timeout does not prove rollback: the bank may have debited funds before losing the reply. Retrying with a new identity may debit again. A stable idempotency key must be enforced by the provider. Transactional Outbox atomically saves local state plus an event but does not prevent redelivery.

## Internal mechanics

1. OrderService sends ChargeAsync to the external provider.
2. The provider commits the debit, but the reply is lost.
3. Timeout leaves an unknown outcome; CancellationToken cannot undo a committed remote side effect.
4. Retries of one logical attempt must reuse its persisted idempotency key.
5. Outbox persists state and event atomically, relays may redeliver, and consumers must deduplicate.
6. Unknown outcomes must be reconciled via provider status APIs/webhooks and durable attempt records.

## Step-by-step explanation

### Debit committed but response lost

A transport timeout indicates failure to receive the response, not payment rollback. The provider may have completed its side effect. Local cancellation cannot atomically undo a remote transaction. Persist paymentAttemptId and states Unknown/Pending/Succeeded/Failed and reconcile instead of blindly charging again.

### One logical payment, one stable retry key

Persist a stable ID for one logical attempt. Reuse the same key and parameters for transport retries. The receiving provider must deduplicate atomically. Q-071 is a sequential in-memory illustration, not a network or cross-process bank test.

### Outbox persists events, not unique payments

Transactional Outbox saves the local Order change with its outbox event in one transaction. A relay can publish, crash before marking delivered, and publish again. PaymentRequested needs consumer inbox/deduplication, while the external charge needs a provider idempotency key and reconciliation.


## Resources

External connections, idempotency keys, payment-attempt IDs, outbox/inbox tables and event delivery.

## Pitfalls and constraints

Local SemaphoreSlim does not survive restarts or coordinate Pods. Outbox does not guarantee exactly-once external payments; key semantics and TTL depend on provider policy.

## Example

```csharp
await provider.ChargeAsync(orderId, amount, stableIdempotencyKey, ct);
```

## Runnable experiments

- [Q-071.cs](../../../../labs/dotnet/Q-071.cs) — `dotnet run --file labs/dotnet/Q-071.cs`

## Review questions

- [Q-071: Can retrying ChargeAsync after a lost bank reply charge twice?](../../../../questions/dotnet/en/Q-071-payment-timeout-duplicate-charge.md)
- [Q-072: Why does Transactional Outbox not replace payment-provider idempotency?](../../../../questions/dotnet/en/Q-072-outbox-not-charge-idempotency.md)
- [Q-073: Does gRPC DeadlineExceeded or local CancellationToken roll back an already committed payment?](../../../../questions/dotnet/en/Q-073-remote-timeout-not-rollback.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Why does a timeout not prove the bank did not debit?

<details>
<summary>Answer criteria</summary>

The reply may be lost after a successful debit.

</details>

### 2. Explain

How does Outbox differ from a provider idempotency key?

<details>
<summary>Answer criteria</summary>

Outbox protects local state+event atomicity; the key deduplicates remote side effects.

</details>

### 3. Predict

Can a retry with a new key cause duplicate debits?

<details>
<summary>Answer criteria</summary>

Yes, when the first charge outcome is unknown.

</details>

### 4. Diagnose

How to reconcile payment after timeout?

<details>
<summary>Answer criteria</summary>

Payment-attempt ID, provider status API/webhook, telemetry and audit.

</details>

### 5. Design

How to design Order→Payment under outbox redelivery?

<details>
<summary>Answer criteria</summary>

Outbox+Inbox, stable provider key, persisted attempts and reconciliation.

</details>


## References

- [https://stripe.com/blog/idempotency](https://stripe.com/blog/idempotency)
- [https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
- [https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[← Previous](remote-io-permit-lifetime.md) · [Next →](postgres-read-committed-stock.md) · [Русский](../payment-timeout-idempotency-outbox.md) · [English](payment-timeout-idempotency-outbox.md)
