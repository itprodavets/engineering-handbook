# Memory model, atomicity and synchronization

[Главная / Home](../../README.md) · [Все вопросы / Questions](../../questions/dotnet/README.md) · [Тема / Topic](README.md) · [Запуск / Run](../../docs/execution.md)

## Race condition vs data race

**Race condition** — программа выдаёт неверный результат из-за неупорядоченного межпоточного взаимодействия. **Data race** — конкурентные несинхронизированные обращения к одной локации памяти, по крайней мере одно из которых является записью (точное формальное определение зависит от модели памяти).

`counter++` **not atomic**: читать → увеличить → записать. Два worker-потока могут оба увидеть старое значение.

```csharp
int counter = 0;
await Task.WhenAll(Enumerable.Range(0, 10_000)
    .Select(_ => Task.Run(() => counter++))); // race
```

**Исправление для одного счётчика:** `Interlocked.Increment(ref counter);`. Для составных инвариантов может требоваться `lock` или другой подход.

## volatile, Interlocked, lock

| Primitive | Guarantee | Does not guarantee |
|---|---|---|
| `volatile` | Специфические правила доступа и упорядочивания памяти | Атомарность `x++` или защита группы операций |
| `Interlocked.Increment` | Атомарный RMW для переменной | Атомарность произвольного набора полей |
| `lock(sync)` | Взаимное исключение для критической секции с **одним и тем же** `sync` | Защиту, если разные потоки используют разные объекты блокировки |

## Pitfalls

- `lock(new object())` внутри каждого worker не создаёт общий lock.
- `await` внутри `lock` запрещён компилятором; для async-семафора использовать `SemaphoreSlim.WaitAsync`, освобождая в `finally`.
- `false sharing` — разные переменные в одной cache line (часто 64 байта на современных CPU, но размер не гарантирован для всех архитектур) вызывают избыточную когерентность кэшей.

[Q-028](../../questions/dotnet/Q-028-lost-update-race.md) · [Q-029](../../questions/dotnet/Q-029-lock-new-object.md) · [Q-034](../../questions/dotnet/Q-034-semaphore-waitasync.md)

References: [Microsoft Interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked); [Internals reference](../../docs/internals-reference.md).

[Главная / Home](../../README.md) · [Все вопросы / Questions](../../questions/dotnet/README.md) · [Тема / Topic](README.md) · [Запуск / Run](../../docs/execution.md)
