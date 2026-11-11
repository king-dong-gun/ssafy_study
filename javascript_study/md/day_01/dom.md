### 1. 변수

#### 변수명 작성 규칙

- 반드시 **문자, 달러 ($) 또는 밑줄 (_)** 로 시작한다.
- 대소문자를 구분한다.
- 예약어 사용이 불가능하다.
    - `for` , `if` , `function` 등
- 카멜 케이스를 사용한다.
    - 변수, 객체, 함수에 사용한다.
- 파스칼 케이스를 사용한다.
    - 클래스, 생성자에 사용한다.
- 대문자 스네이크 케이스를 사용한다.
    - 상수에 사용한다.

#### 변수 선언 키워드

1. `let` : **재할당이 필요한 변수를 선언**할 때 사용한다.

```jsx
// let 키워드
let number = 10
console.log(number)

// 재할당
let number = 20
console.log(number)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/a44cda66-a7db-49a7-9343-d6bd5d2c7c11/image.png)


1. `const` : **재할당이 불가능한 상수를 선언**할 때 사용한다.

```jsx
// const 키워드
const number = 10
console.log("const", number)

// 재할당 -> 오류
number = 20
console.log(number)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/1277be90-701c-418b-a053-a73587deb927/image.png)


1. `~~var` : 재선언/재할당이 가능하지만, 현재는 호이스팅 문제로 사용을 권장하지 않는다.~~
    - 호이스팅이란 코드가 실행되기 전 변수 및 함수 선언문이 스코프의 최상단으로 끌어올려지는 듯한 현상이다.
    - `var` 의 호이스팅은 선언과 초기화가 동시에 진행되기 때문에 변수 선언 문장 이전에 접근해도 `undefined` 를 반환한다.
2. `block scope` : `if` , `for` 함수 등의 중괄호 내부를 가르키고, 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능하다.

```jsx
// block scope
let x = 1
if (x == 1) {
    let x = 1
    console.log(x)  // 블록안의 x
}
console.log(x)  // 블록 밖의 x
```

![](https://velog.velcdn.com/images/king-dong-gun/post/0bc6b83d-5996-4152-b2b8-9a81652a6f4d/image.png)


> 코드의 의도가 명확하고, 버그를 예방할 수 있는 `const` 를 기본으로 사용하자.
>

---

### 2. DOM

> 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공한다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/0ea75a8f-1b55-4a40-956d-2e959c41194e/image.png)


- 브라우저가 문서를 표현하기 위해 사용하는 데이터 구조는 위의 이미지와 같다.
- 각 상자는 객체이며 개발자는 이 객체와 상호작용해 어떤 HTML 태그를 나타내는지 어떤 콘텐츠가 포함되어 있는지를 알아낼 수 있다.
- 이 표현을 객체 모델, 줄여서 `DOM` 이라고 부른다.

---

### 3. document 객체

> 웹 페이지를 나타내는 DOM 트리의 최상위 객체이며 HTML 문서의 모든 콘텐츠에 접근하고 조작할 수 있는 진입점이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/84143f1d-2eef-4dfa-8821-e8754289d0b1/image.png)


- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체이다.
- 모두 document 객체의 하위 객체로 구성된다.

![](https://velog.velcdn.com/images/king-dong-gun/post/e9ca416b-819f-4630-ba5d-788ddeb689cd/image.png)


---

### 4. DOM tree

> HTML 태그를 나타내는 요소의 node는 문서의 구조를 결정한다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/a838b7e0-ab37-4255-be69-b14607655253/image.png)


#### DOM 조작 시 기억해야 할 것

**웹 페이지를 동적으로 만들기 == 웹 페이지를 조작하기**

1. 조작하고자 하는 요소를 선택한다.
2. 선택된 요소의 컨텐츠 또는 속성을 조작한다.

---

### 5. 선택 메서드

1. `document.querySelector(selector)`
    - 요소 한 개 선택한다.
    - 제공한 선택자와 일치하는 첫 번째 요소를 하나 선택한다.
    - 제공한 선택자를 만족하는 첫 번째 element 객체를 반환하고, 없다면 null을 반환한다.
2. `document.querySelectorAll(selector)`
    - 요소 여러 개를 선택한다.
    - 제공한 선택자와 일치하는 여러 element를 선택한다.
    - 제공한 선택자를 만족하는 NodeList를 반환한다.

```html
<body>
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  <script>
    // 1. querySelector(selector)
    // - CSS 선택자와 일치하는 "첫 번째" 요소 하나를 반환 (없으면 null)
    console.log(document.querySelector('.heading'))
    console.log(document.querySelector('.content'))

    // 2. querySelectorAll(selector)
    // - CSS 선택자와 일치하는 "모든" 요소를 NodeList로 반환
    // - NodeList는 배열과 비슷하지만 배열은 아님 (forEach는 가능, map/filter는 불가능)
    console.log(document.querySelectorAll('.content'))
    console.log(document.querySelectorAll('ul > li'))
  </script>
</body>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/fdaa2751-75a6-436e-8935-eab6c928e3d5/image.png)


---

### 6. DOM 조작

DOM 조작에는 **소성 조작, HTML 콘텐츠 조작, DOM 요소 조작, 스타일 조작**이 있다.

#### 속성 조작

1. 클래스 속성 조작
    - 스타일링 및 상태 제어를 위한 클래스 목록을 동적으로 추가/제거한다.
    - `classList` 로 요소의 클래스 목록을 쉽게 제어한다.
    - `add()` , `remove()` , `toggle()`
2. 일반 속성 조작
    - `id` , `href` 등 요소의 모든 HTML 속성 값을 직접 설정/조회한다.

#### HTML 콘텐츠 조작

- 요소의 텍스트 콘텐츠를 표현한다.

```html
<script>
    // HTML 콘텐츠 조작 (textContent)
    // - textContent: 요소 안의 "순수한 텍스트"를 읽거나 바꿈
    // - 값을 대입하면 기존 내용이 통째로 바뀜
    const h1Tag = document.querySelector('.heading')
    console.log(h1Tag.textContent) // DOM 조작

    h1Tag.textContent = '내용 수정'
    console.log(h1Tag.textContent) // 내용 수정 (화면의 제목도 바로 바뀜)
 </script>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/ad0edb2c-2324-4152-83fe-1acfbf982b6f/image.png)


#### DOM 요소 조작

1. `document.createElement(tagName)`
    - 작성한 tagName의 HTML 요소를 생성해 반환한다.
2. `Node.appendChild()`
    - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입한다.
3. `Node.removeChild()`
    - DOM에서 자식 Node를 제거한다.
    - 제거한 Node를 반환한다.

#### style 조작

- 해당 요소의 모든 style 속성 목록을 포함하는 속성이다.

```html
<script>
    // style 조작
    // - style 프로퍼티는 HTML 태그에 style="..." 속성을 직접 쓰는 것과 같음
    // - CSS 속성 이름은 카멜 케이스로 작성 (font-size -> fontSize)
    // - 여러 스타일을 한 번에 바꿀 때는 클래스(classList)를 쓰는 것을 권장
    const pTag = document.querySelector('p')

    pTag.style.color = 'crimson'
    pTag.style.fontSize = '2rem'
    pTag.style.border = '1px solid black'

    console.log(pTag.style) // CSSStyleDeclaration (지정한 color, fontSize, border 확인 가능)
</script>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/8b051735-f296-4ef2-a364-7d2e3a017114/image.png)
