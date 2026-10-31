# Before async/await: APM, EAP and TAP

[Русский](../async-before-await.md) · [English](async-before-await.md)

[Home](../../../../README.en.md) · [Module](../../en/async-lifecycle.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/async-before-await)

> Explain how asynchronous I/O worked before async/await and reason correctly about callbacks.

## Definition

Asynchronous I/O starts work and handles completion later without necessarily blocking a thread throughout the wait. C# 5 async/await (2012) is compiler-supported syntax over awaitables; it did not invent asynchronous I/O. APM (Begin/End, IAsyncResult), EAP (events), and TAP (Task, introduced with .NET 4) preceded it.

## Internal mechanics

1. In APM, BeginRead initiates a read; EndRead obtains its result or exception; a callback may run inline before BeginRead returns.
2. For genuinely pending asynchronous socket I/O, the OS/runtime tracks readiness; one dedicated blocked worker per waiting socket is unnecessary.
3. Some Stream implementations may implement APM by offloading blocking Read; the name BeginRead alone does not guarantee nonblocking I/O.
4. Task.Run(() => stream.Read(...)) offloads blocking I/O onto a ThreadPool worker, which may remain blocked.
5. TAP and async/await simplify composition: the compiler generates state machines and continuations but does not replace OS I/O facilities.

## Step-by-step explanation

### Three generations of APIs

APM arrived with .NET Framework 1.0: BeginX/EndX and IAsyncResult. EAP appeared with .NET 2.0: XAsync plus XCompleted events. .NET 4 introduced Task, TaskCompletionSource, TAP and Task.Factory.FromAsync adapters. C# 5 added async/await in 2012. Distinguish the API abstraction from language syntax.

### BeginRead, callback and EndRead

BeginRead initiates the read and returns IAsyncResult. On completion AsyncCallback calls EndRead to retrieve bytes or an exception. Calling EndRead before completion can block. NetworkStream documentation explicitly allows inline callback execution on synchronous completion; CompletedSynchronously reports that case.

```csharp
IAsyncResult? result = null;
result = stream.BeginRead(buffer, 0, buffer.Length,
    ar => { Console.WriteLine(result is null); stream.EndRead(ar); }, null);
// Inline completion: True, because assignment has not happened yet.
```

### True async I/O vs offloading blocking work

A pending I/O operation and the thread executing its completion are distinct. Proper asynchronous socket operations can remain pending without a worker blocked for the entire delay. Task.Run(() => stream.Read(...)) still blocks whichever worker executes the synchronous Read.

### Inline callback, closure and races

The right-hand side of result = BeginRead(... callback ...) is evaluated before assignment. An inline callback observes the captured result as null. A callback running on another thread may race with the assignment; without synchronization there is no cross-thread visibility guarantee. Use the callback's ar argument instead of the outer variable. Q-038 deterministically simulates an inline callback; it does not claim every real socket completes inline.

### Bridging APM to Task

Task.Factory.FromAsync adapts a valid Begin/End pair to Task. TaskCompletionSource can represent callback completion; RunContinuationsAsynchronously reduces the risk that continuations execute inline inside SetResult. Adapters bridge completion models; they cannot automatically turn blocking implementations into true nonblocking I/O.


## Resources

Sockets, network buffers, operation state and callbacks; CPU on initiation/completion. Worker thread usage depends on implementation and load.

## Pitfalls and constraints

Calling EndRead before completion can block. Do not assume an outer assignment has completed when an APM callback runs inline; use its ar argument.

## Example

```csharp
stream.BeginRead(buffer, 0, buffer.Length, ar => { int n = stream.EndRead(ar); /* process n bytes */ }, null);
```

## Runnable experiments

- [Q-036.cs](../../../../labs/dotnet/Q-036.cs) — `dotnet run --file labs/dotnet/Q-036.cs`
- [Q-038.cs](../../../../labs/dotnet/Q-038.cs) — `dotnet run --file labs/dotnet/Q-038.cs`

## Review questions

- [Q-036: How was asynchronous I/O performed before async/await, and when did APM, EAP and TAP appear?](../../../../questions/dotnet/en/Q-036-apm-eap-tap-history.md)
- [Q-037: Why can NetworkStream.BeginRead scale better than Task.Run(() => stream.Read(...))?](../../../../questions/dotnet/en/Q-037-apm-vs-taskrun-read.md)
- [Q-038: What does a callback print if invoked inline before assigning result = BeginRead(...)?](../../../../questions/dotnet/en/Q-038-inline-apm-callback-captured-result.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

Name the APM → EAP → TAP → async/await timeline and distinguish API from syntax.

<details>
<summary>Answer criteria</summary>

APM: Begin/End and IAsyncResult in .NET 1.0; EAP: events in .NET 2.0; TAP: Task in .NET 4; async/await: C# 5, 2012. Async I/O predates language syntax.

</details>

### 2. Explain

Explain why 1,000 NetworkStream BeginRead calls can remain pending without 1,000 blocked workers whereas Task.Run(Read) cannot.

<details>
<summary>Answer criteria</summary>

OS-managed pending I/O; callbacks at completion; workers only for processing. Task.Run executes a synchronous Read on a worker that can block.

</details>

### 3. Predict

What does a captured result variable contain if the callback runs inline before BeginRead returns?

<details>
<summary>Answer criteria</summary>

null: the BeginRead result assignment happens afterward. ar identifies the completed operation.

</details>

### 4. Diagnose

An old .NET app starts 1,000 BeginRead operations and consumes hundreds of workers. What do you investigate?

<details>
<summary>Answer criteria</summary>

Inspect concrete Stream implementation, true socket APM vs worker fallback, premature EndRead, sync waits, callbacks, stacks and pool counters.

</details>

### 5. Design

How would you wrap an APM API into TAP while preserving errors and avoiding inline continuation hazards?

<details>
<summary>Answer criteria</summary>

Use Task.Factory.FromAsync or TCS with SetException/SetResult and RunContinuationsAsynchronously, exactly one EndRead; handle lifetime/cancellation separately. Do not promise cancellation if legacy API lacks it.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types)
- [https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread)
- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/)
- [https://devblogs.microsoft.com/dotnet/how-async-await-really-works/](https://devblogs.microsoft.com/dotnet/how-async-await-really-works/)

---

[← Previous](async-production-capstone.md) · [Русский](../async-before-await.md) · [English](async-before-await.md)
