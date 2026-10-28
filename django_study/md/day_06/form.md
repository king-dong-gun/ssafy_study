## 1. Django Form

### 1. HTML Form의 한계

기존에는 사용자의 데이터를 입력받기 위해 HTML의 `<form>` 태그를 직접 작성했다.

하지만 HTML Form 자체는 사용자가 입력한 데이터가 **올바른 데이터인지 검사하는 기능이 부족하다.**

예를 들어 다음과 같은 상황을 직접 처리해야 한다.

- 필수 값이 비어 있는지
- 입력 형식이 올바른지
- 글자 수가 제한을 넘었는지
- 잘못된 데이터가 입력되었는지

이러한 검증 로직을 직접 작성하면 코드가 복잡해질 수 있다.

### 2. 유효성 검사

> 사용자가 입력한 데이터가 정확하고 유효한지 확인하는 과정이다.
>

Django Form은 사용자가 입력한 데이터를 자동으로 검사하고, 잘못된 값이 입력되면 오류 메시지를 제공할 수 있다.

- 필수 입력값이 비어 있는 경우
- 이메일 형식이 잘못된 경우
- 설정한 글자 수를 초과한 경우

유효성 검사를 통해 잘못된 데이터가 데이터베이스에 저장되는 것을 막을 수 있다.

Django Form에서는 `is_valid()` 메서드를 사용해 입력 데이터의 유효성을 검사한다.

```
form.is_valid()
```

- 입력 데이터가 유효하면 `True` 반환
- 입력 데이터가 유효하지 않으면 `False` 반환

이후 실제 게시글 생성 과정에서는 `is_valid()`의 결과가 `True`인 경우에만 데이터를 저장하도록 처리한다.

### 3. Django Form

> 사용자 입력 데이터를 수집하고 처리하며, 유효성 검사를 수행하기 위한 Django의 도구이다.
>

Django Form을 사용하면 다음 기능을 쉽게 구현할 수 있다.

- 사용자 입력 데이터 수집
- 입력 데이터 유효성 검사
- 오류 메시지 출력
- HTML Form 자동 생성

---

## 2. Form Class

Django Form을 사용하기 위해 `forms.py` 파일을 생성하고 Form 클래스를 작성한다.

### forms.py

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

`forms.Form`을 상속받아 Form 클래스를 생성한다.

- `title`
    - 문자열 입력 필드
    - 최대 길이 10
- `content`
    - 문자열 입력 필드

### View에서 Form 생성

`views.py`에서 `ArticleForm`을 import하여 Form 객체를 생성한다.

```python
from .forms import ArticleForm

def new(request):
    form = ArticleForm()

    context = {
        "form": form,
    }

    return render(request, "articles/new.html", context)
```

`ArticleForm()`을 생성한 후 `context`를 통해 템플릿으로 전달한다.

### Template에서 Form 출력

기존에는 HTML input을 직접 작성했다.

```python
<input type="text" name="title">
<textarea name="content"></textarea>
```

Django Form을 사용하면 다음과 같이 간단하게 작성할 수 있다.

```python
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}

    {{ form }}

    <input type="submit">
</form>
```

`{{ form }}`을 작성하면 Django가 Form 클래스에 정의된 필드를 기반으로 HTML 입력 요소를 자동 생성한다.

**적용 후에도 `{{ form }}` 을 통해 Django Form이 실제 HTML 입력 요소로 렌더링 된 것을 확인 할 수 있다.**

