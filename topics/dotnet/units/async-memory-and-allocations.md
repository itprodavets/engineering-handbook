# Память, state machine и стоимость асинхронности

[Русский](async-memory-and-allocations.md) · [English](en/async-memory-and-allocations.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-memory-and-allocations)

> Проверить реальную стоимость async без выдуманных размеров объектов.

## Определение

Синтаксис `async` не задаёт фиксированного числа объектов в heap. На готовом fast path может не быть новой Task-аллокации; при незавершённом await runtime должен сохранить состояние продолжения, что может потребовать heap-хранения.

## Внутренний механизм

1. Roslyn строит state machine и сохраняет нужные локальные переменные.
2. Для готовой операции компиляторская state machine может завершиться без перехода к continuation.
3. Для pending await runtime удерживает состояние до продолжения, и детали heap-размещения зависят от реализации.
4. Замеры требуют прогрева и одинакового окружения; текущий поток и весь процесс имеют разные метрики.

## Последовательное объяснение

### State machine ≠ heap-аллокация на каждый вызов

Наличие сгенерированного типа в IL означает необходимость хранить состояние, но не гарантирует отдельный heap-объект при каждом вызове. Реальное представление зависит от того, дошёл ли код до незавершённого await, и оптимизаций runtime. Например, `async Task` с исключительно синхронным завершением может повторно использовать завершённую Task.

### Правильный протокол эксперимента

Прогрей код и JIT; выдели baseline; повтори много раз на одинаковой версии .NET/архитектуре. `GC.GetAllocatedBytesForCurrentThread()` измеряет выделения managed памяти, произведённые текущим потоком, и не показывает все системные ресурсы, другие потоки и retained heap size. BenchmarkDotNet полезен для статистически обоснованного сравнения.

### Долгоживущие продолжения удерживают ссылки

Пока async-метод приостановлен, захваченные значения и `this` могут оставаться достижимыми; отмена и таймауты должны завершать операции и освобождать ресурсы. Важно отличать кратковременные аллокации от retained-memory leaks.

### Когда обсуждать ValueTask

ValueTask<T> может уменьшить аллокации при частом синхронном завершении, но увеличивает сложность потребления и не всегда улучшает производительность. Решение принимай после профилирования, а не по самому факту наличия await.


## Потребляемые ресурсы

Task/awaiter/captured locals/continuation; CPU JIT и GC; точные байты и время только по измерениям с указанными параметрами.

## Ошибки и ограничения

Сравнение двух вариантов на одном запуске может быть искажено JIT, GC, кэшированием, периодом прогрева и переключением потоков.

## Пример

```csharp
long before = GC.GetAllocatedBytesForCurrentThread();
// Execute a controlled hot path repeatedly here.
long bytes = GC.GetAllocatedBytesForCurrentThread() - before;
```

## Запускаемые эксперименты

- [04-allocations.cs](../../../labs/dotnet/async-internals/04-allocations.cs) — `dotnet run --file labs/dotnet/async-internals/04-allocations.cs`

## Вопросы для закрепления


## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Можно ли по ключевому слову async вычислить точное число heap-аллокаций?

<details>
<summary>Критерии ответа</summary>

Нет, зависит от ветки завершения, реализации, версии runtime и оптимизаций.

</details>

### 2. Explain

Что должно остаться достижимым после незавершённого await и почему?

<details>
<summary>Критерии ответа</summary>

Состояние метода, awaiter, нужные локальные данные и continuation до окончания операции.

</details>

### 3. Predict

Будет ли повторное await Task.CompletedTask создавать 1000 отдельных OS thread?

<details>
<summary>Критерии ответа</summary>

Нет, завершённая Task идёт по синхронному fast path; поток не создаётся оператором await.

</details>

### 4. Diagnose

Почему сравнение одного запуска по GC.GetAllocatedBytesForCurrentThread ненадёжно?

<details>
<summary>Критерии ответа</summary>

Требуются baseline, прогрев и повторы; текущий поток не равен всему процессу, GC/JIT шумят.

</details>

### 5. Design

Когда ValueTask<T> оправдан, а когда Task<T> лучше?

<details>
<summary>Критерии ответа</summary>

Measure sync-completion frequency, allocations and consumers; ValueTask often better for hot low-allocation API, Task simpler for composition.

</details>


## Источники

- [https://devblogs.microsoft.com/dotnet/how-async-await-really-works/](https://devblogs.microsoft.com/dotnet/how-async-await-really-works/)

---

[← Назад](async-socket-pipeline.md) · [Далее →](async-production-capstone.md) · [Русский](async-memory-and-allocations.md) · [English](en/async-memory-and-allocations.md)
