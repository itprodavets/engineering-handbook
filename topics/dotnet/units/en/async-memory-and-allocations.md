# Memory, state machines and async allocation cost

[Русский](../async-memory-and-allocations.md) · [English](async-memory-and-allocations.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-memory-and-allocations)

> Measure real async costs without inventing object sizes.

## Definition

The `async` syntax does not imply a fixed number of heap objects. A completed fast path may avoid allocating a new Task; incomplete awaits require retaining continuation state, which can require heap storage.

## Internal mechanics

1. Roslyn generates a state machine and captures necessary locals.
2. The state machine can complete an already-ready operation without scheduling a continuation.
3. Pending await state must survive until resumed; exact heap storage depends on implementation.
4. Measurements need warm-up and controlled conditions; per-thread allocation and process-wide allocation are different metrics.

## Step-by-step explanation

### State machine ≠ a heap allocation per call

A generated state machine type means state must be represented, but does not guarantee one heap object per invocation. Actual representation depends on whether a pending await was encountered and runtime optimizations. An `async Task` method that always completes synchronously may reuse a completed Task.

### A sound measurement protocol

Warm up code and JIT, establish a baseline, run repeated iterations with fixed .NET version and architecture. `GC.GetAllocatedBytesForCurrentThread()` measures managed allocations made by the current thread; it omits other threads, retained heap size and native resources. Use BenchmarkDotNet for careful comparisons.

### Pending continuations retain references

While an async method is suspended, captured locals and `this` can remain reachable. Cancellation and timeouts should let work complete and release resources. Distinguish transient allocations from retained-memory leaks.

### When to consider ValueTask

ValueTask<T> can reduce allocations for often-synchronous completion but complicates consumption and does not always improve performance. Decide based on profiling rather than the mere presence of await.


## Resources

Task/awaiter/captured locals/continuation, JIT and GC CPU; exact bytes and time require measured workload/environment.

## Pitfalls and constraints

A single run can be distorted by JIT, GC, caching, warm-up and thread changes.

## Example

```csharp
long before = GC.GetAllocatedBytesForCurrentThread();
// Execute a controlled hot path repeatedly here.
long bytes = GC.GetAllocatedBytesForCurrentThread() - before;
```

## Runnable experiments

- [04-allocations.cs](../../../../labs/dotnet/async-internals/04-allocations.cs) — `dotnet run --file labs/dotnet/async-internals/04-allocations.cs`

## Review questions


## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Can you derive an exact heap allocation count from the async keyword?

<details>
<summary>Answer criteria</summary>

No; completion path, implementation, runtime version and optimizations matter.

</details>

### 2. Explain

What must remain reachable across a pending await, and why?

<details>
<summary>Answer criteria</summary>

State, awaiter, required locals and continuation until completion.

</details>

### 3. Predict

Does awaiting Task.CompletedTask 1,000 times create 1,000 OS threads?

<details>
<summary>Answer criteria</summary>

No; completed Tasks take the synchronous fast path; await does not create threads.

</details>

### 4. Diagnose

Why is a single GC.GetAllocatedBytesForCurrentThread measurement unreliable?

<details>
<summary>Answer criteria</summary>

Needs warm-up, baseline and repetitions; per-thread != entire process, GC/JIT add noise.

</details>

### 5. Design

When is ValueTask<T> justified and when is Task<T> preferable?

<details>
<summary>Answer criteria</summary>

Measure synchronous completion frequency, allocation and consumers; ValueTask may help hot paths; Task is simpler for composition.

</details>


## References

- [https://devblogs.microsoft.com/dotnet/how-async-await-really-works/](https://devblogs.microsoft.com/dotnet/how-async-await-really-works/)

---

[← Previous](async-socket-pipeline.md) · [Next →](async-production-capstone.md) · [Русский](../async-memory-and-allocations.md) · [English](async-memory-and-allocations.md)
