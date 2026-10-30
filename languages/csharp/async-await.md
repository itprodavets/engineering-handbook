# async / await — from compiler to OS

[Главная / Home](../../README.md) · [Все вопросы / Questions](../../questions/dotnet/README.md) · [Тема / Topic](README.md) · [Запуск / Run](../../docs/execution.md)

## Определения (RU / EN)

**Task** — объект, представляющий состояние и завершение операции; **not an OS thread**. **Thread** — планируемый ОС поток инструкций со стеком и системными ресурсами. **await** — оператор, который использует awaiter: готовый результат обрабатывается синхронно, а незавершённая операция регистрирует continuation и приостанавливает текущий async-метод.

**EN:** Await does not necessarily allocate or switch threads. Awaiting an already completed operation follows a synchronous path. Awaiting incomplete asynchronous I/O normally yields control without reserving a worker thread for the wait.

## Roslyn / IL / CLR

1. Компилятор понижает `async` в машину состояний, содержащую `MoveNext()`, awaiter и сохранённые локальные данные.
2. Код исполняется синхронно до первого `await` с незавершённым awaitable.
3. При незавершённом await регистрируется continuation; CPU не выделяется на всё ожидание для метода.
4. Продолжение может выполниться на другом ThreadPool worker; `await` сам не создаёт поток.
5. Объекты и аллокации зависят от пути и версии runtime: нельзя утверждать, что каждый async-вызов выделяет один Task на heap.

## Network I/O — PostgreSQL example

```csharp
var orders = await db.Orders.AsNoTracking().ToListAsync(ct);
```

**EF Core → Npgsql → socket → OS networking → PostgreSQL.** При незавершённом чтении сетевых данных OS/kernel mechanism уведомляет .NET о готовности сокета. После получения данных CPU снова нужен для декодирования и материализации результата. На Linux обычно используется механизм готовности сокетов (`epoll`), на Windows — I/O completion infrastructure. Подробнее: [ThreadPool and OS scheduling](../../runtimes/clr/threadpool.md).

## Task.Delay vs Task.Run(Thread.Sleep)

| Observable resource | `Task.Delay(5000)` | `Task.Run(() => Thread.Sleep(5000))` |
|---|---|---|
| 10,000 scheduled tasks | 10,000 Task completions / timer states | 10,000 delegates queued or running |
| Worker blocked while waiting | 0 **dedicated workers** for individual timers | 1 worker for each running `Sleep` |
| New OS threads | Not required per timer | Pool may reuse or add workers based on workload |
| CPU during waiting | No spinning per delay | Sleeping worker does not run instructions, but is unavailable for other work |
| Risk | Memory for timers and burst of continuations | ThreadPool starvation, queueing, slow HTTP responses |

**Не утверждаем** фиксированное число worker threads, bytes allocated или CPU% без измерений.

## Exercises / Проверки

[Q-024: completed await prints ABC](../../questions/dotnet/Q-024-completed-await-output.md) · [Q-025: incomplete await prints ACB](../../questions/dotnet/Q-025-incomplete-await-output.md) · [Q-026: WhenAny exception](../../questions/dotnet/Q-026-whenany-faulted-output.md) · [Q-033: nested Task](../../questions/dotnet/Q-033-startnew-nested-task.md)

## References

- [Microsoft: async in depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)
- [Microsoft: file-based C# apps](https://learn.microsoft.com/en-us/dotnet/core/sdk/file-based-apps)
- [Reference: runtime resources and exceptions](../../docs/internals-reference.md)

[Главная / Home](../../README.md) · [Все вопросы / Questions](../../questions/dotnet/README.md) · [Тема / Topic](README.md) · [Запуск / Run](../../docs/execution.md)
