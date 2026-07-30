# 제어문

> 코드가 실행되는 순서와 흐름을 제어하는 구문이다.  
> 조건에 따라 코드를 선택해서 실행하거나, 같은 코드를 반복해서 실행할 때 사용한다.

제어문은 크게 다음과 같이 나눌 수 있다.

- **조건문**: 조건에 따라 실행할 코드를 선택한다.
- **반복문**: 특정 코드를 여러 번 반복한다.

---

## 1. 조건문

> 주어진 조건식을 평가하여 결과가 `True`인지 `False`인지에 따라 실행할 코드를 결정한다.

### `if`문

조건문의 기본 형태이다.  
조건식이 `True`이면 들여쓰기된 코드 블록을 실행한다.

```python
temperature = 33

if temperature >= 33:
    print("폭염주의보입니다.")

print("오늘 기온:", temperature)
```

출력:

```text
폭염주의보입니다.
오늘 기온: 33
```

`temperature >= 33`의 결과가 `True`이므로 `if`문 내부의 코드가 실행된다.

---

### `elif`문

앞의 조건이 `False`일 때 추가 조건을 검사한다.

- `elif`는 여러 개 작성할 수 있다.
- 위에서부터 조건을 검사한다.
- 처음으로 `True`가 된 코드 블록만 실행한다.

```python
rank = 5

if rank == 1:
    print("금메달")
elif rank == 2:
    print("은메달")
elif rank == 3:
    print("동메달")

print("경기 종료")
```

출력:

```text
경기 종료
```

`rank`가 `1`, `2`, `3` 중 어느 값에도 해당하지 않으므로 메달은 출력되지 않는다.

---

### `else`문

앞의 모든 조건이 `False`일 때 실행한다.

`else`에는 별도의 조건식을 작성하지 않는다.

```python
age = 17

if age >= 19:
    result = "입장 가능합니다."
else:
    result = "입장 불가능합니다."

print("고객님은", result)
```

출력:

```text
고객님은 입장 불가능합니다.
```

`age >= 19`가 `False`이므로 `else`문이 실행된다.

![alt text](../../images/python_조건문.png)

---

## 2. 반복문

> 같은 코드 블록을 여러 번 반복해서 실행하는 구문이다.

파이썬의 대표적인 반복문에는 `for`문과 `while`문이 있다.

---

### `for`문

리스트, 문자열, 튜플처럼 반복 가능한 객체의 요소를 하나씩 꺼내면서 반복한다.

반복할 데이터나 횟수가 정해져 있을 때 주로 사용한다.

```python
item_list = ["apple", "banana", "coconut"]

for item in item_list:
    print(item)
```

출력:

```text
apple
banana
coconut
```

반복할 때마다 `item` 변수에 리스트의 값이 하나씩 들어간다.

```text
첫 번째 반복: item = "apple"
두 번째 반복: item = "banana"
세 번째 반복: item = "coconut"
```

---

### `range()`

`range()`는 일정한 범위의 숫자를 만들어 반복할 때 자주 사용한다.

```python
for i in range(5):
    print(i)
```

`range(5)`는 `0`부터 `4`까지의 숫자를 만든다.

출력:

```text
0
1
2
3
4
```

> `range(5)`에서 마지막 숫자 `5`는 포함되지 않는다.

---

### 중첩 반복문

반복문 안에 또 다른 반복문을 작성할 수 있다.

```python
outers = ["A", "B"]
inners = ["C", "D"]

for outer in outers:
    for inner in inners:
        print(outer, inner)
```

출력:

```text
A C
A D
B C
B D
```

실행 순서는 다음과 같다.

```text
outer = "A"
    inner = "C" → A C
    inner = "D" → A D

outer = "B"
    inner = "C" → B C
    inner = "D" → B D
```

바깥쪽 반복문이 한 번 실행될 때마다 안쪽 반복문은 처음부터 끝까지 실행된다.

```text
바깥쪽 반복 2번 × 안쪽 반복 2번 = 총 4번
```

---

### `while`문

조건식이 `True`인 동안 코드 블록을 반복한다.

반복 횟수가 정확하게 정해져 있지 않고, 특정 조건이 만족될 때까지 반복해야 할 때 주로 사용한다.

```python
count = 1

while count < 3:
    print(count)
    count += 1

print("끝")
```

출력:

```text
1
2
끝
```

실행 과정:

```text
count = 1 → 1 < 3은 True → 1 출력 → count는 2
count = 2 → 2 < 3은 True → 2 출력 → count는 3
count = 3 → 3 < 3은 False → 반복 종료
```

