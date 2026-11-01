# Q-060 — WhenAll completion

[Русский](./Q-060-whenall-waits-not-fail-fast.md) · [English](en/Q-060-whenall-waits-not-fail-fast.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-060) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-059-whenany-does-not-cancel-loser.md) · [Следующий →](Q-061-fromexception-oce-vs-fromcanceled.md)

## Вопрос

Если одна входящая Task уже Faulted, а другая ещё pending, завершится ли немедленно Task.WhenAll?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
Task combined=Task.WhenAll(faulted,pending); // remains incomplete until pending completes
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-060.cs
```

[Q-060.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-060.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Нет. WhenAll дожидается завершения всех задач, затем становится Faulted с агрегированными ошибками. Это не fail-fast.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.task.whenall?view=net-10.0)

---

[Русский](./Q-060-whenall-waits-not-fail-fast.md) · [English](en/Q-060-whenall-waits-not-fail-fast.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-060) · [Основная тема](../../topics/dotnet/task-composition.md) · [← Предыдущий](Q-059-whenany-does-not-cancel-loser.md) · [Следующий →](Q-061-fromexception-oce-vs-fromcanceled.md)
