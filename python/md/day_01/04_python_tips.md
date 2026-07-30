# Python 기초 ④ - 알아두면 좋은 Python 개념

Python를 처음 배우면 자주 헷갈리는 개념들을 정리했다.

---

# 다양한 진법 표현

Python은 다양한 진법을 코드에서 직접 표현할 수 있다.

| 진법 | 접두사 | 예시 |
|------|--------|------|
| 2진수 | `0b` | `0b10` |
| 8진수 | `0o` | `0o30` |
| 16진수 | `0x` | `0x10` |

```python
print(0b10)
print(0o30)
print(0x10)
```

실행 결과

```text
2
24
16
```

---

# 부동소수점 오차(Floating Point Error)

컴퓨터는 실수를 **2진수**로 저장한다.

이 과정에서 대부분의 실수는 정확하게 표현되지 못하고 근사값으로 저장된다.

```python
result = 0.1 + 0.2

print(result)
print(result == 0.3)
```

실행 결과

```text
0.30000000000000004
False
```

---

# decimal 모듈

정확한 소수 계산이 필요하다면 `decimal` 모듈을 사용한다.

```python
from decimal import Decimal

a = Decimal("3.2") - Decimal("3.1")
b = Decimal("1.2") - Decimal("1.1")

print(a)
print(b)
print(a == b)
```

실행 결과

```text
0.1
0.1
True
```

> 💡 금융 계산처럼 정확도가 중요한 경우 `float`보다 `Decimal`을 사용하는 것이 적합하다.

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

`None`을 비교할 때는 `==`보다 `is`를 사용하는 것이 권장된다.

```python
if name is None:
    print("값이 없습니다.")
```

---

# 불변(Immutable)과 가변(Mutable)

Python의 객체는 생성 후 수정 가능 여부에 따라 **불변**과 **가변**으로 나뉜다.

## 불변(Immutable)

- int
- float
- bool
- str
- tuple
- range

값을 변경하면 새로운 객체가 생성된다.

```python
name = "Kim"

print(id(name))

name += " Lee"

print(id(name))
```

실행 결과

```text
(첫 번째 id)
(다른 id)
```

> 💡 문자열을 수정하는 것이 아니라 새로운 문자열 객체가 생성된다.

---

## 가변(Mutable)

- list
- dict
- set

객체를 새로 만들지 않고 내부 데이터를 수정한다.

```python
numbers = [1, 2]

print(id(numbers))

numbers.append(3)

print(id(numbers))
```

실행 결과

```text
(같은 id)
(같은 id)
```

> 💡 리스트는 같은 객체를 유지한 채 내부 데이터만 변경된다.

---

# 얕은 복사(Shallow Copy)

변수에 객체를 그대로 대입하면 **같은 객체를 참조**한다.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

실행 결과

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

---

# 깊은 복사(Deep Copy)

새로운 객체를 생성하여 복사한다.

```python
import copy

a = [1, 2, 3]
b = copy.deepcopy(a)

b.append(4)

print(a)
print(b)
```

실행 결과

```text
[1, 2, 3]
[1, 2, 3, 4]
```

---

# id() 함수

객체의 고유한 식별값을 확인할 수 있다.

```python
a = [1, 2]
b = a

print(id(a))
print(id(b))
```

실행 결과

```text
같은 값
같은 값
```

같은 객체를 참조하고 있음을 확인할 수 있다.

---

# type() 함수

객체의 자료형을 확인할 수 있다.

```python
print(type(10))
print(type(3.14))
print(type("Python"))
print(type([1, 2, 3]))
```

실행 결과

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
```

---

# isinstance()

특정 자료형인지 확인할 때 사용한다.

```python
num = 10

print(isinstance(num, int))
print(isinstance(num, float))
```

실행 결과

```text
True
False
```

---

# 정리

- Python은 2진수, 8진수, 16진수를 직접 표현할 수 있다.
- `float`는 부동소수점 오차가 발생할 수 있다.
- 정확한 소수 계산은 `decimal.Decimal`을 사용한다.
- `None`은 값이 없음을 나타내는 객체이다.
- 문자열과 숫자는 **불변 객체**이다.
- 리스트, 딕셔너리, 집합은 **가변 객체**이다.
- 객체의 고유한 식별값은 `id()`로 확인할 수 있다.
- 자료형은 `type()`과 `isinstance()`로 확인할 수 있다.
- 복사할 때는 **얕은 복사**와 **깊은 복사**의 차이를 이해해야 한다.