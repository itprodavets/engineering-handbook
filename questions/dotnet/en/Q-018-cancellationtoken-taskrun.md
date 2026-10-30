# Q-018 — Cancellation of asynchronous work

[Русский](../Q-018-cancellationtoken-taskrun.md) · [English](./Q-018-cancellationtoken-taskrun.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-018) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-017-configureawait-and-context.md) · [Next →](Q-019-valuetask-consumption.md)

## Question

Can CancellationToken forcibly stop a running Task.Run, and is it passed to the delegate automatically?

<details>
<summary>Model answer — reveal after your attempt</summary>

No. Cancellation is cooperative. Task.Run(token) can prevent execution before a task starts, but does not interrupt running code or automatically pass the token into the delegate.

</details>

---

[Русский](../Q-018-cancellationtoken-taskrun.md) · [English](./Q-018-cancellationtoken-taskrun.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-018) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-017-configureawait-and-context.md) · [Next →](Q-019-valuetask-consumption.md)
