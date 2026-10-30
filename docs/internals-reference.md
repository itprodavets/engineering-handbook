# Internals: mechanisms and resources / Механика и ресурсы

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](../runtimes/clr/README.md) · [Запуск / Run](execution.md)

Эти 21 понятие импортированы из учебной Google Таблицы. Это **эталонные краткие определения**, а не обещание фиксированных аллокаций, числа потоков или CPU%.

## Roslyn / C# compiler

**RU:** Компилятор C# анализирует исходный код, проверяет семантику и генерирует сборку с IL и метаданными; async/await понижает в машину состояний.

**EN:** The C# compiler checks source code and emits IL and metadata; it lowers async/await into a state machine.

- **Implementation / реализация:** C# compiler, build time
- **Managed resources:** Память и CPU процесса компиляции; не worker-потоки приложения.
- **OS / CPU / I/O:** Создаёт файлы сборок, не выбирает CPU для runtime-потоков.
- **Risks:** Путаница между компиляцией исходников и выполнением процесса.
- **Guarantees / variability:** Для обычной managed-сборки; Native AOT добавляет последующую нативную компиляцию.
- **Evidence / проверка:** ILSpy / SharpLab; https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth

---

## IL / CIL

**RU:** Промежуточный код инструкций .NET, записанный в управляемой сборке вместе с метаданными, а не машинный код процессора.

**EN:** Intermediate .NET instructions stored in a managed assembly with metadata; not native CPU instructions.

- **Implementation / реализация:** Assembly, CLR
- **Managed resources:** Файл и загруженные страницы сборки; не отдельная Task или Thread.
- **OS / CPU / I/O:** Обычно JIT или предварительная компиляция переводит IL в native code.
- **Risks:** Неверный вывод, что IL непосредственно выполняется CPU.
- **Guarantees / variability:** Сценарий обычных managed-сборок; Native AOT иной способ публикации.
- **Evidence / проверка:** ILSpy; https://learn.microsoft.com/en-us/dotnet/standard/managed-code

---

## JIT

**RU:** Компилятор времени выполнения, преобразующий IL метода в машинные инструкции; возможна поэтапная оптимизация и использование ReadyToRun.

**EN:** Runtime compiler translating IL to native machine code; tiered optimization and ReadyToRun may apply.

- **Implementation / реализация:** CLR / JIT
- **Managed resources:** CPU для компиляции и память для созданного машинного кода.
- **OS / CPU / I/O:** Итоговый машинный код выполняется на CPU как часть потоков ОС.
- **Risks:** Стоимость прогрева, влияние inlining/PGO, нерепрезентативность холодного бенчмарка.
- **Guarantees / variability:** Не каждый вызов JIT-компилируется заново; ReadyToRun и Native AOT меняют путь.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/core/runtime-config/compilation

---

## CLR / CoreCLR

**RU:** Среда выполнения .NET: загрузка, система типов, GC, исключения, JIT, ThreadPool и взаимодействие с ОС.

**EN:** The .NET runtime providing type loading, GC, exceptions, JIT, ThreadPool and OS integration.

- **Implementation / реализация:** Runtime process
- **Managed resources:** Managed heap, runtime bookkeeping, JIT code, native metadata.
- **OS / CPU / I/O:** Использует системные потоки, виртуальную память и API ОС.
- **Risks:** GC pressure, паузы, scheduler contention, ошибки межпоточного доступа.
- **Guarantees / variability:** Объём ресурсов зависит от процесса, версии и параметров runtime.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime

---

## Thread

**RU:** Поток исполнения с собственным стеком и состоянием регистров, планируемый ОС. Поток может работать, быть готовым или ожидать.

**EN:** OS-schedulable execution context with its own stack and register state; it may run, be runnable or wait.

- **Implementation / реализация:** OS scheduler; .NET Thread API
- **Managed resources:** Управляемый wrapper (если есть), TLS, стек/служебные структуры.
- **OS / CPU / I/O:** Стек виртуальной памяти, kernel bookkeeping; CPU-время только во время исполнения.
- **Risks:** Гонки над общей памятью, блокировки, стоимость переключений контекста.
- **Guarantees / variability:** Размер стека и фактическая физическая память зависят от ОС и конфигурации.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading

