# Разделяемая память и синхронизация

[Русский](shared-memory.md) · [English](en/shared-memory.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/shared-memory)

Гонки, атомарность, lock, Interlocked и SemaphoreSlim.

## Определение

Конкурентные Task могут менять один и тот же объект. Task.WhenAll лишь ждёт завершения, но не делает операции атомарными. Синхронизация защищает инвариант общих данных, а не просто «поток».

## Механизм: от языка и runtime до ОС

1. counter++ состоит из чтения, вычисления и записи; две операции могут потерять одно обновление.
2. Interlocked.Increment выполняет атомарную модификацию одного значения; lock обеспечивает исключение в критической секции.
3. lock(new object()) создаёт разные мониторы для разных вызовов и не защищает общее состояние.
4. SemaphoreSlim.WaitAsync ожидает разрешение асинхронно, но не является автоматически рекурсивным mutex.

## Ресурсы

- **Общая память:** Ссылки на общие изменяемые объекты; доступы требуют согласованной синхронизации.
- **Синхронизация:** Мониторы, atomic RMW и/или асинхронные очереди ожидания.
- **CPU:** Конкуренция и повторные попытки могут тратить CPU; блокировки могут увеличивать задержки.

## Ограничения и риски

- volatile не делает counter++ атомарным.
- Порядок захвата lock и удержание разрешений могут вызвать deadlock или длительные ожидания.

## Вопросы для проверки

- [Q-020: Почему await запрещён в lock и чем отличается SemaphoreSlim.WaitAsync()?](../../questions/dotnet/Q-020-await-inside-lock.md)
- [Q-021: Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?](../../questions/dotnet/Q-021-volatile-vs-interlocked.md)
- [Q-039: Чем отличается Race Condition от Data Race и может ли логическая гонка возникнуть без data race?](../../questions/dotnet/Q-039-race-condition-vs-data-race.md)
- [Q-041: Почему volatile int Value не делает Value++ атомарным и что реально гарантирует volatile в C#?](../../questions/dotnet/Q-041-volatile-does-not-make-plus-plus-atomic.md)

## Закрепление на коде

- [Q-028: Всегда ли итог counter равен 10 000? Почему?](../../questions/dotnet/Q-028-lost-update-race.md)
- [Q-029: Защищает ли lock(new object()) переменную counter от гонки?](../../questions/dotnet/Q-029-lock-new-object.md)
- [Q-034: Что напечатает second.IsCompleted после повторного WaitAsync без Release?](../../questions/dotnet/Q-034-semaphore-waitasync.md)
- [Q-035: Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован?](../../questions/dotnet/Q-035-parallel-foreach-async-void.md)
- [Q-040: Какие значения возможны после двух Task.Run(() => state.Value++) и await Task.WhenAll, если Value=0?](../../questions/dotnet/Q-040-lost-update-two-task-run.md)
- [Q-042: Что гарантирует Interlocked.Increment(ref int) и почему ref не связан со ссылочной природой Counter?](../../questions/dotnet/Q-042-interlocked-increment-ref.md)
- [Q-043: Может ли stock стать -1 при Volatile.Read(stock)>0 и последующем Interlocked.Decrement, если stock=1?](../../questions/dotnet/Q-043-check-then-act-stock-negative.md)
- [Q-044: При stock=1 что вернёт CompareExchange(ref stock,0,1) и чему станет равен stock?](../../questions/dotnet/Q-044-compareexchange-returns-prior.md)
- [Q-045: Могут ли оба потока успешно выполнить CompareExchange(ref stock,0,1) при stock=1?](../../questions/dotnet/Q-045-two-buyers-single-item-cas.md)
- [Q-046: Если stock=3, два потока выполняют CompareExchange(ref stock,2,3). Сколько покупок успешны и что возвращают оба CAS?](../../questions/dotnet/Q-046-two-buyers-stock-three-single-cas.md)
- [Q-047: Как CAS-loop ведёт себя при stock=3 и двух покупателях, а затем stock=1 и пяти покупателях?](../../questions/dotnet/Q-047-cas-loop-five-buyers.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)
- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

---

[Русский](shared-memory.md) · [English](en/shared-memory.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/shared-memory)
