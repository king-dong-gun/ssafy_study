### 1. Static Files

> 서버 측에서 변경되지 않고 고정적으로 제공되는 파일이다.
>

웹 사이트를 구성할 때 HTML뿐만 아니라 CSS, JavaScript, 이미지, 폰트 등의 파일도 필요하다.

이처럼 개발자가 미리 준비해두고 사용자에게 동일하게 제공하는 파일을 **정적 파일(Static Files)** 이라고 한다.

- CSS 파일
- JavaScript 파일
- 로고 및 이미지
- 아이콘
- 폰트

웹 사이트의 로고는 사용자가 바뀌더라도 동일한 파일을 사용하므로 Static File에 해당한다.

#### 웹 서버와 정적 파일

웹 서버가 제공하는 가장 기본적인 자원이 **정적파일** 이다.

#### 처리 과정

1. 사용자
    - 브라우저에 `http://example.com/images/logo.png` 라는 주소를 입력하면서 이미지를 요청한다.
2. 웹 서버
    - `/images/logo.png` 의 URL을 확인하고 서버에 미리 약속된 디렉토리에서 `logo.png` 를 찾는다.
3. 웹 서버
    - 찾은 이미지 파일을 HTTP 응답에 담아서 사용자에게 전송한다.
4. 사용자
    - 브라우저가 응답 받은 이미지 파일을 화면에 보여준다.

![](https://velog.velcdn.com/images/king-dong-gun/post/cba54521-b95c-412d-9e92-27a1bee8fb0f/image.png)


---

#### Static Files 기본 경로

Django에서 각 앱의 정적 파일을 저장하는 기본 경로는 다음과 같다.

```python
app폴더/static/
```

`articles` 앱에서 CSS 파일을 사용한다면 다음과 같은 구조를 만들 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/fef53d81-2e2f-4c67-aca6-57054afe9310/image.png)


#### style.css

```css
h1 {
    color: crimson;
}
```

---

#### Template에서 Static File 사용

Django Template에서 Static File을 사용하려면 먼저 `static` 태그를 불러와야 한다.

```html
{% load static %}
```

CSS 파일은 다음과 같이 연결한다.

```html
{% load static %}

<link
    rel="stylesheet"
    href="{% static 'stylesheets/style.css' %}"
>
```

`{% static %}` 태그는 정적 파일에 접근할 수 있는 URL을 만들어준다.

#### 적용 화면

CSS 파일이 정상적으로 적용되어 `h1`의 색상이 변경된 것을 확인할 수 있다.

또한 `{% static %}` 태그를 통해 정적 이미지의 URL이 `/static/...` 형태로 생성되어 브라우저에 정상적으로 출력되는 것을 확인할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/be5c8042-abb4-47d0-a78b-bcf206aeca37/image.png)


---

#### `{% load static %}`

> Django Template에서 Static 관련 Template Tag를 사용할 수 있도록 불러오는 역할을 한다.
>

```html
{% load static %}
```

`{% static %}`을 사용하려면 Template 파일에서 먼저 선언해야 한다.

단, `{% extends %}`를 사용하는 경우 `load` 태그는 상속되지 않기 때문에 필요한 Template 파일에서 직접 작성해야 한다.

---

#### `{% static %}`

> 정적 파일에 접근하기 위한 URL을 생성하는 Template Tag이다.
>

```html
{% static 'stylesheets/style.css' %}
```

라고 작성하면 Django가 `STATIC_URL` 설정을 이용하여 정적 파일의 URL을 만든다.

---

#### STATIC_URL

> 웹 페이지에서 정적 파일에 접근하기 위해 사용하는 URL의 시작 경로이다.
>

기본적으로 다음과 같이 설정된다.

```python
STATIC_URL = 'static/'
```

예를 들어:

```html
{% static 'images/sample-1.png' %}
```

를 사용한다면 브라우저에서는 다음과 같은 주소로 접근하게 된다.

```python
http://127.0.0.1:8000/static/images/sample-1.png
```

`STATIC_URL`은 서버 컴퓨터의 실제 파일 경로가 아니라 **브라우저에서 접근하기 위한 URL 주소**이다.

---

#### Static 이미지 사용

Static 폴더에 이미지를 저장할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/9612be4b-6bf3-4477-948d-6399e1038ca3/image.png)


Template에서는 다음과 같이 사용한다.

```html
{% load static %}

<img
    src="{% static 'images/sample-1.png' %}"
    alt="sample image"
>
```

`{% static %}` 태그를 사용하면 static 폴더에 있는 이미지의 URL을 생성하여 브라우저에 출력할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/c1ca4c44-561c-4b8d-ad5f-5910218f695e/image.png)


---

