### 1. Client-side frameworks

> 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임워크이다.
>
- 웹사이트의 UI를 효율적으로 만들기 위해 미리 짜놓은 코드의 뼈대이다.
- 복잡한 웹 애플리케이션을 레고 조립하듯 부품 단위로 쉽게 개발할 수 있게 도와준다.
- 대표적으로 **Vue, React, Angular**가 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/6753cd76-1c8e-446a-b150-4992b764d1d1/image.png)


#### Client-side frameworks가 필요한 이유

1. **웹에서 하는 일이 많아진다.**
    - 단순히 무언가를 읽는 곳에서 → 무언가를 **하는** 곳으로 변화했다.
    - 음악 스트리밍, 영상 시청, 실시간 채팅 등 복잡한 대화형 웹 사이트를 **웹 애플리케이션**이라 부른다.
2. **다루는 데이터가 많아진다.**
    - 친구가 이름을 변경하면 친구 목록, 타임라인, 스토리 등 이름이 출력되는 모든 곳이 함께 변경되어야 한다.
    - 애플리케이션의 상태가 변경될 때마다 UI가 일관성 있게 업데이트되어야 한다.
3. **Vanilla JS만으로는 간단하지 않다.**
    - 값이 출력되는 곳마다 `querySelector`로 요소를 찾고 `textContent`를 바꾸는 코드가 계속 반복된다.

---

### 2. SPA

> Single Page Application, 단일 페이지에서 동작하는 웹 애플리케이션이다.
>
- 하나의 HTML 파일 위에서 JavaScript가 필요한 부분만 교체하며 페이지 이동 없이 동작한다.
- 마치 하나의 무대에서 배우와 배경만 계속 바꾸는 연극과 같다.

#### SPA 작동 원리

1. 최초 로드 시, 애플리케이션에 필요한 주요 리소스를 다운로드한다.
2. 이후 필요한 데이터만 AJAX 등으로 비동기적으로 받아 화면의 필요한 부분만 갱신한다.
3. JavaScript를 사용하여 클라이언트 측에서 동적으로 콘텐츠를 생성한다. → **CSR 방식**

---

### 3. CSR

> Client Side Rendering, 클라이언트에서 콘텐츠를 렌더링하는 방식이다.
>
- 일단 빈 집(HTML)에 들어간 뒤, 가구(JavaScript)를 배송받아 직접 조립하는 방식이다.

#### CSR 작동 원리

1. 사용자가 웹사이트에 요청을 보낸다.
2. 서버는 최소한의 HTML과 JavaScript 파일을 클라이언트로 전송한다.
3. 브라우저가 JavaScript를 실행하여 DOM을 업데이트하고 페이지를 렌더링한다.
4. 이후 서버는 HTML이 아닌 필요한 데이터(JSON)만 응답한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/47b7b62f-7f53-44ef-9829-40f5ef7e47b2/image.png)


#### CSR과 SPA의 장점

1. **빠른 페이지 전환** : 필요한 데이터만 받아 일부만 다시 렌더링하고, 서버 부하도 줄어든다.
2. **사용자 경험** : 새로고침이 없어 네이티브 앱과 유사한 경험을 제공한다.
3. **Frontend와 Backend의 명확한 분리** : Frontend는 UI, Backend는 데이터 및 API 제공을 담당한다.

#### CSR과 SPA의 단점

1. **느린 초기 로드 속도** : JavaScript가 다운로드되고 실행될 때까지 페이지가 완전히 렌더링되지 않는다.
2. **SEO 문제** : 검색 엔진이 HTML을 분석할 때 아직 콘텐츠가 존재하지 않아 검색에 잘 노출되지 않을 수 있다.

> 이 단점들은 Next.js, Nuxt 같은 SSR을 지원하는 프레임워크로 대부분 해결할 수 있다.
>

#### Django vs. Vue

| 구분 | 지금까지 (Django) | 앞으로 (Vue) |
| --- | --- | --- |
| 방식 | MPA + SSR | SPA + CSR |
| 첫 요청에 받는 것 | 완성된 HTML | 거의 빈 HTML + JS |
| 링크 클릭 시 | 새 HTML 요청 (새로고침) | JS가 화면 일부만 교체 |
| 이후 서버가 주는 것 | HTML | JSON 데이터 |
| 화면을 그리는 곳 | 서버 (Django Template) | 브라우저 (Vue) |
| 강점 | 첫 화면 속도, SEO | 화면 전환 속도, 앱 같은 경험 |

