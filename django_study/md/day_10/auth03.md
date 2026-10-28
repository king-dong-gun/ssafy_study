`Authentication System_02`에서 로그아웃, 회원가입, 회원 탈퇴 기능을 구현했으니, `Authentication System_03`에서는 **회원정보 수정, 비밀번호 변경, 세션 무효화**를 구현해보자.

## 1. 회원정보 수정

> 기존에 저장되어 있는 `User` 객체의 정보를 새로운 입력값으로 변경하는 과정이다.
>

회원정보 수정은 게시글 수정과 비슷하게 동작한다.

기존 사용자의 정보를 수정하기 위해서는 먼저 **수정할 User 객체를 가져온 뒤**, 사용자가 새롭게 입력한 정보로 기존 데이터를 갱신한다.

### 1. UserChangeForm()

`UserChangeForm`은 Django에서 제공하는 **회원정보 수정용 built-in ModelForm**이다.

사용자가 입력한 회원정보를 받아 기존 `User` 객체의 정보를 수정할 때 사용한다.

#### 특징

- Django의 `ModelForm`을 기반으로 만들어져 있다.
- 회원정보 수정 시 사용자의 입력 데이터를 받는다.
- 입력된 데이터에 대해 **유효성 검사**를 진행한다.
- 검증을 통과하면 기존 `User` 객체의 정보를 **수정하고 저장**할 수 있다.
- Django에서는 주로 **관리자 페이지에서 사용자 정보를 수정할 때 사용하는 Form**이다.

#### 사용시 주의점

기본 `UserChangeForm`을 그대로 사용하면 `User` 모델이 가지고 있는 **모든 정보(fields)**가 출력될 수 있다.

문제는 이 안에 일반 사용자가 접근하면 안 되는 정보까지 포함되어 있다는 점이다.

예를 들어 다음과 같은 필드들이 함께 노출될 수 있다.

- `is_staff`
- `is_superuser`
- `groups`
- `user_permissions`
- `is_active`

이러한 정보는 관리자 권한이나 사용자 권한과 관련된 정보이므로, 일반 사용자의 회원정보 수정 화면에 그대로 노출하면 안 된다.

### 2. 구현

#### accounts/urls.py에 주소 등록

```python
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]
```

#### accounts/views.py에 update 함수 작성

```python
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = CustomUserChangeForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)
```

#### accounts/forms.py에 커스텀 유저 모델 사용

```python
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email")
```

#### accounts/update.html 화면 코드 작성

```html
<body>
<h1>회원정보 수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="정보수정">
</form>
</body>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/e2953f6f-f7ca-4891-9bf8-eaeb572a9fee/image.png)


#### 기존

![](https://velog.velcdn.com/images/king-dong-gun/post/cc119741-13c8-446f-973a-9cd1a06a3b25/image.png)


#### 변경

![](https://velog.velcdn.com/images/king-dong-gun/post/32a433a2-be27-4610-8bc2-ea37f8131b42/image.png)


---

## 2. 비밀번호 변경

> Django에서 비밀번호 변경은 단순히 비밀번호 문자열만 바꾸는 것이 아니라, **User 객체의 password 필드를 안전하게 갱신하는 과정**이다.
>

기존 비밀번호를 통해 사용자를 인증한 뒤, 새 비밀번호를 입력받아 암호화하여 저장한다.

### **PasswordChangeForm**

`PasswordChangeForm`은 Django에서 제공하는 **비밀번호 변경용 built-in Form**이다.

현재 로그인한 사용자의 기존 비밀번호를 확인한 뒤, 새로운 비밀번호로 변경할 때 사용한다.

#### 주요 입력값

기본적으로 다음 값을 입력받는다.

- `old_password` : 기존 비밀번호
- `new_password1` : 새 비밀번호
- `new_password2` : 새 비밀번호 확인

#### 사용시 주의점

Django는 비밀번호를 평문 그대로 저장하지 않고, **해시 처리된 형태로 저장**한다.

`PasswordChangeForm`을 사용하면 Django가 내부적으로 비밀번호를 해시 처리해 저장하므로, 개발자가 직접 암호화 코드를 작성할 필요는 없다.

따라서 비밀번호를 직접 `User.password`에 대입하기보다 `PasswordChangeForm`이나 `set_password()`를 사용해야 한다.

### 2. 구현

#### accounts/urls.py에 주소 등록

```python
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.password, name='password'),
]
```

#### accounts/views.py에 password 함수 작성

```python
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        "form": form
    }
    return render(request, "accounts/password.html", context)
