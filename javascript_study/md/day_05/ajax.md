### 1. 비동기

#### 동기

> 프로그램의 실행 흐름이 순차적으로 진행되는 방식이다.
>
- 작업이 작성된 순서대로 실행된다.
- 현재 작업이 완료되어야 다음 작업을 실행할 수 있다.
- 실행 순서를 예측하기 쉽지만, 작업 시간이 길어지면 다음 작업도 지연된다.

**실생활 예시: 음식점에서 주문하기**

1. 첫 번째 손님이 음식을 주문한다.
2. 직원은 첫 번째 손님의 음식이 완성될 때까지 기다린다.
3. 음식이 완성되면 첫 번째 손님에게 전달한다.
4. 그제야 두 번째 손님의 주문을 받는다.

#### 비동기

> 특정 작업의 실행이 완료될 때까지 기다리지 않고 다음 작업을 즉시 실행하는 방식이다.
>
- 시간이 오래 걸리는 작업을 기다리지 않고 다음 코드를 실행할 수 있다.
- 네트워크 요청, 타이머, 파일 처리 등에 활용된다.
- 작업이 완료되는 시점에 따라 실행 결과의 순서가 달라질 수 있다.

**실생활 예시: 카페에서 커피 주문하기**

1. 첫 번째 손님이 아메리카노를 주문한다.
2. 직원은 주문을 접수하고 커피 제조를 요청한다.
3. 커피가 완성될 때까지 기다리지 않고 두 번째 손님의 주문을 받는다.
4. 커피가 완성되면 첫 번째 손님에게 전달한다.

---

### 2. JavaScript Runtime

- JavaScript는 싱글 스레드이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요하다.
    - 브라우저
    - Node.js

#### 브라우저 환경에서의 비동기 처리 관련 요소

#### 1. Call Stack (호출 스택)

> JavaScript 코드가 실행될 때 함수 호출이 순서대로 쌓이는 공간이다.
>
- JavaScript는 기본적으로 하나의 Call Stack에서 작업을 처리한다.
- 가장 나중에 들어온 작업이 먼저 완료되는 LIFO(후입선출) 방식이다.

#### 2. Web API

> 브라우저가 제공하는 기능으로, 시간이 걸리거나 언제 완료될지 모르는 비동기 작업을 처리할 수 있도록 도와준다.
>
- 타이머, 네트워크 요청 등을 처리한다.
- 비동기 작업이 진행되는 동안 JavaScript는 다른 코드를 실행할 수 있다.

#### 3. Task Queue (작업 대기열)

> 비동기 작업이 완료된 후 실행할 콜백 함수들이 순서대로 대기하는 공간이다.
>
- 실행할 준비가 된 콜백 함수가 대기한다.
- 일반적인 Task Queue는 먼저 들어온 작업부터 처리하는 FIFO(선입선출) 방식이다.

#### 4. Event Loop (이벤트 루프)

> Call Stack이 비어 있는지 계속 확인하고, 비어 있다면 Task Queue에서 대기 중인 작업을 Call Stack으로 보내 실행하도록 관리한다.
>
- Call Stack의 상태를 확인한다.
- Call Stack이 비어 있으면 대기 중인 작업이 실행되도록 한다.

