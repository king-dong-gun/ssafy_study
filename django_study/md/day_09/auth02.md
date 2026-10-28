`Authentication System_01`에서 로그인 기능을 구현했으니, `Authentication System_02`에서는

**로그아웃**, **회원 가입**, **회원 탈퇴**를 구현해보자.

---

## 1. LOGOUT

### 1. Logout

로그아웃은 현재 사용자의 **Session을 삭제하는 과정**이다.

로그아웃이 수행되면 다음 두 가지 작업이 진행된다.

- 서버에 저장된 **Session Data 삭제**
- 클라이언트가 가지고 있는 **Session ID 삭제**

서버와 클라이언트에 남아 있는 로그인 관련 세션 정보를 제거하여 로그인 상태를 해제한다.

#### logout (request)

Django에서는 `logout(request)` 함수를 사용하여 로그아웃을 처리할 수 있다.

`logout(request)`가 실행되면 다음과 같은 작업이 수행된다.

1. DB에서 현재 요청에 해당하는 **Session Data 삭제한다.**
2. 현재 **세션 데이터를 제거하고 세션 쿠키를 만료시켜 로그인 상태를 해제**한다**.**

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
```

### 2. 구현

#### accounts/urls.py에 로그아웃 url 등록

로그아웃 경로 및 링크를 생성한다.

```python
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
```

#### accounts/views.py에 로그아웃 함수 작성

Django에서 제공하는 `logout()` 함수를 사용하여 현재 사용자의 세션 정보를 제거한다.

`django.contrib.auth.logout`과 직접 작성한 `logout` 함수의 이름이 겹치므로 `auth_logout`이라는 이름으로 import한다.

```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    ## 인증된 사용자가 보낸 요청을 받아 세션 데이터를 제거
    auth_logout(request)
		return redirect("articles:index")
```

#### articles/index.html에 POST 요청

로그아웃은 세션을 삭제하는 요청이므로 `POST` 방식을 사용하고,

CSRF 공격 방지를 위한 `{% csrf_token %}`을 작성한다.

```html
  <form action="{% url "accounts:logout" %}" method="post">
      {% csrf_token %}
      <input type="submit" value="LOGOUT">
  </form>
```

#### 로그인 성공 후 로그아웃 버튼 클릭

![](https://velog.velcdn.com/images/king-dong-gun/post/7aec73e2-a129-482a-baba-5c0220fa2eb8/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/c9764019-8120-470a-bd18-7e4b461d9b71/image.png)


#### 화면 확인 후 로그 확인

![](https://velog.velcdn.com/images/king-dong-gun/post/464c1b19-01b5-4c85-880c-329f663247a9/image.png)


---

## 2. 회원 가입

### 1. 회원 가입

회원 가입은 새로운 **User 객체를 생성하는 과정**이다.

사용자로부터 **아이디**, **비밀번호** 등의 정보를 입력받아 DB에 새로운 User 객체를 생성하고 저장한다.

사용자가 입력한 회원 정보를 기반으로 새로운 계정을 생성하는 과정이다.

### 2. 구현

#### accounts/urls.py 회원 가입 등록

```python
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]
```

#### accounts/views.py에 signup 함수 작성

Django에서 기본으로 제공하는 회원가입 Form인 `UserCreationForm`을 사용한다.

```python
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def signup(request):
    if request.method == "POST":
        pass
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
```

#### index.html, signup.html에 회원 가입 화면 코드 작성

```html
<!-- index.html -->
<a href="{% url "accounts:signup" %}">[SIGNUP]</a>
```

```html
<!-- sign.html -->
<body>
  <h1>회원가입</h1>
  <form action="{% url "accounts:signup" %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="회원가입">
  </form>
</body>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/eccc74e4-be49-4d07-b04a-16e3edc9af02/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/cfaae35a-5cfa-4bfd-9e8b-73486be872d2/image.png)


#### accounts/views.py에 데이터 저장을 위해 POST 요청

