# Q-037 — Async I/O vs blocking

[Русский](./Q-037-apm-vs-taskrun-read.md) · [English](en/Q-037-apm-vs-taskrun-read.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-037) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-036-apm-eap-tap-history.md) · [Следующий →](Q-038-inline-apm-callback-captured-result.md)

## Вопрос

Почему NetworkStream.BeginRead может масштабироваться лучше, чем Task.Run(() => stream.Read(...))?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Настоящее pending socket I/O не удерживает отдельный заблокированный worker на всё ожидание. Task.Run переносит синхронный Read в ThreadPool: worker блокируется при отсутствии данных. Но абстрактный Stream.BeginRead не гарантирует такую реализацию.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread)

---

[Русский](./Q-037-apm-vs-taskrun-read.md) · [English](en/Q-037-apm-vs-taskrun-read.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-037) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-036-apm-eap-tap-history.md) · [Следующий →](Q-038-inline-apm-callback-captured-result.md)