---

## ThreadPool

**RU:** Управляемые runtime очереди работы и набор повторно используемых ОС-потоков для её выполнения.

**EN:** Runtime-managed work queues and reusable OS worker threads executing queued work.

- **Implementation / реализация:** CLR / ThreadPool + OS scheduler
- **Managed resources:** Очереди, worker state, синхронизация и bookkeeping.
- **OS / CPU / I/O:** Каждый активный worker является потоком ОС; пул может создавать новые по своим эвристикам.
- **Risks:** Starvation при блокирующих ожиданиях, contention, чрезмерные context switches.
- **Guarantees / variability:** 10 000 задач не означает 10 000 worker-потоков; точное число динамическое.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool

---

## Task

**RU:** Управляемая абстракция, отражающая состояние и завершение операции; Task<T> также предоставляет результат. Не является потоком ОС.

**EN:** Managed representation of an operation's completion and state; Task<T> also yields a result. It is not an OS thread.

- **Implementation / реализация:** System.Threading.Tasks
- **Managed resources:** Объект Task либо оптимизированное/повторно используемое представление; возможно хранение continuation и ошибки.
- **OS / CPU / I/O:** Не требует выделенного worker при ожидании; вычислительная Task исполняется некоторым потоком.
- **Risks:** Необработанные исключения, чрезмерные allocations, ошибочное предположение Task = Thread.
- **Guarantees / variability:** Один Task не равен одному Thread; фактические аллокации зависят от API и пути.
- **Evidence / проверка:** https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/Tasks/Task.cs

---

## Task.Run

**RU:** Планирует делегат к выполнению через TaskScheduler.Default, обычно в ThreadPool, и возвращает Task результата/завершения.

**EN:** Queues a delegate for execution using TaskScheduler.Default, normally on the ThreadPool, and returns a Task.

- **Implementation / реализация:** TPL / ThreadPool
- **Managed resources:** Task, делегат; замыкание и другие объекты — если необходимы.
- **OS / CPU / I/O:** Занимает рабочий поток во время выполняемого делегата; новый поток не гарантирован.
- **Risks:** Блокирующий I/O внутри делегата → занятые workers и starvation.
- **Guarantees / variability:** Очередь/поток зависят от состояния пула; Task.Run — не new Thread.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool

---

## Task.Delay

**RU:** Возвращает Task, завершающийся после заданной задержки; обычная положительная задержка обеспечивается внутренним таймером, без блокировки worker на период ожидания.

**EN:** Returns a Task completed after the delay; an ordinary positive delay uses timer machinery without blocking a worker for the waiting interval.

- **Implementation / реализация:** Task / TimerQueue
- **Managed resources:** Состояние ожидания, связанная задача и таймерная регистрация; число объектов зависит от случая.
- **OS / CPU / I/O:** Нет 1 заблокированного worker на каждый таймер. Обработка истечения таймеров и continuation требует CPU.
- **Risks:** Память/таймеры при большом числе задержек; всплеск callback work при одновременном истечении.
- **Guarantees / variability:** Нулевая/отменённая задержка может идти по оптимизированному пути; точные байты не фиксированы.
- **Evidence / проверка:** https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/Timer.cs

---

## await

**RU:** Оператор ожидания awaitable: если операция завершена — извлекает результат; иначе регистрирует продолжение и приостанавливает async-метод без блокировки его потока.

**EN:** Await operator: reads a completed result or registers a continuation and suspends the async method without blocking its thread.

- **Implementation / реализация:** C# compiler + awaiter/runtime
- **Managed resources:** Состояние продолжения; аллокации зависят от оптимизации/пути.
- **OS / CPU / I/O:** Сам await не создаёт поток; продолжение требует исполнения на каком-либо потоке.
- **Risks:** Потеря понимания ExecutionContext/SyncContext; блокирование через .Result/.Wait().
- **Guarantees / variability:** Ни переход на другой поток, ни асинхронная приостановка не гарантированы.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model

---

## Async state machine