![](https://velog.velcdn.com/images/king-dong-gun/post/392aa51a-c107-471b-b34b-4c716d01206d/image.png)


---

## 3. Widget

> Django Form의 각 입력 필드가 HTML에서 어떤 형태로 출력될지 결정하는 구성 요소이다.
>

예를 들어 기본 `CharField`는 HTML에서 `<input>` 형태로 출력된다.

하지만 긴 내용을 입력받아야 하는 경우 `<textarea>` 형태가 더 적절할 수 있다.

### Widget 적용

```python
class ArticleForm(forms.Form):
    # 사용자로부터 입력받을 필드를 정의
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/91542315-41ee-4818-8c79-1d69792ed952/image.png)


`forms.Textarea`를 사용하면 `content` 입력 필드가 `<textarea>` 형태로 출력된다.

Widget을 사용하면 다음과 같은 HTML 입력 형태를 지정할 수 있다.

- TextInput
- Textarea
- Select
- CheckboxInput

즉, Widget은 **입력 필드의 화면 표현 방식을 결정한다.**

---

## 4. Django ModelForm

### Form과 ModelForm의 차이

Django Form과 ModelForm은 모두 사용자 입력 데이터를 처리하지만 목적이 다르다.

| 구분 | Form | ModelForm |
| --- | --- | --- |
| Model 연결 | 연결되지 않음 | 연결됨 |
| 주요 목적 | 사용자 입력 처리 및 검증 | 사용자 입력 처리 + DB 저장 |
| 사용 예시 | 검색, 로그인 | 게시글 작성, 회원가입 |
| DB 저장 | 직접 처리 필요 | `save()` 사용 가능 |

### ModelForm

> Model과 연결된 Form을 자동으로 생성해주는 Django 클래스이다.
>

ModelForm은 Form과 Model을 결합한 형태이다.

Model에 정의된 필드를 기반으로 Form 필드를 자동으로 생성하고, 사용자 입력 데이터를 데이터베이스에 저장할 수 있다.

---

## 5. ModelForm Class

기존 `forms.Form` 대신 `forms.ModelForm`을 상속받는다.

### forms.py

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = "__all__"
```

![](https://velog.velcdn.com/images/king-dong-gun/post/ff07966a-9bca-4009-930d-99f682a73cd4/image.png)


`Meta` 클래스를 사용해도 Model의 필드를 기반으로 동일하게 Form이 생성되는 것을 확인할 수 있다.

### Meta class

> ModelForm 내부에서 어떤 Model과 연결할지, 어떤 필드를 사용할지 설정하는 공간이다.
>

```python
class Meta:
    model = Article
    fields = "__all__"
```

- `model = Article`
    - Article 모델과 Form을 연결한다.
- `fields = "__all__"`
    - Article 모델의 모든 필드를 Form에 사용한다.

### 특정 필드만 사용

```python
class Meta:
    model = Article
    fields = ("title",)
```

### 특정 필드 제외

```python
class Meta:
    model = Article
    exclude = ("title",)
```

`fields` 또는 `exclude`를 사용하여 Form에 어떤 필드를 사용할지 결정할 수 있다.

---

## 6. ModelForm 적용

기존에는 사용자 입력값을 직접 꺼내서 Article 객체를 생성했다.

```python
title = request.POST.get("title")
content = request.POST.get("content")

article = Article(
    title=title,
    content=content,
)

article.save()
```

`ModelForm`을 사용하면 이 과정을 줄일 수 있다.

```python
form = ArticleForm(request.POST)
```

사용자가 입력한 `request.POST` 데이터를 `ArticleForm`에 전달한다.

---

## 7. is_valid()

> Form에 입력된 데이터의 유효성을 검사하고 결과를 True 또는 False로 반환하는 메서드이다.
>

```python
if form.is_valid():
```

입력 데이터가 정상이라면: `True` 를 반환한다.

잘못된 데이터가 있다면: `False` 를 반환한다.

### Create에서 유효성 검사

```python
def create(request):
    form = ArticleForm(request.POST)

    if form.is_valid():
        article = form.save()
        return redirect("articles:detail", article.pk)

    context = {
        "form": form,
    }

    return render(request, "articles/new.html", context)
```

동작 과정은 다음과 같다.

```
사용자 데이터 입력
        ↓
ArticleForm(request.POST)
        ↓
form.is_valid()
        ↓
정상 데이터 → True → DB 저장
잘못된 데이터 → False → 오류 메시지 출력
```

입력값이 잘못된 경우 Django Form 객체 내부에 오류 정보가 저장된다.

이 Form 객체를 다시 Template에 전달하면 사용자는 어떤 입력이 잘못되었는지 확인할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/4fb53f1f-de5e-4b3d-afcd-771d65a393df/image.png)


---

## 8. save()

> ModelForm의 데이터를 기반으로 Model 객체를 생성하거나 수정하고 데이터베이스에 저장하는 메서드이다.
>

```python
article = form.save()
```

Form에 입력된 데이터가 유효하다면 `save()` 메서드를 사용하여 데이터베이스에 바로 저장할 수 있다.

### 게시글 생성

```python
form = ArticleForm(request.POST)

if form.is_valid():
    article = form.save()
```

새로운 객체를 생성하는 경우 별도의 `instance`를 전달하지 않는다.

![](https://velog.velcdn.com/images/king-dong-gun/post/7e0fa7f3-5f9a-49be-ac87-bb82e0ac6cae/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/754ce3c5-e89f-41a4-828b-fd9558984799/image.png)


### 게시글 수정

```python
article = Article.objects.get(pk=article_pk)

form = ArticleForm(
    request.POST,
    instance=article,
)

if form.is_valid():
    form.save()
```

수정할 기존 객체를 `instance`에 전달하면 새로운 객체를 생성하지 않고 기존 객체를 수정한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/80b26373-7988-49a9-91e7-409056da3776/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/203f73c4-9a1b-4447-8eaf-9bd121470c03/image.png)


> `instance` 없음 → 새로운 데이터 생성
>
>
> `instance` 있음 → 기존 데이터 수정
>

---

## 9. ModelForm을 활용한 게시글 작성

기존 게시글 작성 기능은 두 개의 View 함수로 나누어져 있었다.

```python
new()
→ GET 요청
→ 게시글 작성 페이지 출력

create()
→ POST 요청
→ 게시글 저장
```

두 함수의 목적은 결국 **게시글 생성**이라는 동일한 목적을 가진다.

따라서 HTTP Request Method를 이용하여 하나의 View 함수로 합칠 수 있다.

---

## 10. new와 create 함수 결합

### 기존 구조

```python
GET /articles/new/
→ new()

POST /articles/create/
→ create()
```

### 변경된 구조

```python
GET /articles/create/
→ 작성 페이지 출력

POST /articles/create/
→ 게시글 생성
```

하나의 URL과 View 함수에서 요청 방식에 따라 다른 작업을 수행한다.

### views.py

```python
def create(request):

    if request.method == "POST":
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)

    else:
        form = ArticleForm()

    context = {
        "form": form,
    }

    return render(request, "articles/create.html", context)
```

### GET 요청

```python
else:
    form = ArticleForm()
```

GET 요청이 들어오면 빈 Form을 생성하여 작성 페이지를 보여준다.

### POST 요청

```python
if request.method == "POST":
    form = ArticleForm(request.POST)
```

POST 요청이 들어오면 사용자가 작성한 데이터를 Form에 담는다.

이후:

```python
if form.is_valid():
```

유효성 검사를 수행한다.

정상 데이터라면:

```python
article = form.save()
```

데이터베이스에 저장한다.

### URL 변경

기존의 `new/` URL은 더 이상 필요하지 않기 때문에 제거한다.

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:article_pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
]
```

---

## 11. edit과 update 함수 결합

게시글 수정 역시 기존에는 두 개의 View 함수로 나누어져 있었다.

```python
edit()
→ 수정 페이지 출력