#### Static Files 추가 경로

Django에서는 각 앱 내부의 `static` 폴더뿐만 아니라 프로젝트에서 공통으로 사용하는 Static 폴더를 추가로 설정할 수 있다.

#### STATICFILES_DIRS

> Django가 기본 Static 경로 이외에 추가적으로 탐색할 정적 파일 경로를 지정하는 설정이다.
>

기본 경로는 각 앱 내부의:

```python
app/static/
```

이지만 여러 앱에서 공통으로 사용하는 CSS나 이미지가 있다면 프로젝트 최상단에 Static 폴더를 만들 수도 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/d2d5cd2c-0652-4549-a824-15ee8d96d030/image.png)


이 경로를 Django가 찾을 수 있도록 `settings.py`에 설정한다.

#### settings.py

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

Django는 Static File을 찾을 때 추가 경로를 확인하고 각 앱의 `static` 폴더도 탐색한다.

#### 추가 경로의 Static 이미지 사용

Template에서는 다음과 같이 사용한다.

```html
{% load static %}

<img
    src="{% static 'sample-2.png' %}"
    alt="sample image"
>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/e9e188f4-48b4-4e7c-9b1a-014b869a75a4/image.png)


---

### 2. Media Files

> 사용자가 웹 사이트를 통해 직접 업로드하는 파일이다.
>

Static File은 개발자가 미리 준비한 파일이라면 Media File은 사용자가 서비스 이용 중 직접 업로드하는 파일이다.

예를 들면:

| 구분 | 예시 |
| --- | --- |
| Static File | 로고, CSS, 아이콘 |
| Media File | 프로필 사진, 게시글 첨부 이미지 |

> Static = 개발자가 준비한 파일
>
>
> Media = 사용자가 업로드한 파일
>

---

#### ImageField

> 이미지를 업로드하기 위해 사용하는 Django Model Field이다.
>

게시글에 이미지를 추가하려면 Model에 `ImageField`를 작성한다.

#### models.py

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    image = models.ImageField(
        upload_to='images/',
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

#### `upload_to`

업로드한 파일을 어떤 하위 경로에 저장할지 지정한다.

```python
upload_to='images/'
```

#### `blank=True`

Form에서 해당 필드를 비워도 유효성 검사를 통과할 수 있도록 한다.

즉 이미지를 반드시 첨부하지 않아도 게시글을 작성할 수 있다.

---

#### Pillow 설치

Django에서 `ImageField`를 사용하려면 이미지 처리를 위한 **Pillow 라이브러리**가 필요하다.

```
pip install pillow
```

설치 후 Migration을 진행한다.

```python
python manage.py makemigrations
python manage.py migrate
```

필요하다면 의존성도 기록한다.

```
pip freeze > requirements.txt
```

---

#### MEDIA_ROOT

> 사용자가 업로드한 Media File이 실제 서버의 어느 폴더에 저장될지를 지정한다.
>

#### settings.py

```python
MEDIA_ROOT = BASE_DIR / 'media'
```

예를 들어 사용자가 이미지를 업로드하면 실제 파일은 다음과 같이 저장될 수 있다.

```
프로젝트/
└── media/
    └── images/
        └── sample-1.png
```

`MEDIA_ROOT`는 **실제 파일 저장 위치**이다.

---

#### MEDIA_URL

> Media File을 브라우저에서 접근하기 위한 URL의 시작 경로이다.
>

#### settings.py

```python
MEDIA_URL = 'media/'
```

예를 들어 실제 파일이 `media/images/sample-1.png` 에 저장이 되어있으면 브라우저는

`http://127.0.0.1:8000/media/images/sample-1.png` 로 접근한다.

| 설정 | 역할 |
| --- | --- |
| `MEDIA_ROOT` | 실제 파일 저장 경로 |
| `MEDIA_URL` | 브라우저 접근 URL |

---

#### Media URL 연결

개발 환경에서 업로드된 Media File을 제공하기 위해 프로젝트의 `urls.py`에 설정을 추가한다.

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
```

Django 개발 서버가 `/media/`로 들어오는 요청을 확인한 뒤 `MEDIA_ROOT`에 저장된 실제 파일을 찾아 응답하도록 한다.

---

#### 이미지 업로드 기능 구현

파일 업로드를 위해서는 Form과 View에서 추가적인 설정이 필요하다.

#### Form 설정

파일을 서버로 전송하려면 `<form>` 태그에 다음 속성이 필요하다.

```python
enctype="multipart/form-data"
```

#### create.html

```html
<form
    action="{% url 'articles:create' %}"
    method="POST"
    enctype="multipart/form-data"
>
    {% csrf_token %}
    {{ form }}

    <input type="submit">