**RU:** Сгенерированный компилятором тип с состоянием, MoveNext, awaiter и сохраняемыми локальными данными для продолжения после await.

**EN:** Compiler-generated stateful type (MoveNext, awaiters, saved locals) enabling resumption after await.

- **Implementation / реализация:** Roslyn / CLR
- **Managed resources:** Поля состояния; при незавершённом ожидании возможны heap allocations, но не всегда.
- **OS / CPU / I/O:** Фрагменты MoveNext выполняются на потоках, выбранных механизмом continuation.
- **Risks:** Аллокации, удержание захваченных ссылок дольше ожидаемого.
- **Guarantees / variability:** Тип/представление и число heap allocations зависят от компиляции и runtime.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth

---

## TaskScheduler

**RU:** Планировщик исполнения Task; стандартный вариант направляет задания ThreadPool. Не назначает CPU-ядра.

**EN:** Schedules Task execution; the default scheduler uses the ThreadPool, but does not select CPU cores.

- **Implementation / реализация:** TPL / CLR
- **Managed resources:** Очереди работы и структура планировщика (по реализации).
- **OS / CPU / I/O:** Потоки ОС и их CPU размещает OS Scheduler.
- **Risks:** Задержки очереди; ограничения/поведение пользовательского scheduler.
- **Guarantees / variability:** Custom TaskScheduler может выполнять работу иначе, чем TaskScheduler.Default.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool

---

## OS Scheduler

**RU:** Часть ядра ОС, выбирающая готовые потоки для исполнения на логических CPU, осуществляющая вытеснение и миграцию.

**EN:** Kernel subsystem assigning runnable threads to logical CPUs, preempting and migrating them.

- **Implementation / реализация:** OS Kernel
- **Managed resources:** Очереди runnable threads и данные контекста в ядре.
- **OS / CPU / I/O:** Потребляет CPU на планирование; переключение изменяет кэш-локальность.
- **Risks:** Oversubscription, contention, latency, частые context switches.
- **Guarantees / variability:** Политика и квант времени зависят от ОС и приоритетов.
- **Evidence / проверка:** Linux perf sched / Windows ETW; https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading

---

## Asynchronous I/O

**RU:** Операция ввода-вывода, завершение которой можно ожидать без удержания выделенного worker-потока; библиотека и ОС сообщают о готовности/завершении.

**EN:** I/O with nonblocking completion notification rather than one dedicated waiting worker per operation.

- **Implementation / реализация:** Socket / OS / .NET runtime
- **Managed resources:** Буферы, объекты операции, continuation.
- **OS / CPU / I/O:** Сокеты и дескрипторы, сетевые буферы, event processing и CPU при чтении/записи.
- **Risks:** Исчерпание соединений/пула, backpressure, таймауты, ошибки отмены.
- **Guarantees / variability:** Точный механизм зависит от ОС, драйвера и провайдера; async API должен реально поддерживать nonblocking I/O.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth

---

## TimerQueue

**RU:** Внутренний механизм .NET для регистрации и выполнения управляемых таймеров; группирует таймеры и разделяет очереди для снижения конкуренции.

**EN:** Internal .NET timer scheduling mechanism; batches managed timers and partitions queues to reduce contention.

- **Implementation / реализация:** CoreCLR / libraries / OS timer
- **Managed resources:** Регистрации таймеров, списки, синхронизация.
- **OS / CPU / I/O:** Небольшое число native timers обслуживает множество managed timers, callback work требует CPU.
- **Risks:** Lock contention при управлении таймерами, bursts при одновременном истечении.
- **Guarantees / variability:** Деталь исходников текущей реализации, не языковая гарантия C#.
- **Evidence / проверка:** https://github.com/dotnet/runtime/blob/main/src/libraries/System.Private.CoreLib/src/System/Threading/Timer.cs

---

## Race condition

**RU:** Ошибка корректности, когда результат зависит от непредусмотренного порядка параллельных событий. Data race — частный случай неупорядоченных конкурирующих обращений к памяти.

**EN:** Correctness defect where outcome depends on unexpected ordering of concurrent events; a data race is a particular unsynchronized memory-access pattern.

