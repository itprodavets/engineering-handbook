# Q-037 — The async/await execution lifecycle

[Русский](../Q-037-apm-vs-taskrun-read.md) · [English](./Q-037-apm-vs-taskrun-read.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-037) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-036-apm-eap-tap-history.md) · [Next →](Q-038-inline-apm-callback-captured-result.md)

## Question

Why can NetworkStream.BeginRead scale better than Task.Run(() => stream.Read(...))?

<details>
<summary>Model answer — reveal after your attempt</summary>

True pending socket I/O does not pin a worker throughout the wait. Task.Run offloads synchronous Read to a ThreadPool worker which may block. Generic Stream.BeginRead does not by itself promise true async I/O.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread)

---

[Русский](../Q-037-apm-vs-taskrun-read.md) · [English](./Q-037-apm-vs-taskrun-read.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-037) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-036-apm-eap-tap-history.md) · [Next →](Q-038-inline-apm-callback-captured-result.md)
