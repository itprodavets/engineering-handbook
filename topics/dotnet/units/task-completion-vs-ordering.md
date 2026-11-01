# Task: completion synchronization, порядок и таймеры

[Русский](task-completion-vs-ordering.md) · [English](en/task-completion-vs-ordering.md)

[Главная](../../../README.md) · [Модуль](../task-composition.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/task-completion-vs-ordering)

> Различать ожидание конкретной Task, ожидание набора задач и ожидание времени; не путать completion с execution order.

## Определение

`await producer` устанавливает связь с завершением конкретной задачи и позволяет безопасно читать произведённые ею данные после завершения. `await Task.WhenAll(producer,consumer)` ожидает обе задачи, но не упорядочивает операции внутри них. `await Task.Delay(100)` ожидает таймер, а не Producer; время не является протоколом синхронизации.

## Внутренний механизм

1. Task.Run ставит делегат в ThreadPool. После записи data=42 Producer завершает Task; await этой конкретной Task упорядочивает последующее чтение.
2. Task.WhenAll не определяет порядок исполнения Producer и Consumer: Consumer может прочитать data=0 до записи Producer.
3. Task.Delay возвращает Task, связанную с таймером; это не делегат и не выделенный заблокированный worker.
4. Даже если Producer реально завершился раньше таймера, await постороннего таймера не является заменой ожиданию Producer для корректного memory ordering.
5. Для зависимости await producer внутри Consumer или перед чтением. Для timeout используй Task.WaitAsync(TimeSpan, token) либо WhenAny с проверкой победителя и явным контролем проигравшей операции.

## Последовательное объяснение

### Await Producer обеспечивает синхронизацию

Надо отличать ожидание завершения от блокирования thread. После `await producer` код продолжения видит записи, сделанные до успешного завершения producer, если нет других несинхронизированных писателей. Даже если async-метод реально приостанавливался и продолжился на другом worker, гарантия относится к Task completion, а не thread identity.

```csharp
Task producer=Task.Run(() => data=42);
await producer;
Console.WriteLine(data); // 42
```

### WhenAll ждёт, но не упорядочивает

Если Producer и Consumer независимо поставлены в ThreadPool, `await WhenAll` выполняется после того, как Consumer уже прочитал data. Он лишь ждёт завершения обоих и не создаёт happens-before между Producer write и Consumer read. В частности, Consumer может вывести 0. Исправление — сделать `await producer` частью самого Consumer.

```csharp
Task consumer=Task.Run(async () => { await producer; Console.WriteLine(data); });
```

### Task.Delay — таймер, не готовность данных

`await Task.Delay(100)` ждёт примерно указанный интервал, но не доказывает завершение другой Task. Producer может стартовать поздно или работать дольше. Даже успешное завершение Producer «по настенным часам» до таймера не является нужным memory-ordering доказательством между независимыми задачами. В CI можно воспроизвести нулевой результат gate, а не нестабильными гонками времени.

```csharp
await Task.Delay(100);
Console.WriteLine(data); // no producer completion dependency
```

### Победитель WhenAny и последующее чтение

Task.WhenAny возвращает Task победителя. Сам факт победы таймера не означает, что Producer остаётся незавершённым к моменту продолжения после await: Producer может закончить в промежутке. Проверяй идентичность победителя, затем ожидай Producer, если именно он завершился, и отдельно обрабатывай проигравшего при timeout.


## Потребляемые ресурсы

Task completions, scheduler/continuations, таймеры и память их состояний; await при незавершённой задаче обычно не удерживает ThreadPool worker.

## Ошибки и ограничения

`await Task.WhenAll(...)` после чтения не исправляет уже произошедшую гонку. `Task.Delay` не гарантирует конкретного порядка и не заменяет готовность результата. Completed Task не равна Task<T> с данными.

## Пример

```csharp
int data = 0;
Task producer = Task.Run(() => { data = 42; });
Task consumer = Task.Run(async () => { await producer; Console.WriteLine(data); });
await Task.WhenAll(producer, consumer); // 42
```

## Запускаемые эксперименты

- [Q-052.cs](../../../labs/dotnet/Q-052.cs) — `dotnet run --file labs/dotnet/Q-052.cs`
- [Q-053.cs](../../../labs/dotnet/Q-053.cs) — `dotnet run --file labs/dotnet/Q-053.cs`
- [Q-054.cs](../../../labs/dotnet/Q-054.cs) — `dotnet run --file labs/dotnet/Q-054.cs`

## Вопросы для закрепления

- [Q-052: Почему после await producer чтение data без volatile даёт 42?](../../../questions/dotnet/Q-052-await-producer-publishes-data.md)
- [Q-053: Можно ли вывести 0 внутри Consumer, хотя в конце вызван await Task.WhenAll(producer,consumer)?](../../../questions/dotnet/Q-053-whenall-does-not-order-producer-consumer.md)
- [Q-054: Почему await Task.Delay(100) не гарантирует, что другая Task завершилась и опубликовала data=42?](../../../questions/dotnet/Q-054-task-delay-is-not-synchronization.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Различи completion synchronization, execution ordering и waiting for time.

<details>
<summary>Критерии ответа</summary>

await producer — связь с producer; WhenAll — join без порядка внутри; Delay — unrelated timer.

</details>

### 2. Explain

Почему после await producer читаем data=42 без volatile?

<details>
<summary>Критерии ответа</summary>

Producer записал до completion; await синхронизирует наблюдение завершения; других писателей нет.

</details>

### 3. Predict

Что может прочитать Consumer внутри независимой Task, если WhenAll вызывается только потом?

<details>
<summary>Критерии ответа</summary>

0 или 42; WhenAll после события не устанавливает порядок внутри задач.

</details>

### 4. Diagnose

Код проходит тесты с Task.Delay(100), но падает при нагрузке. Почему?

<details>
<summary>Критерии ответа</summary>

Ожидание таймера вместо события, нет зависимости; планировщик/нагрузка меняют timing; нужен await конкретной операции.

</details>

### 5. Design

Как безопасно организовать Consumer и timeout без блокирования worker?

<details>
<summary>Критерии ответа</summary>

await producer для зависимостей; Task.WaitAsync(timeout)/CancellationToken с кооперативной отменой, наблюдением errors и cleanup; у WhenAny проверять winner.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0)

---

[← Назад](task-aggregation.md) · [Далее →](startnew-nested-tasks.md) · [Русский](task-completion-vs-ordering.md) · [English](en/task-completion-vs-ordering.md)
