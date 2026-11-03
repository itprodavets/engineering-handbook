# Q-050 — JIT / Memory Visibility

[Русский](./Q-050-nonvolatile-loop-jit-hoisting.md) · [English](en/Q-050-nonvolatile-loop-jit-hoisting.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-050) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-049-release-before-data-allows-zero.md) · [Следующий →](Q-051-thread-yield-is-not-memory-fence.md)

## Вопрос

Гарантированно ли завершится while(ready==0) без volatile после записи другого потока?

## Фрагмент .NET / C# — попробуйте предсказать результат

```csharp
while (ready == 0) { } // ordinary unsynchronized read
```

<details>
<summary>Эталонный ответ — открыть после своего ответа</summary>

Без `volatile` и другого механизма синхронизации чтение `ready` не образует acquire-операцию и не устанавливает гарантированную публикацию предшествующих записей `data`. Даже если Consumer увидел `ready==1`, чтение `data==42` нельзя выводить из такого флага как из корректного release/acquire-протокола. В цикле `while(ready==0)` JIT может, при допустимых условиях, вынести чтение за цикл; конкретная оптимизация не обязательна. Нельзя принимать типичное поведение x86/конкретного запуска за гарантию C#/.NET Memory Model.

</details>

### Документация и исходники

[https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/classes#1554-volatile-fields)

---

[Русский](./Q-050-nonvolatile-loop-jit-hoisting.md) · [English](en/Q-050-nonvolatile-loop-jit-hoisting.md) · [Все вопросы](README.md) · [Учебная платформа](https://itprodavets.github.io/engineering-handbook/#/ru/question/Q-050) · [Основная тема](../../topics/dotnet/shared-memory.md) · [← Предыдущий](Q-049-release-before-data-allows-zero.md) · [Следующий →](Q-051-thread-yield-is-not-memory-fence.md)
