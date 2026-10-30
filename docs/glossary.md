# Glossary / Глоссарий RU + EN

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](internals-reference.md) · [Запуск / Run](execution.md)

| Term | Перевод (RU) | Definition (EN) | Механизм (RU) | Example |
|---|---|---|---|---|
| I/O | Ввод/вывод | Data exchange with a network, storage or device. | Обмен данными с сетью, диском или устройством. | await socket.ReceiveAsync(...) |
| CPU Core | Ядро CPU | Hardware resource executing machine instructions. | Аппаратный ресурс, выполняющий машинные инструкции. | CPU-bound code |
| OS Kernel | Ядро ОС | Privileged software managing threads, memory and I/O. | Часть ОС, управляющая потоками, памятью и вводом/выводом. | Linux kernel |
| Thread | Поток | An OS-schedulable sequence of execution. | Планируемый ОС поток исполнения инструкций. | Thread.CurrentThread |
| ThreadPool | Пул потоков | A runtime-managed pool of workers for queued work. | Управляемый .NET пул рабочих потоков. | Task.Run(...) |
| Task | Задача | An object representing the eventual completion of an operation. | Объект завершения операции или её результата, а не поток. | Task<List<Order>> |
| await | Ожидание async | Suspends an async method if the awaited operation is incomplete. | Приостанавливает async-метод без обязательной блокировки потока. | await db.Orders.ToListAsync() |
| Continuation | Продолжение | Work that resumes after an awaited operation completes. | Код, продолжающий выполнение после завершения ожидания. | code after await |
| State Machine | Машина состояний | Compiler-generated mechanism retaining async execution state. | Сгенерированное компилятором сохранение состояния async-метода. | compiler async rewrite |
| OS Scheduler | Планировщик ОС | Selects which runnable threads execute on logical CPUs. | Выбирает, какие готовые потоки исполняются на CPU. | preemptive scheduling |
| Time Slice | Квант времени | Scheduling interval after which a thread may be preempted. | Интервал процессорного времени, после которого возможно вытеснение. | time sharing |
| Context Switch | Переключение контекста | Switching execution between threads while retaining their states. | Смена потока на CPU с сохранением состояния. | preemption |
| Concurrency | Конкурентность | Several tasks make progress over overlapping time periods. | Продвижение нескольких задач за пересекающиеся интервалы времени. | 100 runnable threads |
| Parallelism | Параллелизм | Computations actually execute at the same instant. | Реальное одновременное исполнение инструкций. | 8 logical CPUs |
| I/O-bound | Ограничено I/O | Performance primarily limited by I/O latency or throughput. | Производительность прежде всего ограничена I/O. | PostgreSQL network request |
| CPU-bound | Ограничено CPU | Performance primarily limited by computation. | Производительность прежде всего ограничена вычислениями. | large hash computation |
| Socket | Сокет | An operating-system abstraction for network communication. | Интерфейс ОС для сетевого обмена. | TCP connection to PostgreSQL |
| epoll | epoll (Linux) | Linux API to monitor file-descriptor readiness. | Механизм Linux для отслеживания готовности сокетов. | network event loop |
| IOCP | Порты завершения I/O | Windows mechanism for efficient asynchronous I/O completion. | Механизм Windows для обработки завершений I/O. | Windows socket I/O |
| SMT | Многопоточность ядра | Hardware feature exposing multiple logical CPUs per physical core. | Аппаратная поддержка нескольких логических CPU на ядро. | Hyper-Threading |
| Task<T> | Задача с результатом | Represents a future outcome that yields a value of type T. | Представляет операцию, которая завершится значением T или ошибкой. | Task<int> result = ... |
| Task.Run | Запуск работы в ThreadPool | Queues a delegate for execution, normally on a ThreadPool worker. | Ставит делегат в очередь для выполнения потоком ThreadPool. | await Task.Run(Compute) |
| TaskScheduler | Планировщик Task | Chooses how Task work is queued and executed; not which CPU core is used. | Определяет постановку и запуск задач Task, но не назначает ядра CPU. | TaskScheduler.Default |
| Preemption | Вытеснение потока | The OS scheduler interrupts a running thread so another can execute. | Планировщик ОС приостанавливает выполняющийся поток ради другого. | CPU time slice |
| Task.Delay | Асинхронная задержка | Returns a Task completed after a timer delay without occupying a worker for the wait. | Возвращает задачу, завершающуюся по таймеру; рабочий поток во время ожидания не блокируется. | await Task.Delay(5000) |
| Thread.Sleep | Блокирующая задержка потока | Blocks the current thread for a specified interval. | Блокирует текущий поток на указанный интервал. | Thread.Sleep(5000) |
| Timer | Таймер | A runtime or OS mechanism that signals when a specified interval elapses. | Позволяет ожидать истечения времени без отдельного заблокированного потока для каждого таймера. | Task.Delay(5000) |
| Task.WhenAll | Ожидание всех задач | Returns a Task that completes after all provided tasks complete. | Объединяет завершение задач; не выделяет отдельные потоки и не запускает уже созданные задачи. | await Task.WhenAll(tasks) |
| ThreadPool starvation | Нехватка рабочих потоков | A shortage of available workers delays queued work, often because workers are blocked. | Недостаток свободных worker-потоков задерживает выполнение задач из очереди. | Task.Run(() => Thread.Sleep(5000)) |
| Worker Thread | Рабочий поток | An OS thread used by the runtime to execute queued work. | Поток ОС, который ThreadPool использует для выполнения задач из очереди. | ThreadPool worker executing Task.Run |
| Thread Creation | Создание потока ОС | Starting an additional OS thread, distinct from allocating a Task object. | Создание дополнительного потока ОС; не то же, что создание объекта Task. | new Thread(...).Start(); ThreadPool scales workers |

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](internals-reference.md) · [Запуск / Run](execution.md)
