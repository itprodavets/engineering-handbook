# ExecutionContext and AsyncLocal<T>

[Русский](../executioncontext-asynclocal.md) · [English](executioncontext-asynclocal.md)

[Home](../../../../README.en.md) · [Module](../../en/execution-context.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/executioncontext-asynclocal)

> Understand logical context detached from OS thread identity.

## Definition

ExecutionContext carries logical execution data including AsyncLocal<T> and normally flows through async continuations. ThreadStatic storage is tied to a particular thread.

## Internal mechanics

1. Task.Run normally captures and flows ExecutionContext into the delegate.
2. A continuation may run on another worker while AsyncLocal.Value retains its logical value.
3. ExecutionContext.SuppressFlow disables context propagation for subsequently queued async work and must be used carefully.
4. ConfigureAwait(false) does not suppress ExecutionContext.

## Resources

Context capture/restore overhead and references retained by AsyncLocal values.

## Pitfalls and constraints

Do not confuse AsyncLocal with ThreadLocal/ThreadStatic; switching threads does not imply losing logical context.

## Example

```csharp
var trace = new AsyncLocal<string>();
trace.Value = "X";
await Task.Run(() => Console.Write(trace.Value));
```

## Review questions

- [Q-023: Why does AsyncLocal<T> flow through Task.Run to another thread while ThreadStatic does not?](../../../../questions/dotnet/en/Q-023-asynclocal-executioncontext.md)
- [Q-031: Does Task.Run print X or null?](../../../../questions/dotnet/en/Q-031-asynclocal-flow.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/executioncontext-synchronizationcontext)

---

[Next →](synchronizationcontext-configureawait.md) · [Русский](../executioncontext-asynclocal.md) · [English](executioncontext-asynclocal.md)
