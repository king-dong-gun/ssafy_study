### 1. 모듈

> **한 파일로 묶인 변수와 함수의 모음**
> 

#### 예시

```python
# 파이썬이 미리 작성해 둔 수학 관련 변수, 함수가 작성된 모
import math 

print(math.pi) # 3.14..........
print(math.sqrt(4)) # 2.0
```

1. `import` 문 사용
    - 같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수있다.
        - `dot` : 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라!
        
        ```python
        import math
        
        print(math.pi) # 모듈명, 변수명
        print(math.sqrt(4)) # 모듈명, 함수명
        ```
        
        - `from` : 필요한 것만 집어서 가져오는 방식!
        
        ```python
        from math import pi, sqrt
        
        print(pi)         # 변수명
        print(sqrt(4))    # 함수명
        ```
        

![alt text](../../images/python_import.png)

- `import` 시 이름 충돌 다루기
    - 같은 이름을 두 번 가져오면 나중에 `import` 한 것이 덮어쓴ㄷ다.
    
    ```python
    from math import sqrt          # math.sqrt
    from my_math import sqrt       # my_math.sqrt로 덮어씀
    
    result = sqrt(9)               # my_math.sqrt 호출
    ```
    

→ `as` 키워드를 사용하여 별칭 `(alias)` 를 부여한다.
→ `as`를 사용하면 이름 충돌을 방지하거나 긴 이름을 짧게 사용할 수 있다.

```python
from math import sqrt
from my_math import sqrt as my_sqrt    # 별칭 부여

sqrt(4)     # math
my_sqrt(4)  # my_amth
```

---

### 2. 패키지

> 연관된 **모듈들을 하나의 디렉토리에 모아놓은 것이다.**
> 

#### 예시

#### my_pacakage에 math.my_math 모듈생성

![alt text](../../images/python_패키지1.png)

#### my_pacakage에 static.tools 모듈생성

![alt text](../../images/python_패키지2.png)

#### 상위 pacakage에 my_math 모듈 생성

![alt text](../../images/python_패키지3.png)

#### simple.py 실행 파일 생성

![alt text](../../images/python_패키지4.png)

#### 출력 결과

![alt text](<../../images/python_패키지 실행.png>)

> 첫번째 상위 패키지의 x + y로 3 출력
두번째 my_pacakage에 x - y로 1 출력
세번째 my_pacakage에 x % y로 1 출력
> 

---

### 3. 라이브러리

> 프로그램 개발에 자주 사용되는 유용한 코드나 함수들을 모아둔 저장소
> 

![alt text](../../images/python_라이브러리.png)
---
## 핵심 정리

| 구분 | 의미 | 예시 |
|:---|:---|:---|
| **모듈(Module)** | 변수, 함수, 클래스 등을 모아놓은 하나의 `.py` 파일 | `my_math.py`, `math` |
| **패키지(Package)** | 서로 관련된 여러 모듈을 모아놓은 디렉터리 | `my_package/` |
| **라이브러리(Library)** | 프로그램 개발에 활용할 수 있도록 만들어진 모듈과 패키지의 모음 | `NumPy`, `Pandas` |
| **`import`** | 모듈이나 패키지를 불러오는 문법 | `import math` |
| **`from ... import ...`** | 모듈에서 필요한 이름만 선택해서 가져오는 문법 | `from math import sqrt` |
| **`as`** | 모듈이나 함수에 별칭을 지정하는 문법 | `import math as m` |

> **모듈은 파일, 패키지는 모듈을 담은 폴더, 라이브러리는 개발에 활용하는 코드 모음이다.**