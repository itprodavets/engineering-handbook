# Monitor, SemaphoreSlim и асинхронный deadlock

[Русский](mutual-exclusion-and-semaphores.md) · [English](en/mutual-exclusion-and-semaphores.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/mutual-exclusion-and-semaphores)

> Различать привязку Monitor к потоку, разрешения SemaphoreSlim, async deadlock и ошибки отмены.

## Определение

Monitor привязан к потоку: Exit должен выполнить владелец Enter. Вручную написанный Monitor.Enter через await компилируется, но может упасть на Monitor.Exit с другого потока. SemaphoreSlim(2,2) даёт два разрешения, а не два потока; WaitAsync не обязан блокировать worker. Вложенный захват одного SemaphoreSlim(1,1) даёт async deadlock без обязательного блокирования worker.

## Внутренний механизм

1. Monitor.Enter захватывает монитор, который не освобождается автоматически при await.
2. Monitor.Exit на другом worker выбрасывает SynchronizationLockException; await внутри обычного C# lock запрещён.
3. SemaphoreSlim.WaitAsync при отсутствии permit возвращает незавершённую Task; поток может выполнять другую работу.
4. Пока Task.Delay/сетевой I/O ожидается, ранее полученное разрешение остаётся занятым до Release.
5. Outer ждёт Inner, Inner ждёт permit Outer: циклическая асинхронная зависимость — deadlock.
6. После отменённого WaitAsync permit не получен; безусловный Release в finally, охватывающем WaitAsync, увеличит счётчик неправильно.

## Последовательное объяснение

### Monitor.Enter и await

Monitor привязан к потоку, вызвавшему Enter. При реальном async-suspension продолжение может выполниться на другом worker, и Monitor.Exit выбросит SynchronizationLockException. finally выполняется, но не меняет владельца. Компилятор запрещает await внутри обычного lock, однако ручные вызовы Enter/Exit обходят эту защиту.

```csharp
Monitor.Enter(gate);
try { await Task.Delay(100); }
finally { Monitor.Exit(gate); } // unsafe
```

### Два разрешения не равны двум потокам

SemaphoreSlim(2,2) допускает одновременно двух держателей permit. Пока они await Task.Delay(1000), оба разрешения заняты, но отдельные worker-потоки не обязаны ожидать. Последующие WaitAsync при счётчике 0 остаются pending; Wait() в таком положении блокирует поток. FIFO-порядок выдачи разрешений не гарантируется.

### Асинхронный deadlock без блокировки потоков

OuterAsync захватывает единственный permit, печатает Outer entered и вызывает await InnerAsync. InnerAsync ждёт тот же permit, не доходя до Inner entered; Outer не вызовет finally пока Inner не завершится. Это deadlock, хотя ThreadPool worker может быть свободен. В лаборатории ожидающую часть отменяем, чтобы не зависал CI.

### Отмена не даёт право вызвать Release

Если WaitAsync(ct) отменён до получения разрешения, await выбросит OperationCanceledException. try/finally, охватывающий ожидание, всё равно вызовет Release, увеличивая разрешения без захвата. Помещай await WaitAsync ДО try/finally либо явно учитывай успешность захвата.

```csharp
await sem.WaitAsync(ct);
try { await WorkAsync(); }
finally { sem.Release(); }
```


## Потребляемые ресурсы

Monitor thread affinity; SemaphoreSlim permits, wait queues, Task continuations and CPU only when executing. A pending await does not require a dedicated blocked worker.

## Ошибки и ограничения

Не использовать Monitor через await; SemaphoreSlim не реентерабелен, не гарантирует FIFO и не является distributed lock. WaitAsync до try/finally; Release только после успешного приобретения.

## Пример

```csharp
await semaphore.WaitAsync(ct);
try { await WorkAsync(ct); }
finally { semaphore.Release(); }
```

## Запускаемые эксперименты

- [Q-064.cs](../../../labs/dotnet/Q-064.cs) — `dotnet run --file labs/dotnet/Q-064.cs`
- [Q-065.cs](../../../labs/dotnet/Q-065.cs) — `dotnet run --file labs/dotnet/Q-065.cs`
- [Q-066.cs](../../../labs/dotnet/Q-066.cs) — `dotnet run --file labs/dotnet/Q-066.cs`
- [Q-067.cs](../../../labs/dotnet/Q-067.cs) — `dotnet run --file labs/dotnet/Q-067.cs`

## Вопросы для закрепления

- [Q-020: Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?](../../../questions/dotnet/Q-020-await-inside-lock.md)
- [Q-029: Защищает ли lock(new object()) переменную counter от гонки?](../../../questions/dotnet/Q-029-lock-new-object.md)
- [Q-034: Что напечатает second.IsCompleted после повторного WaitAsync без Release?](../../../questions/dotnet/Q-034-semaphore-waitasync.md)
- [Q-064: Почему Monitor.Exit после await на другом потоке выбросит исключение?](../../../questions/dotnet/Q-064-monitor-exit-after-await.md)
- [Q-065: Что означает SemaphoreSlim(2,2) при двух Task.Delay и ожидании ещё двух задач?](../../../questions/dotnet/Q-065-semaphore-permits-vs-threads.md)
- [Q-066: Что будет, если Outer держит SemaphoreSlim(1,1) и await Inner, который тоже ждёт его?](../../../questions/dotnet/Q-066-semaphore-nested-async-deadlock.md)
- [Q-067: Почему finally Release после отменённого WaitAsync может повредить счётчик?](../../../questions/dotnet/Q-067-semaphore-canceled-wait-overrelease.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Как отличаются thread affinity Monitor и permit SemaphoreSlim?

<details>
<summary>Критерии ответа</summary>

Monitor.Exit требует того же потока; SemaphoreSlim Release не проверяет owner, но требует корректного парного вызова.

</details>

### 2. Explain

Почему при await Task.Delay permit занят, а worker может быть свободен?

<details>
<summary>Критерии ответа</summary>

Permit сохраняется до Release; pending Task не блокирует worker.

</details>

### 3. Predict

Что выведет OuterAsync с вложенным InnerAsync на одном SemaphoreSlim(1,1)?

<details>
<summary>Критерии ответа</summary>

Только Outer entered, затем pending deadlock.

</details>

### 4. Diagnose

Почему после отмены WaitAsync CurrentCount стал больше ожидаемого?

<details>
<summary>Критерии ответа</summary>

finally Release выполнен после неуспешного WaitAsync.

</details>

### 5. Design

Как правильно писать CancellationToken + WaitAsync + finally?

<details>
<summary>Критерии ответа</summary>

await WaitAsync(ct) перед try; Release в finally только после успешного приобретения.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor](https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit](https://learn.microsoft.com/en-us/dotnet/api/system.threading.monitor.exit)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim](https://learn.microsoft.com/en-us/dotnet/api/system.threading.semaphoreslim)
- [https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/](https://devblogs.microsoft.com/dotnet/are-deadlocks-still-possible-with-await/)

---

[← Назад](compare-exchange-cas-loop.md) · [Далее →](parallel-foreach-async-void.md) · [Русский](mutual-exclusion-and-semaphores.md) · [English](en/mutual-exclusion-and-semaphores.md)
