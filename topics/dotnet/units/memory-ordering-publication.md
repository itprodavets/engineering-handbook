# Memory Model: видимость, ordering и safe publication

[Русский](memory-ordering-publication.md) · [English](en/memory-ordering-publication.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/memory-ordering-publication)

> Проверять гарантии публикации данных через release/acquire, JIT, поток ОС и happens-before.

## Определение

Атомарная запись флага ещё не означает безопасную публикацию соседних данных. Правильный протокол: сначала data=42, потом Volatile.Write(ready,1) (release); Consumer читает Volatile.Read(ready) (acquire), и только увидев 1 обращается к data. Для этого протокола, при отсутствии других записей, результат равен 42. Перестановка публикации перед записью данных допускает 0.

## Внутренний механизм

1. Producer записывает данные обычным способом до release-публикации ready=1. Acquire-чтение флага связывает это с последующим чтением data.
2. Если сначала записать ready=1, Consumer может прочитать data=0 до поздней записи data=42; volatile не исправляет неправильный программный порядок.
3. Без Volatile.Read обычное чтение флага в цикле не даёт протокола синхронизации; JIT/CPU могут применять оптимизации, в том числе hoisting чтения.
4. Thread.Yield влияет на планировщик ОС, но не является acquire/read fence и не создаёт happens-before между памятью разных потоков.
5. Наличие volatile-протокола не гарантирует fairness, планирование, deadline или ограниченное время активного ожидания; для production часто лучше Task, Channel или другой примитив.

## Последовательное объяснение

### Атомарность ≠ видимость ≠ порядок

Чтение и запись int атомарны в рамках гарантированных типов, но это не доказывает, что две разные записи наблюдаются в нужном порядке. Atomicity отвечает за неделимость одного доступа, Visibility — за видимость записей после синхронизации, Ordering — за допустимые перестановки. JIT/CPU/ОС выполняют разные роли. Для доказательства используй отношения между конкретными операциями, а не фразу «кэш обновится».

### Правильная публикация: data до ready

Producer выполняет `data=42`, затем `Volatile.Write(ref ready,1)` с release. Consumer повторяет `Volatile.Read(ref ready)` с acquire; после наблюдения 1 чтение data получает 42, если никто не изменяет data. Это иллюстрация message passing, аналогичная примеру из спецификации C#. Само чтение ready может какое-то время возвращать 0 — нет ограничения ожидания.

```csharp
data = 42;
Volatile.Write(ref ready, 1);
// Consumer: if (Volatile.Read(ref ready) == 1) Console.WriteLine(data); // 42
```

### Публикация до данных допускает 0

Если `Volatile.Write(ref ready,1)` стоит ДО `data=42`, release не распространяется на последующую запись data. Consumer может заметить 1, выйти из цикла и прочитать старый 0. Возможный interleaving: publish ready=1 → consumer read ready=1 → read data=0 → producer data=42. Лаборатория Q-049 детерминированно фиксирует этот порядок через отдельный тестовый gate.

```csharp
Volatile.Write(ref ready, 1);
data = 42; // too late for publication
```

### Обычное чтение в цикле и JIT

Без volatile цикл `while (ready==0) { }` не содержит гарантированно синхронизированного чтения. JIT может в определённых условиях оптимизировать повторное чтение (например, вынести его из цикла), поэтому завершение не гарантировано. Конкретная оптимизация зависит от версии/архитектуры; не утверждай, что она обязана случиться. Не демонстрируй это бесконечным нестабильным тестом в CI.

```csharp
while (ready == 0) { } // no synchronization contract
```

### Thread.Yield не делает memory barrier

`Thread.Yield()` предлагает ОС уступить исполнение готовому потоку. Он не делает чтение ready volatile и не является доказательством visibility. Даже если loop с Yield на определённой реализации перечитывает значение и обычно завершается, это не означает гарантии Memory Model. Его результат bool сообщает лишь о факте переключения, а не о видимости данных.

