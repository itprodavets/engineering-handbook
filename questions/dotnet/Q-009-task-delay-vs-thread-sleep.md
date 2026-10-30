# Q-009 — Task.Delay / Thread.Sleep

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-008-task-vs-thread.md) · [Следующий →](Q-010-task-whenall-execution.md)

**Level:** Senior / Staff · **Language:** RU + EN · **Topic:** Task.Delay / Thread.Sleep

## Вопрос (RU)

Что произойдёт с ThreadPool, если одновременно запустить 10 000 Task.Delay(5000) и 10 000 Task.Run(() => Thread.Sleep(5000))?

## Question (EN)

What happens to the ThreadPool when 10,000 Task.Delay(5000) operations run versus 10,000 Task.Run(() => Thread.Sleep(5000)) operations?


<details>
<summary><strong>Эталонный ответ RU / Model answer EN — открыть после самостоятельного ответа</strong></summary>

### RU — кратко и технически точно

Task.Delay создаёт 10 000 ожидающих операций с таймерами, но 0 рабочих потоков блокируется специально ради этих задержек. Task.Run помещает 10 000 делегатов в очередь; каждый выполняемый Thread.Sleep блокирует 1 worker на 5 секунд. ThreadPool может использовать существующие или создавать дополнительные потоки; точное число не фиксировано.

### EN — concise interview answer

10,000 Task.Delay operations require zero dedicated blocked worker threads while their timers are pending. Task.Run queues 10,000 delegates; each executing Thread.Sleep blocks one worker for five seconds. The ThreadPool may reuse idle workers or create additional ones; the exact count is workload-dependent.

</details>

**Terminology / Термины:** Task.Delay; Thread.Sleep; timers; starvation; ThreadPool queue

[Механика и ресурсы](../../docs/internals-reference.md)

## Ссылки и проверка / References & verification

- [Глубокая теория / Theory](../../runtimes/clr/threadpool.md)
- [Как оценивать доказательность](../../docs/technical-accuracy.md)
- [Как запускать фрагменты кода](../../docs/execution.md)

---

[Главная / Home](../../README.md) · [Все вопросы / Questions](README.md) · [Тема / Topic](../../runtimes/clr/threadpool.md) · [Запуск / Run](../../docs/execution.md) · [← Предыдущий](Q-008-task-vs-thread.md) · [Следующий →](Q-010-task-whenall-execution.md)
