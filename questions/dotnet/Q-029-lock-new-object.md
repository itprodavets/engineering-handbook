# Q-029 — Wrong lock object

[Русский](./Q-029-lock-new-object.md) · [English](en/Q-029-lock-new-object.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-029) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-028-lost-update-race.md) · [Следующий →](Q-030-cancellation-after-start.md)

## Вопрос

Защищает ли lock(new object()) переменную counter от гонки?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int counter = 0;
await Task.WhenAll(
    Enumerable.Range(0, 10_000).Select(_ =>
        Task.Run(() =>
        {
            lock (new object())
                counter++;
        })));
Console.WriteLine(counter);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-029.cs
```

[Q-029.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-029.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Каждая задача создаёт свой объект блокировки. Общей взаимной блокировки нет; для защиты нужен один общий lock-объект или Interlocked.Increment.

</details>

### Почему это работает

Roslyn lock → Monitor for object; по одной уникальной синхронизации на вызов.

### Риск или ошибка

Race condition из-за отсутствия общего объекта синхронизации. Фактическое число heap allocations зависит от JIT-оптимизаций и требует измерения.

### Что гарантировано

Нет общей блокировки; численный результат недетерминирован.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

---

[Русский](./Q-029-lock-new-object.md) · [English](en/Q-029-lock-new-object.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-029) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-028-lost-update-race.md) · [Следующий →](Q-030-cancellation-after-start.md)