```

#### accounts/password.html 화면 코드 작성

```html
<body>
<h1>비밀번호 변경</h1>
<form action="{% url 'accounts:password' %}" method="POST">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="비밀번호 변경">
</form>
</body>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/2afaa273-f557-48e9-a65a-5a6a2fcf1546/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/dcc67f8e-8ce6-4f8f-aea4-a9dee5147379/image.png)


하지만 비밀번호를 변경하면 기존 세션과의 회원 인증 정보가 일치하지 않아 로그인 상태가 유지되지 않고, ㄹ로그아웃 처리된다….

---

## 3. 세션 무효화 방지

> Django는 로그인한 사용자의 인증 상태를 유지하기 위해 세션에 **인증 관련 해시값**을 함께 저장한다.
>

사용자가 비밀번호를 변경하면 비밀번호에서 만들어지는 해시값도 함께 변경된다.

그러면 기존 세션에 저장되어 있던 인증 해시값과 현재 사용자의 인증 해시값이 서로 달라지게 되어 로그아웃 처리가 된다.

### 1. `update_session_auth_hash`

> 암호 변경 시 세션 무효화를 막아주는 함수이다.
>

암호가 변경되면 새로운 `password` 의 `Session Data` 로 기존 세션을 자동으로 갱신한다.

### 2. 구현

#### **accounts/views.py에 `update_session_auth_hash` 적용**

비밀번호 변경 후에도 로그인 상태를 유지하기 위해 `update_session_auth_hash()`를 사용한다.

```python
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("articles:index")
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        "form": form
    }
    return render(request, "accounts/password.html", context)
```

#### 변경 전

![](https://velog.velcdn.com/images/king-dong-gun/post/b4a8f652-20d8-44e9-bc75-bfc4c0546b31/image.png)


#### 변경 후

![](https://velog.velcdn.com/images/king-dong-gun/post/68c23b93-04c3-4e19-b27e-91f65e9c3ad3/image.png)


변경 전과 변경 후의 `password` 의 해쉬 값이 바뀐 것을 확인할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/0ce64d7e-17e7-4103-86ea-601ab1a0a18c/image.png)

그리고 변경 후에도 로그인이 그대로 유지되는 것을 확인할 수 있다.

이와 같이, `form.save()`를 통해 비밀번호를 변경한 뒤, `update_session_auth_hash(request, user)`로 현재 세션의 인증 정보를 갱신한다.

이렇게 하면 비밀번호가 변경되어도 현재 사용자의 로그인 상태를 유지할 수 있다.

---

## 4. 비밀번호 암호화

사용자의 비밀번호는 **그대로 저장하면 안 된다.**

#### 1. 평문 저장

비밀번호를 사용자가 입력한 그대로 저장하는 방식이다.

```
입력 비밀번호: 1234
DB 저장값:     1234
```

이 방식은 DB가 유출되면 실제 비밀번호가 그대로 노출되기 때문에 **보안에 매우 취약하다.**

#### 2. 인코딩

인코딩은 데이터를 일정한 규칙에 따라 다른 형태로 변환하는 방식이다.

하지만 **규칙을 알면 원래 값으로 되돌릴 수 있기 때문에** 비밀번호 저장 방식으로 적절하지 않다.

| 방식 | 원래 값 복원 | 비밀번호 저장 |
| --- | --- | --- |
| 평문 | 바로 확인 가능 | ❌ |
| 인코딩 | 규칙을 알면 가능 | ❌ |
| 해시 | 복원이 매우 어려움 | ✅ |

#### 3. 해시(Hash)

**해시**는 데이터를 고정된 길이의 값으로 변환하는 과정이다.

해시의 주요 특징

- 입력값의 길이와 관계없이 **고정된 길이의 결과** 생성
- 해시값으로 원래 값을 알아내기 어려운 **단방향성**
- 입력값이 조금만 달라도 결과가 크게 달라지는 **눈사태 효과**

비밀번호 자체를 저장하는 것이 아니라 **비밀번호로 만든 해시값을 저장**한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/e42b27fc-8da3-4bb7-b722-f69668c33f99/image.png)


