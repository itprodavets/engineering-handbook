# Q-044 — CompareExchange

[Русский](./Q-044-compareexchange-returns-prior.md) · [English](en/Q-044-compareexchange-returns-prior.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-044) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-043-check-then-act-stock-negative.md) · [Следующий →](Q-045-two-buyers-single-item-cas.md)

## Вопрос

При stock=1 что вернёт CompareExchange(ref stock,0,1) и чему станет равен stock?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int stock=1;
int previous=Interlocked.CompareExchange(ref stock,0,1);
Console.WriteLine($"{previous} {stock}");
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-044.cs
```

[Q-044.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-044.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Возвращает прежнее значение 1; одновременно атомарно записывает 0, поскольку stock совпал с expected=1. Аргументы: ref location, newValue, expectedValue. При stock=10, current=10, CAS(current-3,current) даёт previous=10,current=10,stock=7.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](./Q-044-compareexchange-returns-prior.md) · [English](en/Q-044-compareexchange-returns-prior.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-044) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-043-check-then-act-stock-negative.md) · [Следующий →](Q-045-two-buyers-single-item-cas.md)
