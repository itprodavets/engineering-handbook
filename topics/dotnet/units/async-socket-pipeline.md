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

## Последовательное объяснение

### Граница EF Core, Npgsql и Socket

EF Core преобразует LINQ в SQL, Npgsql управляет протоколом PostgreSQL и соединением, а `Socket`/`NetworkStream` используют API ОС. Время SQL включает работу на сервере БД; клиентский .NET-процесс не выделяет для каждого удалённого запроса отдельный CPU или worker на всю задержку.

### Что происходит в ядре ОС

На Linux реализация асинхронных сокетов .NET может использовать event polling на основе `epoll`; на Windows для сокетного I/O применяется механизм IOCP. Эти механизмы различаются, но оба позволяют не держать отдельный заблокированный рабочий поток на каждом ожидающем чтении. Низкоуровневые I/O event threads у runtime возможны: «0 выделенных worker на ожидание» не означает «во всём процессе 0 потоков».

### Почему результат может требовать нескольких чтений

При получении сетевых пакетов ядро обновляет состояние сокета, runtime будит соответствующий механизм чтения, Npgsql декодирует сообщения и EF Core материализует записи. Большой результат может чередовать несколько событий I/O и CPU-обработку — `ToListAsync()` не означает «весь список создался в ядре ОС».

### Пул соединений, таймаут и backpressure

Если пул допускает меньше соединений, чем одновременно пришло HTTP-запросов, часть операций ждёт свободное соединение. Нельзя делать вывод о количестве активных SQL только по числу Task. Используй CancellationToken, connection timeout, ограничение конкурентности и наблюдение за количеством DB connections.


## Потребляемые ресурсы

Сокет/дескриптор, пул соединений, network buffers, managed objects, CPU при обработке ответа.

## Ошибки и ограничения

База может стать узким местом, несмотря на освобождённые workers. Нельзя утверждать «1000 запросов = 1000 соединений».

## Пример

```csharp
await using var connection = new NpgsqlConnection(connectionString);
await connection.OpenAsync(ct);
```

## Запускаемые эксперименты

- [03-socket-simulation.cs](../../../labs/dotnet/async-internals/03-socket-simulation.cs) — `dotnet run --file labs/dotnet/async-internals/03-socket-simulation.cs`

## Вопросы для закрепления

- [Q-001: Почему ToListAsync() масштабируется лучше, чем Task.Run(() => ToList()), при 1 000 одновременных HTTP-запросов?](../../../questions/dotnet/Q-001-async-io-scalability.md)
- [Q-004: Что происходит внутри .NET, ОС и CPU между отправкой асинхронного SQL-запроса и получением результата?](../../../questions/dotnet/Q-004-async-postgres-pipeline.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Назови обязанности EF Core, Npgsql, Socket API и ядра ОС.

<details>
<summary>Критерии ответа</summary>

EF Core формирует запрос/объекты, Npgsql — протокол и соединение, Socket/ОС — network bytes, не SQL-объекты.

</details>

### 2. Explain

Каким образом pending network read избегает отдельного заблокированного worker в Linux/Windows?

<details>
<summary>Критерии ответа</summary>

Linux epoll readiness или Windows IOCP completion; механизм runtime возвращает продолжение, CPU нужен для обработки и callbacks.

</details>

### 3. Predict

Если 1 000 HTTP-запросов ждут PostgreSQL, а пул соединений ограничен 100, будут ли одновременно выполняться все 1 000 SQL?

<details>
<summary>Критерии ответа</summary>

Нет, ограничение соединений и поведение приложения мешают; максимум 100 соединений этого пула, но число SQL может быть ниже.

</details>

### 4. Diagnose

p99 растёт, CPU клиента низкий, ThreadPool queue стабильна, DB pool wait увеличивается. Какой уровень системы вероятнее перегружен?

<details>
<summary>Критерии ответа</summary>

Пул соединений/БД, а не доказанное starvation. Проверить длительность SQL, pool occupancy, планы и сеть.

</details>

### 5. Design

Для тяжёлого API выбери: ToListAsync без ограничения, sync Task.Run или bounded async + pagination. Почему?

<details>
<summary>Критерии ответа</summary>

Ограниченный асинхронный I/O с пагинацией/проекцией, таймаутами и мониторингом, учитывая реальные пределы DB pool.

</details>


## Источники

- [https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth](https://learn.microsoft.com/en-us/dotnet/standard/async-in-depth)

---

[← Назад](async-state-machine.md) · [Далее →](async-memory-and-allocations.md) · [Русский](async-socket-pipeline.md) · [English](en/async-socket-pipeline.md)
