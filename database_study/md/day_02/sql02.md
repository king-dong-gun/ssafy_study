### 1. 테이블 생성/수정/삭제

#### DDL (Data Definition Language)

> 데이터베이스의 구조를 정의하거나 변경하는 언어이다.
>

테이블을 생성하거나 구조를 수정하고 삭제할 때 사용한다.

#### CREATE TABLE

> 테이블을 새로 생성한다.
>

```sql
-- 1. Create a table
CREATE TABLE examples(
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);
```

![](https://velog.velcdn.com/images/king-dong-gun/post/fc62a781-7777-41f2-8769-7e596dbee785/image.png)


#### SQLite 데이터 타입

1. `NULL` : 아무런 값도 포함하지 않음을 나타낸다.
2. `INTEGER` : 정수
3. `REAL` : 부동 소수점
4. `TEXT` : 문자열
5. `BLOB` : 이미지, 동영상, 문서 등의 바이너리 데이터

#### 제약 조건

> 테이블의 필드에 적용되는 규칙 또는 제한 사항이다.
>

데이터의 무결성을 유지하고, 데이터베이스의 일관성을 보장한다.

1. `PRIMARY KEY` : 해당 필드를 기본 키로 지정한다.
2. `NOT NULL` : 해당 필드에 NULL값을 허용하지 않도록 지정한다.
3. `FOREIGN KEY` : 다른 테이블과의 외래 키 관계를 정의한다.

#### ALTER TABLE

> 기존 테이블의 구조를 수정한다.
>

**필드 추가**

```sql
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```

**필드 이름 변경**

```sql
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
```

**필드 삭제**

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

**테이블 이름 변경**

```sql
ALTER TABLE old_table_name
RENAME TO new_table_name;
```

#### DROP TABLE

> 기존 테이블을 삭제한다.
>

```sql
DROP TABLE table_name;
```

`DROP TABLE`을 실행하면 테이블의 데이터뿐만 아니라 **테이블 자체가 삭제**된다.

### 2. 데이터 추가/수정/삭제

#### DML (Data Manipulation Language)

> 테이블에 저장된 데이터를 추가, 수정, 삭제하기 위해 사용하는 언어이다.
>

대표적으로 `INSERT`, `UPDATE`, `DELETE`가 있다.

#### INSERT

> 테이블에 새로운 레코드를 추가한다.
>

```sql
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);
```

여러 개의 레코드를 한 번에 추가할 수도 있다.

```sql
INSERT INTO table_name (column1, column2)
VALUES
    (value1, value2),
    (value3, value4),
    (value5, value6);
```

#### UPDATE

> 테이블에 존재하는 레코드의 값을 수정한다.
>

```sql
UPDATE table_name
SET column_name = value
WHERE condition;
```

`WHERE`을 사용하여 수정할 레코드의 조건을 지정한다.

```sql
UPDATE users
SET age = 30
WHERE id = 1;
```

#### DELETE

> 테이블에 존재하는 레코드를 삭제한다.
>

```sql
DELETE FROM table_name
WHERE condition;
```

`WHERE`을 사용하여 삭제할 레코드의 조건을 지정한다.

```sql
DELETE FROM users
WHERE id = 1;
```

> `UPDATE`와 `DELETE`에서 `WHERE` 조건을 작성하지 않으면 여러 레코드 또는 모든 레코드가 영향을 받을 수 있으므로 주의해야 한다.
>

### 3. 여러 테이블 조회 (Multi Table Queries)

> 여러 테이블의 데이터를 연결하여 조회하는 방법이다.
>

#### JOIN

> 두 개 이상의 테이블을 서로 연결하여 필요한 데이터를 조회하는 방법이다.
>

관계형 데이터베이스에서는 데이터가 여러 테이블에 나누어 저장될 수 있다.

`JOIN`은 이러한 테이블에서 **서로 관련된 필드를 기준으로 데이터를 연결하여 조회**할 때 사용한다.

- `JOIN` : 연결할 테이블을 지정한다.
- `ON` : 두 테이블을 연결할 조건을 지정한다.

#### INNER JOIN

> 두 테이블에서 **조건이 일치하는 데이터만** 조회하는 방법이다.
>

두 테이블을 연결했을 때 `ON` 조건을 만족하는 레코드만 결과에 포함된다.

#### 데이터 준비

![](https://velog.velcdn.com/images/king-dong-gun/post/3ad03ae0-2d3a-4206-bb67-d2640f397e6c/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/ed95853e-fe13-4617-b050-e99a612a85a6/image.png)


```sql
-- INNER JOIN
SELECT * FROM articles
INNER JOIN users 
  ON users.id = articles.userId;
```

![](https://velog.velcdn.com/images/king-dong-gun/post/d3fc39f1-7152-42b6-b256-755327cdb1c6/image.png)


#### LEFT JOIN

> 왼쪽 테이블의 **모든 데이터**와 오른쪽 테이블에서 **조건이 일치하는 데이터**를 조회하는 방법이다.
>

오른쪽 테이블에 일치하는 데이터가 없는 경우 해당 값은 `NULL` 로 표시된다.

```sql
SELECT * FROM articles
LEFT JOIN users 
  ON users.id = articles.userId;
```

![](https://velog.velcdn.com/images/king-dong-gun/post/e776c32d-3516-4987-a977-08ba32ae7165/image.png)


#### INNER JOIN과 LEFT JOIN 차이

| 구분 | 조회 결과 | 일치하는 데이터가 없는 경우 |
| --- | --- | --- |
| `INNER JOIN` | 두 테이블에서 조건이 일치하는 데이터만 조회 | 결과에서 제외 |
| `LEFT JOIN` | 왼쪽 테이블 전체 + 오른쪽 테이블에서 일치하는 데이터 조회 | 오른쪽 테이블의 값이 `NULL`로 표시 |