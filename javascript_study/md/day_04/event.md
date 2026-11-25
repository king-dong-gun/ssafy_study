### 1. 이벤트

> 웹 페이지 상에서 '무언가 일어났다는 신호 또는 사건'이다.
>
- 화면 스크롤, 버튼 클릭, 드래그 앤 드롭, 키보드 입력 등 웹에서의 거의 **모든 상호작용은 이벤트와 함께** 한다.
- 모든 DOM 요소는 다양한 형태의 이벤트를 발생시킬 수 있다.
    - button을 클릭하면 `click` 이벤트, input 값 변경 시 `input` 이벤트

**대표적인 이벤트 종류**

| 이벤트 | 설명 |
| --- | --- |
| `click` | 요소 클릭 |
| `input` | 입력값 변경 |
| `mouseover` | 마우스가 요소 위에 올라감 |
| `keydown` | 키보드 키를 누름 |
| `submit` | 폼 제출 |

**실생활 예시: 카페에서 주문하기**

1. 손님이 키오스크에서 아메리카노를 주문한다. → **이벤트**
2. 키오스크가 주문을 받는다. → **이벤트 리스너**
3. 바리스타가 정해 둔 레시피대로 커피를 만든다. → **이벤트 핸들러**

---

### 2. event object

> DOM에서 이벤트가 발생하면, 브라우저가 해당 이벤트에 관한 정보를 담아 자동으로 생성하는 객체이다.
>
- 이벤트 종류 : `mouse`, `input`, `keyboard` 등
- 어떤 요소에서 발생했는지, 마우스 좌표는 어디인지, 눌린 키는 무엇인지 등 상세 정보를 담고 있다.
- 이벤트가 발생하면 연결된 **이벤트 핸들러**에 의해 처리된다.

---

### 3. event handler

> 특정 이벤트가 발생했을 때 실행되는 (콜백)함수이다.
>
- 우리가 직접 호출하는 함수가 아니라, 이벤트가 발생했을 때 브라우저가 대신 호출해 준다.
- 바리스타가 주문이 들어오기 전에는 기다리다가, 주문이 들어온 순간에만 움직이는 것과 같다.

#### addEventListener()

> 특정 DOM 요소에, 지정한 이벤트가 발생했을 때 실행할 이벤트 핸들러를 **등록하는 메서드**이다.
>

```jsx
EventTarget.addEventListener(type, handler)
```

- `EventTarget` : 이벤트를 감지할 DOM 요소
- `type` : 수신할 이벤트 유형 (문자열, `'click'`, `'input'`, `'mouseover'` 등)
- `handler` : 이벤트 발생 시 호출되는 콜백 함수
    - 자동으로 event 객체를 첫 번째 매개변수로 받는다.
- 핸들러는 지금 호출하는 것이 아니라 '누구를 부를지' 알려주는 것이므로 **괄호 없이** 전달한다.
    - `handleClick()` ❌ → `handleClick` ⭕

```html
<button id="btn">버튼</button>
```

```jsx
// 1. 버튼 요소 선택
const btn = document.querySelector('#btn')

// 2. 이벤트 핸들러
const detectClick = function (event) {
  console.log(event)                // PointerEvent
  console.log(event.type)           // click
  console.log(event.currentTarget)  // <button id="btn">버튼</button>
  console.log(this)                 // <button id="btn">버튼</button>
}

// 3. 버튼에 이벤트 핸들러를 등록
btn.addEventListener('click', detectClick)
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/5596e371-3d9c-4b93-b2e2-8306042dda42/image.png)


**코드 흐름**

1. `querySelector()` : 이벤트를 연결할 버튼 요소를 선택한다.
2. `detectClick` : 클릭 시 실행할 핸들러 함수를 정의한다.
3. `event` : 이벤트 발생 시 이벤트 객체가 자동으로 전달된다.
4. `this` : 일반 함수 핸들러에서 `this`는 리스너가 연결된 요소(`event.currentTarget`)를 가리킨다.
5. `addEventListener()` : 버튼에 `click` 이벤트와 핸들러를 연결한다.

#### 일반 함수 vs. 화살표 함수

> 이벤트 핸들러는 화살표 함수로도 작성할 수 있지만, 두 함수는 `this`를 처리하는 방식이 다르다.
>

| 구분 | 일반 함수 | 화살표 함수 |
| --- | --- | --- |
| 자체적인 `this` | 있음 | 없음 |
| 핸들러 안의 `this` | 이벤트가 연결된 요소 | 상위 스코프의 `this` (대부분 `window`) |
| 요소 확인 방법 | `this` 또는 `event.currentTarget` | `event.currentTarget` |
- 화살표 함수를 핸들러로 사용할 때는 `this` 대신 `event.currentTarget`을 사용한다.

---

### 4. 버블링

> 한 요소에 이벤트가 발생하면, 해당 요소의 핸들러가 동작한 후 이어서 부모 요소의 핸들러가 동작하는 현상이다.
>
- 최상단의 조상 요소(document, window)를 만날 때까지 이 과정이 반복된다.
- 가장 깊은 곳에서 시작해 부모 요소로 거슬러 올라가는 모습이 물속 거품과 닮아 버블링이라고 한다.

```html
<form id="form">
  form
  <div id="div">
    div
    <p id="p">p</p>
  </div>
