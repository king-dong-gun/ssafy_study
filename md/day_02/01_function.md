## 1. 함수(Function)

💡특정 작업을 수행하기 위한 **재사용 가능한 코드 묶음**


함수를 사용하는 이유는?

1. 코드의 중복을 방지한다.
2. `재사용성`이 높아지고, `가독성`과 `유지보수성`이 향상한다.

#### 함수 사용 전

```python
# 5와 3을 더하기
num1 = 5
num2 = 3
result1 = num1 + num2
print(result1) # 8 

# 10과 20을 더하기 -> 코드 중복
num3 = 10
num4 = 20
result2 = num3 + num4
print(result2) # 30
```

#### 함수 사용 후

```python
# 덧셈 기능의 함수 정의
def get_sum(num1, num2):
	return num1+ num2
	
# 다른 입력 값으로 함수 사용
result_1 = get_sum(5, 3)
result_2 = get_sum(10, 20)

# 결과 값
print(result_1) # 8
print(result_2) # 30
```

### 함수 정의와 호출

1. 함수 정의
    - 함수 정의는 `def` 키워드로 시작하며 이후 함수명을 작성한다.
    - 괄호 안에 매개변수를 정의한다.
        - 매개변수는(parameter)는 함수에 전달되는 값이다.
2. 함수 body
    - 콜론 (:) 다음에 들여쓰기 된 코드 블록이다.
    - 함수가 실행 될 때 수행되는 코드를 정의한다.
3. Docstring
    - 함수 body 앞에 선택적으로 작성 가능한 함수 설명서이다.
4. 함수 반환 값
    - `return` 키워드 이후 반환할 값을 명시한다.
    - `return` 문은 함수의 실행을 종료하고 결과를 호출 부분으로 반환한다.
    - `return` 값이 없다면 `None` 을 반환한다.
5. 함수 호출
    - 함수명과 소괄호를 활용해 호출한다.
    - 필요한 경우 인자(argument)를 전달한다.
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입된다.

---

## 2. 함수와 반환 값

> 💡print() 함수는 반환 값이 없다!!!!!


1. print() 함수는 화면에 값을 `출력만 할 뿐, 반환 (return)이 없다`.
2. Python에서는 반환 값이 없는 함수는 기본적으로 `None` 으로 간주된다.

#### 예시

```python
retrun_value = print(1)
print(return_value) # None
```

```python
def my_func():
	print("hello")
	
result = my_func()
print(result) # None
```

---

## 3. 매개변수와 인자

1. 매개변수 `parameter` 
    - 함수를 정의할 때 입력받을 값을 저장하기 위해 사용하는 변수이다.
2. 인자 `argument` 
    - 함수를 호출할 때 실제로 전달하는 값이다.

```python
def add_numbers(first_num, second_num) # first_num, second_num는 파라미터
	result = first_num + second_num
	retun result
	
num1 = 1
num2 = 2

sum_result = add_numbers(num1, num2) # num1, num2는 아규먼트
print(sum_result)
```

---

## 4. 인자의 종류

1. 위치 인자
    - 함수 호출 시 인자의 위치에 따라 전달되는 인자
    - 위치 인자는 함수 호출 시 반드시 값을 전달해야 한다.
    
    ```python
    def greet(name, age)
    	print(f"안녕? {name}야 난 {age}살이야")
    
    greet("Dave", 30) # 안녕? Dave야 난 30살이야
    greet(30, "Dave") # 안녕? 30야 난 Dave살이야
    
    greet("Dave") # TypeError: greet() missing 1 required positional argument: 'age'
    ```
    
2. 기본 인자 값
    - 함수 정의에서 매개변수에 기본 값을 할당하는 것이다.
    - 함수 호출 시 인자를 전달하지 않으면, 기본값이 `파라미터`에 할당된다.
    
    ```python
    def greet(name, age = 30)
    	print(f"안녕? {name}야 난 {age}살이야")
    
    greet(name = "Dave") # 안녕? Dave야 난 30살이야
    greet(name = "Dave", age = 50) # 안녕? Dave야 난 50살이야
    ```
    
