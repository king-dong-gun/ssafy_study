## Python_Data Structure

### 1. 비시퀀스 데이터 구조

![alt text](../../images/python_비시퀀스시퀀스.png)

---

### 2. 딕셔너리 메서드

1. `.get(key[,default])` 
    - 키에 연결된 값을 반환한다.
    - 키가 없으면 None 혹은 기본 값을 반환한다.

```python
person = {"name": "Alcie", "age": 25}

print(person.get("name") # Alice
print(person.get("country") # None
print(person.get("country", "Unknown") # Unknown
print(person["country"] # KeyError: "country"
```

1. `.keys()`
    - 딕셔너리 키를 모은 객체를 반환한다.

```python
person = {"name": "Alcie", "age": 25}
print(person.keys()) # dict_keys(["name", "age"])
for item in person.keys():
	print(item)
"""
name
age
"""
```

1. `values()` 
    - 딕셔너리 값을 모은 객체를 반환한다.

```python
person = {"name": "Alcie", "age": 25}
print(person.values()) # dict_values(["Alice", "25"])
for item in person.values():
	print(item)
"""
Alice
25
"""
```

1. `items()` 
    - 딕셔너리 키/값 쌍을 모은 객체를 반환한다.

```python
person = {"name": "Alcie", "age": 25}
print(person.values()) # dict_items([("name", "age") ("Alice", "25")])
for item in person.values():
	print(item)
"""
name Alice
age 25
"""
```

1. `.setdefault(key[,default])` 
    - 키와 연결된 값을 반환한다.
    - 키가 없다면 `default` 와 연결한 키를 딕셔너리에 추가하고 `default` 를 반환한다.

```python
person = {"name": "Alcie", "age": 25}

print(person.setdefault("country", "Korea")) # Korea
print(person) # {"name": "Alice", "age": 25, "country": "Korea"}
```

1. `.update([*other*])`
    - `other` 가 제공하는 키/값 쌍으로 딕셔너리를 갱신하고 기존 키는 덮어쓴다.

```python
person = {"name": "Alcie", "age": 25}
other_person = {"name": "Jane", "country": "Korea"}

person.update(other_person)
print(person) # {"name": "Jane", "age": 25, "country": "Korea"}

person.update(age= 100, address = "Seoul")
print(person) # {"name": "Jane", "age": 100, "country": "Korea", "address": "Seoul"}

```

1. `pop(key[,default])`
    - 키를 제거하고 연결됐던 값을 반환한다. (없으면 에러나 `default`를 반환한다.)

```python
person = {"name": "Alcie", "age": 25}
print(person.pop("age")) # 25
print(person) # {"name": "Alice"}
print(person.pop("country", None)) # None
print(person.pop("country")) # KeyError
```

1. `clear()` 
    - 딕셔너리의 모든 키/값 쌍을 제거한다.

```python
person = {"name": "Alcie", "age": 25}
person.clear()
print(person) # {}
```

---

### 2. 딕셔너리의 확장: `defaultdict`

#### `defaultdict` : 파이썬 내장 모듈 collections에서 제공하는 딕셔너리의 확장판이다.

> 딕셔너리에 존재하지 않는 키를 조회할때, 자동으로 “기본값”을 생성해주는 자료구조이다.
KeyError 걱정 없이 값을 수정하거나 추가할 때 매우 유용하다.
> 

#### 기본 딕셔너리 vs defaultdict

1. 기존 딕셔너리

```python
text = "banana"
counts = {}

for char in text:
	if char not in counts: # 키가 있는지 매번 확인
		counts[char] = 0
	counts[char] += 1
	
print(counts) # {"b":1, "a": 3, "n": 2}
```

1. defaultdict

```python
from collections import defaultdict

text = "banana"
counts = defaultdict(int) # 기본값을 정수(0)으로 설정

for char in text:
	# 키 확인 불필요! 없으면 0으로 자동 생성 후 +1
	counts[char] += 1

print(counts) # defaultdict(<class "int">, {"b": 1, "a": 3, "n": 2})
```

#### defaultdict 구문 및 활용 가이드

- 사용법: defaultdict(자료형) 형태로 선언한다.
- 자주 쓰는 패턴
    1. 숫자 세기: `defaultdict(int)`  → 키가 없으면 0으로 초기화
    2. 그룹핑/리스트 모으기: `defaultdict(list)`  → 키가 없으면 빈 리스트 [] 로 초기화

#### defaultdict 주의사항

- defaultdict 조회만 해도 키가 생성된다.
- “**단순히 키가 있는지 확인할 때**” 는 주의해서 사용해야한다.

---

### 3. Set

