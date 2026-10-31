# Race Condition, Data Race и Lost Update

[Русский](race-condition-vs-data-race.md) · [English](en/race-condition-vs-data-race.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/race-condition-vs-data-race)

> Находить ошибку в инварианте, отличать гонку порядка событий от несинхронизированных обращений к памяти.

## Определение

Race condition — корректность зависит от относительного порядка конкурирующих событий, причём допустимый порядок нарушает инвариант. Data race — конфликтующие обращения к одной области памяти из разных потоков, где хотя бы одно — запись, без достаточной синхронизации. Логическая race condition возможна и без data race, например при двух атомарных операциях check и act.

## Внутренний механизм

1. Два делегата Task.Run могут обращаться к одному объекту Counter; класс — ссылочный тип, но Task.Run не захватывает monitor и не блокирует специально worker.
2. counter++ логически включает read, compute, write; два потока могут прочитать 0 до любого write, оба записать 1 и потерять инкремент.
3. Task.WhenAll ожидает завершения обеих задач и не синхронизирует модификацию поля; для двух инкрементов возможны 1 или 2.
4. Атомарные чтение и запись int не означают атомарность составной операции ++; и на одном ядре переключение выполнения может создать гонку.
5. Инвариант формулируется явно, например stock >= 0; проверяй, защищает ли синхронизация всю транзакцию, а не одну инструкцию.

## Последовательное объяснение

### Race Condition против Data Race

Гонка — более широкая характеристика некорректного алгоритма: результат зависит от порядка событий. Data race описывает несинхронизированные конфликтующие обращения к памяти; обычно требует пересмотра протокола синхронизации. Даже если каждое обращение через Interlocked и data race отсутствует, разделённые check и act могут нарушить бизнес-инвариант.

### Lost Update: два чтения 0

Порядок T1:read(0), T2:read(0), T1:write(1), T2:write(1) допустим для обычного counter++. Оба делегата завершатся, но counter=1, хотя ожидался 2. Это не значит, что Task.Run создаёт по одному отдельному потоку на каждую задачу.

### Почему возможен race на одном ядре

ОС может переключить поток после чтения и до записи. Race condition зависит от чередования событий, а не от одновременного исполнения машинных инструкций на двух физических CPU. Объект Task не содержит своего отдельного стека ОС по определению.

### Инвариант вместо угадывания результата

Для счётчика после двух успешных логических инкрементов ожидаем 2; для склада после покупки ожидаем stock >= 0. Анализируй возможные чередования и спрашивай, где именно гарантируется неделимость всей операции. Не путай значения, возвращаемые постфиксным ++, с финальным значением поля.


## Потребляемые ресурсы

Shared mutable state, cache lines и CPU-время; чем выше contention, тем выше цена синхронизации. Отсутствие физической параллельности не отменяет race.

## Ошибки и ограничения

Не путай состояние гонки с deadlock или с «Task блокирует поток». Не переносите автоматически C++ undefined-behavior правила на C#/.NET. Лаборатория Q-040 специально управляет порядком await, чтобы продемонстрировать Lost Update, а не моделирует конкретный планировщик.

## Пример

```csharp
var state = new Counter();
await Task.WhenAll(Task.Run(() => state.Value++), Task.Run(() => state.Value++));
Console.WriteLine(state.Value); // 1 or 2
// Counter has public int Value;
```

## Запускаемые эксперименты

- [Q-040.cs](../../../labs/dotnet/Q-040.cs) — `dotnet run --file labs/dotnet/Q-040.cs`

## Вопросы для закрепления

- [Q-039: Чем отличается Race Condition от Data Race и может ли логическая гонка возникнуть без data race?](../../../questions/dotnet/Q-039-race-condition-vs-data-race.md)
- [Q-040: Какие значения возможны после двух Task.Run(() => state.Value++) и await Task.WhenAll, если Value=0?](../../../questions/dotnet/Q-040-lost-update-two-task-run.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Чем Race Condition отличается от Data Race?

<details>
<summary>Критерии ответа</summary>

Race — сбой логического инварианта из-за порядка; data race — конфликтующие несинхронизированные обращения. Логическая гонка бывает без data race.

</details>

### 2. Explain

Объясни Lost Update для двух одновременных counter++ из 0.

<details>
<summary>Критерии ответа</summary>

Read/modify/write отдельно; оба читают 0, оба записывают 1.

</details>

### 3. Predict

Какие финальные значения возможны после двух Task.Run(() => state.Value++) и await Task.WhenAll?

<details>
<summary>Критерии ответа</summary>

1 либо 2. Task.WhenAll не защищает поле, но ждёт оба делегата.

</details>

### 4. Diagnose

Промежуточно пропадает обновление заказов под нагрузкой. Как доказать race?

<details>
<summary>Критерии ответа</summary>

Сформулировать инвариант, построить interleaving, воспроизвести через синхронизацию тестовых этапов, сделать трассировку и исключить другие причины.

</details>

### 5. Design

Как обеспечить ровно два корректных изменения общего счётчика?

<details>
<summary>Критерии ответа</summary>

Interlocked.Increment(ref value) для одного числа; lock для нескольких связанных условий/полей. Объяснить tradeoffs и отсутствие необходимости Task.Run для простого ++.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/expressions](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/expressions)
- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)
- [https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices](https://learn.microsoft.com/en-us/dotnet/standard/threading/managed-threading-best-practices)

---

[Далее →](atomicity-and-memory-visibility.md) · [Русский](race-condition-vs-data-race.md) · [English](en/race-condition-vs-data-race.md)
