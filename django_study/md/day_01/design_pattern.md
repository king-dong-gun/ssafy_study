### 1. Web Application

#### 클라이언트와 서버

![](https://velog.velcdn.com/images/king-dong-gun/post/9f49b83d-10d5-44a5-a945-b928a93eafbd/image.png)


- 클라이언트: 서비스를 요청하는 주체이다.
- 서버: 클라이언트의 요청에 응답하는 주체이다.

> 일반적인 웹 서비스에서는 클라이언트가 페이지를 달라고 `요청` 할 경우 서버가 페이지를 `응답` 해준다.
>

#### Frontend & Backend

1. Frontend
- 사용자 인터페이스 (UI)를 구성하고, 사용자가 어플리케이션과 상호작용 할 수 있도록 한다.
    - `HTML` , `CSS` , `JavaScript` , 프론트엔드 프레임워크 등

![](https://velog.velcdn.com/images/king-dong-gun/post/66a724cc-2991-47c0-ba2e-d1ed086525b1/image.png)


1. Backend
- 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당한다.
    - `Python` , `Java` , 백엔드 프레임워크, 데이터베이스, API 등

![](https://velog.velcdn.com/images/king-dong-gun/post/e16dc1f1-3ea0-47e3-85b0-450720fb6f28/image.png)


#### Web Framework

> 웹 어플리케이션을 빠르게 개발할 수 있도록 도와주는 도구이다.
개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공한다.
>

#### Django Framework

> Python 기반의 대표적인 웹 프레임워크
>

Django를 사용하는 이유

1. 다양성
2. 확장성
3. 보안
4. 커뮤니티 지원

---

### 2. 가상 환경 생성 및 활성화

#### 가상 환경 생성 및 활성화 과정

1. 가상 환경 생성
- 현재 디렉토리 안에 `venv` 라는 폴더가 생성된다.
- `venv` 폴더 안에는 파이썬 실행 파일, 라이브러리 등을 담을 공간이 마련된다.
- `venv` 라는 이름의 가상 환경을 생성한 것 이다.

```bash
# 임의의 이름으로 생성 가능하나 관례적으로 venv라고 사용한다.
python -m venv venv
```

![](https://velog.velcdn.com/images/king-dong-gun/post/9ad5d829-633d-4410-8baa-e17ef0876d5d/image.png)


1. 가상 환경 활성화
- 활성화 후 프롬프트 앞에 `(venv)` 와 같이 표시된다면 성공한 것 이다./
- `Mac/Linux` 에서는 명령어가 다르니 주의한다.

```bash
.\venv\Scripts\Activate.ps1
```

![](https://velog.velcdn.com/images/king-dong-gun/post/d43b5ff7-747d-45a2-ab3b-0b5149a2303d/image.png)



1. 가상 환경 종료

```bash
deactivate
```

![](https://velog.velcdn.com/images/king-dong-gun/post/4bf1c44a-1e57-4804-bd23-9bdfb31fd823/image.png)


#### 의존성 패키지

#### 의존성

> 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리이다.
>

#### 패키지 목록 확인

```bash
pip list
```

![](https://velog.velcdn.com/images/king-dong-gun/post/7ef69ffe-b3ce-4509-a65d-b75234becd6f/image.png)


#### 의존성 기록

```bash
pip freeze > requirements.txt
```

#### 의존성 설치

```bash
pip install -r requirements.txt
```

![](https://velog.velcdn.com/images/king-dong-gun/post/2bccfd7a-8f10-4ed8-b8bc-4c739960594b/image.png)


#### 의존성 패키지 관리가 필요한 이유

1. 환경의 통일
    - 버전이 다른 경우 함수명이나 동작이 달라질 수 있다.
    - 제 PC에서는 되는데용? 이 문제를 해결 가능하다.
2. 협업 효율
    - 프로젝트가 커질수록 사용하는 패키지의 개수도 늘어나게 된다.
    - 팀원간 동일한 개발 환경을 즉시 구축 가능하다.

#### 가상 환경 주의사항 및 권장사항

1. 가상 환경에 들어가고 나오는 것이 아니라 사용할 `Python` 환경을 `On/Off` 로 전환하는 개념이다.
2. 프로젝트마다 별도의 가상 환경을 사용한다.
3. 폴더 `venv` 는 `.gitignore` 파일에 작성되어 원격 저장소에 공유하지 않는다.

---

### 3. Django 프로젝트 생성 및 서버 실행

#### Django 설치

```bash
pip install django~=5.2.0
```

![](https://velog.velcdn.com/images/king-dong-gun/post/6e2a8b84-20cc-48c2-b44a-2a57633ace53/image.png)


#### 최신 업데이트

```bash
pip freeze > .\requirements.txt
```

![](https://velog.velcdn.com/images/king-dong-gun/post/50b0ee7e-c781-4020-b850-4b8330ddd7f1/image.png)


#### 프로젝트 생성

```bash
# firstpjt 라는 이름의 django 프로젝트를 생성한다.
django-admin startproject firstpjt .
```

![](https://velog.velcdn.com/images/king-dong-gun/post/3c366b48-259d-4f2b-af2f-7a73820d4f7b/image.png)


#### 서버 실행

```bash
python manage.py runserver
```

![](https://velog.velcdn.com/images/king-dong-gun/post/2cb5b844-1fdb-495a-80c2-e72212e4fd6d/image.png)


#### 서버 확인

`http://127.0.0.1:8000/` 접속 후 확인

![](https://velog.velcdn.com/images/king-dong-gun/post/aac76bbf-b302-4c71-8282-49be05893da0/image.png)


---

### 4. 디자인 패턴

> 소프트웨어 설계에서 반복적으로 발생하는 문제에 대한, 검증되고 재사용 가능한 일반적인 해결책이다.
>

#### MVC 디자인 패턴

하나의 애플리케이션을 구조화하는 대표적인 구조적 디자인 패턴

1. Model
    - 데이터 및 비즈니스 로직 처리
2. View
    - 사용자에게 보여지는 화면을 담당
3. Controller
    - 사용자의 입력을 받아 Model과 View를 제어

#### MTV 디자인 패턴

Django에서는 **MTV 디자인 패턴을 사용한다**. (기존 MVC와 동일, 명칭만 바뀐 것 이다.)

1. Model
2. Template
3. View

![](https://velog.velcdn.com/images/king-dong-gun/post/709f7c3c-cbe8-4a03-b28e-deffecaa4afd/image.png)


#### Project와 Application

1. Django project
- 애플리케이션들의 집합
- `DB 설정` , `URL 연결` , `전체 앱 설정` 등
1. Django application
- 독립적으로 작동하는 기능 단위 모듈
- 각자 특정한 기능을 담당한다.
- `게시글` , `댓글` , `회원 관리` 등

#### 앱 생성

```bash
# articles라는 앱 이름
python manage.py startapp articles
```

![](https://velog.velcdn.com/images/king-dong-gun/post/dfd99f00-4751-4e22-b0ea-d1639c9de421/image.png)


#### 앱 등록

반드시 앱을 생성한 후에 `settings.py` 에 등록해야 한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/70946f53-23bd-4d34-82ba-690c921fd6c3/image.png)


#### 프로젝트 및 앱 구조

#### 프로젝트 구조

1. `settings.py`
    - 프로젝트의 모든 설정을 관리한다.
2. `urls.py`
    - 요청 들어오는 `URL` 에 따라 이에 해당하는 적절한 `views` 를 연결한다.
3. `__init__.py`
    - 해당 폴더를 패키지로 인식하도록 설정하는 파일이다.
4. `asgi.py`
    - 비동기식 웹 서버와의 연결 관련 설정 파일이다.
5. `wsgi.py`
    - 웹 서버와의 연결 관련 설정 파일이다.
6. `manage.py`
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티 파일이다.

#### 앱 구조

1. `admin.py`
    - 관리자용 페이지 설정
2. `models.py`
    - DB와 관련된 Model을 정의하고, MTV 패턴의 M을 의미한다.
3. `views.py`
    - HTTP 요청을 처리하고, 해당 요청에 대한 응답을 반환하고, MTV 패턴의 V이다.

---

### 5. 요청과 응답

사용자가 서버에 접속하는 과정이다.

![](https://velog.velcdn.com/images/king-dong-gun/post/e8911cb8-7b55-4628-9c10-2acde06f3cff/image.png)


#### URLs

- `http://127.0.0.1:8000/articles` 로 요청이 왔을때
    - request 객체를 views 모듈의 index view 함수에 전달하며 호출한다.

```python
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.index),
]
```

#### View

- `view` 함수가 정의되어 있는 곳으로, 특정 경로에 있는 `template` 와 `request`  객체를 결합해 응답 객체를 반환한다.

```python
from django.shortcuts import render

def index(request):
    return render(request, "articles/index.html")
```

#### Template

- `articles` 앱 폴더 안에 `templates` 폴더 생성
    - 폴더명은 반드시 `templates` 여야 하며, 개발자가 직접 생성해야한다.
- `templates`  폴더 안에 `articles` 폴더 생성
- `articles` 폴더 안에 탬플릿 파일 생성

![](https://velog.velcdn.com/images/king-dong-gun/post/6b9aed82-02de-40bb-889e-1c66869c33e7/image.png)


#### Django에서 template을 인식하는 경로 규칙

> `app 폴더`/`templates` /`articles`/`index.html`
>

Django는 `/templates/` 까지 기본 경로로 인식한다.

#### 요청 후 응답 페이지 확인

`127.0.0.1:8000/articles/` 브라우저 요청

![](https://velog.velcdn.com/images/king-dong-gun/post/2e5b370c-53db-463e-9fca-a67e9908da72/image.png)


#### 데이터 흐름에 따른 코드 작성

- 사용자의 요청에서부터 데이터의 흐름은 `URLs`  → `View`  → `Template`

![](https://velog.velcdn.com/images/king-dong-gun/post/a019cccd-53f5-4767-b8c5-951e8fb60878/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/7100ebf7-4439-44e3-9df4-3106e90fd390/image.png)
