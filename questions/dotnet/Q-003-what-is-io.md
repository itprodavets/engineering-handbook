# Q-003 — Основы I/O

[Русский](./Q-003-what-is-io.md) · [English](en/Q-003-what-is-io.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-003) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-002-thread-id-after-await.md) · [Следующий →](Q-004-async-postgres-pipeline.md)

## Вопрос

Что означает аббревиатура I/O и какой вид I/O происходит при обращении к PostgreSQL?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

I/O = Input/Output (ввод/вывод), обмен с сетью, диском или устройством. Обращение к PostgreSQL обычно включает сетевой I/O по TCP; асинхронное ожидание ответа не требует блокировать worker.

</details>

---

[Русский](./Q-003-what-is-io.md) · [English](en/Q-003-what-is-io.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-003) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-002-thread-id-after-await.md) · [Следующий →](Q-004-async-postgres-pipeline.md)
