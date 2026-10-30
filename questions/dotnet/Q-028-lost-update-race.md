# Q-028 — Lost update

[Русский](./Q-028-lost-update-race.md) · [English](en/Q-028-lost-update-race.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-028) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-027-whenall-exceptions-count.md) · [Следующий →](Q-029-lock-new-object.md)

## Вопрос

Всегда ли итог counter равен 10 000? Почему?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int counter = 0;
await Task.WhenAll(
    Enumerable.Range(0, 10_000)
        .Select(_ => Task.Run(() => counter++)));
Console.WriteLine(counter);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-028.cs
```

[Q-028.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-028.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

counter++ не атомарен: параллельные workers могут потерять обновления. Исправление — Interlocked.Increment(ref counter) либо корректная синхронизация.

</details>

### Почему это работает

Shared heap/closure; read-modify-write; OS scheduling; memory model.

### Риск или ошибка

Race condition и потерянные инкременты. Число потоков не равно числу Task.

### Что гарантировано

Нет гарантии точного итогового значения без синхронизации.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)

---

[Русский](./Q-028-lost-update-race.md) · [English](en/Q-028-lost-update-race.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-028) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-027-whenall-exceptions-count.md) · [Следующий →](Q-029-lock-new-object.md)
