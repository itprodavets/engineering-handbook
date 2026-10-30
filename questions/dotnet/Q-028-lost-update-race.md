# Q-028 — Lost update

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../computer-science/concurrency/memory-model.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-027-whenall-exceptions-count.md) · [Следующий →](Q-029-lock-new-object.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Lost update

## Вопрос (RU)

Всегда ли итог counter равен 10 000? Почему?

## Question (EN)

Is counter always 10,000? Why or why not?

## Code challenge / Фрагмент кода

```csharp
int counter = 0;
await Task.WhenAll(
    Enumerable.Range(0, 10_000)
        .Select(_ => Task.Run(() => counter++)));
Console.WriteLine(counter);
```

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-028.cs](../../labs/dotnet/Q-028.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-028.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-028`. The workflow reports stdout in Job Summary.

**Expected / classification:** Неопределённый итог: может быть 10 000 или меньше..

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

counter++ не атомарен: параллельные workers могут потерять обновления. Исправление — Interlocked.Increment(ref counter) либо корректная синхронизация.

### EN — concise interview answer

The result may be 10,000 or lower. Incrementing is not atomic, and competing workers can overwrite one another. Use Interlocked.Increment.

</details>

## Why / Внутренний механизм

Shared heap/closure; read-modify-write; OS scheduling; memory model.

**Risk / ошибка:** Race condition и потерянные инкременты. Число потоков не равно числу Task.

**Guarantee / недетерминированность:** Нет гарантии точного итогового значения без синхронизации.

**Source:** https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../computer-science/concurrency/memory-model.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../computer-science/concurrency/memory-model.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-027-whenall-exceptions-count.md) · [Следующий →](Q-029-lock-new-object.md)
