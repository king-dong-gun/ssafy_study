### 1. HTTP

> 네트워크 상에서 데이터(리소스)를 주고 받기위한 약속이다.
>

#### HTTP request methods

- 데이터에 대해 수행을 원하는 작업을 나타내는 것이다.
- `GET` : 데이터 조회
- `POST` : 데이터 제출 및 변경

#### GET의 특징

> 서버로부터 데이터를 요청하고 받아오는데**(조회)** 사용한다.
>
1. 데이터를 전송한다.
    - URL의 쿼리 문자열을 통해 데이터를 전송한다.
    - http://127.0.0.1:8000/articles/create/?**title%content=내용**
2. 데이터에 제한이 있다
    - URL 길이에 제한이 있어서 대량의 데이터 전송에는 적합하지 않다.
3. 브라우저 히스토리에 남는다.
4. 캐싱
    - 브라우저는 `GET` 요청의 응답을 로컬에 저장할 수 있다.
    - 동일한 URL로 다시 요청할 때, 서버에 접속하지 않고 저장된 결과를 사용한다.

#### POST의 특징

> 서버에 데이터를 제출하여 리소스를 변경 **(생성, 수정, 삭제)** 하는 데 사용한다.
>
1. 데이터를 전송한다.
    - HTTP Body를 통해 데이터를 전송한다.
2. 데이터의 제한이 `GET` 보다 크다.
    - `GET` 에 비해 더 많은 양의 데이터를 전송할 수 있다.
3. 브라우저 히스토리에 남지않는다.
4. 캐싱
    - `POST` 요청은 기본적으로 캐시 할 수 없다.
    - `POST` 요청이 일반적으로 서버의 상태를 변경하는 작업을 수행하기 때문이다.

#### `GET` & `POST` 메서드 정리

| 구분 | GET | POST |
| --- | --- | --- |
| 주요 목적 | 데이터 조회 | 데이터 생성, 수정, 삭제 |
| 데이터 전송 위치 | URL의 Query String | HTTP Body |
| 데이터 노출 | URL에 데이터가 노출됨 | URL에 데이터가 직접 노출되지 않음 |
| 데이터 크기 | URL 길이 제한의 영향을 받음 | GET보다 많은 데이터 전송 가능 |
| 브라우저 히스토리 | 남음 | 남지 않음 |
| 캐싱 | 가능 | 기본적으로 하지 않음 |
| 서버 상태 변경 | 주로 변경하지 않음 | 주로 변경함 |
| 사용 예시 | 게시글 조회, 검색 | 게시글 작성, 수정, 삭제 |

---

### 2. GET 요청을 POST 요청으로 변경

아래는 기존에 get으로 만들었던 게시글 생성 기능이다.

```jsx
  <form action="{% url "articles:create" %}" method="GET">
    <div>
      <label for="title">Title: </label>
      <input type="text" name="title" id="title">
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name="content" id="content"></textarea>
    </div>
    <input type="submit">
  </form>
```

게시글 생성은 서버의 데이터를 변경하는 작업이므로 `GET` 이 아닌 `POST` 요청을 사용한다.

```jsx
  <form action="{% url "articles:create" %}" method="POST">
    <div>
      <label for="title">Title: </label>
      <input type="text" name="title" id="title">
    </div>
    <div>
      <label for="content">Content: </label>
      <textarea name="content" id="content"></textarea>
    </div>
    <input type="submit">
  </form>
```

POST 방식으로 변경한 뒤 게시글을 작성하면 `403 Forbidden` 오류가 발생한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/72936d22-865d-4394-a807-49888988ae29/image.png)


---

### 3. HTTP Response Status Code

> 서버가 클라이언트의 요청을 처리한 결과를 나타내는 3자리 숫자 코드이다.
>

#### 403 Forbidden

> 서버에 요청은 정상적으로 전달되었지만, 권한 문제로 요청이 거절되었다는 의미이다.
>

현재 발생한 `403 Forbidden`의 원인은 POST 요청에 `CSRF Token`이 포함되지 않았기 때문이다.

