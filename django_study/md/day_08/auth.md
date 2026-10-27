## 1. 쿠키 & 세선

### 1. HTTP

> HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약이다.
>

#### 특징

1. 비 연결 지향
    - 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다.
    - 클라이언트는 서버와 서로 연결되어 있는 상태가 아니다.

![](https://velog.velcdn.com/images/king-dong-gun/post/70326c4d-f4b6-4c20-9ac9-54a2518f46be/image.png)



2. 무상태
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않는다.
    - 무상태의 의미
        - 장바구니에 담은 상품은 유지가 불가능하다.
        - 로그인 상태를 유지할 수 없다.

### 2. 쿠키

> 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다.
>

#### 특징

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다.
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식이다.
- `key` - `value` 형식의 데이터이다.

#### 쿠키 사용의 예시

- 로그인 유지 (세션 관리)
- 장바구니
- 언어, 테마 등 사용자 개인 설정 기억

#### 쿠키의 동작 예시

1. **브라우저가 서버에 웹 페이지를 요청**한다.
2. **서버가 응답**하면서 쿠키를 함께 보낸다.
    - 예: 로그인 정보, 사용자 식별 정보 등
3. 브라우저는 **받은 쿠키를 저장**한다.
4. 다음에 같은 **서버에 요청할 때 저장된 쿠키도 같이 보낸다**.
5. 서버는 **쿠키를 보고 사용자를 확인**한다.
    - 예: "아까 로그인한 사용자"
6. 필요하면 서버가 쿠키를 새로 만들거나 수정해서 다시 보낸다.

![](https://velog.velcdn.com/images/king-dong-gun/post/b6f1bbd8-fc6a-4e29-99ac-1ef31c503ee6/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/942d74e2-b222-4f19-a794-67f9e1c01dce/image.png)



#### 쿠키의 작동 원리와 활용

1. 쿠키 저장 방식
    - 브라우저는 쿠키를 `key` - `value` 의 데이터 형식으로 저장한다.
    - 쿠키에는 이름, 값 외에도 만료 시간, 도메인, 경로 등 추가 속성이 포함된다.
2. 쿠키 전송 과정
    - 서버는 HTTP 응답 헤더의 `Set-Cookie` 필드를 통해 클라이언트에게 쿠키를 전송한다.
    - 브라우저는 받은 쿠키를 저장해 두었다가, 동일한 서버에 재요청시 HTTP 요청 `Header` 의 `Cookie` 필드에 저장된 쿠키를 함께 전송한다.
3. 쿠키의 주요 용도
    - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용된다.
    - 이를 사용해 사용자의 로그인 상태를 유지할 수 있다.
    - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할이다.

#### 쿠키의 사용 목적

1. 세션 관리
    - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크 등
2. 개인화
    - 사용자 선호 설정(언어, 테마 등) 저장
3. 추적, 수집
    - 사용자 행동을 기록 및 분석

### 3. 세션

> 서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지하고, 상태 정보를 저장하는 데이터 저장 방식이다.
>

#### 세션의 작동 원리

1. 로그인에 성공하면 서버가 세션을 만든다.
2. 서버는 세션을 구분하기 위한 `session id`를 만든다.
3. 서버가 `session id`를 브라우저에게 보내준다.
4. 브라우저는 받은 `session id`를 **쿠키에 저장한다.**
5. 다음 요청부터 브라우저가 쿠키의 `session id`를 서버에 같이 보낸다.
6. 서버는 `session id`를 확인해서 **"로그인한 사용자"**라고 판단한다.
7. 로그인 상태로 요청을 처리해서 응답한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/2e8ca1c1-f223-47f9-8960-93cfb9a27d9b/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/93aca930-b7fa-4edc-9161-7b9c43453c8c/image.png)



#### 세션의 특징

- **서버 측에서 생성**되어 클라이언트와 서버 간의 상태를 유지한다.
- 상태 정보를 저장하는 데이터 방식이다.
- 쿠키에 `session id` 를 저장하여 매 요청마다 `session id` 를 함께 보낸다.
- 세션은 영구적으로 유지되지 않는다.

| 구분 | 쿠키 | 세션 |
| --- | --- | --- |
| 저장 위치 | **클라이언트(브라우저)** | **서버** |
| 저장하는 것 | 사용자 정보 또는 **세션 ID** | 로그인 정보 등 **세션 데이터** |
| 목적 | 사용자를 기억하고 상태를 유지 | 사용자를 식별하고 로그인 상태를 유지 |
| 요청 시 | 브라우저가 서버에 쿠키를 같이 보냄 | 서버가 쿠키의 세션 ID를 보고 세션을 찾음 |
| 쉽게 말하면 | **브라우저가 들고 있는 정보/번호표** | **서버가 보관하는 사용자 정보** |

#### 쿠키와 세션의 공통 목적

둘 다 결국 **클라이언트와 서버 사이의 상태 정보를 유지하고, 사용자를 식별하기 위해 사용한다.**

예를 들면:

**로그인 상태 유지**, **사용자 구분**, **장바구니 정보 유지** 등에 사용한다.

> **쿠키 = 클라이언트에 저장**
>
>
> **세션 = 서버에 저장**
>
> **공통 목적 = 상태 유지 + 사용자 식별**
>

---

## 2. Django Authentication System

### 1. 인증의 필요성

웹에서는 클라이언트와 서버가 여러 번 요청과 응답을 주고받기 때문에, 서버는 **각 요청이 어떤 사용자에게서 온 것인지 구별할 필요가 있다.**

이때 사용자가 누구인지 확인하는 과정을 **`인증(Authentication)`** 이라고 한다.

**대표적인 인증 방식**

- 아이디 / 비밀번호
- 소셜 로그인(OAuth)
- 생체 인증

**인증은 사용자가 누구인지 확인하기 위해 필요하다.**

### 2. Django Authentication System

Django는 **사용자 인증과 관련된 기능을 모아둔 시스템**을 기본으로 제공한다.

**주요 기능**

- **User Model**: 사용자 인증에 필요한 User Model 관리
- **Session 관리**: 로그인 상태를 유지하고 서버에 저장되는 방식을 관리
- **기본 인증 기능**: 아이디/비밀번호를 이용한 로그인, 로그아웃 등의 기능 제공

`Django Authentication System`을 이용하면 **로그인, 로그아웃, 회원가입, 회원정보 수정**과 같은 기능을 구현할 수 있다.

#### 기본 User Model의 한계

Django는 기본적으로 내장된 User Model을 제공한다.

하지만 기본 User Model은 `username`, `password` 등 기본적인 필드만 제공하기 때문에, **생년월일, 주소, 나이 등 추가 사용자 정보가 필요한 경우 확장이 어렵다.**

실제 프로젝트에서는 요구사항 및 필요한 사용자 정보를 추가하기 위해 **기본 User Model을 그대로 사용하기보다 Custom User Model을 만들어 사용하는 것이 좋다.**

---

## 3. User model 대체해보기

### AUTH_USER_MODEL

> Django 프로젝트의 User를 나타내는데 사용하는 모델을 지정하는 속성이다.
>

**프로젝트 중간에 `AUTH_USER_MODEL` 을 변경하는 것을 강력하게 권장하지 않는다. → 이미 프로젝트가 진행되고 있을 경우 DB 초기화 후 진행해야 한다.**

#### 1. 사전 준비

- 두 번째 `app accounts` 생성 및 등록

>
>
>
> `auth` 와 관련한 경로나 키워드들을 django 내부적으로 `accounts` 라는 이름을 사용하고 있기 때문에 되도록 `accounts` 로 지정하는 것을 권장한다.
>

```python
# accounts 앱 생성
python .\manage.py startapp accounts

# 마이그레이션
python manage.py makemigrations

#마이그레이트
python manage.py migrate
```

![](https://velog.velcdn.com/images/king-dong-gun/post/8b27e657-1a4a-41e0-a8e8-f162cf49f57a/image.png)


#### 2. 커스텀 User 클래스 작성

- 생성한 accounts 앱의 `models.py`에 `AbstractUser` 클래스를 상속받는 커스텀 `User` 클래스를 작성한다.

#### models.py

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	pass
```

#### 3. AUTH_USER_MODEL 값 수정

- django 프로젝트에서 사용하는 기본 `User` 모델을 우리가 작성한 `User` 모델을 사용할 수 있도록 `AUTH_USER_MODEL` 값을 변경한다.
- Django 기본 사용자 모델은 내부적으로 `AUTH_USER_MODEL = "auth.User"` 를 사용하기 때문에 설정을 따로 작성해야 한다.

#### settings.py

```python
AUTH_USER_MODEL = "accounts.User"
```

#### 4. admin site에 대체한 User 모델을 등록

- 이제 **기존 User 클래스를 사용하지 않고 커스텀 User 클래스로 대체** 했기 때문에 `admin`에 새로 등록을 해주어야 한다.

#### admin.py

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

#### 5. 기존 `db.sqlite3` 삭제 후 새로 마이그레이션, 마이그레이트

- 기존 `auth_user` 를 `accounts_user` 로 교체하려면 기존 `db.sqlite3` 를 삭제하고 새로 마이그레이션 → 마이그레이트를 하면 `auth` 가 `accounts` 로 바뀐다.

![](https://velog.velcdn.com/images/king-dong-gun/post/f07938e6-3b2c-4f40-bf2a-da560503eb9b/image.png)


---

## 3. Login

**로그인 = 사용자가 자신이 누구인지 서버에 인증하는 과정**

로그인에 성공하면 서버는 사용자의 세션을 만들고, 그 세션을 찾기 위한 **`Session ID`**를 발급한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/08a3bf40-a5c9-480f-bbbf-2b6c1d67f199/image.png)


### 로그인 기능 구현

### 1. AuthenticationForm

Django에서는 로그인 인증에 사용할 수 있도록 `AuthenticationForm`이라는 기본 Form을 제공한다.

`AuthenticationForm`은 사용자가 로그인할 때 입력하는

- `username`
- `password`

값을 입력받고 인증하는 역할을 한다.

`AuthenticationForm`은 일반적인 `ModelForm`이 아니라 **일반 Form을 상속받은 Form**이다.

import는 다음과 같이 작성

```python
from django.contrib.auth.forms import AuthenticationForm
```

## 2. 로그인 경로 URL 생성

먼저 사용자가 로그인 페이지에 접근할 수 있도록 URL을 작성한다.

### accounts/urls.py

```python
app_name = 'accounts'

urlpatterns = [
    path("login/", views.login, name="login"),
]
```

`/accounts/login/` 주소로 요청이 들어오면 `views.login` 함수가 실행된다.

## 3. 로그인 페이지를 보여주는 View 작성

로그인 페이지에 사용할 `AuthenticationForm`을 생성한 뒤 템플릿으로 전달한다.

### accounts/views.py

```python
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# 로그인은 세션을 Create하는 로직
def login(request):

    # POST 요청이면 로그인 인증 및 세션 생성
    if request.method == "POST":
        pass

    # GET 요청이면 로그인 폼 출력
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)
```

`GET` 요청이 들어왔을 때 `AuthenticationForm()`을 생성하여 로그인 페이지에 전달한다.

## 4. 로그인 Form 출력

View에서 전달받은 `form`을 템플릿에서 출력한다.

### accounts/templates/accounts/login.html

```html
<body>
  <h1>로그인</h1>

  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form }}

    <input type="submit" value="로그인">
  </form>