```jsx
console.log('Hi')

setTimeout(function myFunc() {
  console.log('Work')
}, 3000)

console.log('Bye')
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/88f6cd69-dee9-4656-9186-2850662bd802/image.png)


**실행 순서**

1. `console.log('Hi')`가 Call Stack에서 실행된다.
2. `setTimeout()`이 호출되고 Web API에 타이머가 등록된다.
3. 타이머 완료를 기다리지 않고 `console.log('Bye')`가 실행된다.
4. 3초가 지나면 콜백 함수가 Task Queue에서 대기한다.
5. Call Stack이 비면 Event Loop에 의해 콜백 함수가 실행되어 `Work`가 출력된다.

---

### 3. Callback & Promise

#### 비동기 콜백

- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수이다.
- 연쇄적으로 발생하는 **비동기 작업을 순차적으로 동작**할 수 있게 한다.
- **작업의 순서와 동작을 제어하거나 결과를 처리하는데 사용한다.**

#### 비동기 콜백의 한계

1. 비동기 콜백 함수는 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용된다.
2. 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생한다.
3. 콜백 함수가 계속 중첩되면 코드가 복잡해지고 가독성이 떨어지는 **콜백 지옥(Callback Hell)** 문제가 발생한다.

**예시: 회원 로그인 → 회원 정보 조회 → 주문 내역 조회**

```jsx
loginUser(function (user) {
  getUserInfo(user, function (userInfo) {
    getOrders(userInfo, function (orders) {
      console.log(orders)
    })
  })
})
```

**실행 흐름**

1. `loginUser()` : 로그인을 완료한다.
2. `getUserInfo()` : 로그인한 회원의 정보를 조회한다.
3. `getOrders()` : 회원의 주문 내역을 조회한다.
4. `console.log()` : 조회된 주문 내역을 출력한다.

각 작업이 이전 작업의 결과를 필요로 하기 때문에 콜백 함수가 계속 중첩된다.

이렇게 콜백 함수가 깊게 중첩되면 코드의 가독성이 떨어지고, 오류 처리와 유지보수가 어려워진다.

이를 개선하기 위해 JavaScript에서는 **Promise와 async/await**를 사용한다.

#### Promise

1. 비동기 작업의 결과를 나타내는 객체이다.
2. 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공한다.
3. `then` 메서드를 통해 여러 비동기 작업을 연결하는 **체이닝**하여 순차적으로 연결한다.

#### Promise의 3가지 상태

> Promise는 비동기 작업의 진행 상태에 따라 Pending, Fulfilled, Rejected 중 하나의 상태를 가진다.
>

| 상태 | 의미 | 관련 함수 |
| --- | --- | --- |
| **Pending (대기)** | 작업의 성공 또는 실패가 아직 결정되지 않은 상태 | - |
| **Fulfilled (이행)** | 작업이 성공적으로 완료된 상태 | `resolve()` |
| **Rejected (거부)** | 작업이 실패한 상태 | `reject()` |
- `resolve()` : Promise를 성공 상태로 확정하고 결과 값을 전달한다.
- `reject()` : Promise를 실패 상태로 확정하고 실패 이유를 전달한다.
- 한 번 성공 또는 실패로 확정된 Promise는 다시 Pending 상태로 돌아가지 않는다.

```jsx
const getRandomData =  function () {
    return new Promise((resolve, reject) => {
        const success = Math.random() > 0.5

        setTimeout(() => {
            if (success) {
                resolve("데이터 도착")
            } else {
                reject("에러 발생")
            }
        }, 1000)
    })
}

const result = getRandomData()
    .then((data) => console.log(data))
    .catch((error) => console.log(error))

console.log(result, "결과는 어떻게 될까요?")
```

**코드 흐름**

1. `new Promise()` : Promise 객체를 생성한다.
2. `Math.random()` : 성공 또는 실패 여부를 무작위로 결정한다.
3. `setTimeout()` : 약 1초 후 결과를 처리한다.
4. `resolve()` : 성공하면 결과를 `then()`에 전달한다.
5. `reject()` : 실패하면 오류를 `catch()`에 전달한다.
6. `console.log(result)` : 비동기 작업이 완료되기 전 Promise의 Pending 상태를 확인한다.

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/d99edd92-ef1d-45a8-91dc-8c4bb78f0829/image.png)


#### Promise가 제공하는 이점

1. 실행 순서의 보장
2. 유연한 비동기 처리
3. 체이닝을 통한 연속적인 비동기 처리
4. 에러 처리의 일원화

---

### 4. AJAX

> 비동기적인 웹 에플리케이션 개발을 위한 기술이다.
>
- 브라우저의 HTTP 요청 기능을 사용해 페이지 일부를 갱신하는 방식이다.
- 브라우저와 서버 간의 데이터를 비동기적으로 교환하는 기술이다.
- Ajax를 사용하면 페이지 전체를 새로고침 하지 않아도 동적으로 데이터를 불러와 화면을 갱신할 수 있다.

#### 기존 기술과의 차이

1. JavaScript로 HTTP 요청 `fetch` , `Axios`
2. 서버는 새로운 페이지를 응답으로 만들지 않고, 필요한 부분에 대한 데이터만 처리 후 응답

![](https://velog.velcdn.com/images/king-dong-gun/post/0e775bff-621a-429b-8c32-ba0d9da3adf8/image.png)


#### fetch API

> 브라우저에 내장된, Promise를 반환하는 HTTP 요청 함수이다.
>
- 서버에 HTTP 요청을 보내고 응답을 받는 데 사용한다.
- Promise를 반환하므로 `then()`과 `catch()`를 사용할 수 있다.
- 서버에서 받은 응답은 `response.json()` 등을 통해 JavaScript 데이터로 변환할 수 있다.
- HTTP 오류 응답(404, 500 등)은 자동으로 `catch()`로 이동하지 않으므로 `response.ok`를 확인해야 한다.

#### Axios

> 브라우저와 Node.js 환경에서 모두 사용할 수 있는 Promise 기반의 HTTP 클라이언트 라이브러리이다.
>
- 서버에 HTTP 요청을 보내고 응답을 처리하는 데 사용한다.
- Promise를 반환하므로 `then()`과 `catch()`를 사용할 수 있다.
- JSON 응답 데이터를 자동으로 변환하여 `response.data`로 접근할 수 있다.
- HTTP 오류 응답(404, 500 등)을 기본적으로 `catch()`에서 처리할 수 있다.
- `fetch()`와 달리 별도의 설치 또는 CDN 연결이 필요하다.

**Axios 기본 사용법**

```jsx
axios({
  method: 'get',
  url: 'https://jsonplaceholder.typicode.com/posts/1'
})
  .then((response) => {
    console.log(response.data)
  })
  .catch((error) => {
    console.log(error)
  })
