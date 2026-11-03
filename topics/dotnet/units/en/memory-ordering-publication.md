# Memory model: visibility, ordering and safe publication

[Русский](../memory-ordering-publication.md) · [English](memory-ordering-publication.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/memory-ordering-publication)

> Reason about release/acquire publication, JIT, OS scheduling and happens-before.

## Definition

An atomic flag store does not by itself publish surrounding data. Correct message-passing protocol: write data=42, then Volatile.Write(ready,1) (release); the consumer uses Volatile.Read(ready) (acquire) and reads data only after observing 1. With no other writers, this publishes 42. Publishing the flag before the data permits observing 0.

## Internal mechanics

1. Producer stores data before the release publication of ready=1. The matching acquire observation orders the subsequent data read.
2. Publishing ready=1 first allows the consumer to read data=0 before the later data=42 write; volatile cannot repair the incorrect program order.
3. Without Volatile.Read, ordinary reads inside a loop do not establish the protocol; JIT/CPU optimizations including read hoisting may apply.
4. Thread.Yield affects OS scheduling, but is not an acquire operation or a contractually specified memory fence and establishes no happens-before relationship.
5. The volatile protocol does not guarantee fairness, scheduling or bounded spin time; Tasks, Channels or other higher-level primitives are often preferable in production.

## Step-by-step explanation

### Atomicity is not visibility or ordering

Atomicity concerns indivisible accesses; visibility concerns what another thread observes under an established synchronization protocol; ordering concerns allowed reorderings. An atomic int store alone does not order two different stores. JIT, CPU and scheduler have distinct responsibilities. Prove a protocol by the actual operations, not by assuming caches will refresh.

### Correct publication: data before ready

The producer writes data=42 and then uses release Volatile.Write(ref ready,1). The consumer polls using acquire Volatile.Read and reads data after observing 1; absent other writers, it observes 42. This is the message-passing example covered by the C# language specification. The flag may continue to read as zero for some time; no bounded wait is promised.

```csharp
data = 42;
Volatile.Write(ref ready, 1);
// Consumer: if (Volatile.Read(ref ready) == 1) Console.WriteLine(data); // 42
```

### Publishing before data permits 0

If release-store ready=1 precedes data=42, it does not publish a later store. The consumer can observe ready=1 and data=0. Possible sequence: publish flag → consumer observes flag → reads zero → producer writes 42. Q-049 uses an explicit test gate to make that interleaving deterministic.

```csharp
Volatile.Write(ref ready, 1);
data = 42; // too late for publication
```

### Non-volatile polling and the JIT

Without volatile, `while (ready==0) { }` has no synchronized reads. Under applicable conditions the JIT may hoist or otherwise optimize an ordinary load, so termination is not guaranteed. The actual optimization varies by implementation; do not claim it must occur or run unsafe infinite spin tests in CI.

```csharp
while (ready == 0) { } // no synchronization contract
```

### Thread.Yield is not a memory barrier

Thread.Yield offers the current time slice to another runnable thread. It is not an acquire read nor a memory visibility contract. A loop that happens to terminate on a particular runtime does not prove safe publication. Its boolean result reports scheduling, not memory ordering.

```csharp
while (ready == 0) { Thread.Yield(); } // not a synchronization fix
```

### Why ordinary ready=1 is not safe publication

Compare (1) producer `data=42; Volatile.Write(ref ready,1);` and consumer `if (Volatile.Read(ref ready)==1) Console.WriteLine(data);`—with a single producer and no competing data writers, 42 is safely published—with (2) producer `data=42; ready=1;` and consumer `if (ready==1) Console.WriteLine(data);`. Ordinary flag accesses do not establish the required synchronization; observing 1 is not proof of safely published data under the C#/.NET contract. Distinguish permitted JIT optimization, CPU/cache behavior and OS interleavings. A particular runtime may often print 42 without a normative guarantee. Prefer `Task<T>`, `Channel<T>`, or a correct release/acquire protocol in production.