### 4. Vue

> 사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크이다.
>
- 컴포넌트로 화면을 조립하고, 데이터가 바뀌면 화면도 자동으로 바뀌는 **반응성**이 가장 큰 특징이다.
- 문법이 간결하고 직관적이어서 학습이 비교적 쉽고, 커뮤니티와 생태계가 활발하다.

#### Vue의 2가지 핵심 기능

1. **선언적 렌더링 (Declarative Rendering)**
    - 표준 HTML을 확장하는 템플릿 구문으로, JavaScript 상태(데이터)를 기반으로 화면에 출력될 HTML을 선언적으로 작성한다.
2. **반응성 (Reactivity)**
    - JavaScript 상태 변경을 추적하고, 변경사항이 발생하면 자동으로 DOM을 업데이트한다.
- Vanilla JS : 값 변경 + `document.querySelector(...).textContent = ...` 직접 작성
- Vue : **값만 변경** → 화면 갱신은 Vue가 담당

![](https://velog.velcdn.com/images/king-dong-gun/post/7effb833-dff3-4873-960a-d96990de6ab9/image.png)


#### Component

> 재사용 가능한 코드 블록이다.
>
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고, 각 부분을 개별적으로 다룰 수 있다.
- 애플리케이션은 중첩된 Component의 트리 형태로 구성된다. (`Root` → `Header`, `Main`, `Aside` ...)

![](https://velog.velcdn.com/images/king-dong-gun/post/0d39453f-9ee9-49b0-b65a-4150053188f0/image.png)


---

### 5. Vue Application 생성

```html
<div id="app">
  <h1>{{ message }}</h1>
  <button v-on:click="increment">count</button>
  <p>{{ count }}</p>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref } = Vue

  const app = createApp({
    setup() {
      const message = ref('Hello vue!')
      const count = ref(0)
      const increment = function () {
        count.value++
      }
      return { message, count, increment }
    }
  })

  app.mount('#app')
</script>
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/aef35415-90e4-4ae2-b86d-03dcecd931ed/image.png)


**Vue의 전체적인 흐름**

1. **데이터를 준비한다**
    - `setup()`에서 화면에 보여줄 값(`message`, `count`)과 동작(`increment`)을 만든다.
2. **화면에 데이터를 연결한다**
    - HTML에 `{{ count }}`처럼 "이 자리에는 이 데이터를 보여줘"라고 적어 두고, `mount`로 앱과 화면을 붙인다.
3. **사용자가 무언가를 한다**
    - 버튼을 클릭하면 `increment`가 실행되어 `count` 값이 바뀐다.
4. **Vue가 변화를 알아챈다**
    - `count`는 `ref()`로 만들었기 때문에 Vue가 값이 바뀐 것을 감지한다.
5. **화면이 자동으로 바뀐다**
    - Vue가 `{{ count }}` 자리를 새 값으로 다시 그린다.

→ 데이터 준비 → 화면 연결 → 데이터 변경 → Vue가 감지 → 화면 자동 갱신

---

### 6. ref()

> 반응형 상태(데이터)를 선언하는 함수이다.
>
- 값이 바뀌면 **Vue에게 "바뀌었어!"라고 알려주는 변수**를 만든다.
- 알림을 받은 Vue가 그 값을 쓰는 화면을 자동으로 다시 그린다.

#### ref가 필요한 이유 — 일반 변수의 문제

```jsx
let count = 0count++              // 값은 1이 됨
```

```html
<p>{{ count }}</p>   <!-- 화면은 계속 0 -->
```

- Vue는 `{{ }}`에 적힌 값을 **처음 화면을 그릴 때 한 번** 읽어서 적는다.
- 그다음에는 **"값이 바뀌었다"는 신호가 올 때만** 다시 읽어서 화면을 고친다.
- 일반 변수는 값이 바뀌어도 **신호를 보내지 않는다.**
    - Vue는 모르고, 화면은 그대로이다.

> **식당 주문 벨**
>
> - Vue는 주방 직원이다. 처음 주문(첫 화면)을 받아 간 뒤 벨이 울릴 때만 다시 온다.
> - 일반 변수 = 혼잣말로 "메뉴 바꿀래"
    >     - 직원은 못 들음
> - ref = **벨을 누르고** "메뉴 바꿀게요"
    >     - 직원이 와서 주문을 고침

#### ref가 동작하는 순서

```jsx
const count = ref(0)   // ① 벨이 달린 변수 만들기
count.value++          // ② 값 변경
                       // ③ ref가 Vue에게 "바뀌었어!" 신호
                       // ④ Vue가 {{ count }}를 쓰는 화면을 다시 그림 (0 → 1)
```

#### .value를 붙히는 이유

`ref(0)`은 0을 그대로 주지 않고, **0이 들어 있는 상자(ref 객체)**를 준다.

```jsx
const count = ref(0)

console.log(count)        // RefImpl {...} → 상자
console.log(count.value)  // 0 → 상자 안의 실제 값
```

- 값을 바꿀 때 `.value`를 거쳐야 ref가 변화를 감지하고 신호를 보낼 수 있다.

```jsx
count.value = 10   // ⭕ 상자 안의 값을 바꿈 → 신호 O
count = 10         // ❌ 상자 자체를 바꾸려 함 → 에러 (const)
```

| 위치 | 사용법 | 예시 |
| --- | --- | --- |
| `<script>` 안 | `.value`로 직접 꺼내고 바꿈 | `count.value++` |
| 템플릿 (`<div id="app">` 안) | `.value` 생략 (Vue가 자동으로 꺼내 줌) | `{{ count }}` |

#### 반응형 변수 vs. 일반 변수

```html
<div id="app">
  <p>반응형 변수: {{ reactiveValue }}</p>
  <p>일반 변수: {{ normalValue }}</p>
  <button v-on:click="updateValues">값 업데이트</button>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref } = Vue

  const app = createApp({
    setup() {
      const reactiveValue = ref(0)   // 벨 달린 변수
      let normalValue = 0            // 일반 변수

      const updateValues = function () {
        reactiveValue.value++
        normalValue++
        console.log(normalValue)     // 1, 2, 3... 값은 올라감
      }
      return { reactiveValue, normalValue, updateValues }
    }
  })

  app.mount('#app')
</script>
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/8b938dc9-1d90-4847-8a67-9b8a98b8f6ae/image.png)


