# Планировщик ОС, ядра CPU и ThreadPool

[Русский](os-vs-runtime-scheduler.md) · [English](en/os-vs-runtime-scheduler.md)

[Главная](../../../README.md) · [Модуль](../threadpool-scheduling.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/os-vs-runtime-scheduler)

> Понимать время CPU, вытеснение и очереди .NET.

## Определение

OS Scheduler распределяет готовые потоки по логическим процессорам. .NET ThreadPool управляет доступными worker-потоками и очередями работы, но не выбирает для них конкретное CPU-ядро.

## Внутренний механизм

1. На восьми логических CPU могут одновременно исполняться не более восьми программных потоков в одном аппаратном слоте каждый.
2. ОС может вытеснить ещё не завершившийся поток и запустить другой; это context switch.
3. 100 готовых потоков могут конкурентно продвигаться, чередуясь во времени, но не исполняться все параллельно.
4. ThreadPool планирует задания на workers; планировщик ОС затем размещает эти workers на процессорах.

## Потребляемые ресурсы

CPU time на исполнение и переключение; cache misses при миграции; stacks и kernel bookkeeping потоков.

## Ошибки и ограничения

Низкая загрузка CPU при росте HTTP latency может указывать на ожидание I/O, блокировку или starvation.

## Пример

```csharp
Console.WriteLine(Environment.CurrentManagedThreadId);
```

## Вопросы для закрепления

- [Q-006: Как 8 физических ядер CPU могут выполнять работу 100 готовых к исполнению потоков?](../../../questions/dotnet/Q-006-hundred-threads-eight-cores.md)
- [Q-007: Чем отличается .NET ThreadPool от планировщика ОС? Кто решает, на каком ядре выполняется поток?](../../../questions/dotnet/Q-007-threadpool-vs-os-scheduler.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading](https://learn.microsoft.com/en-us/dotnet/standard/threading/threads-and-threading)

---

[← Назад](task-vs-thread.md) · [Далее →](threadpool-starvation.md) · [Русский](os-vs-runtime-scheduler.md) · [English](en/os-vs-runtime-scheduler.md)
