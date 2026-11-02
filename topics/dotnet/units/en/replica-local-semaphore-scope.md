# SemaphoreSlim is Pod-local while inventory is shared

[Русский](../replica-local-semaphore-scope.md) · [English](replica-local-semaphore-scope.md)

[Home](../../../../README.en.md) · [Module](../../en/microservices-concurrency.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/replica-local-semaphore-scope)

> Explain the scope of static and the source of races between replicas.

## Definition

Three Kubernetes Pods have three independent copies of static SemaphoreSlim(1,1), so three checkouts can pass local gates simultaneously. Enforce the shared stock invariant in InventoryService/PostgreSQL, not OrderService.

## Internal mechanics

1. Each Pod runs a separate CLR process with its own static fields.
2. All three Gates can independently transition 1→0 upon WaitAsync.
3. All three Checkouts may concurrently call the shared InventoryService.ReserveAsync.
4. Only the shared state owner can enforce the SKU invariant using atomic SQL and reservation idempotency.

## Step-by-step explanation

### Three Pods — three permits

Pods A/B/C each host a static Gate in a separate address space. All three calls may independently enter their critical sections and call ReserveAsync at once. Q-068 simulates independent gates in one process; it is a scope demonstration, not a live Kubernetes/network test.

### Invariant at the InventoryService boundary

InventoryService/PostgreSQL owns available and must atomically decide the last item. A local SemaphoreSlim can bound per-instance load, but cannot coordinate replicas or provide exactly-once reservations.

### Why a Redis lease is not automatically safe

A distributed lease may expire during pauses, partitions or slow work. An old holder can continue after another acquires the lock, requiring atomic state-side checks and possibly fencing tokens.


## Resources

Three independent gate counters, ThreadPools and Task states; one shared PostgreSQL row and its transactions.

## Pitfalls and constraints

static does not make an object cluster-global. Redis lease locks have expiration/fencing hazards and do not replace an atomic business predicate.

## Example

```csharp
private static readonly SemaphoreSlim Gate = new(1, 1); // one per process
```

## Runnable experiments

- [Q-068.cs](../../../../labs/dotnet/Q-068.cs) — `dotnet run --file labs/dotnet/Q-068.cs`

## Review questions

- [Q-068: Does static SemaphoreSlim(1,1) protect a last-item SKU across three Pods?](../../../../questions/dotnet/en/Q-068-static-semaphore-three-pods.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

How many static SemaphoreSlim instances exist in three Pods?

<details>
<summary>Answer criteria</summary>

Three, each process-local.

</details>

### 2. Explain

Why can three requests invoke ReserveAsync simultaneously?

<details>
<summary>Answer criteria</summary>

Each gate is independent; there is no shared Gate.

</details>

### 3. Predict

Does Gate(1,1) inside OrderService protect the last SKU?

<details>
<summary>Answer criteria</summary>

No, only the local Pod.

</details>

### 4. Diagnose

Why did overselling emerge after scaling out?

<details>
<summary>Answer criteria</summary>

Inspect local locks, SQL check-then-act and retries.

</details>

### 5. Design

Where should globally safe stock checks be implemented?

<details>
<summary>Answer criteria</summary>

InventoryService/PostgreSQL conditional update and business idempotency.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
- [https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)

---

[Next →](remote-io-permit-lifetime.md) · [Русский](../replica-local-semaphore-scope.md) · [English](replica-local-semaphore-scope.md)
