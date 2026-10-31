# Что компилятор генерирует для async/await

[Русский](async-state-machine.md) · [English](en/async-state-machine.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-state-machine)

> Понимать MoveNext, awaiter и ветвление IsCompleted.

## Определение

Roslyn понижает async-метод в машину состояний с полями для сохранения состояния и методом MoveNext(). Само ключевое слово async не запускает поток.

## Внутренний механизм

1. Вызов async Task-метода начинает исполнение на вызывающем потоке до await незавершённого awaitable.
2. Awaiter.IsCompleted=true означает синхронное продолжение через GetResult(), без обязательного переключения.
3. При IsCompleted=false state machine сохраняет позицию, регистрирует continuation и возвращает Task вызывающему коду.
4. После завершения операции MoveNext продолжает выполнение; количество heap-аллокаций зависит от пути и реализации.

## Последовательное объяснение

### Что реально создаёт Roslyn

Для `async Task<T>` Roslyn создаёт реализацию `IAsyncStateMachine` с полями состояния, awaiter, локальных переменных, которые переживают приостановку, и `AsyncTaskMethodBuilder<T>`. Точка входа создаёт и инициализирует машину, вызывает builder.Start(ref stateMachine) и возвращает Task через builder.Task. Детали физического представления могут отличаться в Debug/Release и между версиями Roslyn/runtime.

### MoveNext: синхронная ветка и незавершённый await

В `MoveNext()` вызов `GetAwaiter()` возвращает awaiter. Если `IsCompleted` истинно, `GetResult()` выполняется прямо сейчас и код идёт дальше. Иначе state machine сохраняет номер состояния и awaiter, а builder регистрирует continuation через механизм вроде `AwaitUnsafeOnCompleted`. Это *схематическое* описание — для реального IL нужно дизассемблировать конкретную сборку.

```csharp
// Schematic, NOT literal Roslyn-generated C#:
var awaiter = operation.GetAwaiter();
if (!awaiter.IsCompleted)
{
    state = 0;
    savedAwaiter = awaiter;
    builder.AwaitUnsafeOnCompleted(ref awaiter, ref this);
    return;
}
var value = awaiter.GetResult();
```

### Завершение, исключения и продолжения

При завершении ожидаемой операции продолжение снова вызывает `MoveNext()`: восстанавливает awaiter/состояние, выполняет `GetResult()` (здесь может быть повторно выброшено исключение) и движется дальше. Успех завершается через builder.SetResult, ошибка — через SetException. Асинхронность — способ разделить один метод на несколько фрагментов исполнения; это не требование создать новый OS Thread.

### Как увидеть именно сгенерированный код

Собери отдельный пример в Debug и Release, открой сборку в ILSpy либо SharpLab и сравни MoveNext, поля состояния, GetAwaiter, IsCompleted и вызовы builder. Логи выполнения показывают результат, но не являются доказательством конкретных IL-инструкций. Утверждения о количестве heap-объектов отдельно проверь профилировщиком.


## Потребляемые ресурсы

Поля состояния и awaiter; возможные continuation и Task allocations; нет обязательного нового ОС-потока.

## Ошибки и ограничения

Нельзя приравнивать await к Task.Run: завершённая Task не обязана приводить даже к приостановке метода.

## Пример

```csharp
async Task Example() { Console.Write("A"); await Task.CompletedTask; Console.Write("B"); }
```

## Запускаемые эксперименты

- [02-state-machine-reflection.cs](../../../labs/dotnet/async-internals/02-state-machine-reflection.cs) — `dotnet run --file labs/dotnet/async-internals/02-state-machine-reflection.cs`

## Вопросы для закрепления

- [Q-012: Запускает ли вызов async Task-метода новый поток или начинает работу синхронно?](../../../questions/dotnet/Q-012-async-starts-synchronously.md)
- [Q-025: Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource.](../../../questions/dotnet/Q-025-incomplete-await-output.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Что представляет собой async state machine? Назови IAsyncStateMachine и MoveNext.

<details>
<summary>Критерии ответа</summary>

Упомянут сгенерированный тип с состоянием и методом MoveNext; async не создаёт поток.

</details>

### 2. Explain

Восстанови цепочку GetAwaiter → IsCompleted → AwaitUnsafeOnCompleted → GetResult → SetResult/SetException.

<details>
<summary>Критерии ответа</summary>

Правильно описаны обе ветки (готово/ожидание), сохранение состояния и механизм ошибок; синтаксис компилятора отделён от деталей реализации.

</details>

### 3. Predict

Какой вывод у async-метода, где await Task.CompletedTask расположен между Console.Write("A") и Console.Write("B"), а вызывающий печатает "C" после вызова?

<details>
<summary>Критерии ответа</summary>

ABC: awaiter уже завершён, приостановки нет; сам async-метод начинает исполняться синхронно.

</details>

### 4. Diagnose

ILSpy показывает MoveNext и поля awaiter. Значит ли это, что каждый вызов обязательно аллоцирует state machine на managed heap?

<details>
<summary>Критерии ответа</summary>

Нет: наличие сгенерированного типа не равно отдельному объекту на heap; фактический путь зависит от async completion и runtime. Измерить профилировщиком.

</details>

### 5. Design

Тебе предложили заменить все Task<T> на ValueTask<T> ради производительности. Какие данные нужны до решения?

<details>
<summary>Критерии ответа</summary>

Измерения sync completion rate, allocations/op, throughput/latency, интерфейсы потребления, повторный await, IValueTaskSource. Без замеров не менять.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Назад](awaiter-completion-path.md) · [Далее →](async-socket-pipeline.md) · [Русский](async-state-machine.md) · [English](en/async-state-machine.md)
