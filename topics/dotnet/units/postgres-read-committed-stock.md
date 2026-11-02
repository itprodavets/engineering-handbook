# PostgreSQL READ COMMITTED: гонка остатков и условный UPDATE

[Русский](postgres-read-committed-stock.md) · [English](en/postgres-read-committed-stock.md)

[Главная](../../../README.md) · [Модуль](../microservices-concurrency.md) · [Все разделы](README.md) · [Платформа](https://itprodavets.github.io/engineering-handbook/#/ru/unit/postgres-read-committed-stock)

> Проверять корректность одного SKU при двух транзакциях на уровне MVCC и row locks.

## Определение

Два Pod при READ COMMITTED могут оба прочитать available=1 обычным SELECT. Если оба затем выполнят UPDATE SET available=available-1 WHERE sku=..., второй UPDATE дождётся lock, но применится к новой версии со значением 0 и может создать -1. Атомарный условный UPDATE ... WHERE available>0 RETURNING available повторно проверит предикат и не допустит отрицательного остатка.

## Внутренний механизм

1. Оба отдельные SELECT могут увидеть available=1.
2. Первый UPDATE получает row lock, записывает 0 и коммитится.
3. Второй UPDATE ждёт, затем уменьшает текущую версию 0→-1, если WHERE только по sku.
4. Условие WHERE available>0 нужно включить в тот же UPDATE; PostgreSQL rechecks WHERE после ожидания конкурентного UPDATE.
5. Если второй statement не обновил строк, это out-of-stock. Дополнительный CHECK available>=0 защищает инвариант от иных писателей.

## Последовательное объяснение

### SELECT + безусловный UPDATE — окно гонки

Два SELECT получают 1. Первый UPDATE записывает 0. Второй ждёт row lock и после commit первого выполняет обновление новой версии 0→-1, так как его WHERE не содержит available>0. Row lock сериализует физические записи, но не гарантирует бизнес-условие, которое проверялось отдельно.

```sql
BEGIN;
SELECT available FROM inventory WHERE sku='IPHONE-17';
UPDATE inventory SET available=available-1 WHERE sku='IPHONE-17';
COMMIT;
```

### Условный UPDATE и результат по RETURNING

В одном statement записывай SET available=available-1 при WHERE available>0. В READ COMMITTED конкурентный второй UPDATE ждёт row lock, затем повторно проверяет WHERE на обновлённой версии: после первого decrement до 0 он обновляет ноль строк. RETURNING возвращает новое значение только победителю; можно добавить CHECK(available>=0).

```sql
UPDATE inventory SET available=available-1
WHERE sku='IPHONE-17' AND available>0
RETURNING available;
```

### Резервирование — отдельная операция от оплаты

Транзакция резервирования может быть короткой и атомарной, а внешний провайдер находится вне PostgreSQL. Для полного заказа требуются reservationId, дедупликация по orderId, expiration/release, payment workflow и компенсация при частичном отказе. Это отдельная тема для дальнейшего обсуждения.


## Потребляемые ресурсы

PostgreSQL MVCC row versions, row-level locks, транзакции и соединения; бизнес-состояние живёт вне Pod.

## Ошибки и ограничения

READ COMMITTED не SERIALIZABLE. SELECT FOR UPDATE в корректной транзакции тоже может защищать read-then-update, но удерживать row lock во время внешнего ChargeAsync обычно рискованно. SQL для одного SKU не превращает Payment/Order в общую ACID-транзакцию.

## Пример

```sql
UPDATE inventory
SET available=available-1
WHERE sku='IPHONE-17' AND available>0
RETURNING available;
```

## Вопросы для закрепления

- [Q-074: Могут ли два Pod под READ COMMITTED прочитать available=1 и затем безусловными UPDATE получить -1?](../../../questions/dotnet/Q-074-postgres-read-committed-check-act.md)
- [Q-075: Как одним SQL statement защитить последний товар через UPDATE ... RETURNING?](../../../questions/dotnet/Q-075-postgres-conditional-update-returning.md)

## Пять уровней понимания

Сначала ответь самостоятельно. Критерии открой только после попытки.

### 1. Recall

Что означает READ COMMITTED для двух SELECT?

<details>
<summary>Критерии ответа</summary>

Каждое отдельное statement видит committed snapshot.

</details>

### 2. Explain

Почему второй UPDATE может уменьшить остаток до -1 даже с row lock?

<details>
<summary>Критерии ответа</summary>

После ожидания работает с новой версией и без available>0 в WHERE.

</details>

### 3. Predict

Что вернёт второй UPDATE ... WHERE available>0 RETURNING?

<details>
<summary>Критерии ответа</summary>

Ноль обновлённых строк после recheck.

</details>

### 4. Diagnose

Что проверять при oversell после scale-out?

<details>
<summary>Критерии ответа</summary>

SQL WHERE, isolation, row waits, отсутствие CHECK, повторы.

</details>

### 5. Design

Как зарезервировать SKU без Redis lock и не держать транзакцию через оплату?

<details>
<summary>Критерии ответа</summary>

Короткий условный UPDATE, reservation idempotency и отдельный payment workflow.

</details>


## Источники

- [https://www.postgresql.org/docs/current/transaction-iso.html](https://www.postgresql.org/docs/current/transaction-iso.html)
- [https://www.postgresql.org/docs/current/sql-update.html](https://www.postgresql.org/docs/current/sql-update.html)

---

[← Назад](payment-timeout-idempotency-outbox.md) · [Русский](postgres-read-committed-stock.md) · [English](en/postgres-read-committed-stock.md)
