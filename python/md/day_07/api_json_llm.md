## 1. API

#### API란?

> API(Application Programming Interface)는 서로 다른 프로그램이 정해진 규칙에 따라 통신할 수 있도록 제공하는 인터페이스이다.
>

#### 비유 방식

- 손님: `클라이언트 (client)`
- 메뉴판: `API 문서`
- 주문: `요청 (request)`
- 주방: `서버 (server)`
- 음식: `응답 (response)`

![](https://velog.velcdn.com/images/king-dong-gun/post/38f70f0b-df6f-4115-8061-119517c10e2e/image.png)


#### `Request` & `Response`

- 클라이언트: 서버에 `요청(request)을 전송`한다.
- 서버: 요청을 처리한 뒤에 `응답(response)을 반환`한다.
- URL: 요청할 자원의 위치를 나타내는 주소다.

#### HTTP 메서드

- `GET`: 데이터를 조회한다.
- `POST` : 데이터를 전송하거나 생성을 요청한다.
- `PUT` : 기존 데이터 전체를 수정한다. (교체)
- `PATCH` : 기존 데이터 일부를 수정한다.
- `DELETE` : 데이터를 삭제한다.
- `OPTIONS` : 사용할 수 있는 메서드를 확인한다.

#### 상태 코드

- 서버가 요청을 처리한 결과를 숫자로 나타낸 값이다.
1. `200` : 요청 성공 → 요청 성공
2. `404` : 요청한 자원을 찾을 수 없다. → URL 경로가 잘못되었거나, 요청한 데이터가 존재하지 않는 경우
3. `500` : 서버 내부 오류 → 서버 코드 실행 중 예외 발생 등으로 정상 처리하지 못한 경우

#### Response 객체

- `requests.get()` : 서버의 응답을 Response 객체로 반환한다.
    - status_code : HTTP 상태 코드
    - text : 응답 데이터를 문자열 형태로 반환
    - json() : JSON 응답을 Python 객체로 변환
    - headers : 응답 헤더 정보
    - elapsed : 요청 처리 시간
    - url : 요청 URL

#### Request 테스트 해보기

1. **JSONPlaceholder :** 회원가입이나 API 키 없이 사용할 수 있는 공개 연습용 API를 가지고 테스트를 해보자
2. 요청 URL:  `URL = "https://jsonplaceholder.typicode.com/users"`

```python
import requests
from pprint import pprint

URL = "https://jsonplaceholder.typicode.com/users"
SAMPLE = [
    {"name": "Leanne Graham", "email": "Sincere@april.biz",
     "address": {"city": "Gwenborough"}},
    {"name": "Ervin Howell", "email": "Shanna@melissa.tv",
     "address": {"city": "Wisokyburgh"}},
]

try:
    response = requests.get(URL, timeout=5)
    print("상태 코드:", response.status_code)   # 200, 요청 성공
    data = response.json()                       # 응답을 파이썬 객체로 변환
except Exception as e:
    print("네트워크를 사용할 수 없어 샘플 데이터로 진행:", e)
    data = SAMPLE

print("사용자 수:", len(data))
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/5c0e1bb6-73c5-47f0-a214-773628345628/image.png)


---

## 2. JSON

#### JSON이란?

> 프로그램 간에 데이터를 주고받거나 저장할 때 사용하는 텍스트 기반 데이터 형식이다.
사람이 읽기 쉬우며 다양한 프로그래밍 언어에서 지원한다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/f1761c06-8bab-4450-8748-94710e949866/image.png)


#### JSON의 구조

```json
{
  "id": 1,
  "name": "김동건",
  "age": 25,
  "isStudent": true,
  "skills": [
    "Python",
    "JavaScript"
  ],
  "address": {
    "city": "Seoul",
    "country": "Korea"
  }
}
```

- 배열(Array): 여러 데이터를 순서대로 저장한다.
- 객체(Object): 데이터를 key-value 형태로 저장한다.
- 중첩 객체: 객체 내부에 객체가 포함된 구조이다.
- response.json()으로 변환하면 배열은 **리스트**, 객체는 **딕셔너리**가 된다.

#### JSON 데이터 접근하기

1. 키로 한 칸씩 들어가기
- 리스트: **인덱스를 이용**해서 값에 접근한다.
- 딕셔너리: **키를 이용**해서 값에 접근한다.
- 중첩된 데이터: 바깥쪽 구조부터 안쪽 구조까지 순서대로 접근한다.

```python
first_user = data[0]

print(first_user["name"])                # 이름
print(first_user["email"])               # 이메일
print(first_user["address"]["city"])     # 주소에 저장된 도시
```

- data[0]: **리스트에서 첫번째 사용자**에게 접근한다.
- first_user[”name”]: **딕셔너리에서 name 키**의 값에 접근한다.
- first_user[”address”][”city”]: **address키에 접근 후 city키에 접근**한다.
- **딕셔너리는 .name이 아니라 [”name”]형식으로 값에 접근**한다.

#### get() 메서드

- `dict["키"]` : 키가 없으면 `KeyError` 가 발생한다.
- `dict.get("키")` : 키가 없으면 `None`을 반환한다.
- `dict.get("키", "기본값")` : 키가 없으면 지정한 기본값을 반환한다.

```python
first = data[0]                 # 첫 번째 사용자
print(first["name"])            # 이름
print(first["email"])           # 이메일

# 첫 번째 사용자의 도시를 꺼내 보세요 (address의 city)
도시 = None                       # first["address"]["city"]
print(도시)
```

### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/c573dee6-e2fd-4594-bf79-f1ee702b6615/image.png)


---

## 3. LLM

#### 챗봇은 어디서 답을 만들까?

- ChatGPT, Claude 등 LLM은 외부 AI 서버에서 실행한다.
- API를 통해 AI 서버에 요청을 보내고 응답을 받는다.

![](https://velog.velcdn.com/images/king-dong-gun/post/3055da3a-d7d7-4fa7-acee-7c56b0e7162d/image.png)

#### 컨텍스트, RAG, 에이전트 (Agent)란?

1. 컨텍스트: LLM에게 답변 생성에 필요한 추가 정보를 함께 제공하는 것이다.
2. RAG: 외부 문서를 검색(Retrieval)하고 검색된 정보를 LLM 입력(Context)으로 활용하여 답변 품질을 높이는 방식이다.
3. 에이전트(Agent): 필요한 도구를 사용해서 작업을 수행한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/ef459af8-73b4-41ca-a388-914c79925c02/image.png)



#### API 키

- API키는 API 사용자를 식별하고 인증하는 비밀 정보이다.
- 환경 변수인 `os.environ` 이나 별도 비밀 파일로 관리한다.

#### 관리 예시

```python
import os
from dotenv import load_dotenv

# .env 파일 읽기
load_dotenv() # 현재 파일과 같은 경로에 있을경우
# load_dotenv(../.env) # 상위 폴더에 있을경우 (상대, 절대경로 사용 가능)

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("OPENAI_API_KEY가 .env 파일에 없습니다.")
else:
    print("OPENAI_API_KEY 읽기 성공")
    # API 키 전체를 출력하지 않고 일부만 확인하는 이유는 키 노출을 방지하기 위해서이다.
    print(API_KEY[:10] + "...")
```

> 💡API키가 노출되면 무단 사용으로 요금 폭탄 맞을 수 있다. 공개 저장소에 API 키를 업로드 하지말자!


#### LLM API Request

```python
headers = {
		# API 인증을 위한 키 전달
    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
    "Content-Type": "application/json",
}
prompt = "대전의 유명한 관광지를 소개해줘."
API_URL = "https://api.openai.com/v1/chat/completions"

body = {
    "model": "gpt-4.1-mini",
    "messages": [
        {
            "role": "user",
            "content": prompt,
        }
    ],
    "temperature": 0.7,
    "max_tokens": 500,
}
response = requests.post(
    API_URL,
    headers=headers,
    json=body,
    timeout=30,
)
print(response.status_code)
print(response.json())

answer = response.json()["choices"][0]["message"]["content"]
print(answer)
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/02a4ab1e-0312-4b31-9d15-26b3d871150f/image.png)


#### 흐름

```
### Request 흐름

1. Header
   - API 인증 정보 전달
   - JSON 요청임을 명시

2. Body
   - 사용할 모델 지정
   - 사용자 입력(prompt) 전달
   - 생성 옵션 설정

3. Response
   - 서버에서 생성된 AI 응답 반환
   - JSON 구조에서 content 값 추출
```

---

## 4. 정리

이번 학습을 통해 API를 이용한 데이터 통신 구조와 JSON 데이터 처리 방식을 이해했다.

- API는 클라이언트와 서버가 데이터를 주고받기 위한 통신 규칙이다.
- HTTP 요청은 Method, Header, Body를 통해 서버에 전달된다.
- 서버 응답은 JSON 형태로 반환되는 경우가 많으며, Python에서는 json() 메서드를 통해 딕셔너리와 리스트 형태로 변환할 수 있다.
- LLM 서비스 역시 API를 통해 요청과 응답을 주고받으며, API Key를 이용해 사용자를 인증한다.

앞으로는 단순히 API를 사용하는 것을 넘어, REST API 설계와 데이터 처리 방식까지 학습할 예정이다.