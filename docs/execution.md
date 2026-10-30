# Запуск кода / Running examples

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](../labs/README.md) · [Запуск / Run](execution.md)

## Почему не кнопка Run прямо в Markdown?

GitHub renders Markdown code fences as **static text**. GitHub itself cannot execute arbitrary C# in a README or question. Поэтому у каждой задачи есть **прямая ссылка на запускаемый файл**, а для облачного выполнения настроены Codespaces и ручной GitHub Actions workflow.

## Option 1 — .NET 10 CLI, local or Codespaces

1. Установить .NET 10 SDK; проверить `dotnet --version`.
2. Из корня репозитория выполнить:

```bash
dotnet run --file labs/dotnet/Q-024.cs
./scripts/run-lab.sh Q-025
```

> .NET 10 **file-based apps** — это поддерживаемый Microsoft механизм запуска одиночного `*.cs` без `.csproj`; команды и SDK описаны в [официальной документации](https://learn.microsoft.com/en-us/dotnet/core/sdk/file-based-apps).

## Option 2 — GitHub Codespaces in browser

После публикации приватного репозитория открой его на github.com, выбери **Code → Codespaces → Create codespace on main**. Файл `.devcontainer/devcontainer.json` поднимает окружение .NET 10. Открой соответствующий файл `labs/dotnet/Q-024.cs`, измени код и выполни из встроенного терминала:

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

[GitHub docs: C# project in Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-dotnet-project-for-codespaces).

## Option 3 — GitHub Actions in browser

Открой вкладку **Actions → Run one lab → Run workflow** и выбери Q-024…Q-035. Workflow установит .NET 10 и запустит указанный файл. Результат появится в job log и Job Summary. Не предполагает execution внутри Markdown, но позволяет запускать код с GitHub UI.

## Why not Polyglot Notebooks?

[Microsoft announced deprecation of Polyglot Notebooks and .NET Interactive in 2026](https://github.com/dotnet/interactive/issues/4163); therefore this handbook uses supported .NET 10 file-based apps. If a maintained notebook kernel becomes available, it may be added as an optional view, without replacing runnable `.cs` source.

## Secure execution

Запускай только проверенный код. Примеры не требуют секретов, API-ключей или доступа к production БД. Недетерминированные примеры проверяются по допустимым свойствам, а не конкретному числу.

[Главная / Home](../README.md) · [Все вопросы / Questions](../questions/dotnet/README.md) · [Тема / Topic](../labs/README.md) · [Запуск / Run](execution.md)
