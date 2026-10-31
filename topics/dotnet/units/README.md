# Разделы углублённого обучения

[Русский](README.md) · [English](en/README.md)

Один механизм — одно объяснение. Вопросы закрепляют материал.

## [Жизненный цикл async/await](../async-lifecycle.md)

- [I/O-bound и CPU-bound — точные определения](io-vs-cpu-bound.md) — Различать вычисление, ожидание сети и физические ресурсы.
- [Контракт awaiter и синхронное завершение](awaiter-completion-path.md) — Понять GetAwaiter/IsCompleted/GetResult и почему await может не приостановить метод.
- [Что компилятор генерирует для async/await](async-state-machine.md) — Понимать MoveNext, awaiter и ветвление IsCompleted.
- [От PostgreSQL до epoll/IOCP и continuation](async-socket-pipeline.md) — Проследить реальную цепочку SQL, сокета, ядра ОС и возвращения в C#.
- [Память, state machine и стоимость асинхронности](async-memory-and-allocations.md) — Проверить реальную стоимость async без выдуманных размеров объектов.
- [Production-разбор: p99 latency и ThreadPool starvation](async-production-capstone.md) — Научиться подтверждать причину задержек и проектировать исправление.
- [Асинхронность до async/await: APM, EAP и TAP](async-before-await.md) — Объяснять, почему неблокирующее I/O существовало без async/await, и правильно анализировать callback.

## [ThreadPool и планировщик ОС](../threadpool-scheduling.md)

- [Thread, Task и Task.Run — разные сущности](task-vs-thread.md) — Отделять единицу выполнения ОС от описания завершения операции.
- [Планировщик ОС, ядра CPU и ThreadPool](os-vs-runtime-scheduler.md) — Понимать время CPU, вытеснение и очереди .NET.
- [ThreadPool starvation и блокирующие ожидания](threadpool-starvation.md) — Объяснять, какие workers заняты и почему растёт очередь.

## [Композиция Task и ошибки](../task-composition.md)

- [WhenAll и WhenAny — семантика завершения](task-aggregation.md) — Различать ожидание всех задач и получение первой завершившейся.
- [Вложенные Task и StartNew(Func<Task>)](startnew-nested-tasks.md) — Отличать завершение outer Task от реальной асинхронной работы.

## [Разделяемая память и синхронизация](../shared-memory.md)

- [Race Condition, Data Race и Lost Update](race-condition-vs-data-race.md) — Находить ошибку в инварианте, отличать гонку порядка событий от несинхронизированных обращений к памяти.
- [volatile, Interlocked и атомарный RMW](atomicity-and-memory-visibility.md) — Различать атомарность одного действия, acquire/release и операции с ref.
- [CompareExchange, CAS-loop и инвариант stock ≥ 0](compare-exchange-cas-loop.md) — Понимать, что меняет CAS через ref, что возвращает previous и почему повторная попытка нужна при конкуренции.
- [Monitor lock и SemaphoreSlim](mutual-exclusion-and-semaphores.md) — Различать блокировку потока и асинхронное ожидание разрешения.
- [Почему Parallel.ForEach(async ...) опасен](parallel-foreach-async-void.md) — Объяснять потерю управления продолжениями async void.

## [Continuation и контексты](../execution-context.md)

- [ExecutionContext и AsyncLocal<T>](executioncontext-asynclocal.md) — Понять логический контекст, не привязанный к ОС-потоку.
- [SynchronizationContext и ConfigureAwait(false)](synchronizationcontext-configureawait.md) — Понять захват контекста и отсутствие гарантии переключения потока.
- [TaskCompletionSource и встроенные continuation](taskcontinuations-tcs.md) — Понимать reentrancy и опасность SetResult под lock.

## [Отмена асинхронных операций](../cancellation.md)

- [CancellationToken — кооперативная отмена](cancellation-tokens.md) — Отличать запрос на отмену от принудительной остановки потока.

## [ValueTask<T> и стоимость ожидания](../valuetask.md)

- [ValueTask<T> и правила потребления](valuetask-ivaluetasksource.md) — Понять, почему struct не гарантирует нулевые аллокации.

## [Блокировки и sync-over-async](../sync-over-async.md)

- [Deadlock и starvation при .Result/.Wait()](sync-over-async.md) — Различать заблокированный поток, цикл ожидания и отсутствие прогресса.
