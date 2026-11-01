# Q-053 — Task composition and exceptions

[Русский](../Q-053-whenall-does-not-order-producer-consumer.md) · [English](./Q-053-whenall-does-not-order-producer-consumer.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-053) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-052-await-producer-publishes-data.md) · [Next →](Q-054-task-delay-is-not-synchronization.md)

## Question

Can Consumer print zero even if the caller later awaits Task.WhenAll(producer,consumer)?

## .NET / C# challenge — predict the outcome first

```csharp
Task producer=Task.Run(()=>data=42);
Task consumer=Task.Run(()=>Console.WriteLine(data));
await Task.WhenAll(producer,consumer);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-053.cs
```

[Q-053.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-053.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

Yes. WhenAll joins both tasks without ordering their internal operations. Consumer may read zero before producer writes. Await producer inside consumer before reading to ensure dependency.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](../Q-053-whenall-does-not-order-producer-consumer.md) · [English](./Q-053-whenall-does-not-order-producer-consumer.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-053) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-052-await-producer-publishes-data.md) · [Next →](Q-054-task-delay-is-not-synchronization.md)