#### 4. 해시 함수

> 임의 길이 데이터를 입력 받아 고정 길이의 값으로 변환해 주는 함수이다.
>

#### 해시 함수의 특징

해시 함수는 데이터를 입력받아 **고정된 길이의 해시값**으로 변환한다.

1. **고정된 길이**
    - 입력 데이터의 길이와 관계없이 결과값의 길이는 항상 일정하다.
2. **단방향성 (One-way)**
    - 해시값을 보고 원래 입력값을 알아내는 것은 매우 어렵다.
3. **눈사태 효과 (Avalanche Effect)**
    - 입력값이 조금만 달라져도 결과값은 완전히 다르게 나온다.

### 5. Django에서 암호화

> django는 기본적으로 `SHA-256` 을 바탕으로 해 비밀번호를 저장한다.
>

#### 1. SHA-256

> 현재 가장 널리 사용되는 표준 암호화 해시 알고리즘이다.
>

어떤 데이터를 넣어도 항상 **256비트**의 결과물을 만들어낸다.

현재는 가장 신회받고, 전 세계 보안 표준으로 사용되고있다.

#### 2. 문제

해시 함수를 활용해 단방향 암호화를 해도 공격자들은 해기 값을 미리 계산해두는 방식으로 공격을 시도한다.

이를 **레인보우 테이블** 공격이라고 한다.

#### 3. 레인보우 테이블

> 공격자가 자주 사용하는 비밀번호들을 미리 수백만, 수십억 개를 해시로 변환해 저장해 둔 거대한 정답지이다.
>

#### 공격방식

1. 공격자가 DB를 탈취해 사용자의 비밀번호 해시 값을 얻는다.
2. 해시 값을 공격자 자신의 레인보우 테이블에서 검색하낟.
3. 테이블에서 일치되는 값을 찾아내면서, 역방향으로 되돌리지 않고, 비밀번호를 알아낸다.

![](https://velog.velcdn.com/images/king-dong-gun/post/f4fda6e8-20df-4629-9dd9-9a4473d7514c/image.png)


#### 4. 레인보우 테이블 방어: Salt

같은 비밀번호라도 사용자마다 서로 다른 `Salt`를 추가한 뒤 해시하기 때문에 **서로 다른 해시값**이 생성된다.

예를 들어 두 사용자가 같은 `qwer1234`를 사용하더라도,

```
User A : qwer1234 + 임의의 Salt → 서로 다른 해시값
User B : qwer1234 + 임의의 Salt → 서로 다른 해시값
```

이처럼 기존에 만들어 둔 레인보우 테이블의 해시값과 일치하지 않게 만들어 **레인보우 테이블 공격을 어렵게 한다.**

`Salt`는 해시값과 함께 데이터베이스에 저장된다.

#### 5. 무차별 대입 공격(Brute-force Attack)

> 가능한 비밀번호를 하나씩 직접 대입해 정답을 찾는 공격 방식이다.
>

`Salt`를 사용하면 레인보우 테이블 공격은 어렵게 만들 수 있지만, 비밀번호를 직접 하나씩 대입하는 공격까지 막을 수는 없다.

![](https://velog.velcdn.com/images/king-dong-gun/post/6a57175d-51e1-4754-80e4-b8287329068c/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/b96ca01a-ed01-46e3-a4a3-d359a82fcddb/image.png)


#### 6. Key Stretching

> 해시 연산을 여러 번 반복해 **비밀번호 검증 속도를 의도적으로 늦추는 방식**이다.
>

공격자가 많은 비밀번호를 대입하려면 그만큼 연산 시간이 오래 걸리기 때문에 **무차별 대입 공격을 어렵게 만든다.**

Django는 이를 위해 `PBKDF2` 알고리즘을 사용한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/5913c98d-e0cd-4c18-90e9-45690e81fae6/image.png)
