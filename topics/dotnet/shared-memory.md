# Разделяемая память и синхронизация

[Русский](shared-memory.md) · [English](en/shared-memory.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/shared-memory)

Гонки, атомарность, lock, Interlocked и SemaphoreSlim.

## Определение

Конкурентные Task могут менять один и тот же объект. Task.WhenAll лишь ждёт завершения, но не делает операции атомарными. Синхронизация защищает инвариант общих данных, а не просто «поток».

## Механизм: от C# до ОС

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

## Закрепление на коде

- [Q-028: Всегда ли итог counter равен 10 000? Почему?](../../questions/dotnet/Q-028-lost-update-race.md)
- [Q-029: Защищает ли lock(new object()) переменную counter от гонки?](../../questions/dotnet/Q-029-lock-new-object.md)
- [Q-034: Что напечатает second.IsCompleted после повторного WaitAsync без Release?](../../questions/dotnet/Q-034-semaphore-waitasync.md)
- [Q-035: Ждёт ли Parallel.ForEach завершения async-лямбд и какой вывод гарантирован?](../../questions/dotnet/Q-035-parallel-foreach-async-void.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)
- [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

---

[Русский](shared-memory.md) · [English](en/shared-memory.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/shared-memory)
