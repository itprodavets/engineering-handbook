# Q-063 — Cancellation of asynchronous work

[Русский](../Q-063-async-task-throws-after-completed-await.md) · [English](./Q-063-async-task-throws-after-completed-await.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-063) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-062-async-task-oce-builder-canceled.md)

## Question

Does calling TestAsync synchronously throw InvalidOperationException if its body awaits CompletedTask then throws?

## .NET / C# challenge — predict the outcome first

```csharp
static async Task F(){await Task.CompletedTask;throw new InvalidOperationException();}
Task task=F(); // Faulted Task, no direct throw
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-063.cs
```

[Q-063.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-063.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

No. The async Task state machine captures the exception into a Faulted Task. CompletedTask may avoid suspension but does not change exception propagation; awaiting the Task throws the InvalidOperationException.

</details>

### Documentation and source

[https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html](https://source.dot.net/System.Private.CoreLib/src/libraries/System.Private.CoreLib/src/System/Runtime/CompilerServices/AsyncTaskMethodBuilderT.cs.html)

---

[Русский](../Q-063-async-task-throws-after-completed-await.md) · [English](./Q-063-async-task-throws-after-completed-await.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-063) · [Canonical lesson](../../../topics/dotnet/en/cancellation.md) · [← Previous](Q-062-async-task-oce-builder-canceled.md)
