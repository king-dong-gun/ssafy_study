### 1. 상속

> 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것을 상속이라 한다.
>

#### 상속이 필요한 이유

1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있다.
    - 기존 클래스를 수정하지 않고도 기능을 확장할 수 있다.
2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있다.
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있다.
3. 유지 보수 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우 해당 클래스만 수정하면 되므로 유지 보수가 용이해진다.
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화할 수 있다.

#### 상속 예시

```python
class Animal
	def eat(self):
		print("먹는 중")

class Dog(Animal):
	def bark(self):
		print("멍멍")
		
my_dog = Dog()
my_dog.bark() # 멍멍

# 부모 클래스 메서드 사용 가능
my_dog.eat() # 먹는 중
```

![alt text](../../images/python_상속.png)

---

### 2. 메서드 오버라이딩

> 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의하는 것이다.
>
- 자식 클래스에서 메서드를 다시 정의하면, 부모 클래스의 메서드 대신 자식 클래스의 메서드가 실행된다.
- 오버라이딩은 동일한 이름과 매개변수를 사용하지만, 내부 동작을 원하는 대로 바꿀 수 있게 해준다.
- 부모 클래스의 기능을 유지하면서도 일부 동작을 맞춤형으로 바꾸고 싶을 때 유용하다.

```python
class Animal:
	def eat(self):
		print("Animal이 먹는 중")
	
class Dog(Animal):
	# 부모 클래스(Dog)의 eat 메서드를 재정의 (오버라이딩)
	def eat(self):
		print("Dog가 먹는 중")

my_dog = Dog()
my_dog.eat() # Dog가 먹는 중
```

---

### 3. 오버로딩

- 같은 이름, 다른 파라미터를 가진 여러 메서드를 정의하는 것이다. **(파이썬은 미지원이다… 참고만)**
- 파이썬은 마지막으로 선언된 메서드만 인식한다.

```python
class Example:
	def do_someting(self, x):
		print("첫 번째 do_something 메서드: " , x)
	
	# 파이썬에서는 메서드가 이름이 같으면 앞선 정의를 덮어쓴다.
	def do_someting(self, x, y):
		print("두 번쨰 do_something 메서드: ". x, y)
		
example = Example()

#TypeError: do_something() missing 1 required positional argument: "y"
example.do_something(10)
```

---

### 4. 다중 상속

>
>
> - 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있다.
> - 상속된 모든 클래스의 요소를 활용 가능하다.
> - 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정된다.**

![alt text](../../images/python_다중상속.png)

#### 다중 상속 예시

```python
class Person:
    ...

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):

    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'
        
 baby1 = FirstChild("애기")
 print(baby1.cry()) # 첫째가 응애
 print(baby1.swim()) # 첫째가 수영
 # FirstChild에는 없으므로 첫번째 부모 Dad에서 찾기
 print(baby1.walk()) # 아빠가 걷기
 print(baby1.gene()) # XY
```

#### 다이아몬드 문제

![alt text](../../images/python_다이아몬드문제.png)

```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass
    
d = D()
print(d.hello()) # B
```

- MRO 알고리즘을 사용해 메서드를 탐색할 클래스의 순서를 미리 정의한다.
- `MRO` : 파이썬이 메서드를 찾는 순서에 대한 규칙 (메서드 결정 순서)
    - **자식 클래스 우선**: 부모 클래스보다 자식 클래스를 먼저 탐색한다.
    - **왼쪽 부모 우선**: 다중 상속 시, 리스트에 나열된 순서(왼쪽에서 오른쪽)대로 탐색한다.
    - **중복 방문 방지**: 공통 부모 클래스는 모든 자식 클래스의 탐색이 끝난 뒤에 단 한번만 탐색한다.

---

### 5. super() 함수

> MRO에 따라 현재 클래스의 부모 클래스의 메서드나 속성에 접근할 수 있게 해주는 내장함수다.
>
- `super()` 를 사용하면 직접 부모 클래스 이름을 적지 않아도 MRO에 따라 자동으로 올바른 매서드를 찾아 실행할 수 있다.
- 다중상속에서 `super()` 를 호출하면 상속 순서에 맞춰 여러 부모 클래스의 메서드를 순차적으로 실행할 수 있다.
- 생성자나 오버라이딩 된 메서드에서 `super()` 를 호출하면 부모 클래스의 초기화나 로직을 그대로 활용 가능하다.

#### 단일 상속 예시

```python
class Person:
    def __init__(self, name):
        self.name = name
        print("Person 생성")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)      # 부모의 __init__ 호출
        self.grade = grade
        print("Student 생성")

s = Student("홍길동", 3)
```

**→ 부모 클래스에 이미 있는 코드를 다시 쓰지 않고 재사용**

#### 다중 상속 예시

```python
class A:
    def hello(self):
        print("A")

class B(A):
    def hello(self):
        print("B")
        super().hello()

class C(A):
    def hello(self):
        print("C")
        super().hello()

class D(B, C):
    pass

d = D()
d.hello()
```

#### MRO

```python
D
↓
B
↓
C
↓
A
↓
object
```

→ **부모를 호출하는 것이 아니라 MRO에서 다음 클래스를 호출한다.**

---

### 6. 정리

`상속(Inheritance)`: 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 것

`상속의 장점`: 코드 재사용, 계층 구조 형성, 유지보수 용이

`메서드 오버라이딩(Method Overriding)`: 부모의 메서드를 자식 클래스에서 같은 이름과 같은 매개변수로 다시 정의하는 것

`오버로딩(Overloading)`: 같은 이름의 메서드를 매개변수만 다르게 여러 개 정의하는 것 (파이썬은 지원하지 않으며 마지막 정의만 사용)

`다중 상속(Multiple Inheritance)`: 둘 이상의 부모 클래스로부터 속성과 메서드를 상속받는 것

`다이아몬드 문제(Diamond Problem)`: 여러 부모가 같은 조상을 가질 때 어떤 메서드를 사용할지 모호해지는 문제

`MRO(Method Resolution Order)`: 파이썬이 메서드와 속성을 탐색하는 순서(규칙)

`MRO 탐색 순서`: 자식 클래스 → 왼쪽 부모 → 오른쪽 부모 → 공통 부모 → object

`super()`: MRO에 따라 다음 클래스의 메서드나 생성자를 호출하는 내장 함수

`super() (단일 상속)`: 부모 클래스의 코드를 재사용하기 위해 사용

`super() (다중 상속)`: 부모가 아닌 MRO에서 다음 클래스의 메서드를 호출