- 버튼을 3번 누르면 화면에는 `반응형 변수: 3`, `일반 변수: 0`이 보인다.
- 콘솔을 보면 `normalValue`도 `1, 2, 3`으로 올라가고 있다.
- **값은 바뀌었지만 신호가 없어서** 화면에 반영되지 않은 것이다.

#### 화면에서 활용

> **사용자가 무언가 하면 화면에서 바뀌어야 하는 값**은 ref로 만든다.
>

| 화면 예시 | ref에 담는 값 |
| --- | --- |
| 좋아요 수, 장바구니 수량 | 숫자 `ref(0)` |
| 입력창 내용, 로그인한 사용자 이름 | 문자열 `ref('')` |
| 메뉴 열림/닫힘, 로그인 여부 | true/false `ref(false)` |
| 할 일 목록, 댓글 목록 | 배열 `ref([])` |
- 가격처럼 절대 바뀌지 않는 값은 일반 `const`로 둬도 된다.

#### 서버(DB)와의 관계

ref는 **브라우저 안에서만** 동작한다. DB에 저장하는 일은 하지 않는다.

**좋아요 99개 → ❤️ 클릭**

1. axios로 서버에 "좋아요 눌렀어요" 요청
2. 서버가 DB를 99 → 100으로 저장
3. 서버가 `{ "like_count": 100 }` 응답 (숫자만 줌)
4. `likeCount.value = 100` 으로 ref에 넣기
5. ref가 Vue에게 신호 → 화면이 100으로 바뀜

| axios (서버 요청) | ref | DB | 내 화면 | 새로고침 후 |
| --- | --- | --- | --- | --- |
| ⭕ | ❌ | 100 | **99** (안 바뀜) | 100 |
| ❌ | ⭕ | **99** (저장 안 됨) | 100 | **99** |
| ⭕ | ⭕ | 100 | 100 | 100 |
- **axios는 저장**, **ref는 화면 반영**을 담당한다. 그래서 둘 다 필요하다.

Django 템플릿은 서버가 DB 값을 **먼저** 채워서 완성된 HTML을 보냈기 때문에 ref가 필요 없었다.

Vue는 화면을 **먼저** 그리고 데이터가 **나중에** 도착하므로, 도착한 값을 ref에 넣어야 화면이 바뀐다.