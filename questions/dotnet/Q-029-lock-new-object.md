# Q-029 — Wrong lock object

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-028-lost-update-race.md) · [Следующий →](Q-030-cancellation-after-start.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Wrong lock object

## Вопрос (RU)

Защищает ли lock(new object()) переменную counter от гонки?

## Question (EN)

Does lock(new object()) protect counter from concurrent increments?

## Code challenge / Фрагмент кода

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

**Попробуй предсказать результат прежде, чем читать ответ.**

**Executable lab:** [Q-029.cs](../../labs/dotnet/Q-029.cs) · [Все лаборатории](../../labs/README.md)

```bash
dotnet run --file labs/dotnet/Q-029.cs
```

**Run remotely after publishing:** [GitHub Actions: Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) — choose `Q-029`. The workflow reports stdout in Job Summary.

**Expected / classification:** Нет; итог не гарантированно равен 10 000..

> В лаборатории код оформлен как отдельное запускаемое приложение; у некоторых заданий есть завершающий `Console.WriteLine()` или безопасный механизм дожидания continuations. Это явно отмечено в соответствующих исходниках.

<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Каждая задача создаёт свой объект блокировки. Общей взаимной блокировки нет; для защиты нужен один общий lock-объект или Interlocked.Increment.

### EN — concise interview answer

No. Each task locks a different freshly allocated object. Mutual exclusion requires a shared lock instance or an atomic increment.

</details>

## Why / Внутренний механизм

Roslyn lock → Monitor for object; по одной уникальной синхронизации на вызов.

**Risk / ошибка:** Race condition из-за отсутствия общего объекта синхронизации. Фактическое число heap allocations зависит от JIT-оптимизаций и требует измерения.

**Guarantee / недетерминированность:** Нет общей блокировки; численный результат недетерминирован.

**Source:** https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-028-lost-update-race.md) · [Следующий →](Q-030-cancellation-after-start.md)
