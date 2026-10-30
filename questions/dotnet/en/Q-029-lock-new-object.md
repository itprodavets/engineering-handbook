# Q-029 — Shared memory and synchronization

[Русский](../Q-029-lock-new-object.md) · [English](./Q-029-lock-new-object.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-029) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-028-lost-update-race.md) · [Next →](Q-030-cancellation-after-start.md)

## Question

Does lock(new object()) protect counter from concurrent increments?

## C# challenge — predict the outcome first

```csharp
int counter = 0;
await Task.WhenAll(
    Enumerable.Range(0, 10_000).Select(_ =>
        Task.Run(() =>
        {
            lock (new object())
                counter++;
        })));
Console.WriteLine(counter);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-029.cs
```

[Q-029.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-029.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No. Each task locks a different freshly allocated object. Mutual exclusion requires a shared lock instance or an atomic increment.

</details>

### Internal mechanism

Roslyn lock → Monitor for object; по одной уникальной синхронизации на вызов.

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/lock)

---

[Русский](../Q-029-lock-new-object.md) · [English](./Q-029-lock-new-object.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-029) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-028-lost-update-race.md) · [Next →](Q-030-cancellation-after-start.md)
