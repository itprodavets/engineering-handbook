# Вопросы и упражнения — C# / .NET

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

## Разделяемая память и синхронизация

[Основная тема](../../topics/dotnet/shared-memory.md)

- [Q-020](Q-020-await-inside-lock.md): Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?
- [Q-021](Q-021-volatile-vs-interlocked.md): Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?
- [Q-028](Q-028-lost-update-race.md): Всегда ли итог counter равен 10 000? Почему? — закрепление
- [Q-029](Q-029-lock-new-object.md): Защищает ли lock(new object()) переменную counter от гонки? — закрепление
- [Q-034](Q-034-semaphore-waitasync.md): Что напечатает second.IsCompleted после повторного WaitAsync без Release? — закрепление
- [Q-035](Q-035-parallel-foreach-async-void.md): Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован? — закрепление

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

## ValueTask<T> и стоимость ожидания

[Основная тема](../../topics/dotnet/valuetask.md)

- [Q-019](Q-019-valuetask-consumption.md): Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память?

## Блокировки и sync-over-async

[Основная тема](../../topics/dotnet/sync-over-async.md)

- [Q-016](Q-016-sync-over-async-deadlocks.md): Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock?
