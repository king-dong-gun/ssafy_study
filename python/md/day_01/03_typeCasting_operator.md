# Python 기초 ③ - 형변환(Type Casting)과 연산자

## 형변환(Type Casting)

형변환(Type Casting)이란 **한 자료형의 값을 다른 자료형으로 변환하는 과정**이다.

Python에서는 **암시적 형변환(Implicit Type Casting)** 과 **명시적 형변환(Explicit Type Casting)** 을 지원한다.

---

# 암시적 형변환 (Implicit Type Casting)

파이썬이 연산 중 자동으로 자료형을 변환한다.

## 정수 + 실수

```python
print(3 + 1.0)
```

실행 결과

```text
4.0
```

정수(`int`)와 실수(`float`)를 함께 연산하면 결과는 `float`가 된다.

---

## Boolean과 정수

Python에서는

- `True` → `1`
- `False` → `0`

으로 취급된다.

```python
print(True + 3)
```

실행 결과

```text
4
```

```python
print(True + False)
```

실행 결과

```text
1
```

---

# 명시적 형변환 (Explicit Type Casting)

개발자가 원하는 자료형으로 직접 변환하는 방법이다.

## 문자열 → 정수

```python
num = int("10")

print(num)
```

실행 결과

```text
10
```

---

## 문자열 → 실수

```python
num = float("3.14")

print(num)
```

실행 결과

```text
3.14
```

---

## 정수 → 문자열

```python
num = str(100)

print(num)
print(type(num))
```

실행 결과

```text
100
<class 'str'>
```

---

## 실수 → 정수

```python
num = int(3.9)

print(num)
```

실행 결과

```text
3
```

> 💡 `int()`는 반올림이 아니라 **소수점을 버린다.**

---

# 산술 연산자

산술 연산자는 숫자를 계산할 때 사용한다.

![alt text](../../images/python_숫자연산자.png)

예시

```python
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 3)
```

실행 결과

```text
9
5
14
3.5
3
1
8
```

---

# 복합 연산자

![alt text](../../images/python_복합연산자.png)

복합 연산자는 **연산과 할당을 동시에 수행**한다.


예시

```python
x = 10

x += 5
print(x)

x *= 2
print(x)

x -= 4
print(x)
```

실행 결과

```text
15
30
26
```

---

# 비교 연산자

![alt text](../../images/python_비교연산자.png)

비교 연산자는 두 값을 비교하여 **True 또는 False**를 반환한다.


예시

```python
print(5 == 5)
print(5 != 3)
print(5 > 3)
print(5 <= 3)
```

실행 결과

```text
True
True
True
False
```

---

# == 와 is의 차이

두 연산자는 비교 대상이 다르다.

## ==

값(Value)이 같은지 비교한다.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

실행 결과

```text
True
```

---

## is

같은 객체(Object)를 가리키는지 비교한다.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

실행 결과

```text
False
```

리스트의 내용은 같지만 서로 다른 객체이다.

같은 객체를 참조하면

```python
a = [1, 2, 3]
b = a

print(a is b)
```

실행 결과

```text
True
```

> 💡 `None`을 비교할 때는 `==`보다 `is`를 사용하는 것이 권장된다.

```python
value = None

print(value is None)
```

---

# 싱글턴(Singleton)

싱글턴(Singleton)은 **프로그램 전체에서 하나만 존재하는 객체**를 의미한다.

Python의 대표적인 싱글턴 객체

- None
- True
- False

예시

```python
a = None
b = None

print(a is b)
```

실행 결과

```text
True
```

두 변수는 같은 `None` 객체를 참조한다.

---

# 논리 연산자

논리 연산자는 여러 조건을 조합할 때 사용한다.

![alt text](../../images/python_논리연산자.png)

---

## and

```python
print(True and True)
print(True and False)
```

실행 결과

```text
True
False
```

---

## or

```python
print(True or False)
print(False or False)
```

실행 결과

```text
True
False
```

---

## not

```python
print(not True)
print(not False)
```

실행 결과

```text
False
True
```

---

# 논리 연산 예제

```python
age = 20
student = True

print(age >= 19 and student)
print(age < 19 or student)
print(not student)
```

실행 결과

```text
True
True
False
```

---

# 연산자 우선순위

연산자는 우선순위에 따라 계산된다.

1. `()` (괄호)
2. `**` (거듭제곱)
3. `*`, `/`, `//`, `%`
4. `+`, `-`
5. 비교 연산자
6. `not`
7. `and`
8. `or`

예시

```python
result = 3 + 2 * 5

print(result)
```

실행 결과

```text
13
```

괄호를 사용하면 우선순위를 변경할 수 있다.

```python
result = (3 + 2) * 5

print(result)
```

실행 결과

```text
25
```

---

# 핵심 정리

- 형변환은 자료형을 다른 자료형으로 변환하는 과정이다.
- 암시적 형변환은 Python이 자동으로 수행한다.
- 명시적 형변환은 개발자가 직접 수행한다.
- `int()`는 소수점을 버리고 정수로 변환한다.
- `==`는 값을 비교한다.
- `is`는 같은 객체인지 비교한다.
- `None` 비교는 `is None`을 사용하는 것이 권장된다.
- 논리 연산자는 여러 조건을 조합할 때 사용한다.
- 괄호를 사용하면 연산 우선순위를 변경할 수 있다.