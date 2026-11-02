# An async network await holds a permit, not necessarily a worker

[Русский](../remote-io-permit-lifetime.md) · [English](remote-io-permit-lifetime.md)

[Home](../../../../README.en.md) · [Module](../../en/microservices-concurrency.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/remote-io-permit-lifetime)

> Separate held semaphore permits, Tasks, sockets and physical workers.

## Definition

After Gate.WaitAsync(), the permit remains held until Release, even throughout a five-second external HTTPS/gRPC await. Genuine pending async I/O need not hold a dedicated blocked worker, but Tasks, permits, network state and queued checkouts remain.

## Internal mechanics

1. Gate.WaitAsync acquires a permit and decreases CurrentCount.
2. ChargeAsync starts I/O; an incomplete await suspends the method.
3. A worker may execute other work while the permit remains held until Release.
4. A subsequent Checkout on the same Pod awaits WaitAsync; another Pod is independent.
5. Concurrency limits should target downstream resources and account for timeouts, backpressure and total replicas.

## Step-by-step explanation

### Await may free the worker but not the permit

A five-second pending external await does not consume five seconds of ASP.NET Core CPU. Gate.CurrentCount nevertheless remains zero until finally releases. Q-069 uses an incomplete TaskCompletionSource to model the wait and show permit lifetime without actual networking.

### Local quotas add up

Three Pods each with SemaphoreSlim(5,5) can generate 15 provider calls in total. A global quota needs coordinated admission or a queue. Internal gRPC and external HTTPS have different latency limits but both experience timeouts and partial failures.

### Isolate limits per downstream

A broad gate around ReserveAsync+ChargeAsync serializes the whole checkout per Pod even if only the external provider needs a limit. A narrow per-downstream limiter with cancellation, timeouts and queue metrics is usually more appropriate.


## Resources

Semaphore permit, pending Task, continuation, connection pools and network buffers. CPU is not continuously used during genuine pending I/O.

## Pitfalls and constraints

Task.Run wrapping synchronous network I/O consumes a worker. Broad critical sections cause queueing and p99 latency despite low CPU; local limits do not enforce a global quota.

## Example

```csharp
await Gate.WaitAsync(ct);
try { await payments.ChargeAsync(orderId, ct); }
finally { Gate.Release(); }
```

## Runnable experiments

- [Q-069.cs](../../../../labs/dotnet/Q-069.cs) — `dotnet run --file labs/dotnet/Q-069.cs`

## Review questions

- [Q-069: During a five-second await ChargeAsync, does CheckoutAsync hold a worker or a permit?](../../../../questions/dotnet/en/Q-069-network-await-permit-lifetime.md)
- [Q-070: How many concurrent payment calls with three Pods each using SemaphoreSlim(5,5)?](../../../../questions/dotnet/en/Q-070-three-pods-provider-quota.md)

## Five levels of understanding

Answer independently; reveal evaluation criteria only after an attempt.

### 1. Recall

What remains occupied during an async ChargeAsync?

<details>
<summary>Answer criteria</summary>

Permit, Task and networking state; worker need not block.

</details>

### 2. Explain

Why might checkout queues grow with low CPU?

<details>
<summary>Answer criteria</summary>

Permits remain held during remote I/O while later requests wait.

</details>

### 3. Predict

How many calls with three Pods each Gate(5,5)?

<details>
<summary>Answer criteria</summary>

Up to 15.

</details>

### 4. Diagnose

How to diagnose high p99 with CurrentCount=0?

<details>
<summary>Answer criteria</summary>

WaitAsync queue, provider latency, connection pools and retries.

</details>

### 5. Design

Where should payment API calls be bounded?

<details>
<summary>Answer criteria</summary>

At the downstream client; coordinate separately for global quotas.

</details>


## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim.waitasync)
- [https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation](https://learn.microsoft.com/en-us/aspnet/core/grpc/deadlines-cancellation)

---

[← Previous](replica-local-semaphore-scope.md) · [Next →](payment-timeout-idempotency-outbox.md) · [Русский](../remote-io-permit-lifetime.md) · [English](remote-io-permit-lifetime.md)
