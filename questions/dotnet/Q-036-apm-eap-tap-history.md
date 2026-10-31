# Q-036 — APM/EAP/TAP

[Русский](./Q-036-apm-eap-tap-history.md) · [English](en/Q-036-apm-eap-tap-history.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-036) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-035-parallel-foreach-async-void.md) · [Следующий →](Q-037-apm-vs-taskrun-read.md)

## Вопрос

Как выполняли асинхронный I/O до async/await и в какие годы появились APM, EAP и TAP?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

APM (.NET 1.0) использовал Begin/End, IAsyncResult и callbacks; EAP (.NET 2.0) использовал события; TAP (.NET 4) — Task и continuations. C# 5 (2012) добавил async/await, который компилируется в state machine. Настоящий неблокирующий I/O зависит от реализации библиотеки и ОС.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types)

---

[Русский](./Q-036-apm-eap-tap-history.md) · [English](en/Q-036-apm-eap-tap-history.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-036) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-035-parallel-foreach-async-void.md) · [Следующий →](Q-037-apm-vs-taskrun-read.md)