</form>
```

일반적인 문자 데이터와 달리 파일을 함께 전송할 때는 반드시 `multipart/form-data`를 사용해야 한다.

#### 적용 화면

게시글 생성 화면에 이미지 파일을 선택할 수 있는 입력 요소가 추가된다.

![](https://velog.velcdn.com/images/king-dong-gun/post/5ca8d334-84f8-4534-90ed-b42e0904b769/image.png)


---

#### request.FILES

문자 데이터는 `request.POST`에 들어가지만 업로드한 파일은 `request.FILES`에 들어간다.

#### views.py

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            article = form.save()
            return redirect(
                'articles:detail',
                article.pk,
            )

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'articles/create.html',
        context,
    )
```

`request.POST` : 일반 입력 데이터

`request.FILES` : 파일 데이터

로 구분할 수 있다.

---

#### 업로드 파일 저장

이미지를 선택하고 게시글을 생성하면 실제 이미지 파일은 MEDIA_ROOT 아래에 저장된다.

![](https://velog.velcdn.com/images/king-dong-gun/post/9a34e400-158d-4006-a441-4d866b6da93f/image.png)


DB에는 이미지 파일 자체가 저장되는 것이 아니라 **파일의 경로 문자열**이 저장된다.

#### 확인 화면

프로젝트의 `media/images` 폴더에 실제 이미지가 저장된 것을 확인할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/154bc30a-a6a8-41a0-bd9b-a56520afd6fe/image.png)


---

#### 업로드 이미지 제공

게시글 상세 페이지에서 업로드한 이미지를 보여주려면 `ImageField`의 `.url` 속성을 사용한다.

#### detail.html

```html
{% if article.image %}
    <img
        src="{{ article.image.url }}"
        alt="image"
    >
{% endif %}
```

#### `.url`

> 저장된 이미지 파일에 브라우저가 접근할 수 있는 URL을 반환한다.
>

`{{ article.image.url }}` 의 결과가 `/media/images/sample-1.png` 가 된다.

이미지를 업로드하지 않은 게시글에서 바로 `.url`을 사용하면 오류가 발생할 수 있기 때문에 조건문을 사용한다.

```html
{% if article.image %}
```

#### 적용 화면

게시글 제목과 내용뿐만 아니라 사용자가 업로드한 이미지가 상세 페이지에 표시된다.

![](https://velog.velcdn.com/images/king-dong-gun/post/e7763408-83f1-4433-8d38-6c77d9021d8c/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/3777681d-0d8a-4200-92dd-c51a648a8b78/image.png)


---

#### 업로드 이미지 수정

게시글 수정에서도 파일을 업로드할 수 있어야 하기 때문에 생성과 동일하게 설정해야 한다.

#### update.html

```html
<form
    action="{% url 'articles:update' article.pk %}"
    method="POST"
    enctype="multipart/form-data"
>
    {% csrf_token %}
    {{ form }}

    <input type="submit">
</form>
```

View에서도 `request.FILES`를 전달한다.

```python
form = ArticleForm(
    request.POST,
    request.FILES,
    instance=article,
)
```

수정에서는

`request.POST` : 수정된 일반 데이터

`request.FILES` : 새로 업로드한 파일

`instance = article` : 수정할 기존 게시글

을 함께 전달한다.

#### 적용 화면

기존 게시글의 이미지를 다른 이미지로 변경한 뒤 수정된 결과를 확인할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/035faa24-c7c6-4079-b6df-9fd704ae2a4b/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/8a18dc11-86a6-4bf1-ae69-1c6ae9ac5982/image.png)


---

#### upload_to 활용

`upload_to`는 단순히 고정된 폴더 문자열만 사용할 수 있는 것이 아니다.

업로드 날짜 등을 이용해 동적으로 경로를 만들 수 있다.

#### 날짜 기반 경로

```python
image = models.ImageField(
    blank=True,
    upload_to='%Y/%m/%d/',
)
```

예를 들어 2100년 1월 1일 업로드한다면 `2100/01/01/` 폴더 아래 저장될 수 있다.

---

#### 함수를 이용한 경로

복잡한 규칙이 필요하다면 함수를 정의할 수도 있다.

```python
def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'
```

```python
image = models.ImageField(
    blank=True,
    upload_to=articles_image_path,
)
```

형태로 사용한다.

`upload_to` 함수는 일반적으로

`instance` : 파일이 첨부되는 Model 객체

`filename` : 업로드한 원본 파일 이름

을 전달받는다.

---

#### Static File과 Media File 비교

