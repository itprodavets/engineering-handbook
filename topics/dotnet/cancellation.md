# Отмена асинхронных операций

[Русский](cancellation.md) · [English](en/cancellation.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/cancellation)

Что реально делает CancellationToken и чего он не делает.

## Определение

CancellationToken — кооперативный сигнал. Он не является Thread.Abort: работающий делегат должен наблюдать отмену, а операции I/O должны её поддерживать.

## Механизм: от языка и runtime до ОС

1. Task.Run с уже отменённым token может не начать выполнение делегата.
2. После начала делегата token не прерывает инструкции CPU принудительно.
3. ThrowIfCancellationRequested или API с CancellationToken завершают операцию, если это поддерживается.
4. Отмена не обязательно откатывает действие, уже выполненное внешней системой.

## Ресурсы

- **CPU:** Код до проверки token продолжает использовать CPU при выполнении вычислений.
- **I/O:** Отмена сетевого вызова зависит от драйвера и этапа операции.

## Ограничения и риски

- Отмена HTTP-запроса не гарантирует, что PostgreSQL прекратит уже выполняющуюся транзакцию.
- Не путать OperationCanceledException с системной ошибкой без анализа причин.

## Вопросы для проверки

- [Q-018: Прерывает ли CancellationToken выполняющуюся Task.Run и автоматически ли попадает в делегат?](../../questions/dotnet/Q-018-cancellationtoken-taskrun.md)

## Закрепление на коде

- [Q-030: Выведет ли программа DONE, если отменить token после запуска делегата?](../../questions/dotnet/Q-030-cancellation-after-start.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads](https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads)

---

[Русский](cancellation.md) · [English](en/cancellation.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/cancellation)
