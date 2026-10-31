# Race conditions, data races and lost updates

[Русский](../race-condition-vs-data-race.md) · [English](race-condition-vs-data-race.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/race-condition-vs-data-race)

> Detect violated invariants; distinguish scheduling races from unsynchronized memory accesses.

## Definition

A race condition occurs when correctness depends on the ordering of concurrent events and some legal ordering breaks an invariant. A data race involves conflicting unsynchronized accesses to one memory location from different threads, at least one being a write. A logical race can exist without a data race, e.g. separate atomic check and act.

## Internal mechanics

1. Two Task.Run delegates can share a Counter instance; its reference type does not imply a monitor or automatically block workers.
2. counter++ logically includes read, compute and write; both threads may read 0 and then write 1, losing an increment.
3. Task.WhenAll waits for both operations but does not serialize modifications; two increments may leave 1 or 2.
4. Atomic individual int loads/stores do not make ++ atomic; interleavings can occur even on a single CPU core.
5. State the invariant explicitly, e.g., stock >= 0; verify synchronization protects the entire operation rather than one instruction.

## Step-by-step explanation

### Race condition versus data race

A race condition is an algorithmic correctness failure depending on event order. A data race describes conflicting unsynchronized memory accesses. Even if all individual accesses are atomic and there is no data race, split check and act steps can violate a business invariant.

### Lost update: two reads of 0

Interleaving T1:read(0), T2:read(0), T1:write(1), T2:write(1) can happen for normal counter++. Both delegates finish but counter=1 rather than 2. Task.Run does not guarantee a new thread per Task.

### Why one CPU core is enough

The OS can switch between threads after the read but before the write. A race depends on interleavings, not necessarily simultaneous instructions on separate cores. A Task does not intrinsically own an OS thread stack.

### Invariants over guessing output

For two successful logical increments we expect 2; for inventory we require stock >= 0. Enumerate possible interleavings and identify the operation that must be atomic. Distinguish the value returned by postfix ++ from the final stored value.


## Resources

Shared mutable state, cache lines and CPU time; contention increases synchronization cost. Physical parallel execution is not required for a race.

## Pitfalls and constraints

Do not confuse races with deadlocks or assume Task implies blocking. Do not blindly apply C++ undefined-behavior rules to C#/.NET. Q-040 forces an async interleaving to demonstrate lost updates; it is not a specific OS scheduling trace.

## Example

```csharp
var state = new Counter();
await Task.WhenAll(Task.Run(() => state.Value++), Task.Run(() => state.Value++));
Console.WriteLine(state.Value); // 1 or 2
// Counter has public int Value;
```

## Runnable experiments

- [Q-040.cs](../../../../labs/dotnet/Q-040.cs) — `dotnet run --file labs/dotnet/Q-040.cs`

## Review questions

- [Q-039: How do race conditions differ from data races, and can a logical race occur without a data race?](../../../../questions/dotnet/en/Q-039-race-condition-vs-data-race.md)
- [Q-040: What outcomes are possible after two Task.Run(() => state.Value++) and awaiting Task.WhenAll, starting at Value=0?](../../../../questions/dotnet/en/Q-040-lost-update-two-task-run.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

What is the difference between a race condition and a data race?

<details>
<summary>Answer criteria</summary>

Race: invariant violation due to event ordering; data race: conflicting unsynchronized memory accesses. Logical races need not include data races.

</details>

### 2. Explain

Explain the lost-update interleaving for two counter++ operations starting at 0.

<details>
<summary>Answer criteria</summary>

Read/modify/write are separate; both read 0 and write 1.

</details>

### 3. Predict

What final values are possible after two Task.Run(() => state.Value++) calls and awaiting WhenAll?

<details>
<summary>Answer criteria</summary>

1 or 2. Task.WhenAll waits for completion but does not protect the field.

</details>

### 4. Diagnose

Orders occasionally lose updates under concurrency. How do you prove the race?

<details>
<summary>Answer criteria</summary>

Define the invariant, construct a concrete interleaving, reproduce with gated scheduling, collect traces, and rule out other causes.

</details>

### 5. Design

How would you guarantee two increments of a shared counter?

<details>
<summary>Answer criteria</summary>

Interlocked.Increment(ref value) for a single counter; lock for related state invariants. Explain tradeoffs and why simple increments do not require Task.Run.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/expressions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/expressions)
- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)
- [https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices](https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices)

---

[Next →](atomicity-and-memory-visibility.md) · [Русский](../race-condition-vs-data-race.md) · [English](race-condition-vs-data-race.md)
