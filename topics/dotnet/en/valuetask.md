# ValueTask<T> and allocation trade-offs

[Русский](../valuetask.md) · [English](valuetask.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/valuetask)

When it helps—and why it is not always faster.

## Definition

ValueTask<T> is a value type that may represent a synchronous result, a Task<T>, or an IValueTaskSource<T>. It can avoid allocations when operations frequently complete synchronously, but introduces usage constraints.

## Mechanics: C# to OS

1. For an already available result, ValueTask<T> can hold it without a separate Task<T>.
2. For pending work, ValueTask<T> may wrap a Task or a reusable source.
3. IValueTaskSource<T> may permit only one consumption; awaiting twice is not always valid.
4. For many APIs, Task<T> is simpler; compare using real allocation profiles.

## Resources

- **Memory:** ValueTask is a struct, but its wrapped source or Task may still need heap memory.
- **CPU:** A larger struct and additional states may cost CPU; there is no universal speed advantage.

## Constraints and pitfalls

- Do not repeatedly await, call AsTask, or store instances without considering the underlying source contract.

## Review questions

- [Q-019: Why isn't it always safe to await ValueTask<T> twice, and does it always save memory?](../../../questions/dotnet/en/Q-019-valuetask-consumption.md)

## Reinforcement challenges

—

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012)

---

[Русский](../valuetask.md) · [English](valuetask.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/valuetask)
