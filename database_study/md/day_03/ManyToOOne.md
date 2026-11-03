### 1. 모델 관계

#### 관계

> 데이터베이스 내 여러 테이블 간의 논리적인 연결 관계를 나타낸다.
>

#### 관계의 종류

1. `1:1 (One to One)관계`
    - 한 테이블의 레코드가 다른 테이블의 단 하나의 레코드와만 1:1로 매칭되는 관계이다.
2. `N:1 (Many to One)관계`
    - 여러 개의 레코드가 하나의 레코드에 소속되는 관계이다.
3. `N:M (Many to Many)관계`
    - 여러 레코드가 여러 레코드와 양방향으로 연결되는 관계이다.

![](https://velog.velcdn.com/images/king-dong-gun/post/35be6bd5-4d02-43a1-b3b9-94e9aac064f4/image.png)


#### 1:N 관계의 예시

1. `야구팀:야구선수`
    - 한팀의 여러 명의 선수가 소속된다.
    - 한 선수가 다른 야구 팀의 소속될 수 없다
2. `계좌:은행`
    - 하나의 계좌는 한 은행에만 소속되어 있다.
    - 한 은행은 여러 개의 계좌를 가질 수 있다.
3. `국가:도시`
    - 하나의 국가는 여러 도시를 가진다.
    - 한 도시가 중복된 국가에 포함되지 않는다.
4. `댓글:게시글`
    - 하나의 게시글에는 여러 개의 댓글이 달린다.
    - 댓글이 소속된 게시글이 없는 경우는 없다.

---

### 2. 댓글 모델 정의

#### ForeignKey (to, on_delete)

> 한 모델이 다른 모델을 참조하는 관계를 설정하는 클래스이다.
>
- `N:1` 관계 표현할 때 사용한다.
- 데이터베이스에서 외래 키로 구현된다.
- `to` 속성
    - 참조하는 모델 class 이름이다. (N:1에서 N이 아닌 1의 class 정보)
- `on_delete` 속성
    - 외래키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의하는 설정

#### 댓글 모델 정의하기

- `ForeignKey` 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 **단수형**으로 작성하는 것을 권장한다.

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/efdb3fab-5103-4e1c-822f-1cb13939423c/image.png)


댓글을 생성하고 저장하려고 하지만, 어떤 게시글에 속한 댓글인지 나타내는 `article` 값이 없기 때문에 무결성 조건을 만족하지 못해 저장에 실패한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/801a01a1-5d92-4be4-bc40-5d2d9e945135/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/83e4e32a-561a-416a-8d91-805cf5c4bd30/image.png)


`pk=1`인 게시글을 조회한 뒤, 해당 게시글을 `comment.article`에 할당하고 댓글을 저장하면 데이터베이스에 정상적으로 저장된다.

![](https://velog.velcdn.com/images/king-dong-gun/post/6a85b71f-b130-4ec5-8193-7d3a36d75379/image.png)


---

### 3. 관계 모델 참조

#### 참조

> `ForeignKey`를 가진 모델에서 자신이 참조하고 있는 모델의 정보에 접근하는 것이다.
>

`Comment`모델에는 `ForeignKey` 인 `article` 이 존재하기 때문에 댓글에서 자신이 속한 게시글의 정보에 접근이 가능하다.

```python
# 해당 댓글이 참조하는 게시글 객체 조회
comment.article

# 해당 댓글이 참조하는 게시글 content에 접근
comment.article.content

```

`Comment(N) → Article(1)` 관계이기 때문에 댓글에서 게시글의 정보를 조회할 수 있다.

#### QuerySet API

1. `.all()` : 모든 댓글 조회

```python
comments = Comment.objects.all()
```

1. `.filter()` : 특정 게시글에 속한 댓글 조회

```python
# pk가 1인 게시글 조회
article = Article.objects.get(pk=1)
# 해당 게시글을 참조하는 댓글 조회
comment = Comment.objects.filter(article=article)
```

---

### 4. 관계 모델 역참조

#### 역참조

> 참조 필드가 없는 쪽에서, 자신을 참조하고 있는 데이터를 거꾸로 조회하는 것이다.
>

`Article` 모델에는 `Comment`를 직접 참조하는 필드가 없기 때문에 Django가 자동으로 만들어주는 `related manager`를 통해 댓글 정보에 접근할 수 있다.

```
# 특정 게시글에 작성된 모든 댓글 조회
article.comment_set.all()
```

`Article(1)` → `Comment(N)` 방향으로 조회하는 것이기 때문에 게시글에서 자신을 참조하는 댓글 정보를 조회할 수 있다.

#### related manager

`ForeignKey`를 정의하면 Django가 역참조를 위해 자동으로 이름을 생성한다.

- 기본 형식
    - `참조하는 모델명 소문자 + _set`
- `Comment` 모델이 `Article`을 참조하고 있으므로 `comment_set`이 생성된다.

```
article.comment_set
```

#### QuerySet API

1. `.all()` : 특정 게시글의 모든 댓글 조회

```
# pk가 1인 게시글 조회
article = Article.objects.get(pk=1)

# 해당 게시글에 작성된 모든 댓글 조회
comments = article.comment_set.all()
```

- `article` : 특정 게시글 객체
- `comment_set` : `Article`에서 `Comment`를 역참조하기 위한 related manager
- `.all()` : 해당 게시글에 연결된 모든 댓글 조회

---

### 5. 댓글 구현

1. 사용자로부터 댓글 데이터 입력을 받기

`CommentForm`을 생성하여 사용자가 댓글 내용을 입력할 수 있도록 한다.

```python
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
```

1. 댓글 CREATE 구현

게시글 상세 페이지에서 댓글 입력 Form을 사용할 수 있도록 `CommentForm` 객체를 생성한다.

```python
from .forms import CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()

    context = {
        'article': article,
        'comment_form': comment_form,

    }
    return render(request, 'articles/detail.html', context)
```

1. 화면 구현

```html
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
</form>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/a1b5828c-bb2a-4878-8050-f3b071a62c62/image.png)


1. URL 연결

URL의 `pk`를 통해 어떤 게시글에 댓글을 작성하는지 전달한다.

```python
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    # 댓글 URL
    path("<int:pk>/comments/", views.comments_create, name="comments_create")
]
```

1. views 함수 생성
    - `CommentForm`에서는 사용자가 `content`만 입력했기 때문에 아직 댓글에 `article` 정보가 없다.
    - 따라서 바로 저장하지 않고 `commit=False`를 사용하여 댓글 객체만 생성한다.
    - 이후 현재 게시글을 댓글의 `article` 필드에 연결한다.
    - 마지막으로 게시글 정보까지 연결된 댓글을 데이터베이스에 저장한다.

```python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        # 댓글 객체 생성, DB 저장은 잠시 중단
        comment = comment_form.save(commit=False)

        # 댓글과 게시글 연결
        comment.article = article

        # DB에 최종 저장
        comment.save()

        return redirect("articles:detail", article.pk)

    context = {
        "article": article,
        "comment_form": comment_form,
    }

    return render(request, "articles/detail.html", context)
```

![](https://velog.velcdn.com/images/king-dong-gun/post/54a92c27-6992-43cb-8f1e-9708618e07b9/image.png)
