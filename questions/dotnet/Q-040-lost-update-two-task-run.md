# Q-040 — Lost Update

[Русский](./Q-040-lost-update-two-task-run.md) · [English](en/Q-040-lost-update-two-task-run.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-040) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-039-race-condition-vs-data-race.md) · [Следующий →](Q-041-volatile-does-not-make-plus-plus-atomic.md)

## Вопрос

Какие значения возможны после двух Task.Run(() => state.Value++) и await Task.WhenAll, если Value=0?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
var state = new Counter();
await Task.WhenAll(Task.Run(() => state.Value++), Task.Run(() => state.Value++));
Console.WriteLine(state.Value);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-040.cs
```

[Q-040.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-040.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

1 или 2. ++ не атомарен: оба потока могут прочитать 0 и записать 1. Task.WhenAll ждёт завершения, но не защищает общую память. Пример лаборатории принудительно устраивает interleaving с потерянным обновлением.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)

---

[Русский](./Q-040-lost-update-two-task-run.md) · [English](en/Q-040-lost-update-two-task-run.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-040) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-039-race-condition-vs-data-race.md) · [Следующий →](Q-041-volatile-does-not-make-plus-plus-atomic.md)
