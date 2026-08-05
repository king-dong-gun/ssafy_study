## 1. Matplotlib & 전처리

### 1) 전처리

> **전처리(Data Preprocessing)**는 데이터를 **분석이나 머신러닝 모델이 사용할 수 있는 형태로 정리하고 변환하는 과정이다.**
>
- 데이터 분석 과정에서는 모델링보다 전처리에 많은 시간이 소요된다. (약 80%정도)
- 모델링은 전처리를 마친 데이터를 바탕으로 진행한다.

### 2) 전처리의 중요성

1. 데이터가 정확할수록 분석과 집계 과정의 오류가 줄어든다.
2. 잘못된 데이터를 입력하면 결과도 잘못될 수 있다.
3. 데이터 전처리 란 결측치 보정, 이상치 처리, 정규화, 인코딩을 수행하는 작업이다.

![](https://velog.velcdn.com/images/king-dong-gun/post/322f5170-3432-419e-9496-bc558c2287ea/image.png)


#### 전처리 전 (Raw Data)

수집한 데이터는 대부분 문제가 있는 상태이다.

| 고객명 | 나이 | 성별 | 구매금액 | 지역 |
| --- | --- | --- | --- | --- |
| 김철수 | 20 | 남 | "50000" | 서울 |
| 이영희 |  | 여 | "70000" | 서울시 |
| 박민수 | 999 | M | 30000 | Seoul |
| 김철수 | 20 | 남 | "50000" | 서울 |

#### 문제점

- **결측치(Missing Value)**
  → 이영희의 나이 데이터 없음
- **이상치(Outlier)**
  → 박민수의 나이 999
- **데이터 타입 오류**
  → 구매금액 `"50000"`은 문자형 데이터
- **데이터 표현 불일치**
  → 서울 / 서울시 / Seoul은 같은 의미지만 다른 값으로 저장됨
- **중복 데이터**
  → 김철수 데이터가 두 번 존재

#### 전처리 과정

| 문제 | 처리 방법 |
| --- | --- |
| 나이 없음 | 평균값으로 대체 |
| 나이 999 | 제거 |
| 문자형 구매금액 | 숫자형으로 변환 |
| 지역명 불일치 | 하나의 형태로 통일 |
| 중복 데이터 | 삭제 |

#### 전처리 후

| 고객명 | 나이 | 성별 | 구매금액 | 지역 |
| --- | --- | --- | --- | --- |
| 김철수 | 20 | 남 | 50000 | 서울 |
| 이영희 | 25 | 여 | 70000 | 서울 |
| ~~박민수~~ | ~~삭제~~ | ~~남~~ | ~~30000~~ | ~~서울~~ |

#### 전처리 4대 작업

1. 결측치: 비어있는 값을 채우거나 해당 데이터를 제거한다.
    - `df.isnull().sum()` : 컬럼별 결측치 개수 확인한다.
    - `fillna(값)` : 결측치를 지정한 값으로 대체한다.
    - `mode()` : 가장 자주 나타나는 값인 최빈값을 반환한다.
2. 이상치: 다른 값보다 지나치게 크거나 작은 값을 확인하고 처리한다.
    - `df.describe()` : 최솟값과 최댓값 등으로 이상치의 단서를 확인한다.
3. 정규화: 서로 다른 값의 범위를 같은 기준으로 조정한다.
4. 인코딩: 범주형 데이터를 숫자로 변환한다.

#### 전처리 후 가능한 작업

1. 데이터 시각화
2. 머신러닝 모델 학습

### 3) 전처리 후 차트를 선택하는 방법

1. 데이터 특성에 적합한 차트를 고르면 데이터 비교, 추이 분석, 분포 파악이 편하다.
2. 차트를 잘못 지정하면 데이터 정보를 왜곡하거나 흐리게 만들기 때문에 유의해야한다.

### 4) 기본 차트

1. `bar` : 막대그래프로 범주별 값을 비교한다. **(값 비교)**
2. `line` : 꺽은선그래프로 시간에 따른 변화를 확인한다. **(변화 추이)**
3. `scatter` : 산점도로 두 값의 관계를 확인한다. **(변수 관계)**
4. `hist` : 히스토그램으로 값의 분포를 확인한다. **(데이터 분포)**

### 5) Matplotlib

> 파이썬에서 가장 널리 사용되는 데이터 시각화 라이브러리이다.
Numpy를 기반으로 해 다양한 형태의 차트와 그래프를 생성할 수 있게 해준다.
>

#### 주요 특징

- **다양한 차트 타입**: 선 그래프, 막대 그래프, 산점도, 히스토그램 등이 있다.
- **고도화된 커스터마이징**: 색상, 스타일, 레이블 등 세밀한 조정이 가능하다.
- **인터랙티브 플롯**: 줌, 팬, 확대/축소 등 사용자 상호작용을 지원한다.
- **다양한 출력 형식**: PNG, PDF, SVG 등 다양한 파일 형식을 지원한다.
- **다른 라이브러리와의 호환성**: Pandas, Seaborn 등과 연동이 가능하다.

#### Matplotlib 설치 및 기본 사용방법

1. 설치 방법

```python
pip install matplotlib
pip install seaborn
```

1. 기본 import

```python
# plt는 matplotlib.pyplot의 별칭(alias)
import platform

# 시각화를 위한 필수 4가지
import numpy as np              # 수치 계산
import pandas as pd             # 표 데이터
import matplotlib.pyplot as plt # 그래프 그리기 (기본)
import seaborn as sns           # 그래프 그리기 (통계 전문)
```

1. 한글 폰트 설정

```python
# 운영체제에 맞는 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'D2coding'      # 윈도우: D2coding
elif platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'        # 맥
else:
    plt.rcParams['font.family'] = 'NanumGothic'        # 리눅스 / 코랩

plt.rcParams['axes.unicode_minus'] = False             # 음수 부호 깨짐 방지
plt.rcParams['figure.figsize'] = (8, 5)                # 기본 그림 크기
```

#### 선 그래프

- 시간에 따른 변화를 나타낸다.
- `x 축` 의 순서를 가진 값이다. (시간, 나이, 온도 등등)

```python
# 기본 선 그래프
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
y = np.array([220, 250, 230, 280, 260, 290, 270, 310, 290, 320, 330, 350])

plt.plot(x, y)
# 선 그래프를 커스터마이징 하고싶다면
# plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o')
plt.title("월별 매출 추이")
plt.xlabel("월")
plt.ylabel("매출 (만원)")
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/6f1c5d7f-9942-40f7-b3b6-396cb1973e2f/image.png)


#### 여러 데이터를 하나의 차트에 표시하려면

```python
# 여러 함수를 한 번에 그리기
# x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x * 5)
# print(y1)
# print(y2)

plt.plot(x, y1, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='red')
plt.plot(x, y3, label='cos(x)', color='green')
plt.title("여러개의 그래프")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()  # 범례 표시 (blue: sin, red: cos [box])
plt.grid(alpha=0.2)
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/772b14fb-6c41-4411-b4de-be298a4eaa6c/image.png)


