### 1. 객체

#### Object

> 키로 구분된 데이터 집합을 저장하는 자료형이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/cee587f1-1def-4b52-82b6-2fba3f1a486d/image.png)


#### 객체 구조

- 중괄호 `{}` 를 사용해서 작성한다.
- 중괄호 안에는 `key: value` 쌍으로 구분된 속성을 여러 개 작성 가능하다.
- `key` 는 문자열만 허용하고, 숫자 키도 문자열로 변환된다.
- `value` 는 모든 자료형을 허용한다.

```jsx
// 1. 객체 구조
// - { key: value } 쌍(속성)의 모음
// - key는 문자열(띄어쓰기가 있으면 따옴표 필요), value는 모든 자료형 가능 (함수도 가능 = 메서드)
const user = {
	name: "Alice",
	"key with space": true,
	gretting: function() {
		return "hello"
	}
}
console.log(user.name)
console.log(user['key with space'])

// 추가
user.address = 'korea'
console.log(user)

// 수정
user.name = 'Bella'
console.log(user.name)

// 삭제
delete user.name
console.log(user)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/dae601ed-b965-40dc-9f87-66186df64949/image.png)


#### in 연산자

> 객체에 특정 속성이 존재하는지 확인하는 연산자이다.
>
- 존재하면 `true`, 존재하지 않으면 `false`를 반환한다.
- 객체 자신의 속성뿐 아니라 **프로토타입에서 상속받은 속성도 확인한다.**
- 배열에서는 특정 인덱스에 요소가 존재하는지도 확인할 수 있다.

```jsx
const user = {
    name: "Alice",
    age: 25
}

console.log("name" in user)    
console.log("address" in user) 
console.log("toString" in user)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/12d76f34-40f3-444a-965b-916d34ea8339/image.png)


#### 프로토 타입

> 자바스크립트 객체가 다른 객체의 속성과 메서드를 상속받을 수 있도록 연결된 객체이다.
>
- 객체는 프로토타입을 통해 다른 객체의 기능을 사용할 수 있다.
- 객체에 없는 속성을 찾으면 프로토타입에서도 검색한다.
- 이러한 연결을 **프로토타입 체인(Prototype Chain)**이라고 한다.

---

### 2. 메서드와 this

#### Method

> 객체 속성에 정의된 함수이다.
>
- 객체의 속성 값이 함수이면 **메서드(Method)**라고 한다.
- 메서드는 객체의 동작이나 기능을 정의한다.
- `객체명.메서드명()` 형태로 호출한다.
- `this` 키워드를 사용해 객체 자신의 속성이나 메서드에 접근하여 특정 작업을 수행 할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/2e073969-72d0-4443-883c-25d18eb2bf23/image.png)


```jsx
const person = {
    name: "Alice",
    greeting: function() {
        return "Hello"
    }
}

console.log(person.greeting())
```

![](https://velog.velcdn.com/images/king-dong-gun/post/0419806a-660a-4b2a-a3a3-a53068c91d95/image.png)


#### this

> 함수나 메서드를 호출한 객체를 가리키는 키워드이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/c40ae3b7-1090-4e32-b28e-4bb6c3117502/image.png)


```jsx
const person = {
    name: "Alice",
    greeting: function() {
        return `Hello my name is ${this.name}`
    }
}

console.log(person.greeting())
```

