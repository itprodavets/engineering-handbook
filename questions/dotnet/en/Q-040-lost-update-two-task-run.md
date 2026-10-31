# Q-040 — Shared memory and synchronization

[Русский](../Q-040-lost-update-two-task-run.md) · [English](./Q-040-lost-update-two-task-run.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-040) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-039-race-condition-vs-data-race.md) · [Next →](Q-041-volatile-does-not-make-plus-plus-atomic.md)

## Question

What outcomes are possible after two Task.Run(() => state.Value++) and awaiting Task.WhenAll, starting at Value=0?

## .NET / C# challenge — predict the outcome first

```csharp
var state = new Counter();
await Task.WhenAll(Task.Run(() => state.Value++), Task.Run(() => state.Value++));
Console.WriteLine(state.Value);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-040.cs
```

[Q-040.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-040.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

1 or 2. ++ is not atomic: both may read 0 and write 1. Task.WhenAll only waits for completion, not mutual exclusion. The lab forces a lost-update interleaving.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked.increment)

---

[Русский](../Q-040-lost-update-two-task-run.md) · [English](./Q-040-lost-update-two-task-run.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-040) · [Canonical lesson](../../../topics/dotnet/en/shared-memory.md) · [← Previous](Q-039-race-condition-vs-data-race.md) · [Next →](Q-041-volatile-does-not-make-plus-plus-atomic.md)