#### 막대 그래프

1. 범주별로 크기를 비교한다.

```python
# titanic 좌석 등급별 생존율
df = pd.read_csv('titanic.csv')
등급별_생존율 = df.groupby('pclass')['survived'].mean()
print(등급별_생존율)

plt.bar(등급별_생존율.index, 등급별_생존율.values)
plt.title('좌석 등급별 생존율')
plt.xlabel('좌석 등급')        # x 축
plt.ylabel('생존율')           # y 축
plt.xticks([1, 2, 3])          # 1,2,3 등급만 눈금으로
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/86f3776a-672a-4844-927d-3791d6f0099c/image.png)


→ 1등급 좌석의 생존률이 높다.

#### 산점도 그래프

1. 두 값의 관계를 나타낸다.

```python
plt.scatter(df['age'], df['fare'], alpha=0.5) # alpha=0.5 : 반투명. 점이 겹칠 때 필수, 겹친 곳이 진해져서 밀집도가 보임
plt.title('나이와 요금의 관계')
plt.xlabel('나이')
plt.ylabel('요금')
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/6ab005e6-22bf-4133-aa4b-66848564e45b/image.png)


→ 젊고 요금이 싸게 탄 승객이 많다.

#### 히스토그램

1. 값의 분포를 나타낸다.

```python
# bins=20 : 나이를 20개 구간으로 쪼개서 각 구간에 몇 명인지 카운팅
# edgecolor='black' : 막대 테두리 (없으면 막대가 붙어 보여서 읽기 힘듦)
# .dropna() : 결측치를 명시적으로 제외
# plt.hist()는 NaN을 자동으로 무시하므로 필수는 아님
plt.hist(df['age'].dropna(), bins=20, edgecolor='black')
plt.title('승객 나이 분포')
plt.xlabel('나이')
plt.ylabel('사람 수')
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/8a428fff-3eb1-4d0b-beda-b45d9b2fc3a6/image.png)


→ 20/30대가 가장 많이 탔다.

#### 서브 플롯

1. 여러 개의 그래프를 하나의 그림에 배치할 때 사용한다.

```python
# 2x2 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 8))    # 2행 2열

# 각 서브플롯에 데이터 그리기
# [0,0] 등급별 생존율
# 막대 그래프
등급 = df.groupby('pclass')['survived'].mean()
axes[0, 0].bar(등급.index, 등급.values)
axes[0, 0].set_title('등급별 생존율')

