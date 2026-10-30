# Q-024 — Completed await

[Русский](./Q-024-completed-await-output.md) · [English](en/Q-024-completed-await-output.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-024) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-023-asynclocal-executioncontext.md) · [Следующий →](Q-025-incomplete-await-output.md)

## Вопрос

Какой вывод и почему? async-метод содержит await уже завершённой Task.

## Фрагмент C# — попробуйте предсказать результат

```csharp
async Task PrintAsync()
{
    Console.Write("A");
    await Task.CompletedTask;
    Console.Write("B");
}
var task = PrintAsync();
Console.Write("C");
await task;
```

### Запустить настоящий код

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

[Q-024.cs](https://github.com/itprodavets/engineering-handbook/blob/main/labs/dotnet/Q-024.cs) · [GitHub Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) · [Codespaces](https://codespaces.new/itprodavets/engineering-handbook)

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

ABC. CompletedTask уже завершена, поэтому await не приостанавливает метод и B печатается до возврата в вызывающий код.

</details>

### Почему это работает

Roslyn state machine; IsCompleted = true; без обязательного ThreadPool worker.

### Риск или ошибка

Нельзя считать, что каждый async-вызов запускается в фоне или переключает поток.

### Что гарантировано

Гарантировано для уже завершённой Task.

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs](https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/common-async-bugs)

---

[Русский](./Q-024-completed-await-output.md) · [English](en/Q-024-completed-await-output.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-024) · [Основная тема](../../topics/dotnet/async-lifecycle.md) · [← Предыдущий](Q-023-asynclocal-executioncontext.md) · [Следующий →](Q-025-incomplete-await-output.md)
