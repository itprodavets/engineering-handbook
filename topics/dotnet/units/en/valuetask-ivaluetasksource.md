# ValueTask<T> and consumption contracts

[Русский](../valuetask-ivaluetasksource.md) · [English](valuetask-ivaluetasksource.md)

[Home](../../../../README.en.md) · [Module](../../en/valuetask.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/valuetask-ivaluetasksource)

> Understand why being a struct does not guarantee zero allocations.

## Definition

ValueTask<T> is a value type wrapping an immediate result, Task<T>, or IValueTaskSource<T>. Some sources support only one consumption, so repeated awaits are unsafe without an explicit guarantee.

## Internal mechanics

1. For frequent synchronous completions, an API may return a result without allocating a separate Task<T>.
2. For incomplete operations, a pooled IValueTaskSource may use a version token.
3. Repeated await or untimely AsTask can violate the source's consumption contract.
4. Choose ValueTask after profiling; Task<T> is often easier to compose.

## Resources

Struct footprint and possible underlying allocations; exact savings require a benchmark/profile.

## Pitfalls and constraints

Do not assume ValueTask<T> is always faster than Task<T>; measure the specific path.

## Example

```csharp
ValueTask<int> GetAsync() => ValueTask.FromResult(42);
int result = await GetAsync();
```

## Review questions

- [Q-019: Why isn't it always safe to await ValueTask<T> twice, and does it always save memory?](../../../../questions/dotnet/en/Q-019-valuetask-consumption.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012)

---

[Русский](../valuetask-ivaluetasksource.md) · [English](valuetask-ivaluetasksource.md)
