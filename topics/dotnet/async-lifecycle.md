# Жизненный цикл async/await

[Русский](async-lifecycle.md) · [English](en/async-lifecycle.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/async-lifecycle)

От вызова C#-метода до сетевого события и продолжения.

## Определение

async/await — способ компоновать незавершённые операции без обязательной блокировки вызывающего потока. Он сам не создаёт параллелизм и не ускоряет PostgreSQL. При готовой операции await может не приостанавливать метод.

## Механизм: от языка и runtime до ОС

1. Roslyn преобразует тело async-метода в state machine с MoveNext, awaiter и сохраняемым состоянием.
2. Метод выполняется на вызывающем потоке до await, который видит незавершённую операцию.
3. Continuation регистрируется; worker больше не обязан обслуживать именно это ожидание. Сокет обрабатывается .NET и ядром ОС.
4. После готовности I/O продолжение выполняет декодирование и материализацию на CPU; поток и ядро могут отличаться от исходных.

## Ресурсы

- **Потоки:** 0 выделенных заблокированных worker-потоков на одно корректное незавершённое асинхронное ожидание.
- **CPU:** Нужен до ожидания и при обработке результата; во время ожидания ядро может работать над другим потоком.
- **Память:** Состояние операции, continuation, сетевые буферы; точный объём зависит от пути и реализации.

## Ограничения и риски

- Нельзя считать, что каждый await переключает поток или немедленно выделяет отдельную Task.
- Асинхронное API не отменяет ограничений пула соединений, объёма данных и пропускной способности БД.

## Вопросы для проверки

- [Q-001: Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов?](../../questions/dotnet/Q-001-async-io-scalability.md)
- [Q-003: Что означает аббревиатура I/O и какой вид I/O происходит при обращении к PostgreSQL?](../../questions/dotnet/Q-003-what-is-io.md)
- [Q-004: Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата?](../../questions/dotnet/Q-004-async-postgres-pipeline.md)
- [Q-005: PostgreSQL выполняет SQL 5 секунд. Что делает ядро CPU нашего .NET-сервера при await ToListAsync()?](../../questions/dotnet/Q-005-cpu-during-io.md)
- [Q-012: Запускает ли вызов async Task-метода новый поток или начинает работу синхронно?](../../questions/dotnet/Q-012-async-starts-synchronously.md)
- [Q-013: Всегда ли await приостанавливает метод, выделяет worker или переключает поток?](../../questions/dotnet/Q-013-completed-await-and-scheduling.md)

## Закрепление на коде

- [Q-024: Какой вывод и почему? async-метод содержит await уже завершённой Task.](../../questions/dotnet/Q-024-completed-await-output.md)
- [Q-025: Какой вывод и почему? Метод ожидает незавершённую TaskCompletionSource.](../../questions/dotnet/Q-025-incomplete-await-output.md)

## Первоисточники

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)
- [https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)

---

[Русский](async-lifecycle.md) · [English](en/async-lifecycle.md)

[Главная](../../README.md) · [Все темы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/lesson/async-lifecycle)
