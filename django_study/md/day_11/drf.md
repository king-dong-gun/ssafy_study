### 1. API

> **Application Programming Interface**의 약자로, **두 소프트웨어가 서로 통신할 수 있도록 하는 인터페이스**이다.
>

클라이언트와 서버처럼 서로 다른 프로그램이 데이터를 주고받을 수 있도록 공통된 규칙과 형식을 제공한다.

API를 활용하면 다른 프로그램의 기능이나 데이터를 직접 구현하지 않고 사용할 수 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/49bfa588-b212-415a-a5d2-38130f4b59a2/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/c2fc8762-a9a7-4355-8b64-7d168fa066f1/image.png)
![](https://velog.velcdn.com/images/king-dong-gun/post/8a1027e8-ab6d-4e25-a94c-d11958dd1977/image.png)


#### API 활용

- 클라이언트가 서버에 필요한 데이터를 요청한다.
- 서버는 요청을 처리한 뒤 결과를 응답한다.
- 클라이언트는 전달받은 데이터를 활용한다.

#### Open API

> 외부 개발자가 사용할 수 있도록 공개된 API이다.
>

대표적인 API는 다음과 같다.

- YouTube API
- Google Map API
- Naver Papago API
- Kakao Map API

#### Third Party API

> 직접 개발하지 않은 외부 서비스에서 제공하는 API이다.
>

다른 서비스의 기능이나 데이터를 자신의 프로그램에 연동할 때 사용한다.

### 2. REST API

> **REST(Representational State Transfer)**는 **API 서버를 설계하기 위한 소프트웨어 아키텍처 스타일**이다.
>

REST는 API를 일관된 방식으로 설계하고, 서로 다른 시스템이 효율적으로 통신할 수 있도록 하는 설계 원칙이다.

REST 원칙을 따르는 API를 **RESTful API**라고 한다.

#### REST API의 구성 요소

REST API에서는 자원을 식별하고, 자원에 수행할 동작을 지정하며, 처리 결과를 표현한다.

| 구성 요소 | 역할 | 사용 기술 |
| --- | --- | --- |
| 자원의 식별 | 어떤 데이터에 접근할 것인가 | URI |
| 자원의 행위 | 어떤 작업을 수행할 것인가 | HTTP Methods |
| 자원의 표현 | 데이터를 어떤 형식으로 전달할 것인가 | JSON 등 |

REST API에서는 URI를 통해 자원을 식별하고, HTTP Method로 수행할 동작을 구분한다.

### 3. URI

> **Uniform Resource Identifier**의 약자로, 인터넷에서 특정 자원을 식별하기 위한 문자열이다.
>

REST API에서는 URI를 통해 요청 대상인 자원을 구분한다.

#### URL

> **Uniform Resource Locator**의 약자로, 네트워크에서 자원의 위치를 나타내는 주소이다.
>

***URL은 URI의 한 종류이다.***

![](https://velog.velcdn.com/images/king-dong-gun/post/3d766416-0cd8-4d42-b0ee-051d233cc237/image.png)


#### URL의 구성 요소

| 구성 요소 | 설명 |
| --- | --- |
| Scheme | 자원에 접근할 때 사용하는 프로토콜 |
| Domain Name | 요청할 서버의 도메인 이름 |
| Port | 서버의 특정 서비스에 접근하기 위한 번호 |
| Path | 서버에서 자원에 접근하는 경로 |
| Query Parameters | 서버에 전달하는 추가 데이터 |
| Anchor | 문서 내부의 특정 위치를 가리키는 식별자 |

#### Scheme

- 클라이언트가 자원에 접근할 때 사용할 프로토콜을 지정한다.
- 일반적으로 웹에서는 `HTTP` 또는 `HTTPS`를 사용한다.

#### Domain Name

- 요청 대상인 서버를 나타낸다.
- IP 주소 대신 사람이 기억하기 쉬운 도메인 이름을 사용한다.

#### Port

- 서버의 특정 서비스에 접근하기 위한 번호이다.
- HTTP의 기본 포트는 `80`, HTTPS의 기본 포트는 `443`이다.
- 기본 포트를 사용하는 경우 생략할 수 있다.

#### Path

- 서버에서 특정 자원에 접근하기 위한 경로이다.
- 실제 파일 경로가 아닌 논리적인 경로로 구성할 수 있다.
- REST API에서는 자원을 중심으로 경로를 설계한다.

#### Query Parameters

- 서버에 추가적인 데이터를 전달할 때 사용한다.
- `?`로 시작하며 여러 값은 `&`로 구분한다.
- Key와 Value의 쌍으로 구성된다.

#### Anchor

- URL에서 `#` 뒤에 작성되는 부분이다.
- 문서 내부의 특정 위치를 가리킨다.
- Fragment에 해당하는 부분은 일반적으로 서버에 전송되지 않는다.

### 4. HTTP Request Methods

> HTTP 요청에서 자원에 대해 수행하고자 하는 동작을 지정하는 방법이다.
>

REST API에서는 동일한 URI를 사용하더라도 HTTP Method에 따라 서로 다른 작업을 수행할 수 있다.

#### HTTP Methods 종류

| Method | 역할 | 서버 상태 변경 |
| --- | --- | --- |
| GET | 데이터 조회(검색) | X |
| POST | 데이터 제출 및 생성 | O |
| PUT | 데이터 전체 수정(교체) | O |
| PATCH | 데이터 일부 수정 | O |
| DELETE | 데이터 삭제 | O |

#### HTTP Response Status Code

> 서버가 클라이언트의 요청을 처리한 결과를 나타내는 3자리 숫자 코드이다.
>

| 상태 코드 | 의미 |
| --- | --- |
| 1XX | 요청 처리 중인 상태 |
| 2XX | 요청이 성공적으로 처리됨 |
| 3XX | 다른 위치로 이동하거나 추가 동작이 필요함 |
| 4XX | 클라이언트 요청에 문제가 있음 |
| 5XX | 서버 내부에 문제가 있음 |

REST API에서는 요청 결과에 맞는 상태 코드를 응답해야 한다.

### 5. JSON

> **JavaScript Object Notation**의 약자로, **데이터를 주고받기 위한 경량의 텍스트 기반 데이터 형식**이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/23b7baff-15bf-4739-8703-7e01f20a477b/image.png)


기존 Django에서는 사용자에게 HTML 페이지를 응답하는 방식으로 웹 서비스를 구현했다.

![](https://velog.velcdn.com/images/king-dong-gun/post/f783ef96-44e3-4f2c-ab44-511f1a03ab1a/image.png)


**REST API에서는 HTML뿐만 아니라 JSON과 같은 데이터 형식으로 응답할 수 있다.**

#### JSON의 특징

1. 텍스트 기반의 데이터 형식이다.
2. `Key`와 `Value`구조로 데이터를 표현할 수 있다.
3. 서로 다른 프로그래밍 언어에서도 사용할 수 있다.
4. 클라이언트와 서버 사이에서 데이터를 주고받는 데 적합하다.

#### 기존 Django와 REST API 비교

| 구분 | 기존 Django | REST API |
| --- | --- | --- |
| 응답 형식 | 주로 HTML | 주로 JSON |
| 화면 구성 | Django Template | Front-end |
| 서버의 역할 | 데이터 처리 및 화면 렌더링 | 데이터 처리 및 제공 |
| 데이터 활용 | 웹 페이지 중심 | 다양한 클라이언트에서 활용 가능 |

![](https://velog.velcdn.com/images/king-dong-gun/post/c44fdb7f-466a-4da2-9b03-2e0fc64b0224/image.png)


REST API에서는 서버가 데이터를 제공하고, 실제 화면 구성은 Vue와 같은 프론트엔드 프레임워크에서 담당할 수 있다.

### 6. Django REST Framework

> Django에서 RESTful API 서버를 쉽게 구축할 수 있도록 지원하는 오픈소스 라이브러리이다.
>

Django REST Framework는 일반적으로 DRF라고 부른다.

DRF는 API 개발에 필요한 기능을 제공하여 반복적인 작업을 줄이고, 데이터 처리 과정을 간단하게 구현할 수 있도록 돕는다.

#### DRF의 주요 기능

- 데이터 직렬화
- 요청 데이터 처리
- 유효성 검사
- HTTP 응답 생성
- 상태 코드 관리

DRF를 사용하려면 `djangorestframework` 패키지를 설치하고 `INSTALLED_APPS`에 `rest_framework`를 등록해야 한다.

### 7. Serialization

> 여러 시스템에서 활용할 수 있도록 데이터 구조나 객체의 상태를 재구성 가능한 형식으로 변환하는 과정이다.
>

Django 모델 객체를 API 응답으로 전달하려면 데이터를 JSON으로 표현할 수 있는 형태로 변환해야 한다.

이러한 변환 과정을 ***Serialization(직렬화)***이라고 한다.

#### Serializer

> **Serialization**을 수행하는 도구 또는 클래스이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/f775edcc-9b5a-4d42-aac8-c7741b6c0b29/image.png)


**Serializer**는 Django 모델 데이터를 API에서 사용할 수 있는 형태로 변환한다.

또한 클라이언트에서 전달받은 데이터의 유효성을 검사하는 역할도 한다.

#### Serialization과 Serializer의 차이

| 구분 | Serialization | Serializer |
| --- | --- | --- |
| 의미 | 데이터를 변환하는 과정 | 변환 작업을 수행하는 도구 |
| 역할 | 데이터를 전송 가능한 형태로 변환 | 직렬화 및 유효성 검사 |
| 구분 | 동작 | 클래스 |

#### ModelSerializer

> Django 모델과 연결하여 **Serializer**를 자동으로 구성할 수 있도록 지원하는 클래스이다.
>

모델 정보를 기반으로 필드를 생성하고, 유효성 검사와 데이터 저장에 필요한 기능을 제공한다.

Django의 **ModelForm과 유사하지만, ModelSerializer는 API 데이터 처리를 목적으로 사용**한다.

#### Serializer의 주요 설정

- `model`: 연결할 Django 모델을 지정한다.
- `fields`: 직렬화에 사용할 필드를 지정한다.
- `__all__`: 모델의 모든 필드를 사용한다.

```python
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

**Serializer**에서 지정한 필드에 따라 API 응답에 포함되는 데이터가 결정된다.

### 8. CRUD with ModelSerializer

> CRUD는 데이터를 `생성(Create)`, `조회(Read)`, `수정(Update)`, `삭제(Delete)`하는 기본적인 데이터 처리 작업이다.
>

***DRF에서는 ModelSerializer와 HTTP Method를 사용하여 CRUD 기능을 구현할 수 있다.***

#### CRUD와 HTTP Method

| CRUD | HTTP Method | 기능 |
| --- | --- | --- |
| Create | POST | 데이터 생성 |
| Read | GET | 데이터 조회 |
| Update | PUT | 데이터 전체 수정 |
| Update | PATCH | 데이터 일부 수정 |
| Delete | DELETE | 데이터 삭제 |

#### API URL 설계

게시글 API는 전체 게시글을 대상으로 하는 URL과 특정 게시글을 대상으로 하는 URL로 구분한다.

| URL | Method | 기능 |
| --- | --- | --- |
| `articles/` | GET | 전체 게시글 조회 |
| `articles/` | POST | 게시글 생성 |
| `articles/1/` | GET | 1번 게시글 조회 |
| `articles/1/` | PUT | 1번 게시글 수정 |
| `articles/1/` | DELETE | 1번 게시글 삭제 |

URI에는 수행할 동작보다 자원을 중심으로 경로를 작성하고, 실제 동작은 HTTP Method로 구분한다.

### 9. CRUD with ModelSerializer

> Django REST Framework의 `ModelSerializer`를 활용하여 데이터의 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 기능을 구현한다.
>

REST API에서는 URI로 자원을 식별하고, HTTP Method를 통해 해당 자원에 수행할 작업을 구분한다.

#### CRUD와 HTTP Method

| HTTP Method | 역할 | URL |
| --- | --- | --- |
| GET | 전체 게시글 조회 | `articles/` |
| GET | 단일 할 일 조회 | `todo/1/` |
| POST | 할 일 생성 | `todo/` |
| DELETE | 할 일 삭제 | `todo/1/` |
| PUT | 할 일 전체 수정 | `todo/1/` |
| PATCH | 할 일 일부 수정 | `todo/1/` |

#### ModelSerializer 구성

할 일목록 조회와 상세 조회는 필요한 데이터가 다를 수 있으므로 Serializer를 구분하여 작성한다.

- `TodoSerializer`: 할 일 목록 조회에 필요한 필드만 반환한다.
- `ModelSerializer`: 할 일 상세 조회 및 생성, 수정에 필요한 필드를 처리한다.

구현

```python
# todo/serializers.py

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
```

### 10. CRUD 구현

> HTTP Method에 따라 요청을 구분하고, Serializer를 활용하여 데이터베이스의 데이터를 처리한다.
>

#### Fixtures 데이터 불러오기

> Fixture는 데이터베이스에 초기 데이터를 입력하기 위해 사용하는 파일이다.
>

Django에서는 `loaddata` 명령어를 사용하여 JSON 형식의 Fixture 데이터를 데이터베이스에 불러올 수 있다.

```
python manage.py loaddata todo.json
```

- `loaddata`: Fixture 파일의 데이터를 데이터베이스에 불러온다.
- `articles.json`: 불러올 Fixture 파일이다.

#### 전체 할 일 조회 및 생성

할 일 목록에 접근하는 `todo/` URL에서는 GET과 POST 요청을 처리한다.

- `GET`: 전체 할 일 을조회하고 JSON 데이터로 반환한다.
- `POST`: 요청받은 데이터를 검증한 뒤 새로운 할 일을 생성한다.

구현

```python
# todos/views.py

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

#### 조회 및 생성 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/5fef1649-b7ca-476b-9fc7-78630a8749b5/image.png)


![](https://velog.velcdn.com/images/king-dong-gun/post/74c5a2ec-087a-4f08-8d1e-d1342b7f2a41/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/fd60c06a-b583-4d50-a08b-34288783f3d6/image.png)


#### 단일 할 일 조회, 삭제 및 수정

특정 할 일에 접근하는 `todo/<int:todo>/` URL에서는 GET, DELETE, PUT, PATCH 요청을 처리한다.

- `GET`: 특정 할 일의 상세 데이터를 조회한다.
- `DELETE`: 해당 할 일을 삭제한다.
- `PUT`: 할 일의 전체 데이터를 수정한다.
- `PATCH`: 할 일의 일부 필드만 수정한다.

구현

```python
# todos/views.py

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def todo_detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if request.method == 'GET':
        serializer = TodoListSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'

        serializer = TodoListSerializer(
            todo,
            data=request.data,
            partial=partial
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
```

#### URL 연결

작성한 View 함수를 URL과 연결하여 클라이언트의 요청을 처리하도록 설정한다.

구현

```python
# articles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list),
		path('todos/<int:todo_pk>/', views.todo_detail),
]
```

#### 조회, 수정, 삭제 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/61345a5f-3bc8-4d82-b7f3-7c151f89539d/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/aa4112f2-009c-4ca9-9dd8-04c215ec63b1/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/f599d099-b6f6-4e96-8717-faaeb7a24300/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/0f1a50cb-5047-458f-8f88-c88fced6f3ca/image.png)


### 12. API 응답 상태 코드

> 서버가 요청을 처리한 결과에 따라 적절한 HTTP 상태 코드를 반환한다.
>

CRUD 구현에서 사용하는 주요 상태 코드는 다음과 같다.

| 상태 코드 | 의미 | 사용 상황 |
| --- | --- | --- |
| 200 OK | 요청 성공 | 조회 및 수정 성공 |
| 201 Created | 자원 생성 성공 | 게시글 생성 |
| 204 No Content | 요청 성공, 응답 본문 없음 | 게시글 삭제 |
| 400 Bad Request | 잘못된 요청 | 입력 데이터 검증 실패 |
| 404 Not Found | 요청한 자원 없음 | 존재하지 않는 게시글 조회 |
| 405 Method Not Allowed | 허용되지 않은 HTTP Method | 지원하지 않는 요청 방식 |

#### PUT과 PATCH의 차이

PUT과 PATCH는 모두 데이터를 수정하지만 수정 범위에 차이가 있다.

| 구분 | PUT | PATCH |
| --- | --- | --- |
| 수정 범위 | 전체 리소스 | 일부 필드 |
| 요청 데이터 | 기본적으로 모든 필수 필드 필요 | 변경할 필드만 전달 가능 |
| 목적 | 전체 수정 | 부분 수정 |

DRF에서는 `partial=True`를 지정하여 일부 필드만 전달받는 수정 작업을 구현할 수 있다.