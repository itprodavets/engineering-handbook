# Microservices: concurrency, networking, payments and PostgreSQL

[Русский](../microservices-concurrency.md) · [English](microservices-concurrency.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/microservices-concurrency)

Process-local Pod permits, network partial failures, idempotency and concurrent SQL.

## Definition

SemaphoreSlim synchronizes only within one process: three Pods can independently enter. Async network waits may release workers while holding permits. Timeout does not prove remote effects were rolled back. Outbox and idempotency solve different problems. Shared inventory needs atomic database protection.

## Mechanics: language/runtime to OS

1. Each Pod has independent memory and its own static SemaphoreSlim Gate.
2. Pending gRPC/HTTPS await need not block a worker, but the permit remains held until Release.
3. A lost reply causes an unknown outcome; a retry without idempotency may charge again.
4. Transactional Outbox atomically persists local state and event, but delivery can repeat.
5. READ COMMITTED permits a race between separate SELECT and unconditional UPDATE; conditional UPDATE can protect a SKU.

## Resources

- **Process memory:** Independent Gate, Task and ThreadPool per Pod.
- **Network I/O:** Sockets, pools, latency and deadlines across internal and external calls.
- **Shared DB:** PostgreSQL MVCC, row locks and transactions enforce global consistency.

## Constraints and pitfalls

- static does not imply cluster-global locking.
- Task.Run around synchronous I/O still blocks a worker.
- Outbox does not ensure exactly-once external payments.
- READ COMMITTED does not fix an unsafe split check-then-act.

## Review questions

- [Q-070: How many concurrent payment calls with three Pods each using SemaphoreSlim(5,5)?](../../../questions/dotnet/en/Q-070-three-pods-provider-quota.md)
- [Q-072: Why does Transactional Outbox not replace payment-provider idempotency?](../../../questions/dotnet/en/Q-072-outbox-not-charge-idempotency.md)
- [Q-073: Does gRPC DeadlineExceeded or local CancellationToken roll back an already committed payment?](../../../questions/dotnet/en/Q-073-remote-timeout-not-rollback.md)
- [Q-074: Can two Pods under READ COMMITTED both read available=1 and then reach -1 via unconditional UPDATE?](../../../questions/dotnet/en/Q-074-postgres-read-committed-check-act.md)
- [Q-075: How can one UPDATE ... RETURNING statement protect the last item?](../../../questions/dotnet/en/Q-075-postgres-conditional-update-returning.md)

## Reinforcement challenges

- [Q-068: Does static SemaphoreSlim(1,1) protect a last-item SKU across three Pods?](../../../questions/dotnet/en/Q-068-static-semaphore-three-pods.md)
- [Q-069: During a five-second await ChargeAsync, does CheckoutAsync hold a worker or a permit?](../../../questions/dotnet/en/Q-069-network-await-permit-lifetime.md)
- [Q-071: Can retrying ChargeAsync after a lost bank reply charge twice?](../../../questions/dotnet/en/Q-071-payment-timeout-duplicate-charge.md)

## Primary references

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
- [https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)
- [https://stripe.com/blog/idempotency](https://stripe.com/blog/idempotency)
- [https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos)
- [https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[Русский](../microservices-concurrency.md) · [English](microservices-concurrency.md)

[Home](../../../README.en.md) · [All topics](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/lesson/microservices-concurrency)
