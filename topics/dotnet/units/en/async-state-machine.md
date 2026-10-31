# What the compiler generates for async/await

[Русский](../async-state-machine.md) · [English](async-state-machine.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-state-machine)

> Understand MoveNext, awaiters and the IsCompleted fast path.

## Definition

Roslyn lowers an async method into a state machine with saved state and a MoveNext() method. The async keyword does not start a thread.

## Internal mechanics

1. Calling an async Task method starts executing on the caller thread until an incomplete awaitable is reached.
2. Awaiter.IsCompleted=true permits synchronous continuation via GetResult(), without a mandatory thread switch.
3. When IsCompleted=false, the state machine stores its position, registers a continuation, and returns a Task to its caller.
4. After completion, MoveNext resumes execution; heap allocations depend on the path and implementation.

## Step-by-step explanation

### What Roslyn actually produces

For an `async Task<T>` method, Roslyn emits an `IAsyncStateMachine` implementation with state, awaiter, captured locals and an `AsyncTaskMethodBuilder<T>`. The entry point initializes the state machine, calls builder.Start(ref stateMachine) and returns builder.Task. Physical details can differ across Debug/Release and compiler/runtime versions.

### MoveNext: the completed fast path and pending await

In `MoveNext()`, GetAwaiter obtains the awaiter. If IsCompleted is true, GetResult runs immediately and execution continues. Otherwise the state machine stores its state number and awaiter, and the builder registers a continuation using machinery such as `AwaitUnsafeOnCompleted`. This is a *schematic* explanation; inspect a compiled assembly for actual IL.

```csharp
// Schematic, NOT literal Roslyn-generated C#:
var awaiter = operation.GetAwaiter();
if (!awaiter.IsCompleted)
{
    state = 0;
    savedAwaiter = awaiter;
    builder.AwaitUnsafeOnCompleted(ref awaiter, ref this);
    return;
}
var value = awaiter.GetResult();
```

### Completion, errors and continuations

When awaited work completes, the continuation calls MoveNext again, restores state/awaiter and calls GetResult (which may rethrow the operation’s exception). Success flows to builder.SetResult; failures to SetException. Async splits one logical method into executable segments and does not require a new OS thread.

### How to inspect real emitted code

Compile a small example in Debug and Release, inspect the assembly in ILSpy or SharpLab, and compare MoveNext, state fields, GetAwaiter, IsCompleted and builder calls. Runtime output alone does not prove specific emitted IL instructions. Investigate heap object counts separately with a profiler.


## Resources

State fields and awaiter; possible continuation/Task allocations; no automatically created OS thread.

## Pitfalls and constraints

Do not equate await with Task.Run: awaiting a completed Task need not suspend at all.

## Example

```csharp
async Task Example() { Console.Write("A"); await Task.CompletedTask; Console.Write("B"); }
```

## Runnable experiments

- [02-state-machine-reflection.cs](../../../../labs/dotnet/async-internals/02-state-machine-reflection.cs) — `dotnet run --file labs/dotnet/async-internals/02-state-machine-reflection.cs`

## Review questions

- [Q-012: Does calling an async Task method start a new thread or run synchronously at first?](../../../../questions/dotnet/en/Q-012-async-starts-synchronously.md)
- [Q-025: What is the output? The method awaits an incomplete TaskCompletionSource.](../../../../questions/dotnet/en/Q-025-incomplete-await-output.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

What is an async state machine? Name IAsyncStateMachine and MoveNext.

<details>
<summary>Answer criteria</summary>

Mentions a generated stateful type with MoveNext; async does not create a thread.

</details>

### 2. Explain

Reconstruct the GetAwaiter → IsCompleted → AwaitUnsafeOnCompleted → GetResult → SetResult/SetException pipeline.

<details>
<summary>Answer criteria</summary>

Explains both branches, stored state and failure handling, distinguishing compiler semantics from runtime implementation.

</details>

### 3. Predict

What prints if an async method writes A, awaits Task.CompletedTask, writes B, and the caller writes C after invoking it?

<details>
<summary>Answer criteria</summary>

ABC: already-completed awaiter means no suspension; async method begins synchronously.

</details>

### 4. Diagnose

ILSpy shows MoveNext and awaiter fields. Does that prove every call heap-allocates the state machine?

<details>
<summary>Answer criteria</summary>

No: existence of a generated type does not imply a heap object per call. Allocation depends on completion/runtime; verify via a profiler.

</details>

### 5. Design

A proposal says replace every Task<T> with ValueTask<T> for speed. What evidence would you request?

<details>
<summary>Answer criteria</summary>

Measure sync-completion rate, allocations per operation, latency/throughput, consumers, repeated awaiting and IValueTaskSource semantics first.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Previous](awaiter-completion-path.md) · [Next →](async-socket-pipeline.md) · [Русский](../async-state-machine.md) · [English](async-state-machine.md)