```python
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
```

#### 회원 데이터 입력

![](https://velog.velcdn.com/images/king-dong-gun/post/b160fcb8-bf37-435a-a820-cfdb9b496da9/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/5d4749b3-37d7-4ca4-8494-0e76d50fd7d2/image.png)


하지만 회원 가입 버튼을 누르면 위와 같은 에러가 나온다.

```
AttributeError

Manager isn't available;
'auth.User' has been swapped for 'accounts.User'
```

#### Custom User 모델과 UserCreationForm 연결

에러가 발생하는 이유는 현재 프로젝트에서 Django 기본 `auth.User`가 아닌 `accounts.User`를 사용하고 있기 때문이다.

`settings.py`에서는 다음과 같이 Custom User 모델을 사용하도록 설정되어 있다.

그리고 `accounts/models.py`에서는 Django의 `AbstractUser`를 상속받아 Custom User 모델을 생성한다.

```python
AUTH_USER_MODEL = 'accounts.User'
```

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

`AbstractUser`를 상속하면 Django 기본 User의 `username`, `password` 등의 필드와 인증 기능을 그대로 사용할 수 있다.

현재는 추가할 필드가 없기 때문에 `pass`를 작성하지만, 이후 필요한 사용자 정보를 추가할 수 있도록 Custom User 모델을 미리 생성한다.

#### 에러 발생 원인

현재 `views.py`에서 사용하고 있는 `UserCreationForm`은 Django에서 기본으로 제공하는 회원가입 Form이다.

```python
from django.contrib.auth.forms import UserCreationForm
```

하지만 프로젝트에서는 기본 `auth.User` 대신 `accounts.User`를 사용하도록 변경했기 때문에, 기본 `UserCreationForm`을 그대로 사용할 경우 User 모델이 서로 맞지 않는 문제가 발생한다.

흐름은 아래와 같다.

```python
settings.py
    ↓
accounts.User 사용

UserCreationForm
    ↓
기본 auth.User 사용

User 모델 불일치
    ↓
AttributeError 발생
```

그래서 프로젝트에서 사용하는 Custom User 모델과 연결된 새로운 회원가입 Form을 만들어야 한다.

### 3. get_user_model()

> 현재 프로젝트에서 활성화된 사용자 모델을 반환하는 함수이다.
>

프로젝트 설정 `AUTH_USER_MODEL` 에 따라 기본 `User` 모델일수도, 내가 직접 만든 `커스텀 User` 모델일 수도 있기 때문에 올바른 모델을 동적으로 가져오기 위해 사용한다.

- 현재 활성화된 User 모델을 직접 가져와야 할 때 `get_user_model()`을 사용한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/256221df-75bd-4893-938f-3b491bd89f84/image.png)


#### **accounts/forms.py 생성**

프로젝트에서 사용하는 Custom User 모델과 연결하기 위해 `UserCreationForm`을 상속받아 새로운 Form을 작성한다.

```python
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
```

#### accounts/views.py에 `UserCreationForm` 가 아닌 `CustomUserCreationForm` 로 교체

```python
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
```

#### 회원 가입 및 DB 확인

![](https://velog.velcdn.com/images/king-dong-gun/post/8e6502cd-8fa4-40f5-8ed8-004f49aabf33/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/e99fe81f-5120-4d87-8e80-638472dc3ddc/image.png)


현재는 DB에 회원 데이터를 저장만 시키고, 회원 가입 후 자동 로그인을 시켜주지는 않는다.

따로 로그인을 진행하면 로그인 된 화면을 볼 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/ebbd8aa1-1707-424f-9eea-d5a8ca809636/image.png)


---

## 3. 회원 탈퇴

### 1. 회원 탈퇴

회원 탈퇴는 현재 로그인한 **User 객체를 삭제하는 과정**이다.

