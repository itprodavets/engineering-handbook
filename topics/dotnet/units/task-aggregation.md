# WhenAny/WhenAll: завершение, ошибки и отмена

[Русский](task-aggregation.md) · [English](en/task-aggregation.md)

[Главная](../../../README.md) · [Модуль](../task-composition.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/task-aggregation)

> Точно понимать вложенные Task, приоритет Faulted/Canceled, aggregation и поведение await.

## Определение

WhenAny даёт Task<Task>: внешняя задача успешно завершается при первом завершении входящей и возвращает Task-победителя, даже если он Faulted/Canceled. WhenAll ждёт все входящие: Faulted приоритетнее Canceled; при нескольких faults агрегат хранит их все, хотя await распространяет одно. WhenAny не отменяет проигравшие операции.

## Внутренний механизм

1. WhenAny возвращает Task<Task> и не выбрасывает fault победителя до ожидания самой возвращённой Task.
2. Проигравшие WhenAny продолжают исполняться, а таймер может выиграть раньше Producer, который затем завершится до resume вызывающего.
3. WhenAll не завершается после первого отказа: он ждёт все входящие Task, затем вычисляет Faulted/Canceled/RanToCompletion.
4. combined.Exception.InnerExceptions содержит отдельные fault-исключения входящих; await combined распространяет одно, а синхронный Wait бросает AggregateException.
5. В результате Faulted+Canceled общее состояние Faulted; отменённая входящая Task всё ещё Canceled.

## Последовательное объяснение

### WhenAny возвращает Task<Task>

`Task.WhenAny(first,second)` возвращает Task<Task>. `await WhenAny(...)` успешно выдаёт Task-победителя даже если он Faulted/Canceled; выбросить исключение победителя можно при следующем `await completed`. Не путай Completed wrapper и Winner. Проигравшие Task продолжают выполнение и автоматически не отменяются.

```csharp
Task completed=await Task.WhenAny(producer,timeout);
if (completed==producer) await producer;
else Console.WriteLine("Timeout");
```

### Победитель и состояние к моменту продолжения

Победитель определяется первым событием завершения. Но пока код после await получит CPU, проигравшая задача тоже может завершиться. Поэтому «таймер выиграл» не означает «Producer ещё не выполнился к моменту Console.WriteLine». При timeout вызывающий код обязан решить, как отменять, наблюдать исключения и освобождать ресурсы проигравшего.

### WhenAll собирает ошибки и дожидается всех

`Task.WhenAll` не fail-fast: возвращённая Task завершается лишь после завершения всех входящих. Когда две Task уже Faulted, `combined.Exception.InnerExceptions.Count == 2` (для двух одиночных исключений). `await combined` распространяет одно исключение, не обязательно агрегирующий объект; для всех ошибок исследуй сохранённую `combined.Exception`.

```csharp
Task combined=Task.WhenAll(first,second);
try { await combined; }
catch { foreach (var ex in combined.Exception!.InnerExceptions) Console.WriteLine(ex); }
```

### Faulted приоритетнее Canceled

Итог WhenAll: есть хотя бы одна Faulted → Faulted; иначе есть хотя бы одна Canceled → Canceled; иначе RanToCompletion. Отмена другой Task при этом не исчезает — её собственный статус остаётся Canceled; но она не прибавляется как отдельный Fault к агрегату исключений. Await WhenAll с fault распространяет одно из fault-исключений.

### Таймер и обработка ошибок

`Task.Delay` даёт возможность timeout, но сам по себе не гарантирует, что Producer успел завершиться. После `WhenAny` проверь идентичность победителя и `await` самого Producer при его успехе, чтобы правильно получить его исключение и memory synchronization. Для APIs, поддерживающих токен, кооперативная отмена обязательна для реальной остановки: истечение времени само не отменяет I/O.


## Потребляемые ресурсы

Объекты Task/continuations, tracking завершения всех входящих, память для исключений и возможный lifetime проигравших WhenAny операций.

## Ошибки и ограничения

Не называй WhenAll fail-fast; не рассчитывай на фиксированный порядок исключений при конкурентных сбоях. Проверка Status не равнозначна обработке ошибок. При timeout отдельно управляй токеном, продолжением, наблюдением ошибок и ресурсами проигравшей Task.

## Пример

```csharp
Task winner = await Task.WhenAny(producer, Task.Delay(1000));
if (winner == producer) await producer; // propagate producer fault
else Console.WriteLine("Timeout");
```

