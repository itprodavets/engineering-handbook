# Q-071 — Payment idempotency

[Русский](./Q-071-payment-timeout-duplicate-charge.md) · [English](en/Q-071-payment-timeout-duplicate-charge.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-071) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-070-three-pods-provider-quota.md) · [Следующий →](Q-072-outbox-not-charge-idempotency.md)

## Вопрос

Может ли при потерянном ответе банка повторный ChargeAsync списать деньги дважды?

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Да. Timeout не доказывает rollback; повтор одной логической попытки требует стабильного provider-enforced idempotency key и reconciliation.

</details>

### Документация и исходники

[https://stripe.com/blog/idempotency](https://stripe.com/blog/idempotency)

---

[Русский](./Q-071-payment-timeout-duplicate-charge.md) · [English](en/Q-071-payment-timeout-duplicate-charge.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-071) · [Основная тема](../../topics/dotnet/microservices-concurrency.md) · [← Предыдущий](Q-070-three-pods-provider-quota.md) · [Следующий →](Q-072-outbox-not-charge-idempotency.md)
