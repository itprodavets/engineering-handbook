# The awaiter contract and synchronous completion

[Русский](../awaiter-completion-path.md) · [English](awaiter-completion-path.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/awaiter-completion-path)

> Understand GetAwaiter/IsCompleted/GetResult and why await may not suspend.

## Definition

`await` is not limited to Task: the compiler uses the awaiter pattern (GetAwaiter, IsCompleted, GetResult and continuation registration). Completed awaitables continue synchronously; pending ones suspend the method.

## Internal mechanics

1. The compiler obtains an awaiter via GetAwaiter().
2. IsCompleted decides whether a result is available immediately.
3. If completed, GetResult runs in the current call stack and propagates an exception if present.
4. Otherwise a continuation is registered and the async method returns control.

## Step-by-step explanation

### A compiler protocol, not just Task

The await syntax uses a suitable awaiter. Besides GetAwaiter and IsCompleted, it needs GetResult and a continuation registration mechanism (INotifyCompletion or ICriticalNotifyCompletion). Awaitables can provide different execution semantics; do not generalize from Task alone.

### Why output is ABC rather than ACB

When PrintAsync is called, its body starts synchronously. Task.CompletedTask already has a completed awaiter, so B prints before PrintAsync returns. The caller prints C later. No new thread is required.

### What changes for a pending Task

With a TaskCompletionSource not yet completed, IsCompleted=false: the method stores its state/awaiter, registers a continuation and returns a Task. The caller proceeds, and SetResult enables resumption. RunContinuationsAsynchronously avoids inline continuations in SetResult.

### How to validate

Run Q-024 and Q-025, then replace CompletedTask with Task.Delay(1): is output ordering guaranteed? No; timer completion and scheduling introduce a race. Use a controlled TaskCompletionSource gate to prove suspension.


## Resources

No waiting worker is required for an already completed await. A pending operation can retain a Task/continuation and references to locals.

## Pitfalls and constraints

Await does not guarantee fairness or a thread switch. Pure CPU-bound loops require a separate scheduling strategy.

## Example

```csharp
async Task PrintAsync() { Console.Write("A"); await Task.CompletedTask; Console.Write("B"); }
var t = PrintAsync(); Console.Write("C"); await t; // ABC
```

## Runnable experiments

- [Q-024.cs](../../../../labs/dotnet/Q-024.cs) — `dotnet run --file labs/dotnet/Q-024.cs`
- [Q-025.cs](../../../../labs/dotnet/Q-025.cs) — `dotnet run --file labs/dotnet/Q-025.cs`

## Review questions

- [Q-013: Does await always suspend, allocate a worker, or switch threads?](../../../../questions/dotnet/en/Q-013-completed-await-and-scheduling.md)
- [Q-024: What is the output and why? The awaited Task is already complete.](../../../../questions/dotnet/en/Q-024-completed-await-output.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

What must an awaitable and awaiter provide for C# await?

<details>
<summary>Answer criteria</summary>

GetAwaiter, IsCompleted, GetResult and continuation registration via OnCompleted/UnsafeOnCompleted; not restricted to Task.

</details>

### 2. Explain

Explain both branches of await depending on IsCompleted.

<details>
<summary>Answer criteria</summary>

True: GetResult and synchronous continuation; false: saved state and continuation.

</details>

### 3. Predict

Does code awaiting Task.CompletedTask print ABC or ACB, and why?

<details>
<summary>Answer criteria</summary>

ABC; the method starts synchronously and the await completes immediately.

</details>

### 4. Diagnose

Why is Task.Delay(1) an unreliable proof of a new continuation thread?

<details>
<summary>Answer criteria</summary>

Short timing and scheduling races; a new thread ID is not guaranteed, await does not create a thread.

</details>

### 5. Design

How would you write a deterministic test of an incomplete await without Thread.Sleep?

<details>
<summary>Answer criteria</summary>

Use TaskCompletionSource with RunContinuationsAsynchronously, assert incomplete, SetResult, then await; controlled order.

</details>


## References

- [https://devblogs.microsoft.com/dotnet/how-async-await-really-works/](https://devblogs.microsoft.com/dotnet/how-async-await-really-works/)

---

[← Previous](io-vs-cpu-bound.md) · [Next →](async-state-machine.md) · [Русский](../awaiter-completion-path.md) · [English](awaiter-completion-path.md)
