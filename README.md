# Engineering Handbook — инженерный справочник

[Русский](README.md) · [English](README.en.md)

**Интерактивный учебник:** [открыть платформу](https://itprodavets.github.io/engineering-handbook/#/ru/home).

Учебник по устройству языков, runtime, многопоточности, инфраструктуре и распределённым системам. Теория хранится отдельно от упражнений; один механизм — одна основная тема.

## Изучаемые темы

- [Жизненный цикл async/await](topics/dotnet/async-lifecycle.md) — 8 вопросов и упражнений
- [ThreadPool и планировщик ОС](topics/dotnet/threadpool-scheduling.md) — 6 вопросов и упражнений
- [Композиция Task и ошибки](topics/dotnet/task-composition.md) — 5 вопросов и упражнений
- [Разделяемая память и синхронизация](topics/dotnet/shared-memory.md) — 6 вопросов и упражнений
- [Continuation и контексты](topics/dotnet/execution-context.md) — 6 вопросов и упражнений
- [Отмена асинхронных операций](topics/dotnet/cancellation.md) — 2 вопросов и упражнений
- [ValueTask<T> и стоимость ожидания](topics/dotnet/valuetask.md) — 1 вопросов и упражнений
- [Блокировки и sync-over-async](topics/dotnet/sync-over-async.md) — 1 вопросов и упражнений

## Практика и код

- [Вопросы и ответы](questions/dotnet/README.md)
- [Запускаемые лаборатории](labs/README.md)
- [Открыть Codespaces](https://codespaces.new/itprodavets/engineering-handbook)
- [Запустить выбранный пример через Actions](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml)

## Как запустить C#

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

Сама страница GitHub Pages не компилирует C#. Для настоящего запуска используй Codespaces или GitHub Actions; интерактивная проверка ответов в браузере — это сравнение с эталоном, а не исполнение C#.

## Следующие направления

Go, Kafka, PostgreSQL, Kubernetes, Linux, system design. Разделы будут заполняться по мере прохождения — без дублирования теории.

## Личный прогресс

Результаты личных ответов и оценки — в приватной Google Таблице, не в репозитории. Браузерная платформа сохраняет отметки только локально на устройстве. GitHub Pages может быть публичным даже при приватном репозитории.

[Как вносить изменения](CONTRIBUTING.md)