Django에서는 현재 요청을 보낸 사용자를 `request.user`로 확인할 수 있으며, `delete()` 메서드를 사용하여 해당 User 객체를 삭제할 수 있다.

`request.user` : 현재 요청을 보낸 사용자 객체

`request.user.delete()` : 현재 로그인 한 `User` 객체를 DB에서 삭제

### 2. 구현

#### accounts/urls.py에 회원 탈퇴 url 등록

```python
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
]
```

#### accounts/views.py에 회원 탈퇴 함수 작성

```python
def delete(request):
    request.user.delete()
    return redirect("articles:index")
```

#### index.html에 회원 탈퇴 코드 작성

```html
  <form action="{% url 'accounts:delete' %}" method="post">
      {% csrf_token %}
      <input type="submit" value="[DELETE]">
  </form>
```

#### 회원 탈퇴 로그, DB 확인

![](https://velog.velcdn.com/images/king-dong-gun/post/fcbb2cfe-d005-4c61-a752-92dda3c6aa62/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/a7b06fcb-6ede-4b7e-b83d-25377d7e1685/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/9aa6d575-010c-4607-8bd0-143b748a044f/image.png)


---

## 4. 인증된 사용자에 대한 접근 제한

### 1. is_authenticated

`is_authenticated`는 **현재 사용자가 인증된 사용자인지 확인하는 User 모델의 속성**이다.

- 인증된 사용자라면 `True`
- 비인증 사용자라면 `False`

주로 다음과 같은 경우에 사용한다.

- 로그인 상태에 따라 다른 메뉴를 보여줄 때
- 로그인한 사용자에게만 특정 기능을 허용하고 싶을 때

#### index.html

```html
{% if request.user.is_authenticated %}
    <!-- 로그인한 사용자에게만 보이는 화면 -->
    <h3>Hello, {{ user.username }}</h3>

    <form action="{% url 'accounts:logout' %}" method="post">
        {% csrf_token %}
        <input type="submit" value="LOGOUT">
    </form>

    <form action="{% url 'accounts:delete' %}" method="post">
        {% csrf_token %}
        <input type="submit" value="[DELETE]">
    </form>

    <a href="{% url 'articles:create' %}">[CREATE]</a>

{% else %}
    <!-- 로그인하지 않은 사용자에게만 보이는 화면 -->
    <a href="{% url 'accounts:login' %}">[LOGIN]</a>
    <a href="{% url 'accounts:signup' %}">[SIGNUP]</a>
{% endif %}
```

#### 로그인 전

![](https://velog.velcdn.com/images/king-dong-gun/post/00e4eb01-38f0-4a5a-a98c-2ea9d39d9775/image.png)


#### 로그인 후

![](https://velog.velcdn.com/images/king-dong-gun/post/91adf7ba-5f61-4c10-8f4e-e32fac8c6668/image.png)


#### 로그인 이후 회원 가입 페이지 리다이렉트 막기

```python
def signup(request):
    if request.user.is_authenticated:
        return redirect("articles:index")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)
```

### 2. login_required

`login_required`는 **인증된 사용자만 특정 페이지에 접근할 수 있도록 제한하는 데코레이터**이다.

로그인하지 않은 사용자가 `@login_required`가 적용된 View에 접근하면, 해당 View를 실행하지 않고 로그인 페이지로 이동한다.

#### articles/views.py에 인증된 사용자만 게시글 작성/수정/삭제 할 수 있도록 데코레이터 등록

```python
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
	...
	return render(request, 'articles/create.html', context)

@login_required
def delete(request, article_pk):
	...
	return redirect('articles:index')

@login_required
def update(request, article_pk):
...
	return render(request, 'articles/update.html', context)
```

#### accounts/views.py에 인증된 사용자만 로그아웃/탈퇴 할 수 있도록 데코레이터 등록

```python
from django.contrib.auth.decorators import login_required

@login_required
def logout(request):
...
	return redirect("articles:index")

@login_required
def delete(request):
...
	return redirect("articles:index")
```