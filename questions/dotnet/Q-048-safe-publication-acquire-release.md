# Q-048 — Memory publication

[Русский](./Q-048-safe-publication-acquire-release.md) · [English](en/Q-048-safe-publication-acquire-release.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-048) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-047-cas-loop-five-buyers.md) · [Следующий →](Q-049-release-before-data-allows-zero.md)

## Вопрос

Почему data=42 перед Volatile.Write(ready,1) и Volatile.Read(ready) позволяет вывести 42?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
int data = 0, ready = 0;
// Producer: data = 42; Volatile.Write(ref ready, 1);
// Consumer: if (Volatile.Read(ref ready) == 1) Console.WriteLine(data);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-048.cs
```

[Q-048.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-048.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

При начальных `data=0`, `ready=0` и отсутствии других писателей: Producer выполняет `data=42`, затем `Volatile.Write(ref ready,1)` (release). Consumer читает `Volatile.Read(ref ready)` (acquire) и, если увидел 1 от этой публикации, последующее чтение `data` получает 42. Release охватывает предшествующую запись, acquire не допускает переноса последующего чтения данных перед проверкой флага. `Interlocked.Increment` здесь не требуется: нужен корректный протокол публикации, а не атомарный инкремент. Гарантии ограниченного времени ожидания флага нет.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](./Q-048-safe-publication-acquire-release.md) · [English](en/Q-048-safe-publication-acquire-release.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-048) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-047-cas-loop-five-buyers.md) · [Следующий →](Q-049-release-before-data-allows-zero.md)
