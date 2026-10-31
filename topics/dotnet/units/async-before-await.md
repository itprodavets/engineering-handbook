# Асинхронность до async/await: APM, EAP и TAP

[Русский](async-before-await.md) · [English](en/async-before-await.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-before-await)

> Объяснять, почему неблокирующее I/O существовало без async/await, и правильно анализировать callback.

## Определение

Асинхронное I/O — способность начать операцию и обработать результат позже без обязательного удержания потока на всё время ожидания. async/await (C# 5, 2012) — синтаксис и компиляторное преобразование над awaitable; он не изобрёл асинхронность. APM (Begin/End, IAsyncResult), EAP (события) и TAP (Task, с .NET 4) существовали раньше.

## Внутренний механизм

1. В APM BeginRead инициирует чтение, а EndRead извлекает результат или ошибку; callback может выполниться inline до возврата из BeginRead.
2. При настоящем незавершённом сетевом I/O операция ожидает готовности сокета через ОС/runtime; отдельный заблокированный worker на каждый ожидающий сокет не требуется.
3. У некоторых реализаций Stream APM может использовать блокирующий Read через worker; название BeginRead само по себе не гарантирует nonblocking I/O.
4. Task.Run(() => stream.Read(...)) переносит синхронное чтение в ThreadPool и может удерживать worker заблокированным.
5. TAP и async/await упрощают композицию операций: компилятор генерирует state machine и continuation, не заменяя подсистему I/O ОС.

## Последовательное объяснение

### Три поколения API

APM был представлен в .NET Framework 1.0: BeginX/EndX и IAsyncResult. EAP стал распространён в .NET 2.0: метод XAsync + событие XCompleted. .NET 4 принёс Task-based Asynchronous Pattern (TAP), Task, TaskCompletionSource и адаптеры Task.Factory.FromAsync. C# 5 в 2012 добавил async/await как более понятное описание последовательных продолжений. Это разные уровни: API и синтаксис.

### BeginRead, callback и EndRead

BeginRead инициирует чтение, возвращая IAsyncResult. При завершении вызывается AsyncCallback, который передаёт IAsyncResult в EndRead для получения числа байтов либо исключения. Если EndRead вызвать до завершения, он может блокироваться. Для конкретного NetworkStream документация допускает callback inline при синхронном завершении; свойство CompletedSynchronously описывает этот случай.

```csharp
IAsyncResult? result = null;
result = stream.BeginRead(buffer, 0, buffer.Length,
    ar => { Console.WriteLine(result is null); stream.EndRead(ar); }, null);
// Inline completion: True, because assignment has not happened yet.
```

### Настоящее I/O и перенос блокировки

Операция ожидания и поток обработки завершения — разные сущности. В сетевом async I/O .NET и ОС отслеживают незавершённую операцию, не удерживая пользовательский worker всю задержку. Однако Task.Run(() => stream.Read(...)) выполняет синхронный Read на worker и удерживает его до окончания ожидания; это не превращает чтение в неблокирующее.

### Inline callback, замыкание и гонки

В выражении result = BeginRead(... callback ...) правая часть вычисляется прежде присваивания. Если callback вызывается inline, captured result всё ещё null. Если callback вызван на другом потоке, результат может быть как null, так и ссылкой в зависимости от порядка выполнения; без синхронизации также нельзя полагаться на видимость записи. Аргумент callback ar содержит завершившийся IAsyncResult и устраняет зависимость от внешнего присваивания. Лаборатория Q-038 моделирует inline-вызов детерминированно — это не гарантия для каждого реального сокета.

### Как перейти от APM к Task

Task.Factory.FromAsync адаптирует корректный Begin/End-паттерн к Task. TaskCompletionSource может представлять завершение callback-API; RunContinuationsAsynchronously снижает риск синхронного исполнения пользовательских continuations внутри SetResult. Это мост абстракций, а не способ гарантированно получить неблокирующий I/O из синхронной реализации.


## Потребляемые ресурсы

Сокеты, сетевые буферы, состояние операции и callback; CPU при инициации и обработке завершения. Количество worker-потоков зависит от реализации и нагрузки.

## Ошибки и ограничения

Не вызывай EndRead раньше завершения на потоке, который должен оставаться свободным: он может блокировать. Не захватывай переменную результата BeginRead в callback, который потенциально выполнится inline; используй аргумент ar.

## Пример

```csharp
stream.BeginRead(buffer, 0, buffer.Length, ar => { int n = stream.EndRead(ar); /* process n bytes */ }, null);
```

## Запускаемые эксперименты

- [Q-036.cs](../../../labs/dotnet/Q-036.cs) — `dotnet run --file labs/dotnet/Q-036.cs`
- [Q-038.cs](../../../labs/dotnet/Q-038.cs) — `dotnet run --file labs/dotnet/Q-038.cs`

## Вопросы для закрепления

- [Q-036: Как выполняли асинхронный I/O до async/await и в какие годы появились APM, EAP и TAP?](../../../questions/dotnet/Q-036-apm-eap-tap-history.md)
- [Q-037: Почему NetworkStream.BeginRead может масштабироваться лучше, чем Task.Run(() => stream.Read(...))?](../../../questions/dotnet/Q-037-apm-vs-taskrun-read.md)
- [Q-038: Что напечатает callback, если он вызван inline до завершения присваивания result = BeginRead(...)?](../../../questions/dotnet/Q-038-inline-apm-callback-captured-result.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Назови последовательность APM → EAP → TAP → async/await и укажи отличие API от синтаксиса.

<details>
<summary>Критерии ответа</summary>

APM: Begin/End, IAsyncResult, .NET 1.0; EAP: события, .NET 2.0; TAP: Task, .NET 4; async/await: C# 5, 2012. Async существовал и раньше.

</details>

### 2. Explain

Объясни, почему 1 000 сетевых BeginRead могут ожидать без 1 000 заблокированных workers, а Task.Run(Read) — нет.

<details>
<summary>Критерии ответа</summary>

Отдельные pending I/O операции ОС; callbacks при завершении, worker нужен на обработку. Task.Run запускает синхронный Read на worker, который может блокироваться.

</details>

### 3. Predict

Что увидит замыкание result при inline callback до возврата BeginRead?

<details>
<summary>Критерии ответа</summary>

null: присваивание результатом BeginRead происходит позже. ar — это аргумент завершённой операции.

</details>

### 4. Diagnose

Приложение на старом .NET запускает 1 000 BeginRead и потребляет сотни workers. Какие гипотезы проверишь?

<details>
<summary>Критерии ответа</summary>

Определить конкретный тип Stream; настоящий socket APM или ThreadPool fallback; EndRead до завершения; sync waits, callbacks, стеки и ThreadPool counters.

</details>

### 5. Design

Как обернуть старый APM API в TAP и безопасно обработать ошибки и продолжения?

<details>
<summary>Критерии ответа</summary>

Task.Factory.FromAsync(Begin/End) или TCS с SetException/SetResult и RunContinuationsAsynchronously, ровно один EndRead, lifetime и отмена отдельно. Не обещать отмены если legacy API её не поддерживает.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/interop-with-other-asynchronous-patterns-and-types)
- [https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread)
- [https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/)
- [https://devblogs.microsoft.com/dotnet/how-async-await-really-works/](https://devblogs.microsoft.com/dotnet/how-async-await-really-works/)

---

[← Назад](async-production-capstone.md) · [Русский](async-before-await.md) · [English](en/async-before-await.md)
