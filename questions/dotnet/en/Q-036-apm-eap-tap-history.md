# Q-036 — The async/await execution lifecycle

[Русский](../Q-036-apm-eap-tap-history.md) · [English](./Q-036-apm-eap-tap-history.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-036) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-035-parallel-foreach-async-void.md) · [Next →](Q-037-apm-vs-taskrun-read.md)

## Question

How was asynchronous I/O performed before async/await, and when did APM, EAP and TAP appear?

<details>
<summary>Model answer — reveal after your attempt</summary>

APM (.NET 1.0) used Begin/End, IAsyncResult and callbacks; EAP (.NET 2.0) used completion events; TAP (.NET 4) introduced Task and continuations. C# 5 (2012) added async/await compiler-generated state machines. True nonblocking I/O depends on library and OS support.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types)

---

[Русский](../Q-036-apm-eap-tap-history.md) · [English](./Q-036-apm-eap-tap-history.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-036) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-035-parallel-foreach-async-void.md) · [Next →](Q-037-apm-vs-taskrun-read.md)
