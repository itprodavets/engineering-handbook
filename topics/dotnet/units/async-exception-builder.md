# AsyncTaskMethodBuilder: Faulted, Canceled и исключения

[Русский](async-exception-builder.md) · [English](en/async-exception-builder.md)

[Главная](../../../README.md) · [Модуль](../cancellation.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-exception-builder)

> Отличать статус Task от типа исключения, объяснять SetException и синхронные сбои внутри async Task.

## Определение

AsyncTaskMethodBuilder.SetException в .NET для `async Task` различает OperationCanceledException (Task.Canceled) и остальные исключения (Task.Faulted). `Task.FromException(new OperationCanceledException())` всегда создаёт Faulted Task. `Task.Yield()` создаёт асинхронную точку продолжения, но не является источником отмены.

## Внутренний механизм

1. Компилятор создаёт state machine; MoveNext оборачивает пользовательское тело async Task необходимой обработкой исключений.
2. AsyncTaskMethodBuilder.SetException получает исключение и при OperationCanceledException вызывает путь TrySetCanceled с токеном из исключения; иначе TrySetException.
3. Отсюда async Task с throw new OperationCanceledException() получает Canceled даже без явного `CancellationTokenSource.Cancel()` в этом конкретном механизме.
4. Task.FromException создаёт уже Faulted Task вне зависимости от класса переданного исключения, включая OperationCanceledException; Task.FromCanceled требует уже отменённый token.
5. Исключение в теле `async Task` даже до первого незавершённого await обычно сохраняется в Task, а не синхронно выбрасывается из вызова; исключения при вычислении аргументов перед вызовом — другой случай.

## Последовательное объяснение

### Статус Task и класс исключения различаются

Нельзя определять Task.Status лишь по имени исключения. `Task.FromException(new OperationCanceledException())` создаёт `Faulted`, хотя `await` этой Task выбросит OperationCanceledException. `Task.FromCanceled(new CancellationToken(true))` создаёт `Canceled`, у которого exception aggregation устроена иначе. Для diagnostics проверяй и статус, и источник Task.

```csharp
Task fault=Task.FromException(new OperationCanceledException());
Task canceled=Task.FromCanceled(new CancellationToken(true));
// fault.Status=Faulted; canceled.Status=Canceled
```

### Почему async Task с OCE становится Canceled

В .NET 10 в AsyncTaskMethodBuilder<T>.SetException есть проверка `exception is OperationCanceledException oce`. При совпадении вызывается `task.TrySetCanceled(oce.CancellationToken, oce)`, иначе `TrySetException(exception)`. Это конкретный runtime source, который объясняет отличия builder от Task.FromException. `Task.Yield()` только меняет continuation scheduling.

```csharp
static async Task F() { await Task.Yield(); throw new OperationCanceledException(); }
// await/catch; F() task status == Canceled
```

### Ошибка после CompletedTask ещё внутри Task

`await Task.CompletedTask` может завершиться синхронно, поэтому `throw` выполняется до того, как вызывающему вернётся значение. Но он всё ещё находится внутри state machine и перехватывается builder. Вызывающий получает Faulted Task, а исключение возникает при `await task`. Отдельный случай: throw в обычном не-async методе до получения Task.

```csharp
static async Task F() { await Task.CompletedTask; throw new InvalidOperationException(); }
Task t=F(); // does not throw out of F()
// t.Status == Faulted
```

### Как правильно классифицировать отмену в production

Перехватить OperationCanceledException недостаточно, чтобы утверждать, что конкретная Task находится в состоянии Canceled. Для Task.FromException(OCE) статус Faulted. При реальной отмене проверяй связанные токены, статус Task и ожидаемое поведение API. Не проглатывай отмену как успех, не называй каждую OCE пользовательским запросом на отмену.


## Потребляемые ресурсы

State machine, Task или внутренний state box, exception record, CancellationToken и ожидание продолжений. Точная аллокация зависит от исполнения.

## Ошибки и ограничения

Не путать canceled Task с Faulted Task, внутри которой лежит OperationCanceledException. Правила Task.Run(Action) и токены отмены отличаются от обработки исключений компиляторного async Task. `await Task.CompletedTask` не обязан приостанавливать выполнение.

## Пример

```csharp
static async Task FailAsync() { await Task.CompletedTask; throw new InvalidOperationException("Error"); }
Task task = FailAsync(); // returns Faulted Task
try { await task; } catch (InvalidOperationException) { }
```

## Запускаемые эксперименты

- [Q-061.cs](../../../labs/dotnet/Q-061.cs) — `dotnet run --file labs/dotnet/Q-061.cs`
- [Q-062.cs](../../../labs/dotnet/Q-062.cs) — `dotnet run --file labs/dotnet/Q-062.cs`
- [Q-063.cs](../../../labs/dotnet/Q-063.cs) — `dotnet run --file labs/dotnet/Q-063.cs`

## Вопросы для закрепления

- [Q-061: Почему Task.FromException(new OperationCanceledException()) имеет Faulted, а Task.FromCanceled(token) имеет Canceled?](../../../questions/dotnet/Q-061-fromexception-oce-vs-fromcanceled.md)
- [Q-062: Почему async Task с throw OperationCanceledException получает Canceled, а Task.FromException(OCE) — Faulted?](../../../questions/dotnet/Q-062-async-task-oce-builder-canceled.md)
- [Q-063: Выбрасывает ли TestAsync() синхронно InvalidOperationException, если внутри await Task.CompletedTask затем throw?](../../../questions/dotnet/Q-063-async-task-throws-after-completed-await.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Назови статусы Task.FromException(OCE), Task.FromCanceled(token) и async Task throw OCE.

<details>
<summary>Критерии ответа</summary>

Faulted, Canceled, Canceled (для async Task builder).

</details>

### 2. Explain

Как AsyncTaskMethodBuilder.SetException решает, что Task отменена?

<details>
<summary>Критерии ответа</summary>

OperationCanceledException → TrySetCanceled(token из OCE), иначе TrySetException. Task.Yield не является причиной.

</details>

### 3. Predict

Будет ли синхронный throw наружу при TestAsync() c await CompletedTask и InvalidOperationException?

<details>
<summary>Критерии ответа</summary>

Нет: метод возвращает Task со статусом Faulted, await task выбрасывает InvalidOperationException.

</details>

### 4. Diagnose

Почему в telemetry встречаются Faulted Task с OperationCanceledException и Canceled Task с тем же типом?

<details>
<summary>Критерии ответа</summary>

Разные способы создания/завершения Task: FromException vs AsyncTaskMethodBuilder/FromCanceled. Проверять происхождение и token.

</details>

### 5. Design

Как проектировать диагностику API, различающую ошибки и отмену?

<details>
<summary>Критерии ответа</summary>

Учитывать Task.Status, token request/correlation, тип исключения, propagated cancellations; не считать OCE синонимом корректной отмены.

</details>


## Источники

- [https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html](https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromcanceled?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromcanceled?view=net-10.0)

---

[← Назад](cancellation-tokens.md) · [Русский](async-exception-builder.md) · [English](en/async-exception-builder.md)