| 구분 | Static File | Media File |
| --- | --- | --- |
| 파일 생성 주체 | 개발자 | 사용자 |
| 예시 | CSS, JS, 로고 | 프로필 사진, 게시글 이미지 |
| 실제 파일 경로 | static 폴더 | MEDIA_ROOT |
| URL 설정 | STATIC_URL | MEDIA_URL |
| 추가 경로 설정 | STATICFILES_DIRS | MEDIA_ROOT |
| Template 사용 | `{% static %}` | `.url` |
| 업로드 처리 | 필요 없음 | `request.FILES` 필요 |

> Static File = 개발자가 미리 준비한 파일
>
>
> Media File = 사용자가 업로드한 파일
>

---

### 3. 참고

#### AWS 인프라

#### AWS

> Amazon에서 제공하는 클라우드 컴퓨팅 서비스이다.
>

직접 서버, 파일 저장소, 데이터베이스 장비를 구축하지 않고 인터넷을 통해 필요한 만큼 사용할 수 있다.

대표적인 서비스

| 서비스 | 역할 |
| --- | --- |
| EC2 | 서버 |
| S3 | 파일 저장소 |
| RDS | 데이터베이스 |

---

#### Django와 AWS

실제 서비스를 운영한다고 가정하면 역할을 다음과 같이 나눌 수 있다.

```
EC2
→ Django 애플리케이션 실행

S3
→ 이미지, Media File, Static File 저장

RDS
→ 게시글, 사용자 정보 등의 DB 데이터 저장
```

동작 흐름의 예시는 다음과 같다.

```
사용자
 ↓
EC2의 Django 서버
 ↓
RDS에서 데이터 조회
 ↓
HTML 응답
 ↓
필요한 이미지 → S3 요청
 ↓
사용자에게 이미지 제공
```

사용자가 이미지를 업로드하는 경우에는 Django 서버가 파일을 받아 S3에 저장하는 방식으로 구성할 수도 있다.

#### AWS 구조

![](https://velog.velcdn.com/images/king-dong-gun/post/56a2cd59-531f-4419-b15d-da86722bd12b/image.png)


---

#### 클라우드를 사용하는 이유

#### 비용 절감

직접 물리 서버를 구매하지 않고 필요한 만큼 사용할 수 있다.

#### 유연성과 확장성

서비스 사용량에 따라 서버나 저장 공간을 조절할 수 있다.

#### 글로벌 서비스

여러 지역의 데이터 센터를 이용하여 다양한 국가의 사용자에게 서비스를 제공할 수 있다.

---

#### BaseModelForm

Django의 `ModelForm`은 내부적으로 `BaseModelForm`을 기반으로 동작한다.

`BaseModelForm`의 생성자에는 여러 인자가 존재하며 그중 파일 데이터를 받는 인자도 존재한다.

```python
files=None
```

그래서 ModelForm을 생성할 때:

```python
ArticleForm(
    request.POST,
    request.FILES,
)
```

처럼 첫 번째 인자에는 일반 데이터, 두 번째 인자에는 파일 데이터를 전달할 수 있다.

`data` → `request.POST`

`files` → `request.FILES`

형태로 연결된다.

---

#### Django Static & Media 정리

#### Static Files 정리

> 개발자가 미리 준비하여 고정적으로 제공하는 파일이다.
>

```python
STATIC_URL = 'static/'
```

추가적인 Static 경로가 필요하다면

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

를 사용한다.

Template에서는

```html
{% load static %}

{% static 'images/logo.png' %}
```

형태로 접근한다.

---

#### Media Files 정리

> 사용자가 웹 서비스를 이용하면서 직접 업로드하는 파일이다.
>

실제 저장 위치

```python
MEDIA_ROOT = BASE_DIR / 'media'
```

브라우저 접근 주소

```python
MEDIA_URL = 'media/'
```

이미지 업로드 Model

```python
image = models.ImageField(
    upload_to='images/',
    blank=True,
)
```

파일 전송 Form

```python
<form enctype="multipart/form-data">
```

View

```python
form = ArticleForm(
    request.POST,
    request.FILES,
)
```

이미지 출력

```
{% if article.image %}
    <img src="{{ article.image.url }}" alt="image">
{% endif %}
```

핵심은 다음과 같다.

> `STATIC_URL` → Static File의 웹 주소
>
>
> `STATICFILES_DIRS` → 추가 Static 탐색 경로
>
> `MEDIA_ROOT` → 업로드 파일의 실제 저장 위치
>
> `MEDIA_URL` → 업로드 파일의 웹 주소
>
> `ImageField` → 이미지 업로드 Model Field
>
> `enctype="multipart/form-data"` → 파일 전송을 위한 Form 설정
>
> `request.FILES` → 업로드한 파일 데이터
>
> `.url` → 업로드한 파일의 접근 URL
>