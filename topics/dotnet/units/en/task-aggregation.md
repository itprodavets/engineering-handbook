# WhenAny/WhenAll: completion, exceptions and cancellation

[Русский](../task-aggregation.md) · [English](task-aggregation.md)

[Home](../../../../README.en.md) · [Module](../../en/task-composition.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/task-aggregation)

> Precisely reason about nested Tasks, Faulted/Canceled precedence, exception aggregation and await.

## Definition

WhenAny returns Task<Task>: its outer Task succeeds upon the first input completion and returns that Task, even if faulted/canceled. WhenAll waits for all inputs and prioritizes Faulted over Canceled; it aggregates all faults, although await propagates one. WhenAny does not cancel losers.

## Internal mechanics

1. WhenAny returns Task<Task> without propagating the winning task's fault until the winner itself is awaited.
2. WhenAny losers continue, and the timeout winner may be followed by producer completion before the caller resumes.
3. WhenAll does not fail fast: it awaits all inputs before selecting Faulted/Canceled/Success.
4. combined.Exception.InnerExceptions holds fault exceptions from the inputs; await propagates one while synchronous Wait throws AggregateException.
5. With Faulted+Canceled input status, the combined Task is Faulted; the canceled input remains Canceled.

## Step-by-step explanation

### WhenAny returns Task<Task>

Task.WhenAny(first,second) returns Task<Task>. Awaiting WhenAny succeeds with the winning Task even if it is Faulted or Canceled; awaiting that winning Task propagates its exception. The losers keep running unless explicitly canceled.

```csharp
Task completed=await Task.WhenAny(producer,timeout);
if (completed==producer) await producer;
else Console.WriteLine("Timeout");
```

### Winner vs state when continuation runs

The winner is the first completed task, but the loser can complete before the caller's continuation runs. 'Timeout won' does not prove the producer remains incomplete at Console.WriteLine. On timeout callers must decide how to cancel, observe faults and clean up the losing operation.

### WhenAll aggregates faults and waits for all

WhenAll is not fail-fast: its returned Task completes after all inputs complete. Two already faulted inputs each storing one exception yield combined.Exception.InnerExceptions.Count == 2. Awaiting combined propagates one exception; inspect combined.Exception for all failures.

```csharp
Task combined=Task.WhenAll(first,second);
try { await combined; }
catch { foreach (var ex in combined.Exception!.InnerExceptions) Console.WriteLine(ex); }
```

### Faulted takes priority over Canceled

WhenAll status precedence: any Faulted → Faulted; otherwise any Canceled → Canceled; otherwise RanToCompletion. A canceled input retains its own status but does not add another fault exception to the aggregate. Awaiting a faulted WhenAll propagates one fault exception.

### Timer race and error handling

Task.Delay supplies a timeout race, not proof of producer completion. After WhenAny inspect the winning Task and await producer when it wins to propagate errors and synchronize access. For APIs supporting tokens, use cooperative cancellation for actual shutdown; elapsed time alone does not stop I/O.


## Resources

Task objects and continuations, tracking all completions, retained exception state and potentially longer lifetime of WhenAny losers.

## Pitfalls and constraints

Do not call WhenAll fail-fast or rely on a specific fault order under concurrent failures. Inspecting Status is not equivalent to handling exceptions. On timeout handle cancellation token, losing work, exceptions and resources.

## Example

```csharp
Task winner = await Task.WhenAny(producer, Task.Delay(1000));
if (winner == producer) await producer; // propagate producer fault
else Console.WriteLine("Timeout");
```

## Runnable experiments

- [Q-055.cs](../../../../labs/dotnet/Q-055.cs) — `dotnet run --file labs/dotnet/Q-055.cs`
- [Q-056.cs](../../../../labs/dotnet/Q-056.cs) — `dotnet run --file labs/dotnet/Q-056.cs`
- [Q-057.cs](../../../../labs/dotnet/Q-057.cs) — `dotnet run --file labs/dotnet/Q-057.cs`
- [Q-058.cs](../../../../labs/dotnet/Q-058.cs) — `dotnet run --file labs/dotnet/Q-058.cs`
- [Q-059.cs](../../../../labs/dotnet/Q-059.cs) — `dotnet run --file labs/dotnet/Q-059.cs`
- [Q-060.cs](../../../../labs/dotnet/Q-060.cs) — `dotnet run --file labs/dotnet/Q-060.cs`

## Review questions

- [Q-014: Does awaiting Task.WhenAny throw the winning task's exception or cancel the other tasks?](../../../../questions/dotnet/en/Q-014-whenany-faulted-task.md)
- [Q-015: How does Task.WhenAll handle several faulted tasks and what does await throw?](../../../../questions/dotnet/en/Q-015-whenall-multiple-exceptions.md)
- [Q-026: What does it print, and does awaiting WhenAny throw the winning task's exception?](../../../../questions/dotnet/en/Q-026-whenany-faulted-output.md)
- [Q-027: How many exceptions are stored by WhenAll when two input Tasks fault?](../../../../questions/dotnet/en/Q-027-whenall-exceptions-count.md)
- [Q-055: If Task.Delay wins WhenAny, must producer still be incomplete when the continuation executes?](../../../../questions/dotnet/en/Q-055-whenany-winner-vs-continuation-time.md)
- [Q-056: Does awaiting WhenAny throw the winner's exception? What does awaiting the returned Task do?](../../../../questions/dotnet/en/Q-056-whenany-faulted-winner-exception.md)
- [Q-057: How many InnerExceptions are stored for two faulted tasks, and what does await combined propagate?](../../../../questions/dotnet/en/Q-057-whenall-multiple-exceptions-await-one.md)
- [Q-058: What status does WhenAll(Faulted,Canceled) have, and what does await propagate?](../../../../questions/dotnet/en/Q-058-whenall-faulted-priority-over-canceled.md)
- [Q-059: Does WhenAny cancel losing tasks and what happens to them?](../../../../questions/dotnet/en/Q-059-whenany-does-not-cancel-loser.md)
- [Q-060: If one input task is already Faulted and another is pending, does WhenAll complete immediately?](../../../../questions/dotnet/en/Q-060-whenall-waits-not-fail-fast.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Describe Task.WhenAny(Task, Task) return type and how a faulted winner behaves.

<details>
<summary>Answer criteria</summary>

Task<Task>; outer RanToCompletion; await winner to propagate its failure.

</details>

### 2. Explain

How does WhenAll choose Faulted/Canceled/Success and what does Exception store?

<details>
<summary>Answer criteria</summary>

Faulted > Canceled > success. Aggregate faults from inputs; all must complete.

</details>

### 3. Predict

Two Task.FromException inputs and awaited WhenAll: count of InnerExceptions and exception propagation?

<details>
<summary>Answer criteria</summary>

Two InnerExceptions; await propagates one of the stored exceptions (not necessarily AggregateException).

</details>

### 4. Diagnose

Why might one input task already be faulted while awaiting WhenAll still has not completed?

<details>
<summary>Answer criteria</summary>

WhenAll waits all, not fail-fast. Investigate pending tasks, cancellation, hangs and resource lifetime.

</details>

### 5. Design

How to implement a timeout with WhenAny, propagate faults and handle the losing task?

<details>
<summary>Answer criteria</summary>

Inspect winner; await producer on producer-win; on timeout cooperatively cancel, observe faults, clean resources. Or WaitAsync while recognizing underlying work may continue.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0)

---

[Next →](task-completion-vs-ordering.md) · [Русский](../task-aggregation.md) · [English](task-aggregation.md)
