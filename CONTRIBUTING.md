# Contributing / Добавление материалов

[Главная / Home](README.md) · [Все вопросы / Questions](questions/dotnet/README.md) · [Тема / Topic](docs/technical-accuracy.md) · [Запуск / Run](docs/execution.md)

- Новый вопрос получает следующий свободный ID, новый Markdown в `questions/dotnet/`, ссылки в README и индексе.
- К каждому вопросу обязательны **RU и EN формулировки**, короткие эталонные ответы, уровень гарантии и ссылки на исследование механизмов.
- Для ловушек — runnable `.cs` в `labs/dotnet/`, команда `dotnet run --file ...`, а также проверка безопасного ожидаемого результата.
- Не переносить личные оценки, исходные ответы и секреты из Google Sheets в репозиторий. Progress stays in private tracker.
- При несоответствии теории исходникам текущего .NET: обновить комментарии и ссылку на версию, не утверждать неподтверждённые bytes/CPU/threads.
- Проверка качества: `python3 scripts/check_links.py` и на SDK10 `python3 scripts/check_labs.py`.

[Семь обязательных пунктов точного разбора](docs/technical-accuracy.md)

[Главная / Home](README.md) · [Все вопросы / Questions](questions/dotnet/README.md) · [Тема / Topic](docs/technical-accuracy.md) · [Запуск / Run](docs/execution.md)
