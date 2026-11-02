# Вопросы и упражнения — .NET / C#

[Русский](README.md) · [English](README.en.md)

[Главная](../../README.md) · [Интерактивная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/home)

Каждый вопрос относится ровно к одной основной теме; похожие задачи выделены как упражнения для закрепления. Эталонные ответы скрыты до попытки.

## Жизненный цикл async/await

[Основная тема](../../topics/dotnet/async-lifecycle.md)

- [Q-001](Q-001-async-io-scalability.md): Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов?
- [Q-003](Q-003-what-is-io.md): Что означает аббревиатура I/O и какой вид I/O происходит при обращении к PostgreSQL?
- [Q-004](Q-004-async-postgres-pipeline.md): Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата?
- [Q-005](Q-005-cpu-during-io.md): PostgreSQL выполняет SQL 5 секунд. Что делает ядро CPU нашего .NET-сервера при await ToListAsync()?
- [Q-012](Q-012-async-starts-synchronously.md): Запускает ли вызов async Task-метода новый поток или начинает работу синхронно?
- [Q-013](Q-013-completed-await-and-scheduling.md): Всегда ли await приостанавливает метод, выделяет worker или переключает поток?
- [Q-024](Q-024-completed-await-output.md): Какой вывод и почему? async-метод содержит await уже завершённой Task. — закрепление
- [Q-025](Q-025-incomplete-await-output.md): Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource. — закрепление
- [Q-036](Q-036-apm-eap-tap-history.md): Как выполняли асинхронный I/O до async/await и в какие годы появились APM, EAP и TAP? — закрепление
- [Q-037](Q-037-apm-vs-taskrun-read.md): Почему NetworkStream.BeginRead может масштабироваться лучше, чем Task.Run(() => stream.Read(...))?
- [Q-038](Q-038-inline-apm-callback-captured-result.md): Что напечатает callback, если он вызван inline до завершения присваивания result = BeginRead(...)? — закрепление

## ThreadPool и планировщик ОС

[Основная тема](../../topics/dotnet/threadpool-scheduling.md)

- [Q-006](Q-006-hundred-threads-eight-cores.md): Как 8 физических ядер CPU могут выполнять работу 100 готовых к исполнению потоков?
- [Q-007](Q-007-threadpool-vs-os-scheduler.md): Чем отличается .NET ThreadPool от планировщика ОС? Кто решает, на каком ядре выполняется поток?
- [Q-008](Q-008-task-vs-thread.md): Чем Task отличается от Thread? Создаёт ли Task новый поток и что делает await?
- [Q-009](Q-009-task-delay-vs-thread-sleep.md): Что произойдёт с ThreadPool, если одновременно запустить 10 000 Task.Delay(5000) и 10 000 Task.Run(() => Thread.Sleep(5000))?
- [Q-010](Q-010-task-whenall-execution.md): Создаёт ли Task.WhenAll новые потоки и запускает ли сам переданные ему задачи?
- [Q-011](Q-011-threadpool-worker-creation.md): Что означает «ThreadPool может создать дополнительный поток» при вызове Task.Run и почему это не означает 10 000 потоков для 10 000 Task?

## Композиция Task и ошибки

[Основная тема](../../topics/dotnet/task-composition.md)

- [Q-014](Q-014-whenany-faulted-task.md): Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные?
- [Q-015](Q-015-whenall-multiple-exceptions.md): Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await?
- [Q-026](Q-026-whenany-faulted-output.md): Что напечатает код и выбросит ли await Task.WhenAny исключение? — закрепление
- [Q-027](Q-027-whenall-exceptions-count.md): Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task? — закрепление
- [Q-033](Q-033-startnew-nested-task.md): Каков тип задачи и ждёт ли один await outer завершения внутренней асинхронной операции? — закрепление
- [Q-052](Q-052-await-producer-publishes-data.md): Почему после await producer чтение data без volatile даёт 42? — закрепление
- [Q-053](Q-053-whenall-does-not-order-producer-consumer.md): Можно ли вывести 0 внутри Consumer, хотя в конце вызван await Task.WhenAll(producer,consumer)? — закрепление
- [Q-054](Q-054-task-delay-is-not-synchronization.md): Почему await Task.Delay(100) не гарантирует, что другая Task завершилась и опубликовала data=42? — закрепление
- [Q-055](Q-055-whenany-winner-vs-continuation-time.md): Если Task.Delay выиграла WhenAny, обязательно ли Producer остаётся незавершённым к моменту продолжения? — закрепление
- [Q-056](Q-056-whenany-faulted-winner-exception.md): Выбросит ли await Task.WhenAny исключение из Faulted Task-победителя? Что меняет await completed? — закрепление
- [Q-057](Q-057-whenall-multiple-exceptions-await-one.md): Сколько исключений в combined.Exception.InnerExceptions при двух Task.FromException и что выбросит await combined? — закрепление
- [Q-058](Q-058-whenall-faulted-priority-over-canceled.md): Какой статус имеет WhenAll(Faulted,Canceled) и какое исключение распространяет await? — закрепление
- [Q-059](Q-059-whenany-does-not-cancel-loser.md): Отменяет ли Task.WhenAny проигравшие Task и как они завершаются? — закрепление
- [Q-060](Q-060-whenall-waits-not-fail-fast.md): Если одна входящая Task уже Faulted, а другая ещё pending, завершится ли немедленно Task.WhenAll? — закрепление

