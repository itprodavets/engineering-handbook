# Q-070 — Distributed concurrency limit

[Русский](./Q-070-three-pods-provider-quota.md) · [English](en/Q-070-three-pods-provider-quota.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-070) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-069-network-await-permit-lifetime.md) · [Следующий →](Q-071-payment-timeout-duplicate-charge.md)

## Вопрос

Сколько одновременно запросов к payment provider при 3 Pod × SemaphoreSlim(5,5)?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

До 15, потому что каждый лимит локальный и не учитывает другие Pod.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)

---

[Русский](./Q-070-three-pods-provider-quota.md) · [English](en/Q-070-three-pods-provider-quota.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-070) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-069-network-await-permit-lifetime.md) · [Следующий →](Q-071-payment-timeout-duplicate-charge.md)