</body>
```

`{{ form }}`을 작성하면 Django가 `AuthenticationForm`에 정의된 `username`, `password` 입력창을 자동으로 만들어준다.

로그인은 서버의 **세션 상태를 변경하는 요청**이므로 `POST` 방식으로 요청한다.

```html
method="POST"
```

POST 요청에서는 CSRF 공격을 방지하기 위해 아래 코드도 작성한다.

```html
{% csrf_token %}
```

## 5. 로그인 요청 처리

사용자가 아이디와 비밀번호를 입력하고 로그인 버튼을 누르면 같은 `login` 함수로 `POST` 요청이 들어온다.

사용자가 입력한 데이터는 `request.POST`에 들어있다.

```python
form = AuthenticationForm(request, request.POST)
```

입력한 정보가 올바른지 유효성 검사를 확인한다.

```python
if form.is_valid():
```

인증에 성공하면 로그인한 사용자 정보를 가져온다.

```python
user = form.get_user()
```

이후 Django가 제공하는 `login()` 함수를 이용해 세션을 생성한다.

```python
auth_login(request, user)
```

## 6. 로그인 View

Django의 `login` 함수와 커스텀 `login` 함수의 이름이 겹칠 수 있기 때문에, Django의 로그인 함수는 `auth_login`이라는 이름으로 import한다.

### accounts/views.py

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):

    # 로그인 요청
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()

            # 세션 생성
            auth_login(request, user)

            return redirect("articles:index")

    # 로그인 페이지 요청
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/3a588fc0-663c-472e-8f15-d721725a649f/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/35305d1e-4c6c-487b-95b3-99b76f8fe15e/image.png)

