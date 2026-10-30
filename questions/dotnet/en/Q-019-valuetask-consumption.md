# Q-019 — ValueTask<T> and allocation trade-offs

[Русский](../Q-019-valuetask-consumption.md) · [English](./Q-019-valuetask-consumption.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-019) · [Canonical lesson](../../../topics/dotnet/en/valuetask.md) · [← Previous](Q-018-cancellationtoken-taskrun.md) · [Next →](Q-020-await-inside-lock.md)

## Question

Why isn't it always safe to await ValueTask<T> twice, and does it always save memory?

<details>
<summary>Model answer — reveal after your attempt</summary>

ValueTask<T> is a struct that can wrap a result, Task, or IValueTaskSource. A source may support only one consumption; allocation savings depend on synchronous completions and usage patterns.

</details>

---

[Русский](../Q-019-valuetask-consumption.md) · [English](./Q-019-valuetask-consumption.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-019) · [Canonical lesson](../../../topics/dotnet/en/valuetask.md) · [← Previous](Q-018-cancellationtoken-taskrun.md) · [Next →](Q-020-await-inside-lock.md)
