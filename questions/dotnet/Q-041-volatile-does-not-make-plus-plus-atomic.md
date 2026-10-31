# Q-041 — volatile

[Русский](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](en/Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-041) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-040-lost-update-two-task-run.md) · [Следующий →](Q-042-interlocked-increment-ref.md)

## Вопрос

Почему volatile int Value не делает Value++ атомарным и что реально гарантирует volatile в C#?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
sealed class Counter { public volatile int Value; }
// Two unsynchronized Value++ operations can lose an update.
```

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Volatile read имеет acquire, volatile write — release семантику. Они не создают глобальный последовательный порядок всех операций и не объединяют read/modify/write в неделимую транзакцию: два потока могут записать 1 вместо 2.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)

---

[Русский](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](en/Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-041) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-040-lost-update-two-task-run.md) · [Следующий →](Q-042-interlocked-increment-ref.md)
