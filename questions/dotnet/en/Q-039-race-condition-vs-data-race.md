# Q-039 — Shared memory and synchronization

[Русский](../Q-039-race-condition-vs-data-race.md) · [English](./Q-039-race-condition-vs-data-race.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-039) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-038-inline-apm-callback-captured-result.md) · [Next →](Q-040-lost-update-two-task-run.md)

## Question

How do race conditions differ from data races, and can a logical race occur without a data race?

<details>
<summary>Model answer — reveal after your attempt</summary>

A race condition is an invariant violation caused by event ordering. A data race is conflicting unsynchronized memory access with at least one write. Two individually atomic check/act operations can still cause a logical race without a data race.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices](https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices)

---

[Русский](../Q-039-race-condition-vs-data-race.md) · [English](./Q-039-race-condition-vs-data-race.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-039) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-038-inline-apm-callback-captured-result.md) · [Next →](Q-040-lost-update-two-task-run.md)
