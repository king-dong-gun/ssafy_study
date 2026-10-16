### 1. ORM

> 객체 지향 프로그래밍 언어의 객체와 데이터베이스의 데이터를 매핑하는 기술이다.
>

#### 문제 상황

1. `Django` 는 `Python`  언어를 사용하지만 데이터베이스는 SQL 언어를 사용한다.
2. 그래서 `ORM` 은 `Django` 와 데이터베이스 사이에서 언어 번역자 역할을 수행한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/787541b0-ec8a-495e-8ede-b08bd3b72d3c/image.png)


#### QuerySet API

> 데이터베이스의 복잡한 SQL 쿼리문을, SQL 대신 직관적인 Python 코드로 데이터베이스에 요청할 수 있게 해주는 도구이다.
>

#### Django에서 Query가 처리되는 과정

1. 파이썬 코드 → ORM
2. ORM → SQL 변환
3. DB 응답 → ORM
4. ORM → QuerySet API 변환

#### QuerySet API 구문 기본 구조

- `Article` : 모델 클래스
    - 데이터베이스 테이블에 대한 python 클래스
- `objects` : 메니저
    - 데이터베이스 질의 작업을 위한 기본 인터페이스
- `all` : QeurySet API
    - 특정 데이터베이스 작업을 수행하는 명령

```python
Article.objects.all()
```

![](https://velog.velcdn.com/images/king-dong-gun/post/2fa803b9-f7de-4e24-8975-19530c7be559/image.png)


단, DB → Django에서 DB가 조회 결과를 전달하면, Django ORM이 해당 데이터를 변환하여 반환한다.

---

### 2. CRUD

> 기본적인 데이터 처리 기능인 생성, 조회, 수정, 삭제를 묶어서 이르는 말이다.
>
- `create` : 데이터 생성/저장
- `read` : 데이터 조회
- `update` : 데이터 수정/갱신
- `delete` : 데이터 삭제

#### QuerySet API 사전 준비

1. 외부 라이브러리 설치 및 의존성 기록
    - `IPython` 은 일반 파이썬 셀보다 자동 완성 등 편리한 파이썬 작업 환경을 만들어 주는 도구이다.

```python
pip install ipython
```

2. Django Shell 접속

```python
python .\manage.py shell -v 2
```

![](https://velog.velcdn.com/images/king-dong-gun/post/934dda28-f937-49a9-8603-f91017b8e438/image.png)


3. 데이터 불러오기
    - `all()` 메서드로 `QuerySet`  반환 확인

![](https://velog.velcdn.com/images/king-dong-gun/post/73183f26-cf5d-4307-bb28-8ef4cd25e2e4/image.png)


#### 데이터 객체 만드는 방법

1. 빈 객체 생성 후 값 할당 및 저장
    - 빈 객체(인스턴스) 생성

   ![](https://velog.velcdn.com/images/king-dong-gun/post/83985e8d-5d29-46cc-b2c3-5bce46c8871d/image.png)


2. 인스턴스에 제목과 본문 내용을 추가

   ![](https://velog.velcdn.com/images/king-dong-gun/post/99393356-906f-4804-9ecd-63653e6413b8/image.png)


3. DB 저장 요청
    - `save()` 요청까지 완료해야 데이터베이스에 저장이 된다.

   ![](https://velog.velcdn.com/images/king-dong-gun/post/b5d36999-44a4-43ec-8d49-6bdbc899e525/image.png)


    ![](https://velog.velcdn.com/images/king-dong-gun/post/815828ae-8e6c-4244-bf0e-53739cfec8dd/image.png)



다른 방법으로 `create()` 메서드를 사용하면 한 번에 생성 및 저장을 한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/1560ff7b-1641-4f95-86b9-dd979d10c20f/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/761b6386-e453-4191-ab3c-6594b2e7c13e/image.png)


---

### 3. view 함수에서 QuerySet API 활용하기

- 웹 페이지에 보여줄 데이터를 DB에서 가져올 때 사용한다.
- 사용자가 입력한 새로운 데이터를 DB에 저장할 때 사용한다.

지금은 전체 게시글 조회를 해보겠다.

#### urls.py

```python
from django.urls import path
from django.urls import path, include
from . import views

app_name = 'articles'
urlpatterns = [
    path("", views.index, name= "index")
]

```

#### views.py

```python
from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }

    return render(request, "articles/index.html", context)

```

#### index.html

```python
<h1>Articles</h1>
<hr>
{% for article in articles %}
    <div>
        <p>글 번호: {{ article.pk }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
    </div>
    <hr>
{% endfor %}
```

#### 실행 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/e685c45c-3a51-4b24-ab31-b6d3e213695b/image.png)
