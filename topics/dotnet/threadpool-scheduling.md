# ThreadPool и планировщик ОС

[Русский](threadpool-scheduling.md) · [English](en/threadpool-scheduling.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/threadpool-scheduling)

Кто планирует work item и кто назначает поток на CPU.

## Определение

Task — представление операции; Thread — последовательность выполнения с ОС-стеком. ThreadPool распределяет work items между worker-потоками, а OS Scheduler размещает эти потоки на логических CPU. Task.Run не означает создание нового Thread.

## Механизм: от языка и runtime до ОС

1. Task.Run ставит делегат в очередь TaskScheduler.Default / ThreadPool; ThreadPool может использовать существующий worker.
2. Если доступных workers недостаточно, ThreadPool может увеличивать их количество по внутренним эвристикам и ограничениям.
3. Ядро ОС выбирает готовые потоки для логических CPU, вытесняет их и может переносить между ядрами.
4. Thread.Sleep блокирует worker, а Task.Delay использует таймер и не резервирует worker для ожидания.

## Ресурсы

- **OS-потоки:** Новые workers используют системные стеки, служебные структуры и виртуальную память.
- **Очереди:** Task.Run помещает делегаты в очередь; 10 000 Task не означает 10 000 одновременно выполняющихся делегатов.
- **CPU:** Спящий worker не расходует CPU на вычисления, но недоступен для полезной работы пула.

## Ограничения и риски

- ThreadPool starvation возникает из-за нехватки доступных worker-потоков и больших очередей, не обязательно при 100% CPU.
- Нельзя вывести точное количество созданных потоков из количества Task.

## Вопросы для проверки

- [Q-006: Как 8 физических ядер CPU могут выполнять работу 100 готовых к исполнению потоков?](../../questions/dotnet/Q-006-hundred-threads-eight-cores.md)
- [Q-007: Чем отличается .NET ThreadPool от планировщика ОС? Кто решает, на каком ядре выполняется поток?](../../questions/dotnet/Q-007-threadpool-vs-os-scheduler.md)
- [Q-008: Чем Task отличается от Thread? Создаёт ли Task новый поток и что делает await?](../../questions/dotnet/Q-008-task-vs-thread.md)
- [Q-009: Что произойдёт с ThreadPool, если одновременно запустить 10 000 Task.Delay(5000) и 10 000 Task.Run(() => Thread.Sleep(5000))?](../../questions/dotnet/Q-009-task-delay-vs-thread-sleep.md)
- [Q-010: Создаёт ли Task.WhenAll новые потоки и запускает ли сам переданные ему задачи?](../../questions/dotnet/Q-010-task-whenall-execution.md)
- [Q-011: Что означает «ThreadPool может создать дополнительный поток» при вызове Task.Run и почему это не означает 10 000 потоков для 10 000 Task?](../../questions/dotnet/Q-011-threadpool-worker-creation.md)

## Закрепление на коде

—

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool](https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool)
- [https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/debug-threadpool-starvation)

---

[Русский](threadpool-scheduling.md) · [English](en/threadpool-scheduling.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/threadpool-scheduling)