![](https://velog.velcdn.com/images/king-dong-gun/post/bd02b1fe-128b-4982-a6ae-9f5b0527370b/image.png)


| 호출 방법 | 대상 |
| --- | --- |
| 일반 함수에서의 단순 호출 | 전역 객체 |
| 객체에서의 메서드 호출 | 메서드를 호출한 객체 |

#### 단순 호출시 this

> 일반 함수에서 `this`는 전역 객체를 가리킨다. (브라우저의 일반 스크립트, 비엄격 모드 기준)
>

```jsx
const myFunc = function () {
    return this
}

console.log(myFunc())
```

![](https://velog.velcdn.com/images/king-dong-gun/post/2abaff32-50ea-4de6-b3ea-ea1415b10c2e/image.png)


- 일반 함수를 단독으로 호출하면 `this`는 전역 객체인 `window`를 가리킨다.
- 단, **엄격 모드(`'use strict'`)에서는 `this`가 `undefined`**이다.

#### 메서드 호출 시 this

> 객체의 메서드로 호출하면 `this`는 메서드를 호출한 객체를 가리킨다.
>

```jsx
const myObj = {
    data: 1,
    myFunc: function () {
        return this
    }
}

console.log(myObj.myFunc())
```

![](https://velog.velcdn.com/images/king-dong-gun/post/2d5ecddd-a3c2-4396-b328-d752fffbf79c/image.png)


- `myObj.myFunc()`에서 `this`는 `myObj`를 가리킨다.
- `this.data`를 사용하면 `myObj`의 `data` 속성에 접근할 수 있다.

#### 중첩된 함수에서의 `this` 문제점

- 일반 함수는 바깥쪽 함수의 `this`를 상속받지 않는다.
- 따라서 `forEach()` 내부의 일반 함수에서 `this`는 `window`를 가리킨다. (브라우저 비엄격 모드 기준)
- **화살표 함수는 자신만의 `this`가 없어 바깥쪽 함수의 `this`를 사용한다.**

**1. 일반 함수 사용**

```jsx
this.numbers.forEach(function (number) {
    console.log(this) // window
})
```

**2. 화살표 함수 사용 (해결)**

```jsx
this.numbers.forEach((number) => {
    console.log(this) // myObj3
})
```

**JavaScript `this` 정리**

- `this`는 함수가 **호출되는 방식**에 따라 가리키는 대상이 결정된다.
- 같은 함수라도 호출 방식에 따라 `this`가 달라질 수 있다.

**장점**

- 하나의 함수를 여러 객체가 공유하면서 각 객체의 데이터에 접근할 수 있다.

**단점**

- 호출 방식에 따라 `this`가 달라져 실수하기 쉽다.

**TIP**

- 일반 함수의 `this`는 호출 방식에 따라 결정된다.
- 화살표 함수는 자신만의 `this`가 없으며 바깥쪽 `this`를 사용한다.
- `this`를 이해할 때는 **"누가 함수를 호출했는가?"**를 확인하는 것이 중요하다.

---

### 3. JSON

> `Key - Value` 형태로 이루어진 자료 표기법이다.
>
1. JavaScript의 `Object`와 유사한 구조를 가지고 있지만, Json은 일정한 형식을 가진 **문자열**이다.
2. JavaScript에서 Json을 사용하기 위해 `Object` 자료형으로 변경해야 한다.
3. 특정 언어에 종속되지 않는 데이터 형식으로 API 통신 등에서 사용된다.

#### Object → JSON

- `JSON.stringify()` 를 사용해 객체를 문자열로 변환한다.

#### JSON → Object

- `JSON.parse()` 를 사용해서 문자열을 객체로 변환한다.

---

### 4. 추가 객체 문법

#### 단축 속성

- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용할 수 있다.

```jsx
const name = "Alice"
const age = 30
const user = {
	name: name,
	age: age
}

// 단축
const name = "Alice"
const age = 30
const user = {
	name, age
}
```

#### 단축 메서드

- 메서드 선언 시 `function` 키워드를 생략 가능하다.

```jsx
const myObj = {
	myFunc: function() {
		return "Hello"
	}
}

// 단축
const myObj = {
	myFunc() {
		return "Hello"
	}
}
```

#### 구조 분해 할당

- 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당할 수 있는 문법이다.
- 함수의 매개변수로도 객체 구조 분해 할당 활용이 가능하다.

```jsx
const userInfo = {
	firstName: 'Alice',
  userId: 'alice123',
  email: 'alice123@gmail.com'
}

// 구조 분해 할당 후 (세 줄 중 하나만 사용, 같은 이름을 다시 선언하면 에러)
// const { firstName } = userInfo
// const { firstName, userId } = userInfo
const { firstName, userId, email } = userInfo
```

#### 객체와 전개 구문

- 객체를 복사, 객체 내부에서 객체를 전개한다.
- 얉은 복사에 활용이 가능하다.

```jsx
const obj = { a: 2, c: 3, d: 4 }
// 전개 구문
// - 객체 안에서 다른 객체의 속성을 펼쳐 넣음 (얕은 복사)
// - 같은 key가 있으면 뒤에 쓴 값이 앞의 값을 덮어씀
const newObj = { ...obj, a: 1, e: 5 }
```

#### 유용한 객체 메서드

```jsx
// 6. 유용한 객체 메서드
// - key, value, [key, value] 쌍을 "배열"로 반환
const profile = {
  name: 'Alice',
  age: 30
}

console.log(Object.keys(profile))
console.log(Object.values(profile))
console.log(Object.entries(profile))
```

![](https://velog.velcdn.com/images/king-dong-gun/post/909e1b1b-9bfb-495c-95b5-3228df1b8664/image.png)


#### Optional chaining (`?.` )

- 속성이 없는 중첩 객체에 접근하려 할 때 에러 발생 없이 안전하게 접근하는 방법이다ㅣ.
- 만약 참조 대상이 `null` 또는 `undefined` 라면 에러가 발생하는 것 대신 평가를 멈추고 `undefined` 을 반환한다.

```jsx
// Optional Chaining
// - ?. 앞의 대상이 null 또는 undefined이면, 에러 대신 undefined를 반환하고 평가를 멈춤
const userData = {
    name: 'Alice',
    greeting: function () {
        return 'hello'
    }
}

// 예전 방식
console.log(userData.address && userData.address.street)

// 변수 옵셔널 체이닝
// ※ 에러가 나면 아래 코드가 실행되지 않으므로, 에러 줄은 주석을 풀어 따로 확인
// console.log(userData.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
console.log(userData.address?.street)

// 함수 옵셔널 체이닝
// console.log(userData.nonMethod()) // Uncaught TypeError: userData.nonMethod is not a function
console.log(userData.nonMethod?.())
```

![](https://velog.velcdn.com/images/king-dong-gun/post/1fb69993-e550-4dad-b872-3cd9b6132238/image.png)


#### Optional chaining (`?.` ) 장점

1. 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있다.
2. 어떤 속성이 필요한지에 대한 보증이 확실하지 않는 경우에 객체의 내용을 보다 편리하게 탐색할 수 있다.
3. 만약 Optional chaning을 사용하지 않는다면 아래 코드와 같이 `&&` 연산자를 사용해야 한다.

```jsx
const userData = {
	name = "Alice",
	greeting: function() {
		return "Hello"
	}
}

console.log(userData.address && userData.address.street)
```

#### Optional chaining (`?.` ) 주의사항

1. Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 한다. **(남용 X)**
2. Optional chaining 앞의 변수는 반드시 선언되어 있어야 한다.

---

### 5. 배열과 함수

#### 배열

> 순서가 있는 데이터 집합을 저장하는 자료구조이다.
>

#### 배열의 구조

- `[]` 대괄호를 이용해 작성한다.
- 요소의 자료형은 제약이 없다
- `push()` , `pop()` , `unshift()` , `shift()` 등 배열 조작 메서드가 있다.

```jsx
const names = ["Alice", "Bella", "Cathy"]
// 추가
names.push("Dan")
console.log(names)
// 삭제
console.log(names.pop())
//배열 앞에 요소 추가
names.unshift("Eric")
console.log(names)
//배열 앞 요소 제거 후 제거 요소 반환
console.log(names.shift())
console.log(names)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/a0cb0c14-8792-4d64-85ae-0b0aa49110b2/image.png)


#### 콜백 함수

> 힘수의 인자로 전달되어, 특정 시점에서 호출
>
- 다른 함수에 전달하여 필요할 때 실행하도록 하는 함수이다.
- 특정 작업이 완료되거나 조건이 충족되었을 때 실행할 수 있다.
- 일정 시간이 지난 후 실행하는 등 비동기 작업에도 활용된다.
- **콜백 함수가 반드시 나중에 실행되는 것은 아니다.** 즉시 실행될 수도 있다.

```jsx
// 1. 인자로 받을 콜백 함수 정의
const greeting = function(name) {
	console.log(`Hello, ${name}!`)
}

// 2. 힘수를 인자로 받는 메인 함수
const processUserInput = function(callback) {
	const name = "Anna"
	// 넘겨받은 함수를 실행
	callback(name)
}

// 3. 실행
processUserInput(greeting)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/fd2d9a1e-faf2-456b-bfb6-86e2a87b1e9d/image.png)


#### 콜백 함수를 사용하는 이유

1. 기능의 유연성
- 숫자를 계산하는 함수에서 더하기, 빼기, 곱하기 등 모든 경우의 수를 함수 하나에 다 넣으면 복잡해 진다.
    - **계산하는 로직만 바꿔 끼우면 해결이 된다.**

```jsx
const calculator = function(a, b, action) {
	return action(a, b)
}

// 콜백 함수
const add = (a, b) => a + b
const sub = (a, b) => a - b

console.log(calculator(10, 20, add))
console.log(calculator(10, 20, sub))
```

![](https://velog.velcdn.com/images/king-dong-gun/post/06e56390-9195-4a81-8687-4d324e863967/image.png)


2. 시점 제어
- **비동기 처리**
    - 어떤 작업이 시간이 걸릴 때 그 작업이 끝난 직후에 실행하고 싶을 때 사용한다.

```jsx
console.log("1. 주문하기")

// 3초 뒤에 실행
setTimeout(function() {
	console.log("2. 커피 나왔습니다 (콜백 실행)")
}, 3000)

console.log("기다리기")
```

![](https://velog.velcdn.com/images/king-dong-gun/post/1432a967-e9a3-43a8-b455-4a6fffe13aa5/image.png)


즉 콜백 함수의 특징은

**함수를 인자로 넘기고, 받은 쪽에서 그 함수를 실행하고, 반복적인 작업**을 시킬 때 아주 유용하다.

---

### 6. 배열의 진화

#### Array Helper Methods

> 배열을 순회하며 특정 로직을 수행하는 고차 함수의 모음이다.
>

#### forEach

- 배열의 요소를 처리하는 다양한 메서드를 제공한다.
- 함수를 인자로 전달하여 배열을 처리한다.
- 반환값은 `undefined` 이다.
- 멈출 수 없다 (`No break` )
    - forEach는 배열의 끝까지 무조건 실행해 `break` 나 `continue` 를 사용할 수 없다.

```jsx
const names = ['Alice', 'Bella', 'Cathy']
// 일반 함수
names.forEach(function (name) {
    console.log("일반 함수: ", name)
})
console.log("====================")
// 화살표 함수를 권장한다.
names.forEach((name) => {
    console.log("화살표 함수: ", name)
})
```

![](https://velog.velcdn.com/images/king-dong-gun/post/a5a157e2-81b1-469d-9bad-cfd81c1d5d3e/image.png)


#### map

> 배열의 모든 요소를 하나씩 순회하면서 콜백 함수의 반환값으로 **새로운 배열을 생성하는 메서드**이다.
>
- 배열의 각 요소에 콜백 함수를 실행한다.
- 콜백 함수의 반환값을 모아 새로운 배열을 만든다.
- 기존 배열은 변경하지 않는다.

```jsx
const names = ['Alice', 'Bella', 'Cathy']

// 일반 함수
const result1 = names.map(function (name) {
    return "일반 함수: " + name
})
console.log(result1)

console.log("====================")

// 화살표 함수를 권장한다.
const result2 = names.map((name) => {
    return "화살표 함수: " + name
})
console.log(result2)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/205d0009-8c81-4066-bfde-1435e419a4eb/image.png)


**forEach()와 map() 비교**

| 구분 | `forEach()` | `map()` |
| --- | --- | --- |
| 목적 | 배열 순회 및 작업 실행 | 배열 요소 변환 |
| 동작 | 각 요소에 콜백 함수 실행 | `return` 값을 모아 새 배열 생성 |
| 반환값 | `undefined` | 새로운 배열 |
| `return` | 반환값을 모으지 않음 | 반환값으로 새 배열 생성 |
| 기존 배열 | 자동 변경 X | 자동 변경 X |
| 간결함 | 새 배열 생성 시 별도 배열과 `push()` 필요 | `map()`만으로 새 배열 생성 |
| 직관성 | 순회하면서 수행할 작업을 표현 | 배열을 변환한다는 목적이 명확함 |
| 불변성 | `push()`로 원본 배열을 변경할 수 있음 | 원본 배열을 유지하고 새 배열 반환 |

---

### 7. filter

> 배열의 모든 요소를 순회하면서 **조건을 만족하는 요소만 추출하여 새로운 배열을 생성하는 메서드**이다.
>
- 콜백 함수의 반환값이 `true`인 요소만 새로운 배열에 포함한다.
- 조건에 맞는 요소가 없으면 빈 배열 `[]`을 반환한다.
- 기존 배열은 변경하지 않는다.

```jsx
const numbers = [1, 2, 3, 4, 5]

// 일반 함수
const result1 = numbers.filter(function (number) {
    return number > 3
})
console.log(result1)

// 화살표 함수
const result2 = numbers.filter((number) => {
    return number > 3
})
console.log(result2)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/002b426f-c328-4666-a51b-fb0a8fc33d15/image.png)


#### map과 filter

두 메서드 모두 새로운 배열을 반환하지만, 목적이 다르다.

| 구분 | `map()` (변형) | `filter()` (선별) |
| --- | --- | --- |
| 목적 | 요소를 가공하여 형태를 변경 | 조건에 맞는 요소만 골라냄 |
| 동작 | 모든 요소에 콜백 함수 적용 | 조건이 참인 요소만 유지 |
| 길이 | 원본과 동일 (1:1) | 원본보다 같거나 짧음 |
| 반환값 | 변형된 새로운 배열 | 조건에 맞는 요소로 구성된 새로운 배열 |
| 비유 | 빵 굽기 (밀가루 → 빵) | 과일 고르기 (썩은 과일 버리기) |
| 기존 배열 | 변경하지 않음 | 변경하지 않음 |