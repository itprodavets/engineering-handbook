# Q-045 — CAS one item

[Русский](./Q-045-two-buyers-single-item-cas.md) · [English](en/Q-045-two-buyers-single-item-cas.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-045) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-044-compareexchange-returns-prior.md) · [Следующий →](Q-046-two-buyers-stock-three-single-cas.md)

## Вопрос

Могут ли оба потока успешно выполнить CompareExchange(ref stock,0,1) при stock=1?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
if (Interlocked.CompareExchange(ref stock,0,1)==1)
    Console.WriteLine("Purchased");
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-045.cs
```

[Q-045.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-045.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. Только один CAS атомарно выполнит 1→0 и вернёт previous=1. Другой увидит 0 и получит previous=0; Purchased печатается один раз, stock=0.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](./Q-045-two-buyers-single-item-cas.md) · [English](en/Q-045-two-buyers-single-item-cas.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-045) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-044-compareexchange-returns-prior.md) · [Следующий →](Q-046-two-buyers-stock-three-single-cas.md)
