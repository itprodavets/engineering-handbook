# ValueTask<T> и стоимость ожидания

[Русский](valuetask.md) · [English](en/valuetask.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/valuetask)

Точная область применения без правил вроде «всегда быстрее».

## Определение

ValueTask<T> — value type, способный описать синхронно готовый результат, Task<T> или IValueTaskSource<T>. Он может сократить аллокации при часто синхронно завершающихся операциях, но добавляет ограничения и усложняет использование.

## Механизм: от языка и runtime до ОС

1. Если результат уже готов, ValueTask<T> может хранить его без отдельного Task<T>.
2. Если результат ожидается, ValueTask<T> может оборачивать Task или управляемый повторно используемый источник.
3. IValueTaskSource<T> может поддерживать только одно получение результата; двойной await не всегда корректен.
4. Для многих операций Task<T> проще: сравнивать нужно на реальных профилях аллокаций.

## Ресурсы

- **Память:** ValueTask — struct, но обёрнутый источник или Task всё ещё может требовать heap-память.
- **CPU:** Большой struct и дополнительные состояния могут повысить стоимость передачи; нет общей гарантии ускорения.

## Ограничения и риски

- Не выполнять повторный await, AsTask или сохранение экземпляра без учёта контракта источника.

## Вопросы для проверки

- [Q-019: Почему ValueTask<T> нельзя всегда await-ить дважды и всегда ли он экономит память?](../../questions/dotnet/Q-019-valuetask-consumption.md)

## Закрепление на коде

—

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2012)

---

[Русский](valuetask.md) · [English](en/valuetask.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/valuetask)
