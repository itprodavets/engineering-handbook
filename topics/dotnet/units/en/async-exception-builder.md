# AsyncTaskMethodBuilder: faulted, canceled and exceptions

[Русский](../async-exception-builder.md) · [English](async-exception-builder.md)

[Home](../../../../README.en.md) · [Module](../../en/cancellation.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-exception-builder)

> Distinguish Task status from exception type and explain SetException and early exceptions in async Task.

## Definition

In .NET, AsyncTaskMethodBuilder.SetException for an async Task treats OperationCanceledException as task cancellation and other exceptions as faults. Task.FromException(new OperationCanceledException()) explicitly constructs a Faulted Task. Task.Yield adds an asynchronous continuation point but does not cause cancellation.

## Internal mechanics

1. Compiler-generated state machine MoveNext wraps the async Task body with exception handling.
2. AsyncTaskMethodBuilder.SetException handles OperationCanceledException via TrySetCanceled using its token and other exceptions via TrySetException.
3. Thus async Task throwing OperationCanceledException becomes Canceled even without explicitly canceling a CancellationTokenSource in this specific builder mechanism.
4. Task.FromException constructs an already Faulted Task regardless of exception type, including OperationCanceledException. Task.FromCanceled requires a canceled token.
5. An exception thrown inside an async Task body, even before a suspending await, normally faults the returned Task instead of throwing from the call; exceptions evaluating arguments before invocation are separate.

## Step-by-step explanation

### Task status and exception type are different

Task.Status is not determined by inspecting exception type alone. Task.FromException(new OperationCanceledException()) creates Faulted even though awaiting it throws OperationCanceledException. Task.FromCanceled(new CancellationToken(true)) creates Canceled; its exception aggregation differs. Inspect Task status and how it was constructed.

```csharp
Task fault=Task.FromException(new OperationCanceledException());
Task canceled=Task.FromCanceled(new CancellationToken(true));
// fault.Status=Faulted; canceled.Status=Canceled
```

### Why async Task with OCE becomes Canceled

In .NET 10, AsyncTaskMethodBuilder<T>.SetException tests `exception is OperationCanceledException oce`. It then invokes `task.TrySetCanceled(oce.CancellationToken, oce)` instead of `TrySetException`. This runtime source explains the builder versus FromException distinction. Task.Yield only schedules continuation.

```csharp
static async Task F() { await Task.Yield(); throw new OperationCanceledException(); }
// await/catch; F() task status == Canceled
```

### An exception after CompletedTask remains in the Task

Awaiting CompletedTask can proceed synchronously, so throw executes before the caller receives the Task. Yet it remains inside compiler-generated state machine handling: the caller receives a Faulted Task, with the exception thrown by await task. Contrast a non-async method throwing before returning any Task.

```csharp
static async Task F() { await Task.CompletedTask; throw new InvalidOperationException(); }
Task t=F(); // does not throw out of F()
// t.Status == Faulted
```

### Correctly classify production cancellation

Catching OperationCanceledException alone does not prove the Task was Canceled. Task.FromException(OCE) is Faulted. For production cancellation, inspect task status, token relationship and API contract. Do not silently turn cancellation into success or assume every OCE was requested by the caller.


## Resources

State machines, Tasks/state boxes, captured exceptions, cancellation tokens and continuations; allocation details depend on execution path.

## Pitfalls and constraints

Do not equate a canceled Task with a Faulted Task containing OperationCanceledException. Task.Run(Action) cancellation-token rules differ from compiler-generated async Task handling. Awaiting CompletedTask may execute without suspension.

## Example

```csharp
static async Task FailAsync() { await Task.CompletedTask; throw new InvalidOperationException("Error"); }
Task task = FailAsync(); // returns Faulted Task
try { await task; } catch (InvalidOperationException) { }
```

## Runnable experiments

- [Q-061.cs](../../../../labs/dotnet/Q-061.cs) — `dotnet run --file labs/dotnet/Q-061.cs`
- [Q-062.cs](../../../../labs/dotnet/Q-062.cs) — `dotnet run --file labs/dotnet/Q-062.cs`
- [Q-063.cs](../../../../labs/dotnet/Q-063.cs) — `dotnet run --file labs/dotnet/Q-063.cs`

## Review questions

- [Q-061: Why is Task.FromException(OCE) Faulted but Task.FromCanceled(token) Canceled?](../../../../questions/dotnet/en/Q-061-fromexception-oce-vs-fromcanceled.md)
- [Q-062: Why is async Task throwing OCE Canceled while Task.FromException(OCE) is Faulted?](../../../../questions/dotnet/en/Q-062-async-task-oce-builder-canceled.md)
- [Q-063: Does calling TestAsync synchronously throw InvalidOperationException if its body awaits CompletedTask then throws?](../../../../questions/dotnet/en/Q-063-async-task-throws-after-completed-await.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Give the statuses for Task.FromException(OCE), Task.FromCanceled(token) and async Task throwing OCE.

<details>
<summary>Answer criteria</summary>

Faulted, Canceled, Canceled (async Task builder).

</details>

### 2. Explain

How does AsyncTaskMethodBuilder.SetException classify cancellation?

<details>
<summary>Answer criteria</summary>

OperationCanceledException → TrySetCanceled(using exception token); otherwise TrySetException. Task.Yield is not the cause.

</details>

### 3. Predict

Does TestAsync throw synchronously to the caller if it awaits CompletedTask then throws InvalidOperationException?

<details>
<summary>Answer criteria</summary>

No: method returns a Faulted Task, and awaiting it throws InvalidOperationException.

</details>

### 4. Diagnose

Why can telemetry show both Faulted and Canceled tasks associated with OperationCanceledException?

<details>
<summary>Answer criteria</summary>

Different task construction/completion paths: FromException vs builder/FromCanceled. Inspect provenance and token.

</details>

### 5. Design

How to design API diagnostics distinguishing failure and cancellation?

<details>
<summary>Answer criteria</summary>

Track Task.Status, cancellation requests and token correlation, exception type and propagation; OCE alone is not proof of requested cancellation.

</details>


## References

- [https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html](https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromcanceled?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromcanceled?view=net-10.0)

---

[← Previous](cancellation-tokens.md) · [Русский](../async-exception-builder.md) · [English](async-exception-builder.md)
