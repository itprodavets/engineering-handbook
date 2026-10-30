# Continuations and execution contexts

[Русский](../execution-context.md) · [English](execution-context.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/execution-context)

SynchronizationContext, TaskScheduler, AsyncLocal and ConfigureAwait.

## Definition

Await may capture a continuation context. ExecutionContext carries logical values such as AsyncLocal, unlike ThreadStatic. ConfigureAwait(false) does not suppress ExecutionContext flow.

## Mechanics: C# to OS

1. AsyncLocal<T> flows through ExecutionContext, which Task.Run normally captures.
2. ConfigureAwait(false) avoids marshaling continuations back to a captured SynchronizationContext or non-default TaskScheduler.
3. TaskCompletionSource may inline continuations; RunContinuationsAsynchronously avoids synchronous inlining.
4. A continuation may run on another worker; physical thread identity is not guaranteed.

## Resources

- **Memory:** ExecutionContext, Task and continuations may retain references; allocations depend on the path.
- **Worker threads:** Task.Run uses the ThreadPool; ConfigureAwait(false) does not create a worker by itself.

## Constraints and pitfalls

- Inlining a continuation while holding a lock can cause reentrancy or lock inversion.
- ThreadStatic and AsyncLocal differ even when one observed run happens to produce the same result.

## Review questions

- [Q-002: Must Environment.CurrentManagedThreadId be the same before and after await ToListAsync()? If not, did await create a new thread?](../../../questions/dotnet/en/Q-002-thread-id-after-await.md)
- [Q-017: What exactly does ConfigureAwait(false) change? Does it suppress ExecutionContext?](../../../questions/dotnet/en/Q-017-configureawait-and-context.md)
- [Q-022: Why can SetResult under a lock run unexpected code, and what does RunContinuationsAsynchronously change?](../../../questions/dotnet/en/Q-022-taskcompletionsource-continuations.md)
- [Q-023: Why does AsyncLocal<T> flow through Task.Run to another thread while ThreadStatic does not?](../../../questions/dotnet/en/Q-023-asynclocal-executioncontext.md)

## Reinforcement challenges

- [Q-031: Does Task.Run print X or null?](../../../questions/dotnet/en/Q-031-asynclocal-flow.md)
- [Q-032: Does awaiting CompletedTask.ConfigureAwait(false) change the managed thread ID?](../../../questions/dotnet/en/Q-032-configureawait-thread-id.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcreationoptions)

---

[Русский](../execution-context.md) · [English](execution-context.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/execution-context)
