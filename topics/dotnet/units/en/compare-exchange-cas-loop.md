# CompareExchange, CAS loops and the stock ≥ 0 invariant

[Русский](../compare-exchange-cas-loop.md) · [English](compare-exchange-cas-loop.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/compare-exchange-cas-loop)

> Understand what CAS changes via ref, what previous returns and why contention requires retries.

## Definition

CompareExchange atomically compares a location with the expected comparand and conditionally stores the new value; it always returns the location's pre-operation value. A CAS loop rereads and retries after contention and can preserve the stock >= 0 invariant.

## Internal mechanics

1. Interlocked.CompareExchange(ref stock, 0, 1) atomically writes 0 if stock==1 and returns the previous 1. If stock==0, it does not write and returns 0.
2. ref passes the variable location, even for value-type int. current is an independent local snapshot; current-1 only computes a proposed value.
3. Separate Volatile.Read(stock)>0 and Interlocked.Decrement(stock) leave a check-then-act window; both buyers can observe 1 and decrement it to -1.
4. A one-shot CAS(3→2) has only one winner; the other sees previous==2 and must not claim success.
5. A CAS loop rereads stock after failure: if positive it retries with a fresh expected value; if zero it returns false.
6. Lock-free does not mean wait-free: an individual thread can repeatedly lose CAS while the system makes progress.

## Step-by-step explanation

### ref and the three CAS arguments

Signature: int CompareExchange(ref int location, int value, int comparand). location is stock itself; value is the new value; comparand is expected. The method returns the old value even on failure. For stock=10 and current=10, CompareExchange(ref stock,current-3,current) writes 7, leaves current at 10 and returns previous=10.

```csharp
int stock=10, current=10;
int previous=Interlocked.CompareExchange(ref stock,current-3,current);
// stock=7; current=10; previous=10
```

### Atomic operation is not an atomic algorithm

Volatile.Read(ref stock)>0 and Interlocked.Decrement(ref stock) are separate. Both buyers can observe stock=1 before either decrements, then each atomically decrements: 1→0→-1. CAS combines expected-value validation and write into one atomic operation.

```csharp
if (Volatile.Read(ref stock)>0)
    Interlocked.Decrement(ref stock); // unsafe check-then-act
```

### One item and two competing CAS calls

From stock=1 only one thread can CAS 1→0; the winner gets previous=1 and prints Purchased. The loser receives previous=0. With stock=3, two one-shot CAS(3→2) calls still allow only one transition: insufficient for two purchases.

### CAS-loop trace: stock=3 and two buyers

Both read current=3. T1 CAS(3→2) succeeds; stock becomes 2, previous=3. T2 CAS(3→2) fails with previous=2 and does not change stock. It loops, reads current=2, CAS(2→1) succeeds returning previous=2. Two purchases leave stock=1. With five buyers competing for stock=1, only one returns true; others reread zero and return false.

### Linearization point and algorithm boundaries

Successful CAS is the atomic point at which a purchase commits an inventory decrement; a read yielding zero justifies failure at that observation. This is a linearizable in-memory counter assuming all writers follow the same protocol and no restocking in this exercise. Real inventory also needs database transactions, idempotency and reservation semantics.


## Resources

Hardware/runtime atomic operations, cache coherence, contention and retry costs. Pausing one worker need not stop progress of others in a lock-free CAS loop.

## Pitfalls and constraints

CompareExchange returns the OLD value, not newValue. One-shot CAS does not support arbitrary inventory. A correct in-memory CAS is not a transaction spanning inventory, payment and database. The loop is not wait-free.

## Example

```csharp
static bool TryBuy(ref int stock)
{
    while (true)
    {
        int current = Volatile.Read(ref stock);
        if (current <= 0) return false;
        int previous = Interlocked.CompareExchange(ref stock, current - 1, current);
        if (previous == current) return true;
    }
}
```

## Runnable experiments

- [Q-043.cs](../../../../labs/dotnet/Q-043.cs) — `dotnet run --file labs/dotnet/Q-043.cs`
- [Q-044.cs](../../../../labs/dotnet/Q-044.cs) — `dotnet run --file labs/dotnet/Q-044.cs`
- [Q-045.cs](../../../../labs/dotnet/Q-045.cs) — `dotnet run --file labs/dotnet/Q-045.cs`
- [Q-046.cs](../../../../labs/dotnet/Q-046.cs) — `dotnet run --file labs/dotnet/Q-046.cs`
- [Q-047.cs](../../../../labs/dotnet/Q-047.cs) — `dotnet run --file labs/dotnet/Q-047.cs`

## Review questions

- [Q-043: Can stock become -1 after a volatile positive check and an Interlocked.Decrement when starting at stock=1?](../../../../questions/dotnet/en/Q-043-check-then-act-stock-negative.md)
- [Q-044: Starting from stock=1, what does CompareExchange(ref stock,0,1) return and what is stock afterward?](../../../../questions/dotnet/en/Q-044-compareexchange-returns-prior.md)
- [Q-045: Can both threads successfully execute CompareExchange(ref stock,0,1) when stock starts at 1?](../../../../questions/dotnet/en/Q-045-two-buyers-single-item-cas.md)
- [Q-046: If stock=3 and two threads perform CompareExchange(ref stock,2,3), how many succeed and what do the calls return?](../../../../questions/dotnet/en/Q-046-two-buyers-stock-three-single-cas.md)
- [Q-047: How does a CAS loop behave with stock=3/two buyers and stock=1/five buyers?](../../../../questions/dotnet/en/Q-047-cas-loop-five-buyers.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Name the arguments to CompareExchange and its return value.

<details>
<summary>Answer criteria</summary>

ref location, value(new), comparand(expected). Returns the pre-operation location value, not the new value.

</details>

### 2. Explain

Why does CAS avoid overselling when volatile check + Interlocked.Decrement does not?

<details>
<summary>Answer criteria</summary>

CAS atomically combines check and update; only one 1→0 transition can occur. A split check-then-act allows both decrements.

</details>

### 3. Predict

Both threads read current=3. First CAS(3→2) succeeds; second fails. What are the second thread's current, previous and stock values, and what happens next?

<details>
<summary>Answer criteria</summary>

On failure current=3, previous=2, stock=2; next loop reads current=2, CAS(2→1) returns previous=2 and leaves stock=1.

</details>

### 4. Diagnose

Why does a large number of CAS retries not imply deadlock or wait freedom?

<details>
<summary>Answer criteria</summary>

Other threads can make progress while one loses repeatedly; lock-free is not wait-free. Measure contention/retries and investigate backoff.

</details>

### 5. Design

Design TryBuy preserving stock>=0 without lock for five buyers and one item.

<details>
<summary>Answer criteria</summary>

Volatile.Read; reject at <=0; CAS(old→old-1); success if previous==old; otherwise retry with fresh value. One true, four false, stock zero. This is not a DB transaction.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read](https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read)
- [https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives](https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives)

---

[← Previous](atomicity-and-memory-visibility.md) · [Next →](mutual-exclusion-and-semaphores.md) · [Русский](../compare-exchange-cas-loop.md) · [English](compare-exchange-cas-loop.md)
