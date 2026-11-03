# Q-041 — volatile

[Русский](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](en/Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-041) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-040-lost-update-two-task-run.md) · [Следующий →](Q-042-interlocked-increment-ref.md)

## Вопрос

Почему volatile int Value не делает Value++ атомарным и что реально гарантирует volatile в C#?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
sealed class Counter { public volatile int Value; }
// Two concurrent Value++ operations can both read 5 and write 6.
```

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

`volatile`/`Volatile.Read` обеспечивают acquire-семантику чтения, а `volatile`/`Volatile.Write` — release-семантику записи. Это ограничения на переупорядочивание обращений к памяти, а не атомарность выражения. `Value++` логически состоит из read → add → write. Два потока могут оба прочитать 5 и оба записать 6: lost update. `volatile` не гарантирует чтение самого нового значения по реальному времени и не устанавливает глобальный total order.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/volatile)

---

[Русский](./Q-041-volatile-does-not-make-plus-plus-atomic.md) · [English](en/Q-041-volatile-does-not-make-plus-plus-atomic.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-041) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-040-lost-update-two-task-run.md) · [Следующий →](Q-042-interlocked-increment-ref.md)