# [0,1] 성별 생존율
# 막대 그래프
성별 = df.groupby('sex')['survived'].mean()
axes[0, 1].bar(성별.index, 성별.values, color='coral')
axes[0, 1].set_title('성별 생존율')

# [1,0] 나이 분포
# 히스토그램
axes[1, 0].hist(df['age'].dropna(), bins=20, edgecolor='black')
axes[1, 0].set_title('나이 분포')

# [1,1] 나이 vs 요금
# 산점도 그래프
axes[1, 1].scatter(df['age'], df['fare'], alpha=0.4)
axes[1, 1].set_title('나이 vs 요금')

plt.tight_layout() # 서브플롯 간격 자동 조정
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/e0e731e9-72b1-40fe-ad5c-aa1fab3f53f6/image.png)


→ 2행 2열로 서브플롯 생성

### 6) Seaborn과의 연동

1. Matplotlib은 Seaborn과 함께 사용할 때 더욱 강력해진다.
2. Matplotlib보다 더 간단한 코드로 보기 좋은 통계 그래프를 만들 수 있는 도구이다.

```python
# Matplotlib : 내가 직접 집계해서 넘겨야 함
등급 = df.groupby('pclass')['survived'].mean()
plt.bar(등급.index, 등급.values)

# Seaborn : 집계를 알아서 해줌
sns.barplot(data=df, x='pclass', y='survived')
```

#### countplot

- 개수를 세서 막대 그래프로 나타낸다.

```python
sns.countplot(data=df, x='survived')
plt.title('생존자 / 사망자 수')
plt.xticks([0, 1], ['사망(0)', '생존(1)'])
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/5959dc5f-2d9d-4330-8b23-2a2589ecaef9/image.png)


#### barplot

- 범주별 평균을 구해준다.

```python
sns.barplot(data=df, x='pclass', y='survived')
plt.title('등급별 생존율')
plt.ylabel('생존율')
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/30c4bc19-1ef7-4ede-9a77-449210da6d0f/image.png)


#### countplot vs barplot

| 함수 | counting하는 것 | y축 지정 |
| --- | --- | --- |
| `countplot()` | 범주별 데이터의 **개수(빈도)** | 개수를 직접 세는 그래프이므로 `y`를 지정하지 않음 |
| `barplot()` | 범주별 **평균값** 또는 지정한 통계값 | 숫자 데이터를 집계하므로 `y`에 숫자형 컬럼을 지정 |

#### heatmap

- 2차원 데이터를 색상으로 인코딩 된 행렬로 시각화 하는데 사용한다.
- 데이터의 패턴, 상관관계, 밀도 등 한눈에 파악하는데 매우 유용하다.

```python
# 범주형 변수인 성별이나 승선 도시는 이 상관행렬에 직접 포함되지 않음
# 이러한 변수는 앞에서 사용한 그룹별 생존율이나 교차표로 분석하는 것이 적절함
# sex 성별 추가 불가능 ::> 문자열
# 숫자로 바꿔서 heatmap 추가
# df_corr = df.copy()

# df_corr["sex"] = df_corr["sex"].map({
#     "male": 0,
#     "female": 1
# })
# corr = df_corr.corr(numeric_only=True)

corr = df.corr(numeric_only=True)

corr.round(2)

# np.triu()는 행렬의 상삼각(Upper Triangle) 부분만 남기고 아래쪽 값을 0으로 만드는 함수
# mask = np.triu(np.ones_like(corr, dtype=bool))

plt.figure(figsize=(9, 6))
sns.heatmap(
    corr,
    # mask=mask,
    annot=True,     # 	칸 안에 숫자 표시
    fmt=".2f",      # 	소수점 2자리
    cmap="coolwarm",#  	색 팔레트 (파랑↔빨강)
    vmin=-1,
    vmax=1,
    center=0,       # 	0을 색의 중앙(흰색)으로
    linewidths=0.5) # 	칸 사이 선

plt.title("상관계수 히트맵")
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/543651af-5d20-4168-af46-2d04e4eca1a8/image.png)


#### 상관 관계

- `pclass`와 `fare`는 서로 반대로 움직이는 경향이 있다.

  → **음의 상관관계**

- `sibsp`와 `parch`는 모두 가족 구성원 수와 관련된 변수이므로 함께 증가하는 경향이 있다.

  → **양의 상관관계**

- 생존 여부인 `survived`는 특히 `fare`와 `pclass`와의 상관관계가 비교적 크게 나타나는 것을 히트맵에서 확인할 수 있다.
- `sex`를 여성은 `1`, 남성은 `0`으로 변환한 경우:
    - `sex`와 `survived`의 상관계수가 양수이면 여성이 생존과 더 관련 있다는 의미이다.
    - 상관계수가 음수이면 남성이 생존과 더 관련 있다는 의미이다.

#### histplot

- 분포 + 곡선 + 그룹비교를 한다.
- histplot()은 데이터의 분포를 시각화하는데 사용되는 히스토그램을 그리는데 최적화된 함수이다.
- 다양한 옵션을 통해 세부적인 통계량과 커널 밀도 추정(KDE) 곡선을 함께 표시 가능하다.

```python
# 기본
sns.histplot(data=df, x='age', bins=20)
plt.title('나이 분포')
plt.show()

