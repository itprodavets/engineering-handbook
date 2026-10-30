# Q-028 — Shared memory and synchronization

[Русский](../Q-028-lost-update-race.md) · [English](./Q-028-lost-update-race.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-028) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-027-whenall-exceptions-count.md) · [Next →](Q-029-lock-new-object.md)

## Question

Is counter always 10,000? Why or why not?

## .NET / C# challenge — predict the outcome first

```csharp
int counter = 0;
await Task.WhenAll(
    Enumerable.Range(0, 10_000)
        .Select(_ => Task.Run(() => counter++)));
Console.WriteLine(counter);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-028.cs
```

[Q-028.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-028.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

The result may be 10,000 or lower. Incrementing is not atomic, and competing workers can overwrite one another. Use Interlocked.Increment.

</details>

### Internal mechanism

Shared heap/closure; read-modify-write; OS scheduling; memory model.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)

---

[Русский](../Q-028-lost-update-race.md) · [English](./Q-028-lost-update-race.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-028) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-027-whenall-exceptions-count.md) · [Next →](Q-029-lock-new-object.md)