다음 코드는 `count`에 1을 더한 뒤 다시 저장한다.

```python
count += 1
```

아래 코드와 같은 의미이다.

```python
count = count + 1
```

`count += 1`이 없다면 `count`가 계속 `1`이므로 조건이 항상 `True`가 된다.

```python
count = 1

while count < 3:
    print(count)
```

출력:

```text
1
1
1
1
...
```

이처럼 반복문이 끝나지 않는 상태를 **무한 반복** 또는 **무한 루프**라고 한다.

---

## 3. 반복 제어 키워드

반복문 실행 중에 반복의 흐름을 바꾸기 위해 `break`와 `continue`를 사용할 수 있다.

---

### `break`

`break`를 만나면 현재 반복문을 즉시 종료한다.

```python
for i in range(5):
    if i == 2:
        break

    print(i)
```

출력:

```text
0
1
```

실행 과정:

```text
i = 0 → 출력
i = 1 → 출력
i = 2 → break 실행 → 반복문 종료
```

`break`를 만나면 `2`, `3`, `4`는 출력되지 않는다.

> 중첩 반복문에서 `break`를 사용하면 가장 가까운 안쪽 반복문만 종료한다.

---

### `continue`

`continue`를 만나면 현재 반복의 남은 코드를 건너뛰고 다음 반복으로 넘어간다.

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

출력:

```text
0
1
3
4
```

`i`가 `2`일 때 `continue`를 만나므로 아래의 `print(i)`가 실행되지 않는다.

```text
i = 0 → 출력
i = 1 → 출력
i = 2 → continue → 출력하지 않고 다음 반복
i = 3 → 출력
i = 4 → 출력
```

---

## 4. `map()` 내장 함수

> `map()`은 제어문은 아니지만, 반복 가능한 객체의 모든 요소에 같은 함수를 적용할 때 사용한다.

기본 구조:

```python
map(function, iterable)
```

- `function`: 각 요소에 적용할 함수
- `iterable`: 리스트, 튜플 등 반복 가능한 객체

---

### 문자열 리스트 만들기

```python
numbers1 = input().split()
print(numbers1)
```

사용자가 다음과 같이 입력하면:

```text
1 2 3
```

`input()`은 입력값 전체를 문자열로 받는다.

```python
"1 2 3"
```

`split()`은 공백을 기준으로 문자열을 나눈다.

```python
["1", "2", "3"]
```

출력:

```text
['1', '2', '3']
```

각 값은 숫자가 아니라 문자열이다.

---

### 정수 리스트 만들기

```python
numbers2 = list(map(int, input().split()))
print(numbers2)
```

사용자가 다음과 같이 입력하면:

```text
1 2 3
```

실행 과정은 다음과 같다.

```text
input()
→ "1 2 3"

input().split()
→ ["1", "2", "3"]

map(int, ["1", "2", "3"])
→ 각 문자열에 int() 적용

list(...)
→ [1, 2, 3]
```

출력:

```text
[1, 2, 3]
```

각 문자열에 `int()`를 반복해서 적용하는 과정은 다음과 같다.

```text
"1" → int("1") → 1
"2" → int("2") → 2
"3" → int("3") → 3
```

반복문으로 작성하면 다음과 비슷하다.

```python
numbers = []

for number in input().split():
    numbers.append(int(number))

print(numbers)
```

> `map()`의 결과는 바로 리스트가 아니므로, 리스트가 필요하면 `list()`로 변환한다.

---

## 핵심 정리

| 구분 | 의미 | 사용 예시 |
|:---|:---|:---|
| **`if`** | 조건이 `True`이면 코드를 실행한다. | `if age >= 19:` |
| **`elif`** | 앞의 조건이 `False`일 때 다른 조건을 검사한다. | `elif rank == 2:` |
| **`else`** | 앞의 모든 조건이 `False`일 때 실행한다. | `else:` |
| **`for`** | 반복 가능한 객체의 요소를 하나씩 꺼내 반복한다. | `for item in items:` |
| **`while`** | 조건이 `True`인 동안 반복한다. | `while count < 3:` |
| **`break`** | 반복문을 즉시 종료한다. | `if i == 2: break` |
| **`continue`** | 현재 반복의 남은 코드를 건너뛰고 다음 반복으로 넘어간다. | `if i == 2: continue` |
| **`map()`** | 반복 가능한 객체의 각 요소에 같은 함수를 적용한다. | `map(int, values)` |

> **조건문은 실행할 코드를 선택하고, 반복문은 코드를 여러 번 실행하며, `break`와 `continue`는 반복의 흐름을 조절한다.**