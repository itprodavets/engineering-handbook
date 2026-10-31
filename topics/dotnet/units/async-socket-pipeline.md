# От PostgreSQL до epoll/IOCP и continuation

[Русский](async-socket-pipeline.md) · [English](en/async-socket-pipeline.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/async-socket-pipeline)

> Проследить реальную цепочку SQL, сокета, ядра ОС и возвращения в C#.

## Определение

Npgsql отправляет запрос по сокету. При нехватке данных асинхронный receive ждёт готовности/завершения I/O с помощью механизмов runtime и ОС, а не одного заблокированного worker на запрос.

## Внутренний механизм

1. EF Core преобразует LINQ в команду; Npgsql получает соединение, формирует протокол и отправляет байты.
2. На Linux сокетная готовность может отслеживаться через epoll; на Windows completion-ориентированный I/O использует IOCP.
3. Сетевой стек принимает данные; runtime организует продолжение чтения, а EF Core материализует строки.
4. Большой ответ чередует несколько чтений, CPU-обработку и ожидания; один await не обязательно соответствует одному network receive.

## Потребляемые ресурсы

Сокет/дескриптор, пул соединений, network buffers, managed objects, CPU при обработке ответа.

## Ошибки и ограничения

База может стать узким местом, несмотря на освобождённые workers. Нельзя утверждать «1000 запросов = 1000 соединений».

## Пример

```csharp
await using var connection = new NpgsqlConnection(connectionString);
await connection.OpenAsync(ct);
```

## Вопросы для закрепления

- [Q-001: Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов?](../../../questions/dotnet/Q-001-async-io-scalability.md)
- [Q-004: Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата?](../../../questions/dotnet/Q-004-async-postgres-pipeline.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Назад](async-state-machine.md) · [Русский](async-socket-pipeline.md) · [English](en/async-socket-pipeline.md)
