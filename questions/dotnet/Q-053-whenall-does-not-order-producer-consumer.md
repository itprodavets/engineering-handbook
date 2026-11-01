# Q-053 — WhenAll ordering

[Русский](./Q-053-whenall-does-not-order-producer-consumer.md) · [English](en/Q-053-whenall-does-not-order-producer-consumer.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-053) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-052-await-producer-publishes-data.md) · [Следующий →](Q-054-task-delay-is-not-synchronization.md)

## Вопрос

Можно ли вывести 0 внутри Consumer, хотя в конце вызван await Task.WhenAll(producer,consumer)?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task producer=Task.Run(()=>data=42);
Task consumer=Task.Run(()=>Console.WriteLine(data));
await Task.WhenAll(producer,consumer);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-053.cs
```

[Q-053.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-053.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Да. WhenAll только ждёт обе Task и не задаёт порядок их действий. Consumer может прочитать 0 до записи producer. Для гарантии await producer должен находиться перед чтением Consumer.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](./Q-053-whenall-does-not-order-producer-consumer.md) · [English](en/Q-053-whenall-does-not-order-producer-consumer.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-053) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-052-await-producer-publishes-data.md) · [Следующий →](Q-054-task-delay-is-not-synchronization.md)