</form>
```

```jsx
const formElement = document.querySelector('#form')
const divElement = document.querySelector('#div')
const pElement = document.querySelector('#p')

formElement.addEventListener('click', function () {
  console.log('form이 클릭되었습니다.')
})
divElement.addEventListener('click', function () {
  console.log('div가 클릭되었습니다.')
})
pElement.addEventListener('click', function () {
  console.log('p가 클릭되었습니다.')
})
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/7c2549ac-e2b4-4903-85be-df91408a3d96/image.png)


- `<p>`만 클릭했는데도 `p → div → form` 순서로 3개의 핸들러가 모두 동작한다.

#### target vs. currentTarget

| 속성 | 설명 |
| --- | --- |
| `event.target` | 이벤트가 실제로 시작된 가장 안쪽 요소, 버블링이 진행되어도 변하지 않음 |
| `event.currentTarget` | 이벤트 핸들러가 연결된 '현재' 요소, `this`와 같음 |
- 부모 요소에만 핸들러를 연결해도, 자식 요소를 클릭하면 버블링으로 핸들러가 실행된다.
- 이때 `currentTarget`은 항상 부모 요소이고, `target`은 실제로 클릭한 요소가 된다.

> `console.log(event)`로 객체 전체를 출력하면 `currentTarget`은 `null`로 보인다.
`currentTarget`은 이벤트가 처리되는 동안에만 사용할 수 있으므로 `console.log(event.currentTarget)`로 직접 확인해야 한다.
>

#### 캡처링 (capturing)

- 이벤트가 최상위 조상에서 타겟 요소까지 **하위로** 전파되는 단계이다. (버블링과 반대)
- 이벤트 흐름 : 캡처링(위 → 아래) → 타겟에서 실행 → 버블링(아래 → 위)
- 캡처링은 실제로 다루는 경우가 거의 없으므로 버블링을 중심으로 이해하면 된다.

#### 버블링이 필요한 이유

- 각자 다른 동작을 하는 버튼이 여러 개 있을 때, 버튼마다 핸들러를 등록할 필요 없이 **공통 조상에 핸들러를 하나만** 등록하면 된다.
- 부모의 핸들러에서 `event.target`을 이용하면 실제 어떤 버튼에서 이벤트가 발생했는지 알 수 있다.

```jsx
const divTag = document.querySelector('div')

divTag.addEventListener('click', function (event) {
  console.log(event.target)
})
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/35ba8263-328f-4fdd-9a45-fa84be322323/image.png)


---

### 5. 이벤트 기본 동작 취소하기

> HTML 요소가 기본적으로 가지고 있는 동작이 방해가 될 때, 이를 취소할 수 있다.
>
- `form` 제출 시 발생하는 페이지 새로고침을 막을 수 있다.
- `<a>` 태그를 클릭했을 때 페이지 이동을 막고, 대신 다른 로직을 수행할 수 있다.

#### .preventDefault()

> 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정한다.
>
- 택배 기사님의 기본 동작은 '문 앞에 두기'인데, '경비실에 맡겨 주세요'라고 요청하면 기본 동작은 취소되고 내가 정한 방식으로 처리되는 것과 같다.

```html
<form id="my-form">
  <input type="text" name="username">
  <button type="submit">Submit</button>
</form>
```

```jsx
const formTag = document.querySelector('#my-form')

const handleSubmit = function (event) {
  event.preventDefault()
  console.log('제출이 취소되었습니다.')
}

formTag.addEventListener('submit', handleSubmit)
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/c4907bf2-747a-4e04-be65-80357eccb548/image.png)


- submit 버튼을 눌러도 페이지가 새로고침되지 않는다.