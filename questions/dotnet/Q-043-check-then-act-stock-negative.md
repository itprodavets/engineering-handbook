# Q-043 — Check-Then-Act

[Русский](./Q-043-check-then-act-stock-negative.md) · [English](en/Q-043-check-then-act-stock-negative.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-043) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-042-interlocked-increment-ref.md) · [Следующий →](Q-044-compareexchange-returns-prior.md)

## Вопрос

Может ли stock стать -1 при Volatile.Read(stock)>0 и последующем Interlocked.Decrement, если stock=1?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
if (Volatile.Read(ref stock)>0)
    Interlocked.Decrement(ref stock);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-043.cs
```

[Q-043.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-043.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Да. Два покупателя могут прочитать 1 до любого декремента. Атомарные декременты выполняются как 1→0→-1. Операция проверки и действие не атомарны вместе; нарушается инвариант stock>=0.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.decrement](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.decrement)

---

[Русский](./Q-043-check-then-act-stock-negative.md) · [English](en/Q-043-check-then-act-stock-negative.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-043) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-042-interlocked-increment-ref.md) · [Следующий →](Q-044-compareexchange-returns-prior.md)
