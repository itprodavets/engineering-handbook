# Q-062 — Cancellation of asynchronous work

[Русский](../Q-062-async-task-oce-builder-canceled.md) · [English](./Q-062-async-task-oce-builder-canceled.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-062) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-061-fromexception-oce-vs-fromcanceled.md) · [Next →](Q-063-async-task-throws-after-completed-await.md)

## Question

Why is async Task throwing OCE Canceled while Task.FromException(OCE) is Faulted?

## .NET / C# challenge — predict the outcome first

```csharp
static async Task F(){await Task.Yield();throw new OperationCanceledException();}
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-062.cs
```

[Q-062.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-062.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

AsyncTaskMethodBuilder.SetException recognizes OCE and uses TrySetCanceled with its token. Task.Yield only adds a continuation; it does not cause cancellation. FromException explicitly creates Faulted.

</details>

### Documentation and source

[https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html](https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html)

---

[Русский](../Q-062-async-task-oce-builder-canceled.md) · [English](./Q-062-async-task-oce-builder-canceled.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-062) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-061-fromexception-oce-vs-fromcanceled.md) · [Next →](Q-063-async-task-throws-after-completed-await.md)
