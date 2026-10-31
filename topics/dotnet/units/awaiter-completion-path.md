# Контракт awaiter и синхронное завершение

[Русский](awaiter-completion-path.md) · [English](en/awaiter-completion-path.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/awaiter-completion-path)

> Понять GetAwaiter/IsCompleted/GetResult и почему await может не приостановить метод.

## Определение

`await` применим не только к Task: компилятор использует awaiter pattern (GetAwaiter, IsCompleted, GetResult и регистрацию продолжения). При готовом awaitable метод идёт дальше синхронно; при незавершённом — сохраняет состояние.

## Внутренний механизм

1. Сначала вызывается GetAwaiter() у awaitable.
2. IsCompleted определяет, доступен ли результат прямо сейчас.
3. Если завершено — GetResult выполняется в текущем стеке вызовов; при исключении оно пробрасывается.
4. Иначе регистрируется continuation; async-метод возвращает управление вызывающему коду.

## Последовательное объяснение

### Это протокол компилятора, не только Task

Синтаксис `await` проверяется через подходящий awaiter. Помимо GetAwaiter и IsCompleted нужен GetResult и возможность зарегистрировать continuation (INotifyCompletion либо ICriticalNotifyCompletion). Разные awaitable могут обеспечивать разные правила исполнения; нельзя выводить семантику всего языка только по реализации Task.

### Почему ABC — не ACB

Когда PrintAsync вызывается, её тело начинает исполняться синхронно. `Task.CompletedTask` уже имеет завершённый awaiter, поэтому `B` печатается до возврата из PrintAsync. Вызывающий код печатает `C` позже. Новый поток не нужен ни на одном этапе.

### Что меняется при незавершённой Task

С `TaskCompletionSource` без SetResult awaiter возвращает `IsCompleted=false`: метод сохраняет state/awaiter, регистрирует продолжение и возвращает Task. Вызывающий код продолжает работу, а `SetResult` разрешает дальнейшее выполнение. С `RunContinuationsAsynchronously` continuation не встраивается синхронно в SetResult.

### Как доказать

Запусти Q-024 и Q-025, затем поменяй CompletedTask на Task.Delay(1): станет ли порядок гарантированным? Нет, короткий timer и планирование дают гонку, поэтому для доказательства асинхронной приостановки используй управляемый TaskCompletionSource gate.


## Потребляемые ресурсы

Для завершённого await не требуется рабочий поток для ожидания; незавершённое ожидание может удерживать Task/continuation и ссылки на локальные данные.

## Ошибки и ограничения

Нельзя считать, что `await` гарантирует fairness или переключение потока. Для чисто CPU-bound циклов нужна отдельная стратегия планирования.

## Пример

```csharp
async Task PrintAsync() { Console.Write("A"); await Task.CompletedTask; Console.Write("B"); }
var t = PrintAsync(); Console.Write("C"); await t; // ABC
```

## Запускаемые эксперименты

- [Q-024.cs](../../../labs/dotnet/Q-024.cs) — `dotnet run --file labs/dotnet/Q-024.cs`
- [Q-025.cs](../../../labs/dotnet/Q-025.cs) — `dotnet run --file labs/dotnet/Q-025.cs`

## Вопросы для закрепления

- [Q-013: Всегда ли await приостанавливает метод, выделяет worker или переключает поток?](../../../questions/dotnet/Q-013-completed-await-and-scheduling.md)
- [Q-024: Какой вывод и почему? async-метод содержит await уже завершённой Task.](../../../questions/dotnet/Q-024-completed-await-output.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Что обязаны предоставить awaitable и awaiter для C# await?

<details>
<summary>Критерии ответа</summary>

GetAwaiter, IsCompleted, GetResult, регистрация continuation через OnCompleted/UnsafeOnCompleted; не только Task.

</details>

### 2. Explain

Объясни две ветки await по значению IsCompleted.

<details>
<summary>Критерии ответа</summary>

True: GetResult и синхронное продолжение; false: сохранение state и continuation.

</details>

### 3. Predict

Выведет ли код с await Task.CompletedTask буквы ABC или ACB и почему?

<details>
<summary>Критерии ответа</summary>

ABC; метод начинается синхронно, await уже завершён.

</details>

### 4. Diagnose

Почему Task.Delay(1) — плохой способ доказать, что продолжение на другом потоке?

<details>
<summary>Критерии ответа</summary>

Малая задержка и scheduler создают гонку, разные ThreadId не гарантия, await не создаёт Thread.

</details>

### 5. Design

Как написать детерминированный тест незавершённого await без Thread.Sleep?

<details>
<summary>Критерии ответа</summary>

TaskCompletionSource с RunContinuationsAsynchronously, сначала assert false IsCompleted, затем SetResult и await; фиксированный порядок.

</details>


## Источники

- [https://devblogs.microsoft.com/dotnet/how-async-await-really-works/](https://devblogs.microsoft.com/dotnet/how-async-await-really-works/)

---

[← Назад](io-vs-cpu-bound.md) · [Далее →](async-state-machine.md) · [Русский](awaiter-completion-path.md) · [English](en/awaiter-completion-path.md)