```csharp
// Safe publication
int data = 0, ready = 0;
// Producer: data = 42; Volatile.Write(ref ready, 1);
// Consumer: if (Volatile.Read(ref ready) == 1) Console.WriteLine(data);

// Unsafe publication: ordinary accesses to ready
// Producer: data = 42; ready = 1;
// Consumer: if (ready == 1) Console.WriteLine(data);
```


## Resources

Atomic reads/writes, JIT/CPU ordering, busy-wait CPU costs, cache coherence and OS scheduling.

## Pitfalls and constraints

Volatile.Read does not promise the chronologically latest store on every core; Thread.Yield does not synchronize memory. An unsafe infinite spin loop must not be used as an executable test. Publishing an object also requires reasoning about later mutations.

## Example

```csharp
int data = 0, ready = 0;
Task producer = Task.Run(() => { data = 42; Volatile.Write(ref ready, 1); });
Task consumer = Task.Run(() => { while (Volatile.Read(ref ready) == 0) Thread.Yield(); Console.WriteLine(data); });
await Task.WhenAll(producer, consumer); // prints 42
```

## Runnable experiments

- [Q-048.cs](../../../../labs/dotnet/Q-048.cs) — `dotnet run --file labs/dotnet/Q-048.cs`
- [Q-049.cs](../../../../labs/dotnet/Q-049.cs) — `dotnet run --file labs/dotnet/Q-049.cs`

## Review questions

- [Q-048: Why does data=42 before release-store and acquire-reading ready safely publish 42?](../../../../questions/dotnet/en/Q-048-safe-publication-acquire-release.md)
- [Q-049: Can the consumer see zero if producer publishes ready before writing data?](../../../../questions/dotnet/en/Q-049-release-before-data-allows-zero.md)
- [Q-050: Does while(ready==0) without volatile necessarily terminate after another thread writes ready=1?](../../../../questions/dotnet/en/Q-050-nonvolatile-loop-jit-hoisting.md)
- [Q-051: Why does Thread.Yield in an ordinary polling loop not replace Volatile.Read?](../../../../questions/dotnet/en/Q-051-thread-yield-is-not-memory-fence.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Define atomicity, visibility and ordering. Distinguish acquire and release.

<details>
<summary>Answer criteria</summary>

Atomicity is indivisibility, visibility is cross-thread observation, ordering constrains reordering. Acquire governs later accesses; release prior accesses.

</details>

### 2. Explain

Explain why data=42 precedes the release flag store and why the consumer uses an acquire read.

<details>
<summary>Answer criteria</summary>

Correct publication protocol: observing 1 makes prior data stores visible. No bounded-wait guarantee.

</details>

### 3. Predict

Compare (A) producer data=42 then release flag, consumer acquire-reads; and (B) producer release-stores flag before data=42. Can each consumer print zero, and why?

<details>
<summary>Answer criteria</summary>

In (A), absent interfering writers, observing the published flag implies data=42. In (B), zero is possible without any CPU/JIT reordering: the consumer runs after the flag but before the data write. Atomic increment does not solve publication ordering.

</details>

### 4. Diagnose

Can Thread.Yield guarantee termination of an ordinary `while(ready==0)` polling loop? How would you investigate?

<details>
<summary>Answer criteria</summary>

No. Scheduling is not memory synchronization. Inspect JIT optimizations, memory protocol, field type, volatile/locks, CPU starvation.

</details>

### 5. Design

Design producer-to-consumer transfer without busy-waiting.

<details>
<summary>Answer criteria</summary>

Prefer Task<T>/await, Channel<T> or proper synchronization primitives; handle errors, cancellation and resource usage.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read](https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0)

---

[← Previous](atomicity-and-memory-visibility.md) · [Next →](compare-exchange-cas-loop.md) · [Русский](../memory-ordering-publication.md) · [English](memory-ordering-publication.md)