```csharp
while (ready == 0) { Thread.Yield(); } // not a synchronization fix
```


## Потребляемые ресурсы

Атомарные чтения/записи, JIT/CPU переупорядочивание, CPU-время busy-wait, кэш-когерентность, планировщик ОС.

## Ошибки и ограничения

Volatile.Read не обещает видеть хронологически последнюю запись на любом ядре; Thread.Yield не является memory synchronization. Опасный цикл без volatile не запускается как тест на бесконечное ожидание. Публикация объекта требует анализа всех последующих изменений.

## Пример

```csharp
int data = 0, ready = 0;
Task producer = Task.Run(() => { data = 42; Volatile.Write(ref ready, 1); });
Task consumer = Task.Run(() => { while (Volatile.Read(ref ready) == 0) Thread.Yield(); Console.WriteLine(data); });
await Task.WhenAll(producer, consumer); // prints 42
```

## Запускаемые эксперименты

- [Q-048.cs](../../../labs/dotnet/Q-048.cs) — `dotnet run --file labs/dotnet/Q-048.cs`
- [Q-049.cs](../../../labs/dotnet/Q-049.cs) — `dotnet run --file labs/dotnet/Q-049.cs`

## Вопросы для закрепления

- [Q-048: Почему data=42 перед Volatile.Write(ready,1) и Volatile.Read(ready) позволяет вывести 42?](../../../questions/dotnet/Q-048-safe-publication-acquire-release.md)
- [Q-049: Может ли Consumer увидеть data=0, если Producer сначала Volatile.Write(ready,1), потом data=42?](../../../questions/dotnet/Q-049-release-before-data-allows-zero.md)
- [Q-050: Гарантированно ли завершится while(ready==0) без volatile после записи другого потока?](../../../questions/dotnet/Q-050-nonvolatile-loop-jit-hoisting.md)
- [Q-051: Почему Thread.Yield() в цикле с обычным чтением ready не заменяет Volatile.Read?](../../../questions/dotnet/Q-051-thread-yield-is-not-memory-fence.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Определи atomicity, visibility и ordering. Чем acquire отличается от release?

<details>
<summary>Критерии ответа</summary>

Atomicity — неделимость; visibility — наблюдаемость записей; ordering — разрешённый порядок. Acquire для последующих чтений, release для предшествующих записей.

</details>

### 2. Explain

Объясни, почему data=42 перед Volatile.Write(ready,1), а Consumer читает Volatile.Read(ready).

<details>
<summary>Критерии ответа</summary>

Корректный протокол публикации; после наблюдения 1 видны предшествующие записи. Не обещать ограниченное время ожидания.

</details>

### 3. Predict

Может ли Consumer вывести 0, если Producer сначала публикует ready=1, а потом пишет data=42?

<details>
<summary>Критерии ответа</summary>

Да. Consumer читает 1 и data=0 до поздней записи. Это допустимый interleaving.

</details>

### 4. Diagnose

Может ли `Thread.Yield()` гарантировать завершение цикла с обычным `while(ready==0)`? Что проверишь?

<details>
<summary>Критерии ответа</summary>

Нет. OS scheduling не заменяет memory synchronization. Изучить JIT, optimized code, тип поля, volatile/lock, наличие CPU starvation.

</details>

### 5. Design

Предложи без busy-wait передачу значения от Producer к Consumer для production.

<details>
<summary>Критерии ответа</summary>

Лучше `Task<T>` и await, `Channel<T>`, SemaphoreSlim или другие примитивы с корректным протоколом; учитывать отмену/ошибки/ресурсы.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read](https://learn.microsoft.com/en-us/dotnet/api/system.threading.volatile.read)
- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0)

---

[← Назад](atomicity-and-memory-visibility.md) · [Далее →](compare-exchange-cas-loop.md) · [Русский](memory-ordering-publication.md) · [English](en/memory-ordering-publication.md)
