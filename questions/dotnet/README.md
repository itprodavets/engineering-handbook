# C# / .NET — Interview Questions (RU / EN)

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/README.md) · [Запуск / Run](../../docs/execution.md)

Все вопросы имеют постоянный ID. Короткие ответы скрыты внутри `<details>`, чтобы можно было сначала подумать самостоятельно. Code puzzles Q-024–Q-035 имеют запускаемые файлы.

| ID | Question / Вопрос | Type |
|---|---|---|
| [Q-001](Q-001-async-io-scalability.md) | Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов? | Theory |
| [Q-002](Q-002-thread-id-after-await.md) | Всегда ли совпадают Environment.CurrentManagedThreadId до и после await ToListAsync()? Если они разные, создал ли await | Theory |
| [Q-003](Q-003-what-is-io.md) | Что означает аббревиатура I/O и какой вид I/O происходит при обращении к PostgreSQL? | Theory |
| [Q-004](Q-004-async-postgres-pipeline.md) | Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата? | Theory |
| [Q-005](Q-005-cpu-during-io.md) | PostgreSQL выполняет SQL 5 секунд. Что делает ядро CPU нашего .NET-сервера при await ToListAsync()? | Theory |
| [Q-006](Q-006-hundred-threads-eight-cores.md) | Как 8 физических ядер CPU могут выполнять работу 100 готовых к исполнению потоков? | Theory |
| [Q-007](Q-007-threadpool-vs-os-scheduler.md) | Чем отличается .NET ThreadPool от планировщика ОС? Кто решает, на каком ядре выполняется поток? | Theory |
| [Q-008](Q-008-task-vs-thread.md) | Чем Task отличается от Thread? Создаёт ли Task новый поток и что делает await? | Theory |
| [Q-009](Q-009-task-delay-vs-thread-sleep.md) | Что произойдёт с ThreadPool, если одновременно запустить 10 000 Task.Delay(5000) и 10 000 Task.Run(() => Thread.Sleep(50 | Theory |
| [Q-010](Q-010-task-whenall-execution.md) | Создаёт ли Task.WhenAll новые потоки и запускает ли сам переданные ему задачи? | Theory |
| [Q-011](Q-011-threadpool-worker-creation.md) | Что означает «ThreadPool может создать дополнительный поток» при вызове Task.Run и почему это не означает 10 000 потоков | Theory |
| [Q-012](Q-012-async-starts-synchronously.md) | Запускает ли вызов async Task-метода новый поток или начинает работу синхронно? | Theory |
| [Q-013](Q-013-completed-await-and-scheduling.md) | Всегда ли await приостанавливает метод, выделяет worker или переключает поток? | Theory |
| [Q-014](Q-014-whenany-faulted-task.md) | Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные? | Theory |
| [Q-015](Q-015-whenall-multiple-exceptions.md) | Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await? | Theory |
| [Q-016](Q-016-sync-over-async-deadlocks.md) | Почему .Result и .Wait() опасны в ASP.NET Core? Будет ли обязательно deadlock? | Theory |
| [Q-017](Q-017-configureawait-and-context.md) | Что именно меняет ConfigureAwait(false)? Подавляет ли он ExecutionContext? | Theory |
| [Q-018](Q-018-cancellationtoken-taskrun.md) | Прерывает ли CancellationToken выполняющуюся Task.Run и автоматически ли попадает в делегат? | Theory |
| [Q-019](Q-019-valuetask-consumption.md) | Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память? | Theory |
| [Q-020](Q-020-await-inside-lock.md) | Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()? | Theory |
| [Q-021](Q-021-volatile-vs-interlocked.md) | Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock? | Theory |
| [Q-022](Q-022-taskcompletionsource-continuations.md) | Почему SetResult под lock может вызвать неожиданный код и как помогает RunContinuationsAsynchronously? | Theory |
| [Q-023](Q-023-asynclocal-executioncontext.md) | Почему AsyncLocal<T> сохраняет значение при Task.Run на другом потоке, а ThreadStatic — нет? | Theory |
| [Q-024](Q-024-completed-await-output.md) | Какой вывод и почему? async-метод содержит await уже завершённой Task. | C# code puzzle |
| [Q-025](Q-025-incomplete-await-output.md) | Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource. | C# code puzzle |
| [Q-026](Q-026-whenany-faulted-output.md) | Что напечатает код и выбросит ли await Task.WhenAny исключение? | C# code puzzle |
| [Q-027](Q-027-whenall-exceptions-count.md) | Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task? | C# code puzzle |
| [Q-028](Q-028-lost-update-race.md) | Всегда ли итог counter равен 10 000? Почему? | C# code puzzle |
| [Q-029](Q-029-lock-new-object.md) | Защищает ли lock(new object()) переменную counter от гонки? | C# code puzzle |
| [Q-030](Q-030-cancellation-after-start.md) | Выведет ли программа DONE, если отменить token после запуска делегата? | C# code puzzle |
| [Q-031](Q-031-asynclocal-flow.md) | Что напечатает Task.Run — X или null? | C# code puzzle |
| [Q-032](Q-032-configureawait-thread-id.md) | Изменится ли managed thread id на await CompletedTask.ConfigureAwait(false)? | C# code puzzle |
| [Q-033](Q-033-startnew-nested-task.md) | Каков тип задачи и ждёт ли один await outer завершения внутренней асинхронной операции? | C# code puzzle |
| [Q-034](Q-034-semaphore-waitasync.md) | Что напечатает second.IsCompleted после повторного WaitAsync без Release? | C# code puzzle |
| [Q-035](Q-035-parallel-foreach-async-void.md) | Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован? | C# code puzzle |

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../languages/csharp/README.md) · [Запуск / Run](../../docs/execution.md)