## Запускаемые эксперименты

- [Q-055.cs](../../../labs/dotnet/Q-055.cs) — `dotnet run --file labs/dotnet/Q-055.cs`
- [Q-056.cs](../../../labs/dotnet/Q-056.cs) — `dotnet run --file labs/dotnet/Q-056.cs`
- [Q-057.cs](../../../labs/dotnet/Q-057.cs) — `dotnet run --file labs/dotnet/Q-057.cs`
- [Q-058.cs](../../../labs/dotnet/Q-058.cs) — `dotnet run --file labs/dotnet/Q-058.cs`
- [Q-059.cs](../../../labs/dotnet/Q-059.cs) — `dotnet run --file labs/dotnet/Q-059.cs`
- [Q-060.cs](../../../labs/dotnet/Q-060.cs) — `dotnet run --file labs/dotnet/Q-060.cs`

## Вопросы для закрепления

- [Q-014: Выбрасывает ли await Task.WhenAny ошибку первой упавшей задачи и отменяет ли остальные?](../../../questions/dotnet/Q-014-whenany-faulted-task.md)
- [Q-015: Как Task.WhenAll обрабатывает несколько faulted Task и что выбрасывает await?](../../../questions/dotnet/Q-015-whenall-multiple-exceptions.md)
- [Q-026: Что напечатает код и выбросит ли await Task.WhenAny исключение?](../../../questions/dotnet/Q-026-whenany-faulted-output.md)
- [Q-027: Сколько исключений в Exception.InnerExceptions при двух завершившихся с ошибкой Task?](../../../questions/dotnet/Q-027-whenall-exceptions-count.md)
- [Q-055: Если Task.Delay выиграла WhenAny, обязательно ли Producer остаётся незавершённым к моменту продолжения?](../../../questions/dotnet/Q-055-whenany-winner-vs-continuation-time.md)
- [Q-056: Выбросит ли await Task.WhenAny исключение из Faulted Task-победителя? Что меняет await completed?](../../../questions/dotnet/Q-056-whenany-faulted-winner-exception.md)
- [Q-057: Сколько исключений в combined.Exception.InnerExceptions при двух Task.FromException и что выбросит await combined?](../../../questions/dotnet/Q-057-whenall-multiple-exceptions-await-one.md)
- [Q-058: Какой статус имеет WhenAll(Faulted,Canceled) и какое исключение распространяет await?](../../../questions/dotnet/Q-058-whenall-faulted-priority-over-canceled.md)
- [Q-059: Отменяет ли Task.WhenAny проигравшие Task и как они завершаются?](../../../questions/dotnet/Q-059-whenany-does-not-cancel-loser.md)
- [Q-060: Если одна входящая Task уже Faulted, а другая ещё pending, завершится ли немедленно Task.WhenAll?](../../../questions/dotnet/Q-060-whenall-waits-not-fail-fast.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Опиши тип Task.WhenAny(Task, Task) и поведение ошибки победителя.

<details>
<summary>Критерии ответа</summary>

Task<Task>; внешняя Task RanToCompletion, вернётся winner; await winner распространяет ошибку.

</details>

### 2. Explain

Как WhenAll решает Faulted/Canceled/RanToCompletion и что хранит Exception?

<details>
<summary>Критерии ответа</summary>

Faulted > Canceled > success. Aggregate исключения faulted входящих; все задачи завершены.

</details>

### 3. Predict

Два Task.FromException и await WhenAll: сколько InnerExceptions и что выбрасывает await?

<details>
<summary>Критерии ответа</summary>

Два InnerExceptions, await выбрасывает одно из сохранённых исключений (не обязательно AggregateException).

</details>

### 4. Diagnose

Почему одна Task уже faulted, а await Task.WhenAll ещё не завершился?

<details>
<summary>Критерии ответа</summary>

WhenAll ждёт все, не fail-fast. Исследовать оставшиеся pending, cancellation, hangs и resource lifetime.

</details>

### 5. Design

Как безопасно построить timeout через WhenAny, обработать fault и не забыть проигравшую Task?

<details>
<summary>Критерии ответа</summary>

Task winner=await WhenAny(producer,delay); if winner==producer await producer; else cancel cooperative, observe faults, cleanup. Или WaitAsync с учётом того, что underlying operation может продолжиться.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenany?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0)

---

[Далее →](task-completion-vs-ordering.md) · [Русский](task-aggregation.md) · [English](en/task-aggregation.md)
