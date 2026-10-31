# volatile, Interlocked and atomic read-modify-write

[Русский](../atomicity-and-memory-visibility.md) · [English](atomicity-and-memory-visibility.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/atomicity-and-memory-visibility)

> Distinguish single-operation atomicity, acquire/release and by-reference updates.

## Definition

C# volatile provides acquire semantics for reads and release for writes but does not make ++ atomic. Interlocked.Increment(ref int) atomically modifies one variable without acquiring a C# Monitor. ref refers to the variable location, not to whether the containing type is a class.

## Internal mechanics

1. An ordinary ++ logically includes read/compute/write; two threads may both write the same new value.
2. Volatile reads/writes provide partial acquire/release ordering, not mutual exclusion across read and write.
3. Interlocked.Increment(ref int) performs indivisible read-modify-write on a variable; two increments starting at zero yield 2.
4. CLR/JIT typically emits hardware atomic operations; exact instructions and costs vary with architecture and contention.
5. Atomic RMW does not protect separately performed checks, other fields or an external transaction; these need a larger protocol.

## Step-by-step explanation

### Atomicity, visibility and ordering

Atomicity means an operation is indivisible; visibility concerns observations across threads under appropriate synchronization; ordering concerns compiler/JIT/CPU rearrangements. These are distinct properties; acquire/release is not the same as atomic RMW.

### What volatile guarantees

C# volatile reads have acquire semantics and writes have release semantics. This restricts certain reorderings across those accesses; it is NOT a global sequential order and does not make Value++ atomic. Two volatile increments can still lose an update.

```csharp
sealed class Counter { public volatile int Value; }
// Value++ still reads, computes and writes separately
```

### How ref passes the original variable

Interlocked.Increment(ref int location) receives the int variable by reference. It directly updates a local int, an int field, or an array element when valid ref usage permits. It typically uses CPU atomics instead of Monitor.Enter/Exit.

```csharp
int counter=0;
int updated=Interlocked.Increment(ref counter);
// updated=1; counter=1
```

### What Interlocked does not guarantee

An atomic single-counter increment does not create a critical section around neighboring operations. Check-and-decrement requires a CAS loop or lock. Separate updates to other fields are not covered by the same atomicity guarantee.


## Resources

Cache-coherence traffic and contention over shared cache lines. Atomic RMW can be costlier than normal writes; it is not a Monitor lock nor a promise of zero CPU stalls.

## Pitfalls and constraints

volatile does not make counter++ atomic, establish a universal total order, or guarantee that reads always see the chronologically latest value. ref also works with value-type int; do not confuse it with Counter being a class.

## Example

```csharp
int counter = 0;
Interlocked.Increment(ref counter); // atomically counter=1
```

## Runnable experiments

- [Q-042.cs](../../../../labs/dotnet/Q-042.cs) — `dotnet run --file labs/dotnet/Q-042.cs`

## Review questions

- [Q-021: Why is volatile counter++ unsafe, and how do Interlocked.Increment and lock differ?](../../../../questions/dotnet/en/Q-021-volatile-vs-interlocked.md)
- [Q-028: Is counter always 10,000? Why or why not?](../../../../questions/dotnet/en/Q-028-lost-update-race.md)
- [Q-041: Why does volatile int Value not make Value++ atomic, and what ordering does C# volatile provide?](../../../../questions/dotnet/en/Q-041-volatile-does-not-make-plus-plus-atomic.md)
- [Q-042: What does Interlocked.Increment(ref int) guarantee, and why is ref unrelated to Counter being a reference type?](../../../../questions/dotnet/en/Q-042-interlocked-increment-ref.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Distinguish atomicity, visibility and ordering. What do volatile acquire/release operations mean?

<details>
<summary>Answer criteria</summary>

Three distinct properties; C# volatile read acquire, write release. No global total order or atomic ++.

</details>

### 2. Explain

Explain why two volatile Value++ operations may still result in 1.

<details>
<summary>Answer criteria</summary>

Both read 0, compute 1 and write 1. volatile does not combine the operations.

</details>

### 3. Predict

After two completed Interlocked.Increment(ref counter) from zero, what is the final value after WhenAll?

<details>
<summary>Answer criteria</summary>

2; each atomic RMW updates the same variable; ref refers to the int location.

</details>

### 4. Diagnose

A volatile flag behaves as expected but an increment counter loses updates. Diagnose the mechanism.

<details>
<summary>Answer criteria</summary>

Non-atomic RMW; use Interlocked/lock, force an interleaving in a test, assert the invariant.

</details>

### 5. Design

Choose volatile, Interlocked or lock for a flag, counter and multi-field invariant.

<details>
<summary>Answer criteria</summary>

volatile for suitable signaling/ordering protocols; Interlocked for a single atomic state update; lock for a shared multi-field critical section.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read](https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read)

---

[← Previous](race-condition-vs-data-race.md) · [Next →](compare-exchange-cas-loop.md) · [Русский](../atomicity-and-memory-visibility.md) · [English](atomicity-and-memory-visibility.md)