```

![](https://velog.velcdn.com/images/king-dong-gun/post/10f99dd7-a728-48ad-b0d2-4020e57f282b/image.png)


**코드 흐름**

1. `axios()` : 서버에 HTTP 요청을 보내고 Promise 객체를 반환한다.
2. `method: 'get'` : 서버에 데이터를 조회하도록 요청한다.
3. `url` : 요청을 보낼 서버 주소를 지정한다.
4. `then()` : 요청이 성공하면 응답을 전달받는다.
5. `response.data` : 서버에서 받은 데이터를 출력한다.
6. `catch()` : 요청에 실패하거나 오류가 발생하면 처리한다.

#### fetch API와 Axios의 차이

| 구분 | fetch API | Axios |
| --- | --- | --- |
| 설치 | 브라우저 내장 | 별도 설치 필요 |
| Promise 반환 | O | O |
| JSON 변환 | `response.json()` | 자동 변환 |
| 응답 데이터 접근 | 변환된 데이터 사용 | `response.data` |
| HTTP 오류 처리 | `response.ok` 확인 필요 | 기본적으로 `catch()` 처리 |

#### then & catch 체이닝 (Chaining)

> 여러 비동기 작업을 `then()`과 `catch()`로 연결하여 순차적으로 처리하는 방식이다.
>
- Axios는 Promise 객체를 반환한다.
- `then()`과 `catch()`도 새로운 Promise 객체를 반환한다.
- `then()`을 연속해서 작성하여 여러 비동기 작업을 연결할 수 있다.
- 이전 `then()`에서 반환한 값은 다음 `then()`의 인자로 전달된다.

```jsx
// Promise를 반환하는 함수 정의
const orderCoffee = function () {
    return new Promise((resolve, reject) => {
        resolve('커피 주문 완료')
    })
}

// Promise 체이닝
orderCoffee()
    .then((result1) => {
        console.log(result1)
        return '커피 제조 완료'
    })
    .then((result2) => {
        console.log(result2)
        return '커피 전달 완료'
    })
    .then((result3) => {
        console.log(result3)
    })
```

![](https://velog.velcdn.com/images/king-dong-gun/post/7eae2b08-c858-4578-866e-00f0f883e2de/image.png)


**then 메서드 체이닝의 장점**

1. **가독성** : 비동기 작업의 순서와 의존 관계를 명확하게 표현할 수 있다.
2. **에러 처리** : 여러 단계에서 발생한 오류를 마지막 `catch()`에서 처리할 수 있다.
3. **유연성** : 각 단계에서 데이터를 가공하거나 다른 작업을 수행할 수 있다.
4. **코드 관리** : 작업을 단계별로 분리하여 유지보수가 편리하다.