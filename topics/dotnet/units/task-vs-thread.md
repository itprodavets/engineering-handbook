# Thread, Task и Task.Run — разные сущности

[Русский](task-vs-thread.md) · [English](en/task-vs-thread.md)

[Главная](../../../README.md) · [Модуль](../threadpool-scheduling.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/task-vs-thread)

> Отделять единицу выполнения ОС от описания завершения операции.

## Определение

Thread — планируемый ОС контекст выполнения со стеком; Task — управляемый объект завершения операции. Task.Run ставит делегат в ThreadPool, а не гарантированно создаёт новый Thread.

## Внутренний механизм

1. Объект Task может находиться в состоянии ожидания I/O без выделенного рабочего потока.
2. Task.Run использует доступный worker для выполнения делегата; worker затем возвращается пулу.
3. Task.WhenAll отслеживает завершение переданных задач и не запускает их заново.
4. Поток ОС имеет свой стек, а Task — не имеет отдельного стека ОС как неотъемлемого свойства.

## Потребляемые ресурсы

Thread: стек ОС, TCB/системные структуры, OS scheduling; Task: managed state и continuation.

## Ошибки и ограничения

«10000 Task = 10000 Thread» — неверно; отличай очередь задач от числа занятых worker-потоков.

## Пример

```csharp
var task = Task.Run(() => Compute());
var result = await task;
```

## Вопросы для закрепления

- [Q-008: Чем Task отличается от Thread? Создаёт ли Task новый поток и что делает await?](../../../questions/dotnet/Q-008-task-vs-thread.md)
- [Q-010: Создаёт ли Task.WhenAll новые потоки и запускает ли сам переданные ему задачи?](../../../questions/dotnet/Q-010-task-whenall-execution.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool](https://learn.microsoft.com/en-us/dotnet/standard/threading/the-managed-thread-pool)

---

[Далее →](os-vs-runtime-scheduler.md) · [Русский](task-vs-thread.md) · [English](en/task-vs-thread.md)
