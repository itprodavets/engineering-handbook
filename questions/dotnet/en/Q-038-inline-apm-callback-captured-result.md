# Q-038 — The async/await execution lifecycle

[Русский](../Q-038-inline-apm-callback-captured-result.md) · [English](./Q-038-inline-apm-callback-captured-result.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-038) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-037-apm-vs-taskrun-read.md) · [Next →](Q-039-race-condition-vs-data-race.md)

## Question

What does a callback print if invoked inline before assigning result = BeginRead(...)?

## .NET / C# challenge — predict the outcome first

```csharp
IAsyncResult? result = null;
result = stream.BeginRead(buffer,0,buffer.Length, ar => Console.WriteLine(result is null),null);
```

### Run the actual code

```bash
dotnet run --file labs/dotnet/Q-038.cs
```

[Q-038.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-038.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Model answer — reveal after your attempt</summary>

True: the right-hand side executes before result is assigned, so it is still null. The callback ar parameter identifies the completed operation. Another-thread callback can race with assignment. The lab simulates inline execution rather than a real socket.

</details>

### Documentation and source

[https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread)

---

[Русский](../Q-038-inline-apm-callback-captured-result.md) · [English](./Q-038-inline-apm-callback-captured-result.md) · [All questions](../README.en.md) · [Interactive handbook](https://itprodavets.github.io/engineering-handbook/#/en/question/Q-038) · [Canonical lesson](../../../topics/dotnet/en/async-lifecycle.md) · [← Previous](Q-037-apm-vs-taskrun-read.md) · [Next →](Q-039-race-condition-vs-data-race.md)
