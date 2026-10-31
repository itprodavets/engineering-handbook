# I/O-bound и CPU-bound — точные определения

[Русский](io-vs-cpu-bound.md) · [English](en/io-vs-cpu-bound.md)

[Главная](../../../README.md) · [Модуль](../async-lifecycle.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/io-vs-cpu-bound)

> Различать вычисление, ожидание сети и физические ресурсы.

## Определение

I/O-bound — операция, задержка или пропускная способность которой определяется внешним вводом/выводом. CPU-bound ограничена скоростью исполнения инструкций. Вызов PostgreSQL включает как CPU-работу, так и сетевое ожидание.

## Внутренний механизм

1. До отправки SQL процессор выполняет код EF Core/Npgsql и сериализацию сетевого запроса.
2. При незавершённом асинхронном ожидании worker не закреплён за запросом; ОС может выполнять другие потоки.
3. После получения данных CPU снова нужен для чтения, декодирования, материализации объектов и ответа HTTP.
4. Async не делает PostgreSQL быстрее: пулы соединений, БД и объём результата остаются ограничениями.

## Потребляемые ресурсы

CPU-время до/после ожидания; буферы и сокет во время I/O; 0 специально заблокированных worker для корректного pending async-read.

## Ошибки и ограничения

Не считай Database I/O отдельным видом аппаратной работы: удалённый PostgreSQL обычно означает Network I/O на клиенте.

## Пример

```csharp
var orders = await db.Orders.AsNoTracking().ToListAsync(ct);
```

## Вопросы для закрепления

- [Q-003: Что означает аббревиатура I/O и какой вид I/O происходит при обращении к PostgreSQL?](../../../questions/dotnet/Q-003-what-is-io.md)
- [Q-005: PostgreSQL выполняет SQL 5 секунд. Что делает ядро CPU нашего .NET-сервера при await ToListAsync()?](../../../questions/dotnet/Q-005-cpu-during-io.md)

## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[Далее →](async-state-machine.md) · [Русский](io-vs-cpu-bound.md) · [English](en/io-vs-cpu-bound.md)
