# Атомарность, volatile и Interlocked

[Русский](atomicity-and-memory-visibility.md) · [English](en/atomicity-and-memory-visibility.md)

[Главная](../../../README.md) · [Модуль](../shared-memory.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/atomicity-and-memory-visibility)

> Понимать read-modify-write и модель видимости памяти.

## Определение

counter++ — чтение, вычисление и запись, а не гарантированная атомарная операция. volatile регулирует некоторые правила доступа/упорядочивания, но не обеспечивает атомарный ++. Interlocked.Increment атомарно изменяет одну переменную.

## Внутренний механизм

1. Roslyn генерирует операции чтения и записи для ++; их общий порядок может перемешаться с другими потоками.
2. Два потока могут прочитать прежнее значение и записать одинаковый результат: потерянное обновление.
3. Interlocked осуществляет атомарный read-modify-write для одной локации памяти.
4. Для нескольких связанных полей нужна синхронизация инварианта, например общий lock.

## Потребляемые ресурсы

Shared memory и cache-coherence; атомарные инструкции могут создавать contention между ядрами.

## Ошибки и ограничения

volatile не решает гонку counter++; число успешно запущенных Task не определяет точное значение счётчика.

## Пример

```csharp
int counter = 0;
Interlocked.Increment(ref counter);
```

## Вопросы для закрепления

- [Q-021: Почему volatile counter++ небезопасен и чем Interlocked.Increment отличается от lock?](../../../questions/dotnet/Q-021-volatile-vs-interlocked.md)
- [Q-028: Всегда ли итог counter равен 10 000? Почему?](../../../questions/dotnet/Q-028-lost-update-race.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)

---

[Далее →](mutual-exclusion-and-semaphores.md) · [Русский](atomicity-and-memory-visibility.md) · [English](en/atomicity-and-memory-visibility.md)
