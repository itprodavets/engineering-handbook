# Q-042 — Interlocked.Increment

[Русский](./Q-042-interlocked-increment-ref.md) · [English](en/Q-042-interlocked-increment-ref.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-042) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Следующий →](Q-043-check-then-act-stock-negative.md)

## Вопрос

Что гарантирует Interlocked.Increment(ref int) и почему ref не связан со ссылочной природой Counter?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int counter = 0;
Interlocked.Increment(ref counter);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-042.cs
```

[Q-042.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-042.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

`Interlocked.Increment(ref value)` — атомарная операция read-modify-write над одной адресуемой переменной `int`, возвращающая новое значение. `ref` передаёт саму переменную независимо от того, является ли содержащий её объект ссылочным типом. Десять потоков по 1000 инкрементов дают 10000 при старте с нуля, отсутствии других записей и без значимого переполнения. Операция предоставляет гарантии упорядочивания памяти, но не защищает другие поля или отдельный check-then-act. Это не C# `lock`/`Monitor` для целого блока.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)

---

[Русский](./Q-042-interlocked-increment-ref.md) · [English](en/Q-042-interlocked-increment-ref.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-042) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Следующий →](Q-043-check-then-act-stock-negative.md)
