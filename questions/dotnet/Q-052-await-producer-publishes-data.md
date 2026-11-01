# Q-052 — Task completion

[Русский](./Q-052-await-producer-publishes-data.md) · [English](en/Q-052-await-producer-publishes-data.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-052) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-051-thread-yield-is-not-memory-fence.md) · [Следующий →](Q-053-whenall-does-not-order-producer-consumer.md)

## Вопрос

Почему после await producer чтение data без volatile даёт 42?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task producer=Task.Run(()=>data=42);
await producer;
Console.WriteLine(data);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-052.cs
```

[Q-052.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-052.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Производитель записывает data до завершения своей Task; await именно producer обеспечивает синхронизацию с завершением. Важна зависимость от Task, не thread ID и не сам факт существования await.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)

---

[Русский](./Q-052-await-producer-publishes-data.md) · [English](en/Q-052-await-producer-publishes-data.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-052) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-051-thread-yield-is-not-memory-fence.md) · [Следующий →](Q-053-whenall-does-not-order-producer-consumer.md)
