# CompareExchange, CAS-loop и инвариант stock ≥ 0

[Русский](compare-exchange-cas-loop.md) · [English](en/compare-exchange-cas-loop.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/compare-exchange-cas-loop)

> Понимать, что меняет CAS через ref, что возвращает previous и почему повторная попытка нужна при конкуренции.

## Определение

Compare-and-Swap / CompareExchange — атомарное сравнение значения в location с comparand и условная запись value; всегда возвращает старое значение location. CAS-loop повторяет чтение и попытку, когда значение изменилось, и может атомарно реализовать проверку остатка и уменьшение с соблюдением stock >= 0.

## Внутренний механизм

1. Interlocked.CompareExchange(ref stock, 0, 1) атомарно записывает 0 при stock==1 и возвращает предыдущее значение 1. Если stock==0, запись не происходит и возвращается 0.
2. ref указывает на саму переменную int, а не на то, что Counter — класс. current — независимая локальная копия; current-1 лишь вычисляет аргумент.
3. Отдельные Volatile.Read(stock)>0 и Interlocked.Decrement(stock) оставляют окно Check-Then-Act; два покупателя могут увидеть 1, затем оба уменьшить до -1.
4. Простой CAS(3→2) допускает только одного победителя; второй видит previous==2 и не должен считать покупку успешной.
5. CAS-loop перечитывает stock после неудачи: если осталось >0, повторяет CAS со свежим expected; если 0, возвращает false.
6. Lock-free не равнозначно wait-free: отдельный поток может многократно проигрывать CAS, хотя система продолжает делать успехи.

## Последовательное объяснение

### ref и три аргумента CAS

Сигнатура int CompareExchange(ref int location, int value, int comparand). location — сама ячейка stock. value — новое значение; comparand — ожидаемое. Возвращается старое значение (даже при неуспехе). При stock=10, current=10: CompareExchange(ref stock,current-3,current) запишет 7; current останется 10; previous будет 10.

```csharp
int stock=10, current=10;
int previous=Interlocked.CompareExchange(ref stock,current-3,current);
// stock=7; current=10; previous=10
```

### Атомарная операция не означает атомарный алгоритм

Проверка Volatile.Read(ref stock)>0 и действие Interlocked.Decrement(ref stock) независимы. Оба покупателя могут получить true при stock=1, затем каждый атомарно уменьшает его: 1→0→-1. CAS делает сравнение ожидаемого и запись частью одной атомарной операции, не оставляя окна между ними.

```csharp
if (Volatile.Read(ref stock)>0)
    Interlocked.Decrement(ref stock); // unsafe check-then-act
```

### Один товар и два конкурирующих CAS

Из stock=1 только один поток способен выполнить CAS(1→0); победитель получает previous=1 и печатает Purchased. Второй видит 0, получает previous=0 и ничего не покупает. При stock=3 два CAS(3→2) тоже дают лишь один успешный переход: это недостаточно для двух независимых покупок.

### Разбор CAS-loop: stock=3 и два покупателя

Оба считывают current=3. T1 выполняет CAS(3→2): stock становится 2, previous=3, успех. T2 пытается CAS(3→2), получает previous=2, не меняет stock, previous!=current. Он возвращается к началу while, читает current=2, CAS(2→1) успешно записывает 1, возвращает previous=2. Итого две покупки, stock=1. Если stock=1 и покупателей 5, только один вернёт true, остальные при следующем чтении stock=0 вернут false.

### Точка линеаризации и границы алгоритма

Успешный CAS — атомарная точка, в которую операция покупки фиксирует уменьшение остатка; возврат false при current<=0 подтверждает отсутствие товара при соответствующем чтении. Это линейризуемый in-memory счётчик с предположением, что все конкурирующие изменения идут через согласованный протокол и никто не увеличивает stock в анализируемом сценарии. Для настоящего склада требуются транзакции БД, идемпотентность и семантика резервирования.


## Потребляемые ресурсы

Атомарные инструкции CPU / runtime, когерентность кэшей, стоимость contention/retries. Временная остановка одного worker не обязана останавливать прогресс других участников CAS-loop.

## Ошибки и ограничения

