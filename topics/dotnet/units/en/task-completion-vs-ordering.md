# Tasks: completion synchronization, ordering and timers

[Русский](../task-completion-vs-ordering.md) · [English](task-completion-vs-ordering.md)

[Home](../../../../README.en.md) · [Module](../../en/task-composition.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/task-completion-vs-ordering)

> Distinguish awaiting a specific Task, awaiting several Tasks and waiting for time; avoid confusing completion with execution order.

## Definition

Awaiting producer synchronizes with that task's completion and enables safe observation of its writes afterward. Awaiting WhenAll(producer,consumer) waits for both but does not order work inside them. Awaiting Task.Delay(100) waits for a timer rather than producer; elapsed time is not a synchronization protocol.

## Internal mechanics

1. Task.Run queues work. The producer writes data=42 and completes its Task; awaiting that Task synchronizes a subsequent read.
2. Task.WhenAll does not order producer and consumer execution: the consumer may read zero before the producer writes.
3. Task.Delay returns a timer-backed Task; it is neither a delegate nor one blocked worker per delay.
4. Even if producer seems to finish before the timer, awaiting an unrelated delay does not replace awaiting producer for synchronization.
5. Express the dependency by awaiting producer before reading. For timeouts use Task.WaitAsync or WhenAny with winner inspection and explicit handling of the losing operation.

## Step-by-step explanation

### Awaiting the producer synchronizes completion

Await is about operation completion, not necessarily blocking a thread. After awaiting producer, continuation code can observe writes performed before its successful completion, absent interfering unsynchronized writers. A thread switch is neither required nor relevant to the synchronization guarantee.

```csharp
Task producer=Task.Run(() => data=42);
await producer;
Console.WriteLine(data); // 42
```

### WhenAll waits but does not order work

If producer and consumer are scheduled independently, awaiting WhenAll after the consumer has read data only joins both tasks. It does not impose an order between their internal reads and writes. The consumer can print zero. Await producer inside consumer to establish that dependency.

```csharp
Task consumer=Task.Run(async () => { await producer; Console.WriteLine(data); });
```

### Task.Delay is a timer, not data readiness

`await Task.Delay(100)` waits approximately the specified duration; it does not establish that another Task finished. The producer may start late or take longer. Even producer's wall-clock completion before the timer is not itself the synchronization proof. Use deterministic test gates rather than flaky sleeps to reproduce the race.

```csharp
await Task.Delay(100);
Console.WriteLine(data); // no producer completion dependency
```

### WhenAny winner vs later observation

WhenAny returns the completed winner. A timeout winning does not mean the producer is still incomplete when the caller resumes: it may complete in between. Check task identity, then await producer when it wins; handle the losing operation explicitly on timeout.


## Resources

Task completion state, scheduling/continuations, timers and their memory; an incomplete await generally does not tie up a ThreadPool worker.

## Pitfalls and constraints

Awaiting WhenAll after a read does not retroactively fix a race. Task.Delay does not enforce readiness or ordering. Task completion is distinct from a Task<T> return value.

## Example

```csharp
int data = 0;
Task producer = Task.Run(() => { data = 42; });
Task consumer = Task.Run(async () => { await producer; Console.WriteLine(data); });
await Task.WhenAll(producer, consumer); // 42
```

## Runnable experiments

- [Q-052.cs](../../../../labs/dotnet/Q-052.cs) — `dotnet run --file labs/dotnet/Q-052.cs`
- [Q-053.cs](../../../../labs/dotnet/Q-053.cs) — `dotnet run --file labs/dotnet/Q-053.cs`
- [Q-054.cs](../../../../labs/dotnet/Q-054.cs) — `dotnet run --file labs/dotnet/Q-054.cs`

## Review questions

- [Q-052: Why does reading data after await producer yield 42 without volatile?](../../../../questions/dotnet/en/Q-052-await-producer-publishes-data.md)
- [Q-053: Can Consumer print zero even if the caller later awaits Task.WhenAll(producer,consumer)?](../../../../questions/dotnet/en/Q-053-whenall-does-not-order-producer-consumer.md)
- [Q-054: Why does awaiting Task.Delay(100) not establish producer completion or visibility?](../../../../questions/dotnet/en/Q-054-task-delay-is-not-synchronization.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Distinguish completion synchronization, execution ordering and a timer delay.

<details>
<summary>Answer criteria</summary>

await producer joins producer; WhenAll joins a set without internal ordering; Delay awaits an unrelated timer.

</details>

### 2. Explain

Why is data=42 observable after await producer without volatile?

<details>
<summary>Answer criteria</summary>

Producer wrote before completion; await synchronizes with completion; no concurrent writers.

</details>

### 3. Predict

What might the consumer read if its independent Task runs before a later WhenAll?

<details>
<summary>Answer criteria</summary>

0 or 42; a later WhenAll does not order the tasks internally.

</details>

### 4. Diagnose

Why does code relying on Task.Delay(100) pass tests but fail under load?

<details>
<summary>Answer criteria</summary>

Awaiting a timer instead of the producer, no dependency; scheduler/load changes timing; await actual operation.

</details>

### 5. Design

How to design a dependent consumer and timeout without blocking workers?

<details>
<summary>Answer criteria</summary>

Use await producer for dependency; WaitAsync timeout/cooperative CancellationToken, fault observation and cleanup; check WhenAny winner.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0)

---

[← Previous](task-aggregation.md) · [Next →](startnew-nested-tasks.md) · [Русский](../task-completion-vs-ordering.md) · [English](task-completion-vs-ordering.md)
