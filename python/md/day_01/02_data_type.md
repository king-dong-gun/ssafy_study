# Python 기초 ② - 자료형(Data Type)

## 자료형(Type)이란?

자료형(Data Type)은 **값의 종류**와 **그 값으로 수행할 수 있는 연산**을 결정하는 속성이다.

Python은 다양한 자료형을 제공하며, 크게 다음과 같이 분류할 수 있다.

- 숫자형(Number)
- 시퀀스(Sequence)
- 매핑(Mapping)
- 집합(Set)
- 기타(None, Boolean)

---

# 숫자형(Number)

## int (정수)

정수를 저장하는 자료형이다.

```python
age = 20
temperature = -5
```

---

## float (실수)

실수를 저장하는 자료형이다.

```python
pi = 3.14
height = 175.5
```

> 💡 `int`와 `float`를 함께 연산하면 결과는 `float`가 된다.

```python
print(3 + 1.5)
```

실행 결과

```text
4.5
```

---

# 시퀀스(Sequence)

시퀀스는 **여러 개의 데이터를 순서대로 저장하는 자료형**이다.

대표적인 시퀀스 자료형

- str
- list
- tuple
- range

공통 특징

> - 순서(Index)가 존재한다.
> - 인덱싱이 가능하다.
> - 슬라이싱이 가능하다.
> - 길이를 구할 수 있다.
> - 반복문으로 순회할 수 있다.
> 
> ![alt text](../../images/python_시퀀스타입.png)

---

# 문자열(String)

문자열은 문자의 나열을 저장하는 **변경 불가능(Immutable)** 한 시퀀스 자료형이다.

```python
name = "홍길동"
language = "Python"
```

## 인덱싱

```python
text = "Python"

print(text[0])
print(text[-1])
```

실행 결과

```text
P
n
```

---

## 슬라이싱

```python
text = "Python"

print(text[0:3])
```

실행 결과

```text
Pyt
```

> 💡 슬라이싱의 마지막 인덱스는 포함되지 않는다.

---

## f-string

문자열 안에서 변수나 표현식을 쉽게 출력할 수 있다.

```python
name = "홍길동"
age = 25

print(f"안녕하세요. 제 이름은 {name}이고 나이는 {age}살입니다.")
```

실행 결과

```text
안녕하세요. 제 이름은 홍길동이고 나이는 25살입니다.
```

---

# 리스트(List)

리스트는 여러 개의 값을 **순서대로 저장하는 변경 가능한(Mutable)** 시퀀스 자료형이다.

특징

- `[]` 사용
- 서로 다른 자료형 저장 가능
- 추가, 수정, 삭제 가능

```python
data = [1, "Python", True, [1, 2]]
```

---

## 값 수정

```python
numbers = [1, 2, 3]

numbers[1] = 100

print(numbers)
```

실행 결과

```text
[1, 100, 3]
```

---

## 슬라이싱으로 수정

```python
numbers = [1, 2, 3, 4]

numbers[1:3] = [20, 30]

print(numbers)
```

실행 결과

```text
[1, 20, 30, 4]
```

> 💡 리스트는 **가변(Mutable)** 자료형이므로 생성 후에도 자유롭게 수정할 수 있다.

---

# 중첩 리스트(Nested List)

리스트 안에는 또 다른 리스트를 저장할 수 있다.

```python
students = [
    ["홍길동", 20],
    ["김철수", 21]
]

print(students[0][0])
```

실행 결과

```text
홍길동
```

---

# 튜플(Tuple)

튜플은 여러 개의 값을 저장하는 **변경 불가능(Immutable)** 한 시퀀스 자료형이다.

- `()` 사용
- 생성 후 수정 불가능

```python
point = (10, 20)

print(point)
```

튜플은 **데이터를 변경하지 않도록 보호할 때** 자주 사용한다.

---

# range

연속된 정수를 생성하는 시퀀스 자료형이다.

주로 반복문에서 사용된다.

```python
range(5)
```

```python
list(range(5))
```

실행 결과

