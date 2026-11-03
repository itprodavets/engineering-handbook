# Q-049 — Incorrect publication

[Русский](./Q-049-release-before-data-allows-zero.md) · [English](en/Q-049-release-before-data-allows-zero.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-049) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-048-safe-publication-acquire-release.md) · [Следующий →](Q-050-nonvolatile-loop-jit-hoisting.md)

## Вопрос

Может ли Consumer увидеть data=0, если Producer сначала Volatile.Write(ready,1), потом data=42?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int data = 0, ready = 0;
// Producer: Volatile.Write(ref ready, 1); data = 42;
// Consumer may observe ready==1 while data is still 0.
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-049.cs
```

[Q-049.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-049.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Да, Consumer может вывести 0 даже без переупорядочивания JIT или CPU. Допустимое чередование: Producer делает `Volatile.Write(ref ready,1)` → Consumer видит `ready==1` → читает старое `data==0` → Producer позже пишет `data=42`. Release не публикует будущие записи. Исправление — поменять порядок: сначала данные, затем release-флаг; Consumer должен читать флаг с acquire. Лаборатория воспроизводит это чередование детерминированно.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](./Q-049-release-before-data-allows-zero.md) · [English](en/Q-049-release-before-data-allows-zero.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-049) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-048-safe-publication-acquire-release.md) · [Следующий →](Q-050-nonvolatile-loop-jit-hoisting.md)
