### 1. 데이터 타입

#### 원시 자료형

- 값 자체가 변수에 직접 저장되는 자료형이다.
- **불변**이며 변수 간 할당 시 값이 복사된다.
- `Number` , `String` , `Boolean` , `null` , `undefined` 등

#### 참조 자료형

- 데이터가 저장된 메모리의 주소가 변수에 저장되는 자료형이다.
- **가변**이며 변수 간 할당 시 주소가 복사된다.
- `Object` , `Array` , `Function` 등

---

### 2. 연산자 종류

#### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

```jsx
let a = 0

a += 10
console.log(a)

a -= 3
console.log(a)

a += 10
console.log(a)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/9758d295-7028-4121-bba1-dd4ded5b57b2/image.png)


#### 증가 & 감소 연산자

- 증가 연산자 `++` : 피연산자를 1 증가시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환한다.
- 감소 연산자 `--` : 피연산자를 1 감소시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환한다.

```jsx
let x = 3
const y = x ++
console.log(x, y)

let m = 3
const n = ++n
console.log(m, n)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/af0f41ff-34e0-43a0-8cc3-6f6a8e8a9a95/image.png)


#### 비교 연산자

- 피연산자들 (숫자, 문자, Boolean)을 비교하고 겨과 값을 boolean으로 반환하는 연산자

```jsx
console.log(3 > 2)
console.log(3 < 2)
console.log("A" < "B")
console.log("Z" < "a")
console.log("가" < "나")
```

![](https://velog.velcdn.com/images/king-dong-gun/post/5ea6290e-15f5-4c78-a526-925db40e551c/image.png)


#### 동등 연산자

- 두 연산자가 같은 값으로 평가 `==` 되는지 비교한 후 boolean 값을 반환
- **암묵적 타입 변환**을 통해 타입을 일치시킨 후 같은 값인지 비교한다.
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별한다.

```jsx
console.log(1 == 1)
console.log("hello" == "hello")
console.log(1 == "1")
console.log(0 == false)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/194679dc-9f43-4c50-a31b-eeeea5f13020/image.png)


#### 일치 연산자

- 두 피연산자의 값과 타입이 모두 같은 경우 `true` 를 반환한다.
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교한다.
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않는다.
- 특별한 경우를 제외하고는 **예측하지 못한 결과를 방지하기 위해 일치 연산자 사용을 권장한다.**

```jsx
console.log(1 === 1)
console.log("hello" === "hello")
console.log(1 === "1")
console.log(0 === false)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/e797dabb-b119-44cc-9fed-631b3f20845c/image.png)


#### 논리 연산자

- and 연산 : `&&`
- or 연산 : `||`
- not 연산 : `!`

```jsx
console.log(true && false)
console.log(true && true)

console.log(false || true)
console.log(false || false)

console.log(1 && 0)
console.log(0 && 1)
console.log(4 && 7)
console.log(1 || 0)
console.log(0 || 1)
console.log(4 || 7)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/ae6faa56-d7d4-4eee-9646-b79dcc5181c4/image.png)


---

### 3. 조건문

#### if

> 조건 표현식의 결과 값을 boolean 타입으로 변환 후에 참/거짓을 판단한다.
>

#### 삼항 연산자

- 간단한 조건부 로직을 간결하게 표현할 때 유용하다
- 복잡한 로직이나 대다수의 경우에는 가독성이 떨어질 수 있으므로 적절한 상황에서만 사용한다.

삼항 연산자 표현식

```jsx
// condition : 평가할 조건 true or false
// expression1 : 조건이 true일 경우 반환할 값 또는 표현식
// expression2 : 조건이 false일 경우 반환할 값 또는 표현식
condition ? expression1 : expression2

const age = 20
const message = (age >= 18) ? "성인" : "미성년자"
console.log(message)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/08aa78f6-46c4-4408-a2ae-a3ae8813943b/image.png)


---

### 4. 반복문

#### while

> 조건문이 참이면 문장을 계속해서 수행한다.
>

```jsx
// - 조건이 참인 동안 반복
let i = 0

while (i < 6) {
	console.log(i)
	i += 1
}
```

