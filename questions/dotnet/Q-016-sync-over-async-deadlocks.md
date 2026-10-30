# Q-016 — Sync-over-async / blocking

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-015-whenall-multiple-exceptions.md) · [Следующий →](Q-017-configureawait-and-context.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Sync-over-async

## Вопрос (RU)

Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock?

## Question (EN)

Why are .Result and .Wait() dangerous in ASP.NET Core? Is a deadlock guaranteed?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

.Result и .Wait() блокируют вызывающий поток до завершения Task, увеличивая риск ThreadPool starvation. Deadlock не гарантирован: классический случай связан с однопоточным SynchronizationContext; стандартный ASP.NET Core его не устанавливает.

### EN — concise interview answer

They block the caller and can cause ThreadPool starvation. Deadlock is not inevitable: the classic case involves a single-threaded SynchronizationContext, which standard ASP.NET Core does not install.

</details>

**Terminology / Термины:** Result; Wait; deadlock; ASP.NET Core; starvation

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-015-whenall-multiple-exceptions.md) · [Следующий →](Q-017-configureawait-and-context.md)
