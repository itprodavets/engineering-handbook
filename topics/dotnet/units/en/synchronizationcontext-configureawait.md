# SynchronizationContext and ConfigureAwait(false)

[Русский](../synchronizationcontext-configureawait.md) · [English](synchronizationcontext-configureawait.md)

[Home](../../../../README.en.md) · [Module](../../en/execution-context.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/synchronizationcontext-configureawait)

> Understand context capture and why thread switching is not guaranteed.

## Definition

SynchronizationContext specifies where continuations may be posted. ConfigureAwait(false) for a normal Task await avoids requiring a captured SynchronizationContext/nondefault TaskScheduler and does not start a new thread.

## Internal mechanics

1. In UI applications, the context may require resumption on a particular UI thread.
2. Ordinary ASP.NET Core does not install that SynchronizationContext per HTTP request.
3. If the Task is complete at await time, execution commonly continues synchronously on the same thread.
4. CurrentManagedThreadId may change across an incomplete await, but it is not required to.

## Resources

Continuation/context state and possible scheduling, but zero threads automatically created by await.

## Pitfalls and constraints

ConfigureAwait(false) is not a ‘switch to ThreadPool’ operation and does not suppress AsyncLocal.

## Example

```csharp
int id = Environment.CurrentManagedThreadId;
await Task.CompletedTask.ConfigureAwait(false);
Console.WriteLine(id == Environment.CurrentManagedThreadId);
```

## Review questions

- [Q-002: Must Environment.CurrentManagedThreadId be the same before and after await ToListAsync()? If not, did await create a new thread?](../../../../questions/dotnet/en/Q-002-thread-id-after-await.md)
- [Q-017: What exactly does ConfigureAwait(false) change? Does it suppress ExecutionContext?](../../../../questions/dotnet/en/Q-017-configureawait-and-context.md)
- [Q-032: Does awaiting CompletedTask.ConfigureAwait(false) change the managed thread ID?](../../../../questions/dotnet/en/Q-032-configureawait-thread-id.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)

---

[← Previous](executioncontext-asynclocal.md) · [Next →](taskcontinuations-tcs.md) · [Русский](../synchronizationcontext-configureawait.md) · [English](synchronizationcontext-configureawait.md)