```text
[0, 1, 2, 3, 4]
```

```python
list(range(2, 5))
```

실행 결과

```text
[2, 3, 4]
```

```python
list(range(2, 10, 2))
```

실행 결과

```text
[2, 4, 6, 8]
```

---

# 딕셔너리(Dictionary)

딕셔너리는 **Key와 Value를 한 쌍으로 저장하는 변경 가능한(Mutable) 자료형**이다.

> 💡 Java의 `Map`과 가장 비슷하다.

특징

- Key는 중복될 수 없다.
- Value는 중복될 수 있다.
- Python 3.7부터 입력한 순서를 유지한다.

```python
student = {
    "name": "홍길동",
    "age": 25
}
```

---

## 값 조회

```python
print(student["name"])
```

실행 결과

```text
홍길동
```

존재하지 않는 Key를 조회하면 `KeyError`가 발생한다.

```python
print(student["score"])
```

---

## 값 추가

```python
student["gender"] = "남"

print(student)
```

실행 결과

```text
{'name': '홍길동', 'age': 25, 'gender': '남'}
```

---

## 값 수정

```python
student["gender"] = "여"

print(student)
```

실행 결과

```text
{'name': '홍길동', 'age': 25, 'gender': '여'}
```

---

# 집합(Set)

집합은 **순서가 없고 중복을 허용하지 않는 변경 가능한(Mutable) 자료형**이다.

특징

- `{}`
- 중복 제거
- 인덱싱 불가능
- 슬라이싱 불가능

```python
numbers = {1, 2, 3, 3, 2}

print(numbers)
```

실행 결과

```text
{1, 2, 3}
```

---

## 집합 연산

```python
set1 = {1, 2, 3}
set2 = {3, 6, 9}
```

합집합

```python
print(set1 | set2)
```

```text
{1, 2, 3, 6, 9}
```

차집합

```python
print(set1 - set2)
```

```text
{1, 2}
```

교집합

```python
print(set1 & set2)
```

```text
{3}
```

---

# Boolean

Boolean은 참(True)과 거짓(False)을 표현하는 자료형이다.

주로 비교 연산과 논리 연산의 결과로 사용된다.

```python
print(10 > 3)
print(10 == 3)
```

실행 결과

```text
True
False
```

---

# None

`None`은 **값이 없음을 나타내는 객체**이다.

Java의 `null`과 비슷한 개념이다.

```python
name = None

print(name)
```

실행 결과

```text
None
```

---

# Collection

Collection은 여러 개의 데이터를 하나로 묶어 저장하는 자료형이다.

대표적인 Collection

- List
- Tuple
- Dictionary
- Set

---

# 불변(Immutable)과 가변(Mutable)

컬렉션은 생성 후 내용을 변경할 수 있는지에 따라 나뉜다.

| 자료형 | 변경 가능 |
|---------|-----------|
| str | ❌ |
| list | ✅ |
| tuple | ❌ |
| range | ❌ |
| dict | ✅ |
| set | ✅ |

---

## 불변(Immutable)

![alt text](../../images/python_불변가변.png)

새로운 객체가 생성된다.

```python
name = "Kim"

name += " Lee"

print(name)
```

---

## 가변(Mutable)

기존 객체의 내용이 변경된다.

```python
numbers = [1, 2]

numbers.append(3)

print(numbers)
```

실행 결과

```text
[1, 2, 3]
```

---

# 핵심 정리

- `int`는 정수, `float`는 실수이다.
- 문자열(`str`)은 변경할 수 없다.
- 리스트(`list`)는 생성 후 수정할 수 있다.
- 튜플(`tuple`)은 생성 후 수정할 수 없다.
- `range`는 연속된 정수를 생성한다.
- 딕셔너리(`dict`)는 Key-Value 형태로 데이터를 저장한다.
- 집합(`set`)은 중복을 허용하지 않는다.
- `None`은 값이 없음을 의미한다.
- 자료형은 **불변(Immutable)** 과 **가변(Mutable)** 으로 구분할 수 있다.