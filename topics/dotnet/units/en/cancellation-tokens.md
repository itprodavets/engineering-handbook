# CancellationToken is cooperative cancellation

[Русский](../cancellation-tokens.md) · [English](cancellation-tokens.md)

[Home](../../../../README.en.md) · [Module](../../en/cancellation.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/cancellation-tokens)

> Distinguish cancellation requests from forced thread termination.

## Definition

CancellationToken communicates a cancellation request. It cannot forcibly interrupt a running thread or automatically stop started Task.Run code; the operation must observe the token or pass it to a cancellation-aware API.

## Internal mechanics

1. CancellationTokenSource.Cancel marks cancellation requested and invokes registered callbacks.
2. Task.Run(token) may be canceled before execution starts; an already running delegate is not forcibly interrupted.
3. For I/O pass the token to the provider, but cancellation behavior depends on the API.
4. After checking the token, ThrowIfCancellationRequested typically produces OperationCanceledException.

## Resources

CancellationTokenSource registrations/callbacks; canceling does not guarantee immediate worker release.

## Pitfalls and constraints

Do not assume Cancel has finished all operations; await their actual completion.

## Example

```csharp
using var cts = new CancellationTokenSource();
await Task.Delay(1000, cts.Token);
```

## Review questions

- [Q-018: Can CancellationToken forcibly stop a running Task.Run, and is it passed to the delegate automatically?](../../../../questions/dotnet/en/Q-018-cancellationtoken-taskrun.md)
- [Q-030: Will the program print DONE when the token is canceled after the delegate starts?](../../../../questions/dotnet/en/Q-030-cancellation-after-start.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads)

---

[Русский](../cancellation-tokens.md) · [English](cancellation-tokens.md)
