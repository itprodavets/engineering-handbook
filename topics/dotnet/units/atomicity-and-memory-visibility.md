# volatile, Interlocked и атомарный RMW

[Русский](atomicity-and-memory-visibility.md) · [English](en/atomicity-and-memory-visibility.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/atomicity-and-memory-visibility)

> Различать атомарность одного действия, acquire/release и операции с ref.

## Определение

volatile в C# придаёт volatile-чтению acquire, а volatile-записи release семантику, но не делает ++ атомарным. Interlocked.Increment(ref int) изменяет единственную переменную атомарно, без захвата C# Monitor. ref адресует саму переменную int, а не ссылочный тип.

## Внутренний механизм

1. Обычный ++ логически состоит из read/compute/write; два потока могут записать один и тот же новый результат.
2. Volatile read/write обеспечивают частичное упорядочивание (acquire/release) и не устраняют interleaving между чтением и записью.
3. Interlocked.Increment(ref int) выполняет неделимый read-modify-write над адресуемым значением; два завершённых ++ из нуля дают 2.
4. Типично CLR/JIT использует атомарные инструкции CPU, но конкретная инструкция и затраты определяются платформой и конкуренцией.
5. Atomic RMW не защищает отдельную связанную проверку, другие поля или транзакцию вне памяти; эти случаи требуют отдельного алгоритма.

## Последовательное объяснение

### Atomicity, Visibility и Ordering

Atomicity: отдельная операция неделима. Visibility: наблюдаемость записей между потоками при корректной синхронизации. Ordering: разрешённые переупорядочивания compiler/JIT/CPU. Это разные свойства; acquire/release не эквивалентны atomic RMW. Гарантии C# следует отличать от поведения конкретного процессора.

### Что гарантирует volatile

В C# volatile-чтение имеет acquire-семантику; volatile-запись — release. Это ограничивает определённые перемещения memory accesses через операции. Это НЕ полная глобальная последовательность всех обращений и НЕ атомарность выражения Value++. Даже volatile int может потерять обновление при двух инкрементах.

```csharp
sealed class Counter { public volatile int Value; }
// Value++ still reads, computes and writes separately
```

### Как ref передаёт исходную переменную

Сигнатура Interlocked.Increment(ref int location) принимает ссылку на саму переменную int. Например int counter=0; Interlocked.Increment(ref counter) изменяет локальную переменную counter. Не имеет значения, находится ли int в классе, массиве или локальной переменной (при соблюдении правил ref). Механизм обычно использует атомарную инструкцию CPU, а не Monitor.Enter/Exit.

```csharp
int counter=0;
int updated=Interlocked.Increment(ref counter);
// updated=1; counter=1
```

### Чего Interlocked не гарантирует

Атомарный инкремент одного счётчика не создаёт критическую секцию для остальных операций. Если требуется проверить остаток и уменьшить его как одну транзакцию, необходим CAS-loop или lock. Если кроме счётчика изменяется ещё одно поле, атомарность отдельного int не делает общий инвариант корректным.


## Потребляемые ресурсы

Когерентность кэшей и конкуренция за общую cache line. Atomic RMW может стоить дороже обычной записи; это не Monitor lock и не гарантия отсутствия ожидания CPU.

## Ошибки и ограничения

volatile не делает counter++ атомарным, не устанавливает глобальный total order и не гарантирует, что volatile-чтение всегда вернёт последнее по реальному времени значение. ref работает и с value-type int; не путай с тем, что Counter — class.

## Пример

```csharp
int counter = 0;
Interlocked.Increment(ref counter); // atomically counter=1
```

## Запускаемые эксперименты

- [Q-042.cs](../../../labs/dotnet/Q-042.cs) — `dotnet run --file labs/dotnet/Q-042.cs`

## Вопросы для закрепления

- [Q-021: Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?](../../../questions/dotnet/Q-021-volatile-vs-interlocked.md)
- [Q-028: Всегда ли итог counter равен 10 000? Почему?](../../../questions/dotnet/Q-028-lost-update-race.md)
- [Q-041: Почему volatile int Value не делает Value++ атомарным и что реально гарантирует volatile в C#?](../../../questions/dotnet/Q-041-volatile-does-not-make-plus-plus-atomic.md)
- [Q-042: Что гарантирует Interlocked.Increment(ref int) и почему ref не связан со ссылочной природой Counter?](../../../questions/dotnet/Q-042-interlocked-increment-ref.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Различи atomicity, visibility и ordering. Что значит acquire/release для volatile?

<details>
<summary>Критерии ответа</summary>

Три независимых свойства. C# volatile read acquire, write release; нет глобального total order и нет атомарного ++.

</details>

### 2. Explain

Объясни почему два volatile Value++ всё равно могут дать результат 1.

<details>
<summary>Критерии ответа</summary>

Оба читают 0; каждый вычисляет 1; оба пишут 1. volatile не объединяет операции.

</details>

### 3. Predict

Два успешных Interlocked.Increment(ref counter) из counter=0: что выводит чтение после WhenAll?

<details>
<summary>Критерии ответа</summary>

2; каждый атомарный RMW изменяет одно значение, ref указывает на исходную переменную int.

</details>

### 4. Diagnose

Под нагрузкой volatile-флаг работает, но общий счётчик теряет инкременты. Какие возможны причины и тесты?

<details>
<summary>Критерии ответа</summary>

RMW не атомарен, заменить на Interlocked/lock, написать детерминированный gated test и проверить инвариант.

</details>

### 5. Design

Как выбрать volatile, Interlocked или lock для одного флага, счётчика и мульти-полевого инварианта?

<details>
<summary>Критерии ответа</summary>

Volatile — ограниченные сигналы/ordering с корректным протоколом; Interlocked — атомарное изменение одного состояния; lock — единая критическая секция над связанным состоянием.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read](https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read)

---

[← Назад](race-condition-vs-data-race.md) · [Далее →](compare-exchange-cas-loop.md) · [Русский](atomicity-and-memory-visibility.md) · [English](en/atomicity-and-memory-visibility.md)