![](https://velog.velcdn.com/images/king-dong-gun/post/dea07b38-0a00-4451-b2c3-c0c01b1e7581/image.png)


#### for

> 특정한 조건이 거짓으로 판별될 때까지 반복한다.
>

```jsx
// - for ([초기문]; [조건문]; [증감문]) / 매번 i를 재할당하므로 let 사용 (const 불가)
for (let i = 0; i < 6; i++) {
    console.log(i)
}

// for의 i는 블록 스코프라 반복문 밖에서는 보이지 않음
// -> 여기서 출력되는 i는 1번 while에서 선언한 바깥 i
// -> 1번 코드를 지우고 실행하면 ReferenceError: i is not defined
console.log(i)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/5b6d3725-fb70-4457-bb71-21442b34828e/image.png)


#### for … in

> 객체의 열거 가능한 속성의 키에 대해 반복한다.
>

```jsx
// - 객체의 "키(key)"를 하나씩 꺼냄
const fruits = {
    a: 'apple',
    b: 'banana'
}

for (const property in fruits) {
    console.log(property) // a, b
    console.log(fruits[property])
}
```

![](https://velog.velcdn.com/images/king-dong-gun/post/72f8316e-b4f0-4cfe-aa11-91b0a7bb9f95/image.png)


#### for … of

> 반복 가능한 객체의 값에 대해 반복한다.
>

```jsx
// - 반복 가능한(iterable) 객체(배열, 문자열 등)의 "값(value)"을 하나씩 꺼냄
// - 매 반복마다 새 변수가 만들어지므로 const 사용 가능
const numbers = [0, 1, 2, 3]
for (const number of numbers) {
  console.log(number)
}

const myStr = 'apple'

for (const str of myStr) {
  console.log(str)
}
```

![](https://velog.velcdn.com/images/king-dong-gun/post/967d5b64-e02c-4d5c-afd5-700640ea7f51/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/a0ea13e7-ce71-4447-a36d-eb2660764d56/image.png)

---

### 5. 함수

#### 함수 구조

`fuction` 키워드, 함수 이름, 함수 매개변수, `statements` , return 값으로 구성된다.

- return문이 없거나 return 뒤에 값이 없으면 함수는 `undefined` 를 반환한다.

```jsx
fuction name ([param[, param, [..., param]]]) {
	statements
	return value
}
```

#### 함수 정의의 2가지 방법

1. 선언식
    - 선언 된 함수는 나중 사용을 위해 저장되며, call 될 때 실행된다.
2. 표현식
    - 자바스크립트 함수는 표현식을 사용하여 정의 될 수 있으며, 함수 표현식은 변수로 저장될수 있다.

#### 함수 선언식 특징

- 선언 전에 호출할 수 있다 (함수 전체가 호이스팅 됨)
- 코드의 구조와 가독성 면에서는 표현식에 장점이 있다.

```jsx
add(1, 2)

function add(num1, num2) {
	return num1 + num2
}
```

#### 함수 표현식 특징

- 선언 전에 호출할 수 없다
- 함수 이름이 없는 익명 함수를 사용할 수 있다.

```jsx
sub(2, 1)   // RefernceError: Cannot access "sub" before initializtion

const sub = function(num1, num2) {
	return num1 - num2
}
```

#### 함수 표현식 사용을 권장하는 이유

1. 선언 전에 호출할 수 없으므로 **정의 후 호출** 순서가 코드에 그대로 드러나 실행 흐름을 예측하기 쉽다.
2. 변수에 할당되므로 함수를 값으로 다루기 쉽다.
3. 블록 스코프를 가지는 `let` , `const` 와 함께 사용해 더 엄격한 스코프 관리가 가능하다.

---

### 6. 매개변수

#### 기본 함수 매개변수

- 함수 호출 시 인자를 전달하지 않거나 `undefined` 를 전달할 경우, 지정된 기본값으로 매개변수를 초기화한다.

```jsx
const greeting = function(name = "kim") {
	return `hi ${name}`
}

console.log(greeting())
```

![](https://velog.velcdn.com/images/king-dong-gun/post/ba19ced7-5c05-409d-a24f-1436c3d33eb0/image.png)


#### 나머지 매개변수

- 정해지지 않은 개수의 인자들을 배열로 모아서 받는 방법이다
- 누락된 인자는 `undefined` 로 할당된다.
- 작성규칙
    - 함수 정의 시 나머지 매개변수는 하나만 작성할 수 있다.
    - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 한다.

```jsx
const myFunc = function(param1, param2, ... restParams) {
	return [param1, param2, restParams]
}

console.log(myFunc(1,2,3,4,5))    // [1,2,[3,4,5]]
console.log(myFunc(1,2))          // [1,2,[]]
```

---

### 7. 화살표 함수 표현식

> 함수 표현식의 간결한 표현법이다.
>

#### 작성 방식

1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(`⇒`)를 작성한다.
2. 함수의 매개변수가 하나뿐이면, 매개변수의 `()` 제거가 가능하다.
    - 하지만 생략하지 않는 것을 권장한다.
3. 함수 본문의 표현식이 한 줄이면 `{}` , `return` 제거가 가능하다.

```jsx
// 일반 함수
const arrow = function(name) {
	return `hello, ${name}`
}

// 화살표 함수
const arrow = name => `hello, ${name}`
```