> 고유한 항목들의 정렬되지 않은 컬렉션이다.
> 
1. Set은 내부적으로 해시 테이블을 사용하여 데이터를 저장한다.
2. 항목의 고유성을 효율적으로 보장하고, 항목의 추가, 삭제, 존재 여부 확인이 데이터의 크기에 관계 없이 매우 빠르다.
3. 수학적인 잡합 연산을 간편하게 수행할 수 있는 것이 가장 큰 특징이다.

#### set 메서드

1. `.add(x)` : 세트에 x를 추가한다.

```python
my_set = {"a", "b", "c", 1, 2, 3}

my_set.add("d")
print(my_set) # {1, "b", 3, 2, "c", "d", "a"}

my_set.add("d")
# 순서가 없지만 같은 프로그램을 실행하는 동안은 같은 순서
print(my_set) # {1, "b", 3, 2, "c", "d", "a"}
```

1. `.remove(x)` : 항목에서 x를 제거한다. x가 없을 경우 keyError가 발생한다.

```python
my_set = {"a", "b", "c", 1, 2, 3}

my_set.remove(2)
print(my_set) # {"b", 1, 3, "c", "a"}

my_set.remove(10) # KeyError: 10
```

#### 세트의 집합 메서드

![alt text](../../images/python_set.png)

---

### 해시 테이블

> 해시 테이블은 `키, 값` 을 저장하는 자료구조이다.
> 

#### 해시 테이블의 원리

1. 키를 해시 함수를 통해 해시 값으로 변환한다.
2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾는다.
3. 이로 인해 검색, 삽입, 삭제를 매우 빠르게 수행한다.

![alt text](../../images/python_해시테이블.png)

#### 해시란?

> **임의의 크기**를 가진 데이터를 고정된 크기의 **고유한 값**으로 변환하는 것 이다.
> 

#### set의 요소 & dict의 키와 해시 테이블 관계

1. set
    - 각 요새를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷에 위치시킨다.
    - 이에따라 `순서` 보다는 `버킷 위치 (인덱스)` 가 요소의 위치를 결정한다.
    - 따라서 set은 `순서를 보장하지 않는다!!!`
2. dict
    - 키 → 해시 함수 → 해시 값 → 해시 테이블 저장
    - set와 달리 삽입 순서는 유지한다는 것이 언어 사양데 따라 보장된다. (python 3.7이상)
        - 키를 추가한 순서대로 반복문 순회할 때 나오게 된다.
        - 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계된 것 이다.
3. pop
    - 정수(숫자)값은 해시 값 숫자 자기 자신과 동일하거나 단순 계산으로 고정된다.
    - 문자열은 해시 계산 시 해시 난수화가 적용되므로, 실행마다 순서가 달라질 수 있다.

#### 난수 시드 (Random Seed)

> **난수를 생성할 때 사용하는 시작값**
> 
1. **계산 순서**
    1. 시드(seed)를 설정한다.
    2. 시드를 기준으로 난수 생성 알고리즘이 실행된다.
    3. 난수가 생성된다.
    4. **같은 시드 → 같은 난수**, **다른 시드 → 다른 난수**

**예시**

```
random.seed(10)

10(시드)
    ↓
난수 생성 알고리즘
    ↓
5 → 2 → 6 → 1 ...
```

---

#### 해시 난수화 (Random Seed)

> **프로그램 실행마다 해시 계산에 사용할 시드를 바꿔 보안을 강화하는 기능**
> 
1. **계산 순서**
    1. 프로그램이 시작된다.
    2. 파이썬이 **랜덤한 Hash Seed**를 생성한다.
    3. Hash Seed를 이용해 `hash()` 값을 계산한다.
    4. 계산된 해시값으로 `dict`, `set`의 저장 위치를 결정한다.
    5. 프로그램을 다시 실행하면 Hash Seed가 바뀌어 저장 위치도 달라질 수 있다.

**예시**

```
프로그램 시작
      ↓
Hash Seed 생성 (1234)
      ↓
hash("apple") 계산
      ↓
저장 위치 결정
```

다시 실행

```
프로그램 시작
      ↓
Hash Seed 생성 (9876)
      ↓
hash("apple") 계산 (이전과 다른 값)
      ↓
저장 위치 변경
```

#### hashable

- hash() 함수에 넣어 해시 값을 구할 수 있는 객체를 의미한다.
- 대부분의 불변 타입은 해시가 가능하다.
    - `int`, `str` , `tuple`  (단, 내부에 불변만 있을 경우에만)
- 가변형 객체 (`list`, `dict` , `set` )은 기본적으로 해시 불가능하다.
    - 값이 변하면 해시 값도 달라질 수 있어서 해시 테이블 무결성이 깨지기 때문