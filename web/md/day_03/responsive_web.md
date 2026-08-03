## 1. 반응형 웹과 UX/UI

### 1. 반응형 웹 디자인

> 디바이스 종류나 화면 크기에 상관없이, 어디서든 일관된 **레이아웃** 및 사용자 경험을 제공하는 디자인 기술
>

---

### 2. UX

> 제품이나 서비스를 사용하는 사람들이 느끼는 전체적인 경험과 만족도를 개선하고, 최적화하기 위한 디자인과 개발 분야이다.
>

#### UX 설계

1. `이해 및 분석` : 유저 리서치, 데이터 분석, 페르소나 설정 등등
2. `구조화` : 정보 구조 설계, 유저 시나리오 및 저니 맵 작성 등등
3. `구체화 및 검증` : 와이어프레임, 프로토타입 제작 및 사용성 테스트 등등

---

### 3. UI

> 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소들을 개발하고 구현하는 분야이다.
>

#### UI 설계

1. `핵심 목표` : 단순히 보기 좋은 디자인을 넘어 정보의 위계를 잡아 사용자가 무엇을 먼저 봐야할지 유도하고, 일관성을 통해 학습 비용을 줄이는 것이 목표이다.
2. 주요 요소
- `레이아웃 & 그리드` : 정보의 배치와 정렬
- `타이포그래피 & 컬러` : 가독성 확보 및 중요도 표현
- `인터랙션 요소` : 버튼의 상태 (기본, 호버, 클릭) 표현 및 시각적 피드백
1. 필요 도구 및 산출물
- 와이어프레임: 화면의 뼈대와 구조 설계
- 디자인 시스템: 버튼, 폰트, 컬러 등 UI 컴포넌트의 표준화된 규칙 가이드
- 프로토타입: 실제 동작하는 것처럼 구현된 시뮬레이션 모델

---

#### 4. Bootstrap Grid system

> 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 **컬럼으로 구성**된 시스템
>

#### Grid system 기본 요소

1. `Container` : 컬럼들을 담고 있는 공간
2. `Column` : 실제 컨텐츠를 포함하는 부분
3. `Gutter` : 컬럼과 컬럼 사이의 여백 영역 (상하좌우)
4. 1개의 row안에 12개의 column 영역이 구성

```html
<div class = "container">
	<div class = "row">
		<div class = "col-4"></div>
		<div class = "col-4"></div>
		<div class = "col-4"></div>
	</div>
</div>
```

![](https://velog.velcdn.com/images/king-dong-gun/post/21fb9d3e-b400-4677-a51f-ee6a6261319c/image.png)


#### 12칸 분배해보기

```html
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
      <div class="col">
        <div class="box">col</div>
      </div>
    </div>
```

#### 출력 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/f94866b7-fe9a-4e7b-afc0-d1953e24df8d/image.png)


#### 중첩(Nesting) 하나의 컬럼에 다른 row 넣기

```html
<div class="container">
    <div class="row">
      <div class="box col-4">
        <div>col-4</div>
      </div>
      <div class="box col-8">
        <div class="row">
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
          <div class="col-6">
            <div class="box">col-6</div>
          </div>
        </div>
      </div>
    </div>
  </div>
```

#### 출력 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/043c9c14-4ec6-49d8-b82f-b395f4629650/image.png)


→ 오른쪽 8개 Column이 다시 12개로 분리된다.

#### 상쇄 (Offset) 상쇄로 Column을 생략해보기

```html
<div class="container">
    <div class="row">
      <div class="col-4">
        <div class="box">col-4</div>
      </div>
      <div class="col-4 offset-4">
        <div class="box">col-4 offset-4</div>
      </div>
    </div>
    <div class="row">
      <div class="col-3 offset-3">
        <div class="box">col-3 offset-3</div>
      </div>
      <div class="col-3 offset-3">
        <div class="box">col-3 offset-3</div>
      </div>
    </div>
    <div class="row">
      <div class="col-6 offset-3">
        <div class="box">col-6 offset-3</div>
      </div>
    </div>
  </div>
```

#### 출력 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/8bcd60bb-1808-46cf-8341-f74d410c7c1d/image.png)


---

### 5. Gutters

> Grid system에서 column 사이에 여백 영역이다.
`x축` 은 padding, `y축` 은 margin으로 여백 생성
>

![](https://velog.velcdn.com/images/king-dong-gun/post/4200b8a8-6613-49ce-a1aa-f8b83058c353/image.png)


#### `gx-0` → 여백제거

```html
<div class="container">
    <div class="row gx-0">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

#### 출력 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/724436db-0b4e-479f-9fed-26a621f57166/image.png)


#### `gy-5` → y축 여백 증가

```html
<div class="container">
    <div class="row gy-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

#### 출력 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/0d6ad34f-a9be-4578-9b83-4f1c3374d7be/image.png)


#### `g-5` → x, y축 여백 증가

```html
<div class="row g-5">
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
      <div class="col-6">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

### 출력 화면

![](https://velog.velcdn.com/images/king-dong-gun/post/bbfac224-521a-422f-a4d4-258cdcc3a8a3/image.png)


---

### 6. BreakPoints

> 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점이다.
>

#### 화면 크기에 따라 각 열의 너비가 달라지는 **Bootstrap 반응형 그리드**

```html
<!-- 기본 화면: 모든 박스 col-12 → 한 줄에 1개 -->
<!-- sm 이상: 모든 박스 col-sm-6 → 한 줄에 2개 -->
<!-- md 이상: 첫 줄 col-md-1 + col-md-10 + col-md-1 -->
<!-- md 이상: 네 번째 박스 col-md-12 → 다음 줄 전체 차지 -->
<div class="container">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-1">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-10">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-1">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-6 col-md-12">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

#### 출력 화면


[▶ 실행 영상 보기](https://velog.velcdn.com/images/king-dong-gun/post/4e1e99a4-c412-409d-9892-262f5b23b804/image.mp4)


#### **4개의 박스가 한 줄에 몇 개씩 배치될지** 정한 Bootstrap 그리드

```html
<!-- 기본 화면: col-12 → 한 줄에 1개 -->
<!-- sm 이상: col-sm-4 → 한 줄에 3개 -->
<!-- md 이상: col-md-6 → 한 줄에 2개 -->
<!-- g-4: 박스 사이의 가로·세로 간격 -->
<!-- offset-md-0: md 이상에서 왼쪽 여백 0칸 -->
<div class="container">
    <div class="row g-4">
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6">
        <div class="box">col</div>
      </div>
      <div class="col-12 col-sm-4 col-md-6 offset-md-0">
        <div class="box">col</div>
      </div>
    </div>
  </div>
```

#### 출력 화면

[▶ 실행 영상 보기](https://velog.velcdn.com/images/king-dong-gun/post/1a507aef-a8fc-482d-bb57-97ef901f22f6/image.mp4)


>💡Bootstrap Grid system은 화면 크기에 따라 12개의 칸을 각 요소에 나누어 주는 것이다!


---

### 7. CSS 레이아웃 총 정리

1. `position` : 흐름을 무시하고 **원하는 좌표**에 배치 할 때
2. `FlexBox` : Grid로 나눈 **구역 내부를** 정렬할 때
3. `Bootstrap Grid system` : 웹 페이지의 **전체적인 구조**를 잡을 때