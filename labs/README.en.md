# Runnable C# / .NET 10 labs

[Русский](README.md) · [English](README.en.md)

[Home](../README.en.md) · [Interactive practice](https://itprodavets.github.io/engineering-handbook/#/en/practice) · [Execution guide](../docs/execution.en.md)

This folder contains **42 standalone runnable C# examples**. Each lab is linked to a challenge Q-024–Q-075, and each challenge belongs to exactly one canonical lesson. Theory is not duplicated across labs.

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

| Challenge | Source file | Explanation |
|---|---|---|
| Q-024 | [C#](dotnet/Q-024.cs) | [Explanation](../questions/dotnet/en/Q-024-completed-await-output.md) |
| Q-025 | [C#](dotnet/Q-025.cs) | [Explanation](../questions/dotnet/en/Q-025-incomplete-await-output.md) |
| Q-026 | [C#](dotnet/Q-026.cs) | [Explanation](../questions/dotnet/en/Q-026-whenany-faulted-output.md) |
| Q-027 | [C#](dotnet/Q-027.cs) | [Explanation](../questions/dotnet/en/Q-027-whenall-exceptions-count.md) |
| Q-028 | [C#](dotnet/Q-028.cs) | [Explanation](../questions/dotnet/en/Q-028-lost-update-race.md) |
| Q-029 | [C#](dotnet/Q-029.cs) | [Explanation](../questions/dotnet/en/Q-029-lock-new-object.md) |
| Q-030 | [C#](dotnet/Q-030.cs) | [Explanation](../questions/dotnet/en/Q-030-cancellation-after-start.md) |
| Q-031 | [C#](dotnet/Q-031.cs) | [Explanation](../questions/dotnet/en/Q-031-asynclocal-flow.md) |
| Q-032 | [C#](dotnet/Q-032.cs) | [Explanation](../questions/dotnet/en/Q-032-configureawait-thread-id.md) |
| Q-033 | [C#](dotnet/Q-033.cs) | [Explanation](../questions/dotnet/en/Q-033-startnew-nested-task.md) |
| Q-034 | [C#](dotnet/Q-034.cs) | [Explanation](../questions/dotnet/en/Q-034-semaphore-waitasync.md) |
| Q-035 | [C#](dotnet/Q-035.cs) | [Explanation](../questions/dotnet/en/Q-035-parallel-foreach-async-void.md) |

| Q-036 | [C#](dotnet/Q-036.cs) | [Explanation](../questions/dotnet/en/Q-036-apm-eap-tap-history.md) |
| Q-038 | [C#](dotnet/Q-038.cs) | [Explanation](../questions/dotnet/en/Q-038-inline-apm-callback-captured-result.md) |
| Q-040 | [C#](dotnet/Q-040.cs) | [Explanation](../questions/dotnet/en/Q-040-lost-update-two-task-run.md) |
| Q-042 | [C#](dotnet/Q-042.cs) | [Explanation](../questions/dotnet/en/Q-042-interlocked-increment-ref.md) |
| Q-043 | [C#](dotnet/Q-043.cs) | [Explanation](../questions/dotnet/en/Q-043-check-then-act-stock-negative.md) |
| Q-044 | [C#](dotnet/Q-044.cs) | [Explanation](../questions/dotnet/en/Q-044-compareexchange-returns-prior.md) |
| Q-045 | [C#](dotnet/Q-045.cs) | [Explanation](../questions/dotnet/en/Q-045-two-buyers-single-item-cas.md) |
| Q-046 | [C#](dotnet/Q-046.cs) | [Explanation](../questions/dotnet/en/Q-046-two-buyers-stock-three-single-cas.md) |
| Q-047 | [C#](dotnet/Q-047.cs) | [Explanation](../questions/dotnet/en/Q-047-cas-loop-five-buyers.md) |

| Q-048 | [C#](dotnet/Q-048.cs) | [Explanation](../questions/dotnet/en/Q-048-safe-publication-acquire-release.md) |
| Q-049 | [C#](dotnet/Q-049.cs) | [Explanation](../questions/dotnet/en/Q-049-release-before-data-allows-zero.md) |
| Q-052 | [C#](dotnet/Q-052.cs) | [Explanation](../questions/dotnet/en/Q-052-await-producer-publishes-data.md) |
| Q-053 | [C#](dotnet/Q-053.cs) | [Explanation](../questions/dotnet/en/Q-053-whenall-does-not-order-producer-consumer.md) |
| Q-054 | [C#](dotnet/Q-054.cs) | [Explanation](../questions/dotnet/en/Q-054-task-delay-is-not-synchronization.md) |
| Q-055 | [C#](dotnet/Q-055.cs) | [Explanation](../questions/dotnet/en/Q-055-whenany-winner-vs-continuation-time.md) |
| Q-056 | [C#](dotnet/Q-056.cs) | [Explanation](../questions/dotnet/en/Q-056-whenany-faulted-winner-exception.md) |
| Q-057 | [C#](dotnet/Q-057.cs) | [Explanation](../questions/dotnet/en/Q-057-whenall-multiple-exceptions-await-one.md) |
| Q-058 | [C#](dotnet/Q-058.cs) | [Explanation](../questions/dotnet/en/Q-058-whenall-faulted-priority-over-canceled.md) |
| Q-059 | [C#](dotnet/Q-059.cs) | [Explanation](../questions/dotnet/en/Q-059-whenany-does-not-cancel-loser.md) |
| Q-060 | [C#](dotnet/Q-060.cs) | [Explanation](../questions/dotnet/en/Q-060-whenall-waits-not-fail-fast.md) |
| Q-061 | [C#](dotnet/Q-061.cs) | [Explanation](../questions/dotnet/en/Q-061-fromexception-oce-vs-fromcanceled.md) |
| Q-062 | [C#](dotnet/Q-062.cs) | [Explanation](../questions/dotnet/en/Q-062-async-task-oce-builder-canceled.md) |
| Q-063 | [C#](dotnet/Q-063.cs) | [Explanation](../questions/dotnet/en/Q-063-async-task-throws-after-completed-await.md) |

| Q-064 | [C#](dotnet/Q-064.cs) | [Explanation](../questions/dotnet/en/Q-064-monitor-exit-after-await.md) |
| Q-065 | [C#](dotnet/Q-065.cs) | [Explanation](../questions/dotnet/en/Q-065-semaphore-permits-vs-threads.md) |
| Q-066 | [C#](dotnet/Q-066.cs) | [Explanation](../questions/dotnet/en/Q-066-semaphore-nested-async-deadlock.md) |
| Q-067 | [C#](dotnet/Q-067.cs) | [Explanation](../questions/dotnet/en/Q-067-semaphore-canceled-wait-overrelease.md) |
| Q-068 | [C#](dotnet/Q-068.cs) | [Explanation](../questions/dotnet/en/Q-068-static-semaphore-three-pods.md) |
| Q-069 | [C#](dotnet/Q-069.cs) | [Explanation](../questions/dotnet/en/Q-069-network-await-permit-lifetime.md) |
| Q-071 | [C#](dotnet/Q-071.cs) | [Explanation](../questions/dotnet/en/Q-071-payment-timeout-duplicate-charge.md) |

**GitHub Pages editing:** The website offers an editable example and reference-output prediction, not actual C# execution. Run code in Codespaces or Actions. To run a browser-modified snippet, copy it into your Codespaces lab file.
