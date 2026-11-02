# Микросервисы: синхронизация, сеть, платежи и PostgreSQL

[Русский](microservices-concurrency.md) · [English](en/microservices-concurrency.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/microservices-concurrency)

Локальные разрешения в Pod, сетевые partial failures, идемпотентность и конкурентный SQL.

## Определение

SemaphoreSlim синхронизирует только один процесс: три Pod могут одновременно войти в свои секции. Async network wait может не блокировать worker, но удерживает semaphore permit. Timeout не доказывает, что remote side effect отменён. Outbox и идемпотентность решают разные задачи. Общий остаток защищается атомарно в БД.

## Механизм: от языка и runtime до ОС

1. Каждый Pod имеет отдельную память и static SemaphoreSlim Gate.
2. gRPC/HTTPS await может не удерживать worker, но permit остаётся до Release.
3. Потерянный ответ означает неизвестный результат; повтор без ключа может списать снова.
4. Transactional Outbox фиксирует локальное состояние и событие, но возможна повторная доставка.
5. READ COMMITTED допускает гонку между отдельным SELECT и безусловным UPDATE; условный UPDATE может защитить SKU.

## Ресурсы

- **Память процессов:** Отдельные Gate, Task и ThreadPool у каждого Pod.
- **Сетевой I/O:** Socket, connection pool, latency и deadlines внутренних и внешних вызовов.
- **Общая БД:** MVCC PostgreSQL, row locks и транзакции отвечают за глобальную корректность.

## Ограничения и риски

- static не означает cluster-global lock.
- Task.Run над sync I/O блокирует worker, несмотря на async-обёртку.
- Outbox не обеспечивает exactly-once external payment.
- READ COMMITTED не защищает раздельный check-then-act без корректного SQL.

## Вопросы для проверки

- [Q-070: Сколько одновременно запросов к payment provider при 3 Pod × SemaphoreSlim(5,5)?](../../questions/dotnet/Q-070-three-pods-provider-quota.md)
- [Q-072: Почему Transactional Outbox не заменяет идемпотентность платежного провайдера?](../../questions/dotnet/Q-072-outbox-not-charge-idempotency.md)
- [Q-073: Означает ли gRPC DeadlineExceeded или локальный CancellationToken откат успешно списанного платежа?](../../questions/dotnet/Q-073-remote-timeout-not-rollback.md)
- [Q-074: Могут ли два Pod под READ COMMITTED прочитать available=1 и затем безусловными UPDATE получить -1?](../../questions/dotnet/Q-074-postgres-read-committed-check-act.md)
- [Q-075: Как одним SQL statement защитить последний товар через UPDATE ... RETURNING?](../../questions/dotnet/Q-075-postgres-conditional-update-returning.md)

## Закрепление на коде

- [Q-068: Защитит ли static SemaphoreSlim(1,1) последний SKU от трёх Pod?](../../questions/dotnet/Q-068-static-semaphore-three-pods.md)
- [Q-069: Что удерживает CheckoutAsync во время 5-секундного await ChargeAsync: worker или permit?](../../questions/dotnet/Q-069-network-await-permit-lifetime.md)
- [Q-071: Может ли при потерянном ответе банка повторный ChargeAsync списать деньги дважды?](../../questions/dotnet/Q-071-payment-timeout-duplicate-charge.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
- [https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)
- [https://stripe.com/blog/idempotency](https://stripe.com/blog/idempotency)
- [https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
- [https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[Русский](microservices-concurrency.md) · [English](en/microservices-concurrency.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/microservices-concurrency)
