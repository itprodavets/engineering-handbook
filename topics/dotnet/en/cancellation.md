# Cancellation of asynchronous work

[Русский](../cancellation.md) · [English](cancellation.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/cancellation)

What CancellationToken actually does and does not do.

## Definition

CancellationToken is a cooperative signal. It is not Thread.Abort: running code must observe cancellation, and I/O APIs must support it.

## Mechanics: language/runtime to OS

1. Task.Run with an already canceled token may avoid starting the delegate.
2. After a delegate starts, a token does not forcibly interrupt CPU instructions.
3. ThrowIfCancellationRequested or token-aware APIs cooperatively stop an operation.
4. Cancellation does not necessarily roll back work already done by an external system.

## Resources

- **CPU:** Computations keep using CPU until the running code checks the token.
- **I/O:** Canceling a network operation depends on the driver and operation phase.

## Constraints and pitfalls

- Canceling an HTTP request does not guarantee PostgreSQL stops an already executing transaction.
- Do not classify OperationCanceledException as an unexpected system fault without examining its cause.

## Review questions

- [Q-018: Can CancellationToken forcibly stop a running Task.Run, and is it passed to the delegate automatically?](../../../questions/dotnet/en/Q-018-cancellationtoken-taskrun.md)

## Reinforcement challenges

- [Q-030: Will the program print DONE when the token is canceled after the delegate starts?](../../../questions/dotnet/en/Q-030-cancellation-after-start.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads)

---

[Русский](../cancellation.md) · [English](cancellation.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/cancellation)
