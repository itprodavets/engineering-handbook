# Q-052 — Task composition and exceptions

[Русский](../Q-052-await-producer-publishes-data.md) · [English](./Q-052-await-producer-publishes-data.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-052) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-051-thread-yield-is-not-memory-fence.md) · [Next →](Q-053-whenall-does-not-order-producer-consumer.md)

## Question

Why does reading data after await producer yield 42 without volatile?

## .NET / C# challenge — predict the outcome first

```csharp
Task producer=Task.Run(()=>data=42);
await producer;
Console.WriteLine(data);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-052.cs
```

[Q-052.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-052.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

The producer writes data before Task completion; awaiting that same Task synchronizes the subsequent read. The relevant fact is the producer dependency, not thread identity or merely writing await.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model)

---

[Русский](../Q-052-await-producer-publishes-data.md) · [English](./Q-052-await-producer-publishes-data.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-052) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-051-thread-yield-is-not-memory-fence.md) · [Next →](Q-053-whenall-does-not-order-producer-consumer.md)
