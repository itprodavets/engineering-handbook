# Q-061 — Cancellation of asynchronous work

[Русский](../Q-061-fromexception-oce-vs-fromcanceled.md) · [English](./Q-061-fromexception-oce-vs-fromcanceled.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-061) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-060-whenall-waits-not-fail-fast.md) · [Next →](Q-062-async-task-oce-builder-canceled.md)

## Question

Why is Task.FromException(OCE) Faulted but Task.FromCanceled(token) Canceled?

## .NET / C# challenge — predict the outcome first

```csharp
Task a=Task.FromException(new OperationCanceledException());
Task b=Task.FromCanceled(new CancellationToken(true));
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-061.cs
```

[Q-061.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-061.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

FromException always creates a Faulted Task regardless of exception type. FromCanceled with an already canceled token constructs Canceled. OCE type alone does not determine Task.Status.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.fromexception?view=net-10.0)

---

[Русский](../Q-061-fromexception-oce-vs-fromcanceled.md) · [English](./Q-061-fromexception-oce-vs-fromcanceled.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-061) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-060-whenall-waits-not-fail-fast.md) · [Next →](Q-062-async-task-oce-builder-canceled.md)
