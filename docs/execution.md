# Запуск C#-примеров

[Русский](execution.md) · [English](execution.en.md)

[Главная](../README.md) · [Лаборатории](../labs/README.md) · [Интерактивная практика](https://itprodavets.github.io/engineering-handbook/#/ru/practice)

GitHub Pages не исполняет C#. На сайте можно предсказать вывод, сравнить его с эталоном, изменить код и скопировать его. **Проверка предсказания — не выполнение программы.**

## Через GitHub Codespaces

[Открыть Codespaces](https://codespaces.new/itprodavets/engineering-handbook). Создай облачное окружение и в терминале выполни:

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

Если код был изменён на сайте, нажми «Копировать код», открой соответствующий `labs/dotnet/Q-###.cs` в Codespaces, замени содержимое и выполни команду. Для работы используется SDK .NET 10.

## Через GitHub Actions

Открой [Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) → **Run workflow** → введи ID зарегистрированного примера, например `Q-024`. Результат выводится в логах и Job Summary. **Actions выполняет только сохранённый в репозитории код, а не твои несохранённые изменения в Pages.**

## Локально

С установленным SDK .NET 10 запусти аналогичную команду из корня репозитория. Результаты конкурентных примеров могут быть недетерминированными; нельзя считать один запуск доказательством отсутствия race condition.

## О публикации Pages

Для приватных репозиториев GitHub Pages требует соответствующего тарифа GitHub. В Settings → Pages выбери Source → GitHub Actions. **Опубликованная Pages-страница обычно публична даже при приватном исходном репозитории.** В сайт не включены личные ответы, оценки и секреты.

[Документация GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [C# file-based apps (.NET 10)](https://learn.microsoft.com/en-us/dotnet/core/sdk/file-based-apps)
