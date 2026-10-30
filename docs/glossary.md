# Глоссарий

[Русский](glossary.md) · [English](glossary.en.md)

[Главная](../README.md) · [Интерактивный глоссарий](https://itprodavets.github.io/engineering-handbook/#/ru/glossary)

Термины C#/.NET, ОС и многопоточности. Полное объяснение механизма ищи в одной основной теме, а не в повторяющихся ответах.

## I/O

Обмен данными с сетью, диском или устройством.

Пример: `await socket.ReceiveAsync(...)`

## CPU Core

Аппаратный ресурс, выполняющий машинные инструкции.

Пример: `CPU-bound code`

## OS Kernel

Часть ОС, управляющая потоками, памятью и вводом/выводом.

Пример: `Linux kernel`

## Thread

Планируемый ОС поток исполнения инструкций.

Пример: `Thread.CurrentThread`

## ThreadPool

Управляемый .NET пул рабочих потоков.

Пример: `Task.Run(...)`

## Task

Объект завершения операции или её результата, а не поток.

Пример: `Task<List<Order>>`

## await

Приостанавливает async-метод без обязательной блокировки потока.

Пример: `await db.Orders.ToListAsync()`

## Continuation

Код, продолжающий выполнение после завершения ожидания.

Пример: `code after await`

## State Machine

Сгенерированное компилятором сохранение состояния async-метода.

Пример: `compiler async rewrite`

## OS Scheduler

Выбирает, какие готовые потоки исполняются на CPU.

Пример: `preemptive scheduling`

## Time Slice

Интервал процессорного времени, после которого возможно вытеснение.

Пример: `time sharing`

## Context Switch

Смена потока на CPU с сохранением состояния.

Пример: `preemption`

## Concurrency

Продвижение нескольких задач за пересекающиеся интервалы времени.

Пример: `100 runnable threads`

## Parallelism

Реальное одновременное исполнение инструкций.

Пример: `8 logical CPUs`

## I/O-bound

Производительность прежде всего ограничена I/O.

Пример: `PostgreSQL network request`

## CPU-bound

Производительность прежде всего ограничена вычислениями.

Пример: `large hash computation`

## Socket

Интерфейс ОС для сетевого обмена.

Пример: `TCP connection to PostgreSQL`

## epoll

Механизм Linux для отслеживания готовности сокетов.

Пример: `network event loop`

## IOCP

Механизм Windows для обработки завершений I/O.

Пример: `Windows socket I/O`

## SMT

Аппаратная поддержка нескольких логических CPU на ядро.

Пример: `Hyper-Threading`

## Task<T>

Представляет операцию, которая завершится значением T или ошибкой.

Пример: `Task<int> result = ...`

## Task.Run

Ставит делегат в очередь для выполнения потоком ThreadPool.

Пример: `await Task.Run(Compute)`

## TaskScheduler

Определяет постановку и запуск задач Task, но не назначает ядра CPU.

Пример: `TaskScheduler.Default`

## Preemption

Планировщик ОС приостанавливает выполняющийся поток ради другого.

Пример: `CPU time slice`

## Task.Delay

Возвращает задачу, завершающуюся по таймеру; рабочий поток во время ожидания не блокируется.

Пример: `await Task.Delay(5000)`

## Thread.Sleep

Блокирует текущий поток на указанный интервал.

Пример: `Thread.Sleep(5000)`

## Timer

Позволяет ожидать истечения времени без отдельного заблокированного потока для каждого таймера.

Пример: `Task.Delay(5000)`

## Task.WhenAll

Объединяет завершение задач; не выделяет отдельные потоки и не запускает уже созданные задачи.

Пример: `await Task.WhenAll(tasks)`

## ThreadPool starvation

Недостаток свободных worker-потоков задерживает выполнение задач из очереди.

Пример: `Task.Run(() => Thread.Sleep(5000))`

## Worker Thread

Поток ОС, который ThreadPool использует для выполнения задач из очереди.

Пример: `ThreadPool worker executing Task.Run`

## Thread Creation

Создание дополнительного потока ОС; не то же, что создание объекта Task.

Пример: `new Thread(...).Start(); ThreadPool scales workers`