3. 키워드 인자
    - 함수 호출 시 `Key` , `Value` 형태로 값을 전달하는 인자
    - 파라미터와 인자를 일치시키지 않고, 특정 파라미터에 값을 할당할 수 있다.
    - 인자의 순서는 중요하지 않고, 인자의 이름을 명시하여 전달한다.
    - **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 한다!**
    
    ```python
    def greet(name, age)
    	print(f"안녕? {name}야 난 {age}살이야")
    
    greet(name = "Dave", age = 30) # 안녕? Dave야 난 30살이야
    greet(age = 30, name = "Dave") # 안녕? Dave야 난 30살이야
    
    greet(age = 30, "Dave") # positional argument follows keyword argument
    ```
    
    4. 임의의 인자 목록
    
    - 정해지지 않은 개수의 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 `*` 를 붙여서 사용한다.
    - 여러 개의 인자를 튜플로 처리한다.
    1. 임의의 키워드 인자 목록
        - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
        - 함수 정의 시 매개변수 앞에 `**` 를 붙여서 사용한다.
        - 여러 개의 인자를 딕셔너리로 처리한다.
    
   
   > 💡 함수 인자 권장 작성 순서
    `위치`  → `기본` → `가변` → `가변 키워드` 
     **상황에 따라 유연하게 조정해서 사용해라!!**
    
    ---
    
### 5. 재귀 함수

> 💡 함수 내부에서 자기 자신을 다시 호출하는 함수이다.

```python
def count(num):
    if num > 5:
        return

    print(num)
    count(num + 1)

count(1)
```

#### 사용하는 이유

- 반복되는 문제를 간결하게 해결할 수 있다.
- 상황에 따라 반복문보다 알고리즘 코드가 더 명확해질 수 있다.

#### 특징

- 자기 자신을 호출한다.
- **반드시 종료 조건(Base Case)** 이 있어야 한다.
- 종료 조건이 없으면 `RecursionError`가 발생한다.
    
    
   ![](https://velog.velcdn.com/images/king-dong-gun/post/27bce814-5c61-44b2-88b7-a6b77cebf048/image.png)

    
---
    
### 6. 내장 함수

> 💡 파이썬에 기본적으로 내장된 함수이다.

```python
len(iterable)
sum(iterable)
max(iterable)
min(iterable)
sorted(iterable)
```

---

### 7. 함수와 Scope

> 💡 함수는 코드 내부에 `Local Scope`를 생성하고, 그 외 공간을 `Global Scope`로 구분한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/93299a06-8d0a-4e19-9e95-e791f3ef75c3/image.png)


#### Scope 예시

```python
def func():
    num = 20
    print("local", num)  # local 20

func()
print("global", num)
# NameError: name 'num' is not defined
# global scope에 num 정의 X
```

#### 이름 검색 규칙

```text
Local Scope      # 지역 범위(현재 작업 중) ← 가장 먼저 탐색
    ↓
Enclosed Scope   # 지역 범위 한 단계 위 범위
    ↓
Global Scope     # 최상단에 위치한 범위
    ↓
Built-in Scope   # 정의하지 않고 사용할 수 있는 모든 것
```

---

### 8. global 키워드

> 💡 변수의 Scope를 전역 범위로 지정하기 위해 사용한다.

#### 예시

```python
num = 0  # 전역 변수

def increment():
    global num
    num += 1

print(num)  # 0
increment()
print(num)  # 1
```

---

### 참고

#### 1. 함수명 작성 규칙

- 소문자와 언더스코어(`snake_case`)를 사용한다.
- 동사로 시작해 함수의 동작을 설명한다.
- 약어 사용을 지양한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/20c06fac-6f78-42ba-a380-a1a5fcc939eb/image.png)


#### 2. 단일 책임 원칙

- 모든 객체는 하나의 명확한 목적과 책임만을 가져야 한다.

> `명확한 목적`, `책임 분리`, `유지보수성`

#### 3. 람다 표현식

> 💡 익명 함수를 만드는데 사용되는 표현식으로, 한 줄로 간단한 함수를 정의한다.

![image.png]

```python
lambda 매개변수: 표현식
```

---

### 정리

- 함수 : 재사용 가능한 코드 묶음
- `return` : 값을 반환
- `print()` : 화면에 출력 (`None` 반환)
- `Parameter` : 정의할 때의 변수
- `Argument` : 호출할 때 전달하는 값
- `*args` : 여러 위치 인자 → 튜플
- `**kwargs` : 여러 키워드 인자 → 딕셔너리
- `재귀 함수` : 자기 자신을 호출하는 함수 (종료 조건 필수)
- `LEGB` : Local → Enclosed → Global → Built-in
- `global` : 함수 내부에서 전역 변수 수정
- `lambda` : 한 줄로 작성하는 익명 함수