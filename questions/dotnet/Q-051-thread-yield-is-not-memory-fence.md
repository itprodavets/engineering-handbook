# Q-051 — Thread.Yield

[Русский](./Q-051-thread-yield-is-not-memory-fence.md) · [English](en/Q-051-thread-yield-is-not-memory-fence.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-051) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-050-nonvolatile-loop-jit-hoisting.md) · [Следующий →](Q-052-await-producer-publishes-data.md)

## Вопрос

Почему Thread.Yield() в цикле с обычным чтением ready не заменяет Volatile.Read?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
while (ready == 0) { Thread.Yield(); }
```

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Yield влияет на планирование ОС, не создаёт acquire/read barrier и не устанавливает happens-before. На конкретном runtime цикл может завершиться, но контракт memory synchronization отсутствует.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0](https://learn.microsoft.com/en-us/dotnet/api/system.threading.thread.yield?view=net-10.0)

---

[Русский](./Q-051-thread-yield-is-not-memory-fence.md) · [English](en/Q-051-thread-yield-is-not-memory-fence.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-051) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-050-nonvolatile-loop-jit-hoisting.md) · [Следующий →](Q-052-await-producer-publishes-data.md)