## Разделяемая память и синхронизация

[Основная тема](../../topics/dotnet/shared-memory.md)

- [Q-020](Q-020-await-inside-lock.md): Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?
- [Q-021](Q-021-volatile-vs-interlocked.md): Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?
- [Q-028](Q-028-lost-update-race.md): Всегда ли итог counter равен 10 000? Почему? — закрепление
- [Q-029](Q-029-lock-new-object.md): Защищает ли lock(new object()) переменную counter от гонки? — закрепление
- [Q-034](Q-034-semaphore-waitasync.md): Что напечатает second.IsCompleted после повторного WaitAsync без Release? — закрепление
- [Q-035](Q-035-parallel-foreach-async-void.md): Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован? — закрепление
- [Q-039](Q-039-race-condition-vs-data-race.md): Чем отличается Race Condition от Data Race и может ли логическая гонка возникнуть без data race?
- [Q-040](Q-040-lost-update-two-task-run.md): Какие значения возможны после двух Task.Run(() => state.Value++) и await Task.WhenAll, если Value=0? — закрепление
- [Q-041](Q-041-volatile-does-not-make-plus-plus-atomic.md): Почему volatile int Value не делает Value++ атомарным и что реально гарантирует volatile в C#?
- [Q-042](Q-042-interlocked-increment-ref.md): Что гарантирует Interlocked.Increment(ref int) и почему ref не связан со ссылочной природой Counter? — закрепление
- [Q-043](Q-043-check-then-act-stock-negative.md): Может ли stock стать -1 при Volatile.Read(stock)>0 и последующем Interlocked.Decrement, если stock=1? — закрепление
- [Q-044](Q-044-compareexchange-returns-prior.md): При stock=1 что вернёт CompareExchange(ref stock,0,1) и чему станет равен stock? — закрепление
- [Q-045](Q-045-two-buyers-single-item-cas.md): Могут ли оба потока успешно выполнить CompareExchange(ref stock,0,1) при stock=1? — закрепление
- [Q-046](Q-046-two-buyers-stock-three-single-cas.md): Если stock=3, два потока выполняют CompareExchange(ref stock,2,3). Сколько покупок успешны и что возвращают оба CAS? — закрепление
- [Q-047](Q-047-cas-loop-five-buyers.md): Как CAS-loop ведёт себя при stock=3 и двух покупателях, а затем stock=1 и пяти покупателях? — закрепление
- [Q-048](Q-048-safe-publication-acquire-release.md): Почему data=42 перед Volatile.Write(ready,1) и Volatile.Read(ready) позволяет вывести 42? — закрепление
- [Q-049](Q-049-release-before-data-allows-zero.md): Может ли Consumer увидеть data=0, если Producer сначала Volatile.Write(ready,1), потом data=42? — закрепление
- [Q-050](Q-050-nonvolatile-loop-jit-hoisting.md): Гарантированно ли завершится while(ready==0) без volatile после записи другого потока?
- [Q-051](Q-051-thread-yield-is-not-memory-fence.md): Почему Thread.Yield() в цикле с обычным чтением ready не заменяет Volatile.Read?
- [Q-064](Q-064-monitor-exit-after-await.md): Почему Monitor.Exit после await на другом потоке выбросит исключение? — закрепление
- [Q-065](Q-065-semaphore-permits-vs-threads.md): Что означает SemaphoreSlim(2,2) при двух Task.Delay и ожидании ещё двух задач? — закрепление
- [Q-066](Q-066-semaphore-nested-async-deadlock.md): Что будет, если Outer держит SemaphoreSlim(1,1) и await Inner, который тоже ждёт его? — закрепление
- [Q-067](Q-067-semaphore-canceled-wait-overrelease.md): Почему finally Release после отменённого WaitAsync может повредить счётчик? — закрепление

