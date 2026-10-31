# Q-046 — CAS expected value

[Русский](./Q-046-two-buyers-stock-three-single-cas.md) · [English](en/Q-046-two-buyers-stock-three-single-cas.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-046) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-045-two-buyers-single-item-cas.md) · [Следующий →](Q-047-cas-loop-five-buyers.md)

## Вопрос

Если stock=3, два потока выполняют CompareExchange(ref stock,2,3). Сколько покупок успешны и что возвращают оба CAS?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int previous=Interlocked.CompareExchange(ref stock,2,3);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-046.cs
```

[Q-046.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-046.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Ровно один успешный переход 3→2, stock=2. Победитель получает 3, проигравший получает 2. Второй должен заново прочитать остаток и повторить CAS с expected=2, чтобы купить ещё один товар.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](./Q-046-two-buyers-stock-three-single-cas.md) · [English](en/Q-046-two-buyers-stock-three-single-cas.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-046) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-045-two-buyers-single-item-cas.md) · [Следующий →](Q-047-cas-loop-five-buyers.md)