![](https://velog.velcdn.com/images/king-dong-gun/post/c4b73a9a-0d3d-4b83-bb4d-bc3763cac1dd/image.png)


---

### 4. CSRF

> Cross-Site Request Forgery의 약자로 **사이트 간 요청 위조**를 의미한다.
>

사용자가 의도하지 않은 요청을 다른 사이트에서 강제로 보내도록 만드는 공격이다.

예를 들어 사용자가 어떤 사이트에 로그인한 상태에서 악성 사이트에 접속했을 때, 사용자의 인증 정보를 이용해 게시글 작성, 정보 변경 등의 요청을 대신 보내는 방식이다.

#### CSRF Token

Django는 이러한 CSRF 공격을 방지하기 위해 `POST` 요청을 보낼 때 **CSRF Token**을 확인한다.

서버는 사용자에게 고유한 토큰을 전달하고, 이후 요청에 포함된 토큰이 서버가 발급한 값과 일치하는지 확인한다.

```
사용자
  ↓
서버가 CSRF Token 발급
  ↓
form에 Token 포함
  ↓
POST 요청
  ↓
서버가 Token 확인
  ↓
정상 요청이면 처리
```

`CSRF Token`이 없는 상태에서 POST 요청을 보내면 Django가 요청을 신뢰할 수 없다고 판단하여 `403 Forbidden` 응답을 반환한다.

#### CSRF Token 적용

Django Template에서는 `<form>` 내부에 csrf 코드를 작성한다.

```
{% csrf_token %}
```

적용 예시는 다음과 같다.

```html
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}

  <div>
    <label for="title">Title: </label>
    <input type="text" name="title" id="title">
  </div>

  <div>
    <label for="content">Content: </label>
    <textarea name="content" id="content"></textarea>
  </div>

  <input type="submit">
</form>
```

이후 다시 게시글을 작성하면 CSRF 검증을 통과하여 정상적으로 POST 요청을 처리할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/3621046c-2b0f-42e8-9d8c-fde7d6c25dc5/image.png)


---

### 5. Redirect

> 클라이언트에게 현재 요청을 처리한 뒤 **다른 URL로 다시 요청하도록 지시하는 응답**이다.
>

게시글을 생성한 뒤 `create.html`을 바로 `render`할 수도 있지만, 이 경우 사용자가 새로고침하면 기존 POST 요청이 다시 전송될 수 있다.

그러면 같은 게시글이 중복으로 생성될 가능성이 있다.

따라서 게시글 저장이 완료되면 `redirect()`를 사용하여 게시글 상세 페이지로 이동한다.

```python
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)
```

동작 과정은 다음과 같다.

```
new.html
  ↓
POST 요청
  ↓
create 함수
  ↓
게시글 DB 저장
  ↓
redirect 응답
  ↓
게시글 상세 페이지로 GET 요청
```

즉 `render()`는 현재 요청에 대한 HTML을 바로 응답하지만, `redirect()`는 브라우저에게 **새로운 URL로 다시 요청하라고 지시한다.**

---

### 6. GET과 POST 사용 정리

게시글 CRUD에서는 다음과 같이 요청 방식을 구분할 수 있다.

| 기능 | 요청 방식 | 이유 |
| --- | --- | --- |
| 게시글 목록 조회 | GET | 데이터 조회 |
| 게시글 상세 조회 | GET | 데이터 조회 |
| 게시글 작성 페이지 | GET | 작성 화면 조회 |
| 게시글 생성 | POST | DB 데이터 생성 |
| 게시글 수정 페이지 | GET | 수정 화면 조회 |
| 게시글 수정 | POST | DB 데이터 변경 |
| 게시글 삭제 | POST | DB 데이터 삭제 |

즉, **데이터를 보여주는 요청은 GET**, **서버의 데이터를 변경하는 요청은 POST**를 사용한다.

---

### 7. Cache

> 자주 사용하는 데이터나 응답 결과를 임시로 저장해두었다가 다시 요청할 때 빠르게 제공하기 위한 저장 공간이다.
>

GET 요청은 일반적으로 데이터를 조회하기 위한 요청이므로 캐싱할 수 있다.

동일한 데이터를 다시 요청했을 때 캐시에 저장된 응답을 활용하면 서버가 동일한 작업을 반복하지 않아도 된다.

#### Cache의 장점

1. 응답 속도를 높일 수 있다.
2. 서버의 불필요한 작업을 줄일 수 있다.
3. 네트워크 및 서버 부하를 줄일 수 있다.

반면 POST 요청은 일반적으로 서버의 데이터를 생성하거나 변경하기 때문에 기본적으로 캐시하지 않는다.