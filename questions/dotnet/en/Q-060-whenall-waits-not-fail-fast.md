# Q-060 — Task composition and exceptions

[Русский](../Q-060-whenall-waits-not-fail-fast.md) · [English](./Q-060-whenall-waits-not-fail-fast.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-060) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-059-whenany-does-not-cancel-loser.md) · [Next →](Q-061-fromexception-oce-vs-fromcanceled.md)

## Question

If one input task is already Faulted and another is pending, does WhenAll complete immediately?

## .NET / C# challenge — predict the outcome first

```csharp
Task combined=Task.WhenAll(faulted,pending); // remains incomplete until pending completes
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-060.cs
```

[Q-060.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-060.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No. WhenAll waits until every input has completed before becoming Faulted and aggregating failures. It is not fail-fast.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](../Q-060-whenall-waits-not-fail-fast.md) · [English](./Q-060-whenall-waits-not-fail-fast.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-060) · [Canonical lesson](../../../topics/dotnet/en/task-composition.md) · [← Previous](Q-059-whenany-does-not-cancel-loser.md) · [Next →](Q-061-fromexception-oce-vs-fromcanceled.md)