CompareExchange не возвращает newValue; он возвращает значение ДО операции. Простой CAS без цикла не покрывает произвольный остаток. Даже корректный in-memory CAS не делает продажу и запись в БД одной транзакцией. Нельзя считать TryBuy wait-free.

## Пример

```csharp
static bool TryBuy(ref int stock)
{
    while (true)
    {
        int current = Volatile.Read(ref stock);
        if (current <= 0) return false;
        int previous = Interlocked.CompareExchange(ref stock, current - 1, current);
        if (previous == current) return true;
    }
}
```

## Запускаемые эксперименты

- [Q-043.cs](../../../labs/dotnet/Q-043.cs) — `dotnet run --file labs/dotnet/Q-043.cs`
- [Q-044.cs](../../../labs/dotnet/Q-044.cs) — `dotnet run --file labs/dotnet/Q-044.cs`
- [Q-045.cs](../../../labs/dotnet/Q-045.cs) — `dotnet run --file labs/dotnet/Q-045.cs`
- [Q-046.cs](../../../labs/dotnet/Q-046.cs) — `dotnet run --file labs/dotnet/Q-046.cs`
- [Q-047.cs](../../../labs/dotnet/Q-047.cs) — `dotnet run --file labs/dotnet/Q-047.cs`

## Вопросы для закрепления

- [Q-043: Может ли stock стать -1 при Volatile.Read(stock)>0 и последующем Interlocked.Decrement, если stock=1?](../../../questions/dotnet/Q-043-check-then-act-stock-negative.md)
- [Q-044: При stock=1 что вернёт CompareExchange(ref stock,0,1) и чему станет равен stock?](../../../questions/dotnet/Q-044-compareexchange-returns-prior.md)
- [Q-045: Могут ли оба потока успешно выполнить CompareExchange(ref stock,0,1) при stock=1?](../../../questions/dotnet/Q-045-two-buyers-single-item-cas.md)
- [Q-046: Если stock=3, два потока выполняют CompareExchange(ref stock,2,3). Сколько покупок успешны и что возвращают оба CAS?](../../../questions/dotnet/Q-046-two-buyers-stock-three-single-cas.md)
- [Q-047: Как CAS-loop ведёт себя при stock=3 и двух покупателях, а затем stock=1 и пяти покупателях?](../../../questions/dotnet/Q-047-cas-loop-five-buyers.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Перечисли аргументы CompareExchange и объясни, что возвращается.

<details>
<summary>Критерии ответа</summary>

ref location, value(new), comparand(expected). Возвращается прежнее значение location, а не значение после операции.

</details>

### 2. Explain

Почему CAS безопаснее проверки volatile + Interlocked.Decrement при stock=1?

<details>
<summary>Критерии ответа</summary>

CAS объединяет проверку и изменение, для двух потоков только один переход 1→0 возможен. Раздельный check-then-act допускает оба декремента.

</details>

### 3. Predict

Два потока прочитали current=3. Первый CAS(3→2) успешен, второй нет. Какие current, previous, stock видит второй и что затем происходит?

<details>
<summary>Критерии ответа</summary>

При неуспехе current=3, previous=2, stock=2; следующий цикл читает current=2, CAS(2→1) возвращает previous=2, stock=1.

</details>

### 4. Diagnose

Почему некорректно считать, что множество повторов CAS означает deadlock или wait-free?

<details>
<summary>Критерии ответа</summary>

Другие потоки могут продвигаться, пока конкретный проигрывает; алгоритм lock-free, но без гарантии для каждого потока. Измерять contention/retries/backoff.

</details>

### 5. Design

Опиши TryBuy для stock>=0 без lock, учитывая пять покупателей при stock=1.

<details>
<summary>Критерии ответа</summary>

Volatile.Read, reject at <=0; CAS(old→old-1), success if previous==old; else retry with new current. 1 true, 4 false, stock=0. Не считать это DB-транзакцией.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read](https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read)
- [https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives](https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives)

---

[← Назад](atomicity-and-memory-visibility.md) · [Далее →](mutual-exclusion-and-semaphores.md) · [Русский](compare-exchange-cas-loop.md) · [English](en/compare-exchange-cas-loop.md)