## Continuation и контексты

[Основная тема](../../topics/dotnet/execution-context.md)

- [Q-002](Q-002-thread-id-after-await.md): Всегда ли совпадают Environment.CurrentManagedThreadId до и после await ToListAsync()? Если они разные, создал ли await новый поток?
- [Q-017](Q-017-configureawait-and-context.md): Что именно меняет ConfigureAwait(false)? Подавляет ли он ExecutionContext?
- [Q-022](Q-022-taskcompletionsource-continuations.md): Почему SetResult под lock может вызвать неожиданный код и как помогает RunContinuationsAsynchronously?
- [Q-023](Q-023-asynclocal-executioncontext.md): Почему AsyncLocal<T> сохраняет значение при Task.Run на другом потоке, а ThreadStatic — нет?
- [Q-031](Q-031-asynclocal-flow.md): Что напечатает Task.Run — X или null? — закрепление
- [Q-032](Q-032-configureawait-thread-id.md): Изменится ли managed thread id на await CompletedTask.ConfigureAwait(false)? — закрепление

## Отмена асинхронных операций

[Основная тема](../../topics/dotnet/cancellation.md)

- [Q-018](Q-018-cancellationtoken-taskrun.md): Прерывает ли CancellationToken выполняющуюся Task.Run и автоматически ли попадает в делегат?
- [Q-030](Q-030-cancellation-after-start.md): Выведет ли программа DONE, если отменить token после запуска делегата? — закрепление
- [Q-061](Q-061-fromexception-oce-vs-fromcanceled.md): Почему Task.FromException(new OperationCanceledException()) имеет Faulted, а Task.FromCanceled(token) имеет Canceled? — закрепление
- [Q-062](Q-062-async-task-oce-builder-canceled.md): Почему async Task с throw OperationCanceledException получает Canceled, а Task.FromException(OCE) — Faulted? — закрепление
- [Q-063](Q-063-async-task-throws-after-completed-await.md): Выбрасывает ли TestAsync() синхронно InvalidOperationException, если внутри await Task.CompletedTask затем throw? — закрепление

## ValueTask<T> и стоимость ожидания

[Основная тема](../../topics/dotnet/valuetask.md)

- [Q-019](Q-019-valuetask-consumption.md): Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память?

## Блокировки и sync-over-async

[Основная тема](../../topics/dotnet/sync-over-async.md)

- [Q-016](Q-016-sync-over-async-deadlocks.md): Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock?

## Микросервисы: синхронизация, сеть, платежи и PostgreSQL

[Основная тема](../../topics/dotnet/microservices-concurrency.md)

- [Q-068](Q-068-static-semaphore-three-pods.md): Защитит ли static SemaphoreSlim(1,1) последний SKU от трёх Pod? — закрепление
- [Q-069](Q-069-network-await-permit-lifetime.md): Что удерживает CheckoutAsync во время 5-секундного await ChargeAsync: worker или permit? — закрепление
- [Q-070](Q-070-three-pods-provider-quota.md): Сколько одновременно запросов к payment provider при 3 Pod × SemaphoreSlim(5,5)?
- [Q-071](Q-071-payment-timeout-duplicate-charge.md): Может ли при потерянном ответе банка повторный ChargeAsync списать деньги дважды? — закрепление
- [Q-072](Q-072-outbox-not-charge-idempotency.md): Почему Transactional Outbox не заменяет идемпотентность платежного провайдера?
- [Q-073](Q-073-remote-timeout-not-rollback.md): Означает ли gRPC DeadlineExceeded или локальный CancellationToken откат успешно списанного платежа?
- [Q-074](Q-074-postgres-read-committed-check-act.md): Могут ли два Pod под READ COMMITTED прочитать available=1 и затем безусловными UPDATE получить -1?
- [Q-075](Q-075-postgres-conditional-update-returning.md): Как одним SQL statement защитить последний товар через UPDATE ... RETURNING?