# KDE 곡선 (데이터 분포를 부드럽게 추정한 밀도 곡선) 추가
# kde=True를 설정하면 히스토그램 막대 위에 데이터 분포를 부드러운 곡선으로 추정하여 나타내는 KDE 곡선이 추가됨
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('나이 분포 + 분포 곡선')
plt.show()

# 그룹별로 나눠 보기
# hue 파라미터를 사용하면 범주형 변수에 따라 데이터를 그룹화하고, 각 그룹별 분포를 하나의 플롯에 표시할 수 있음
# hue='survived' 한 줄이면 데이터를 생존/사망으로 나눠서 색만 다르게 겹쳐 그림
sns.histplot(data=df, x='age', bins=20, hue='survived')
plt.title('생존 여부별 나이 분포')
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/2ccc9e12-58a0-437f-8650-99ceadd68810/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/31b23e82-5fcb-49a4-a542-6b589b47e3ef/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/88acb69c-3082-4079-9f81-fcae1e4ed401/image.png)



#### scatterplot

- 관계 + 그룹을 나타낸다.
- 두 변수 간의 관계를 시각화 하는데 사용되는 가장 기본적인 그래프이다.
- Seaborn의 `scatterplot()` 함수는 산점도를 그리는데 사용한다.

```python
sns.scatterplot(data=df, x='age', y='fare', hue='survived', alpha=0.6)
plt.title('나이·요금과 생존 여부')
plt.show()

# 추세선을 같이 보려면 regplot()
sns.regplot(data=df, x='age', y='fare', color='red', scatter_kws={'alpha': 0.4})
plt.title('나이와 요금 (추세선 포함)')
plt.show()
```

#### 출력 결과

![](https://velog.velcdn.com/images/king-dong-gun/post/76e79fd5-4629-4e1e-914c-57bf77fa2c08/image.png)

![](https://velog.velcdn.com/images/king-dong-gun/post/5b42d963-787d-4096-8ea9-82cc55877f14/image.png)



---

## 2. 탐색적 자료 분석 (EDA)

### 1) EDA란

> 수집한 데이터가 들어왔을 때 이를 다양한 각도에서 관찰하고 이해하는 과정이다.
>

### 2) 과정

1. 문제 정의 및 목표 설정
    - 타이타닉 호 승객데이터를 기반으로 생존에 영향을 미치는 요인을 분석한다.
        - 기본 EDA
        - 데이터 전처리
        - 인사이트 발굴 등등
2. 모듈 import

    ```python
    from IPython.display import Image
    import numpy as np
    import pandas as pd
    import seaborn as sns
    ```

3. 데이터셋 로드

    ```python
    df = sns.load_dataset("titanic")
    df.head()
    
    # 데이터 컬럼 확인
    ```

4. 기본 데이터 조회
    - 상위 5개 행, 하위 5개 행
    - 데이터가 몇 개의 행과 열로 이루어져 있는지
    - 컬럼별 데이터의 dtype과 개수 확인
    - 데이터 컬럼별 결측치 확인
    - 생존자와 사망자의 분포 확인 등등
5. 탐색적 데이터 분석 (EDA)
    - 항구별 생존자 합계 계산
    - 항구별 생존율 계산
    - 항구별 생존자 합계 및 생존율 계산
    - 성별 생존자 합계 및 생존율 계산 등등
6. 전처리
    - 결측치 확인 및 대체
    - 중복된 컬럼 제거

---

### 3. 정리

- 전처리는 결측치, 이상치, 중복, 데이터 타입 등을 정리하는 과정이다.
- `Matplotlib`은 그래프를 세밀하게 직접 설정할 때 사용한다.
- `Seaborn`은 통계 그래프를 더 간단하게 그릴 때 사용한다.
- `countplot()`은 개수, `barplot()`은 평균값을 나타낸다.
- `histplot()`은 분포, `scatterplot()`은 변수 관계, `heatmap()`은 상관관계를 확인할 때 사용한다.
- `EDA`는 데이터를 여러 각도에서 살펴보고 특징과 패턴을 찾는 과정이다.