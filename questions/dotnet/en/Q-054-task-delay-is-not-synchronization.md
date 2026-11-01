# Q-054 — Task composition and exceptions

[Русский](../Q-054-task-delay-is-not-synchronization.md) · [English](./Q-054-task-delay-is-not-synchronization.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-054) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-053-whenall-does-not-order-producer-consumer.md) · [Next →](Q-055-whenany-winner-vs-continuation-time.md)

## Question

Why does awaiting Task.Delay(100) not establish producer completion or visibility?

## .NET / C# challenge — predict the outcome first

```csharp
await Task.Delay(100);
Console.WriteLine(data); // no producer dependency
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-054.cs
```

[Q-054.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-054.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Task.Delay is a timer-backed Task, not a producer completion check or a blocked worker. Producer may start or finish later. Await producer or use another synchronization mechanism.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.delay?view=net-10.0)

---

[Русский](../Q-054-task-delay-is-not-synchronization.md) · [English](./Q-054-task-delay-is-not-synchronization.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-054) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-053-whenall-does-not-order-producer-consumer.md) · [Next →](Q-055-whenany-winner-vs-continuation-time.md)
