# Q-047 — CAS-loop

[Русский](./Q-047-cas-loop-five-buyers.md) · [English](en/Q-047-cas-loop-five-buyers.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-047) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-046-two-buyers-stock-three-single-cas.md)

## Вопрос

Как CAS-loop ведёт себя при stock=3 и двух покупателях, а затем stock=1 и пяти покупателях?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
while (true) {
  int current=Volatile.Read(ref stock);
  if (current<=0) return false;
  if (Interlocked.CompareExchange(ref stock,current-1,current)==current) return true;
}
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-047.cs
```

[Q-047.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-047.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

При stock=3 и двух покупателях оба могут купить, stock=1: проигравший CAS перечитывает current и повторяет попытку. При stock=1 и пяти покупателях один получает true, четыре false, stock=0. На каждой итерации проверяется current<=0; значение не станет -1 при соблюдении протокола.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.compareexchange)

---

[Русский](./Q-047-cas-loop-five-buyers.md) · [English](en/Q-047-cas-loop-five-buyers.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-047) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-046-two-buyers-stock-three-single-cas.md)