update()
→ 수정된 데이터 저장
```

이 두 함수 역시 **게시글 수정**이라는 같은 목적을 가지고 있으므로 하나의 함수로 결합할 수 있다.

### views.py

```python
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == "POST":
        form = ArticleForm(
            request.POST,
            instance=article,
        )

        if form.is_valid():
            form.save()
            return redirect("articles:detail", article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        "article": article,
        "form": form,
    }

    return render(request, "articles/update.html", context)
```

### GET 요청

```python
form = ArticleForm(instance=article)
```

기존 게시글 데이터를 Form에 넣어 수정 페이지에 보여준다.

### POST 요청

```python
form = ArticleForm(
    request.POST,
    instance=article,
)
```

기존 게시글 객체와 사용자가 수정한 데이터를 함께 전달한다.

`instance=article`을 작성하지 않으면 새로운 게시글이 생성될 수 있다.

따라서 수정에서는 반드시 수정할 기존 객체를 전달해야 한다.

---

## 12. ModelForm의 Keyword Argument

ModelForm은 여러 개의 인자를 받을 수 있다.

```python
ArticleForm(request.POST, instance=article)
```

여기서 `request.POST`는 첫 번째 인자인 `data`에 전달된다.

`instance=article`은 수정할 기존 Model 객체를 전달한다.

`instance`는 여러 인자 중 뒤쪽에 위치하기 때문에 일반적으로 이름을 명시하여 전달한다.

```python
instance=article
```

---

## 13. Widgets 응용

Widget을 사용하면 입력 필드의 속성을 세부적으로 설정할 수 있다.

### forms.py

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                "class": "my-title",
                "placeholder": "Enter the title",
            }
        ),
    )

    class Meta:
        model = Article
        fields = "__all__"
```

`attrs`를 사용하면 HTML의 속성을 지정할 수 있다.

- `class`
- `placeholder`
- `rows`
- `cols`

등을 추가할 수 있다.

### Textarea 적용

```python
content = forms.CharField(
    label="내용",
    widget=forms.Textarea(
        attrs={
            "class": "my-content",
            "placeholder": "Enter the content",
            "rows": 5,
            "cols": 50,
        }
    ),
)
```

#### 적용 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/e3c9f847-0f37-4c4a-8c25-39d0d0d52820/image.png)


---

## 14. Form 필드 수동 렌더링

`{{ form }}`을 사용하면 전체 Form을 한 번에 출력할 수 있다.

하지만 각 필드를 직접 배치하고 싶은 경우 개별적으로 렌더링할 수도 있다.

```html
<form action="" method="POST">
    {% csrf_token %}

    <div>
        {{ form.title.errors }}

        <label for="{{ form.title.id_for_label }}">
            Title:
        </label>

        {{ form.title }}
    </div>

    <div>
        {{ form.content.errors }}

        <label for="{{ form.content.id_for_label }}">
            Content:
        </label>

        {{ form.content }}
    </div>

    <input type="submit">
</form>
```

각 필드를 직접 출력하면 HTML 구조와 디자인을 더 세밀하게 조절할 수 있다.

---