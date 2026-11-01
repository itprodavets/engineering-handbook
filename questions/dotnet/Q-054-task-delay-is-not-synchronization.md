# Q-054 — Task.Delay timing

[Русский](./Q-054-task-delay-is-not-synchronization.md) · [English](en/Q-054-task-delay-is-not-synchronization.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-054) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-053-whenall-does-not-order-producer-consumer.md) · [Следующий →](Q-055-whenany-winner-vs-continuation-time.md)

## Вопрос

Почему await Task.Delay(100) не гарантирует, что другая Task завершилась и опубликовала data=42?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
await Task.Delay(100);
Console.WriteLine(data); // no producer dependency
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-054.cs
```

[Q-054.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-054.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Task.Delay — таймерная задача, а не делегат или ожидание Producer. Producer может работать дольше или позже получить CPU. Нужны await producer или другой корректный synchronization primitive.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0)

---

[Русский](./Q-054-task-delay-is-not-synchronization.md) · [English](en/Q-054-task-delay-is-not-synchronization.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-054) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-053-whenall-does-not-order-producer-consumer.md) · [Следующий →](Q-055-whenany-winner-vs-continuation-time.md)