- **Implementation / реализация:** Application / memory model
- **Managed resources:** Разделяемое изменяемое состояние.
- **OS / CPU / I/O:** Конкурирующие потоки и операции на общей памяти.
- **Risks:** Потерянные инкременты, неконсистентные данные и нарушенные инварианты.
- **Guarantees / variability:** Нельзя выводить наличие гонки лишь из числа Task; важно разделяемое состояние.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading

---

## Deadlock

**RU:** Взаимная блокировка: набор исполнителей бесконечно ожидает действия друг друга, поэтому никто не может продвинуться.

**EN:** Cycle of waits in which participants cannot make progress because each depends on another.

- **Implementation / реализация:** Application / locks / async waits
- **Managed resources:** Ожидающие задачи и заблокированные потоки (в зависимости от примитивов).
- **OS / CPU / I/O:** CPU может оставаться низким при отсутствии прогресса.
- **Risks:** Нарушение порядка захвата lock, sync-over-async, циклические ожидания.
- **Guarantees / variability:** Deadlock возможен и при асинхронном ожидании, без отдельного заблокированного потока.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives

---

## Lock contention

**RU:** Ситуация, когда несколько потоков конкурируют за одну блокировку и хотя бы один не может захватить её немедленно.

**EN:** Competition for the same lock when one or more contenders cannot acquire it immediately.

- **Implementation / реализация:** Monitor / Lock / OS
- **Managed resources:** Состояние ожидания и синхронизация.
- **OS / CPU / I/O:** Потери времени на ожидание и конкуренцию; возможны context switches.
- **Risks:** Рост latency и снижение throughput при слишком широкой критической секции.
- **Guarantees / variability:** Не всякая синхронизация даёт Monitor contention; важно, какой примитив измеряем.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime

---

## ThreadPool starvation

**RU:** Состояние, когда готовая работа ждёт в очереди из-за отсутствия доступных worker-потоков, часто потому, что они заблокированы.

**EN:** Ready work is delayed because no ThreadPool workers are available, often due to blocking operations.

- **Implementation / реализация:** CLR / ThreadPool
- **Managed resources:** Очередь work items, дополнительные worker stacks при росте пула.
- **OS / CPU / I/O:** CPU может быть низким, хотя задержки велики; растёт queue length / thread count.
- **Risks:** Большие задержки API, таймауты, задержки timer continuations.
- **Guarantees / variability:** ThreadPool адаптирует число worker; конкретный темп роста не гарантирован.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation

---

## Context switch

**RU:** Планировщик прекращает исполнение одного потока на CPU и возобновляет другой с сохранением/восстановлением соответствующего контекста.

**EN:** The scheduler stops one thread and resumes another, saving and restoring execution context.

- **Implementation / реализация:** OS Kernel / CPU
- **Managed resources:** Состояние регистров и планировщика; не managed Task.
- **OS / CPU / I/O:** CPU затраты на смену потока и возможное ухудшение эффективности кэша.
- **Risks:** Частые переключения и миграции ухудшают latency/throughput.
- **Guarantees / variability:** Стоимость зависит от архитектуры, ОС и состояния кэша.
- **Evidence / проверка:** Linux perf sched / Windows ETW

---

## GC

**RU:** Служба runtime, отслеживающая достижимость и освобождающая память управляемых объектов; перемещение объектов и паузы зависят от режима и фазы.

**EN:** Runtime memory manager reclaiming unreachable managed objects; movement and pauses depend on GC mode and phase.

- **Implementation / реализация:** CLR / GC
- **Managed resources:** Managed heap, поколения, корни, служебные структуры.
- **OS / CPU / I/O:** CPU GC-работы, memory commit/working set, в некоторых фазах паузы приложения.
- **Risks:** Allocation pressure, рост latency, удержание объектов ссылками.
- **Guarantees / variability:** GC не освобождает произвольные unmanaged-ресурсы в предсказуемый момент.
- **Evidence / проверка:** https://learn.microsoft.com/en-us/dotnet/core/diagnostics/built-in-metrics-runtime


[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](../runtimes/clr/README.md) · [Запуск / Run](execution.md)
