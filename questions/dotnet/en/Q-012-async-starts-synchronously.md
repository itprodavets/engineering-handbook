# Q-012 — The async/await execution lifecycle

[Русский](../Q-012-async-starts-synchronously.md) · [English](./Q-012-async-starts-synchronously.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-012) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-011-threadpool-worker-creation.md) · [Next →](Q-013-completed-await-and-scheduling.md)

## Question

Does calling an async Task method start a new thread or run synchronously at first?

<details>
<summary>Model answer — reveal after your attempt</summary>

It executes on the calling thread until the first await of an incomplete awaitable. The compiler generates a state machine; async alone does not queue work to the ThreadPool.

</details>

---

[Русский](../Q-012-async-starts-synchronously.md) · [English](./Q-012-async-starts-synchronously.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-012) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-011-threadpool-worker-creation.md) · [Next →](Q-013-completed-await-and-scheduling.md)
