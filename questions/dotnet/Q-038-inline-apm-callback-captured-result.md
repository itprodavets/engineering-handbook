# Q-038 — Inline callback

[Русский](./Q-038-inline-apm-callback-captured-result.md) · [English](en/Q-038-inline-apm-callback-captured-result.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-038) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-037-apm-vs-taskrun-read.md) · [Следующий →](Q-039-race-condition-vs-data-race.md)

## Вопрос

Что напечатает callback, если он вызван inline до завершения присваивания result = BeginRead(...)?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
IAsyncResult? result = null;
result = stream.BeginRead(buffer,0,buffer.Length, ar => Console.WriteLine(result is null),null);
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-038.cs
```

[Q-038.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-038.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

True: при вычислении правой части присваивания result ещё null. Аргумент ar содержит IAsyncResult завершившейся операции. Если callback на другом потоке, возникает гонка с присваиванием. Лаборатория моделирует inline callback, не реальный сокет.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread](https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.networkstream.beginread)

---

[Русский](./Q-038-inline-apm-callback-captured-result.md) · [English](en/Q-038-inline-apm-callback-captured-result.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-038) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-037-apm-vs-taskrun-read.md) · [Следующий →](Q-039-race-condition-vs-data-race.md)
