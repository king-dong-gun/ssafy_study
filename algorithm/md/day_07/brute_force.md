### 1. 반복과 재귀

- 반복과 재귀는 유사한 작업을 수행할 수 있다.
- 반복은 수행하는 작업이 완료될 때 까지 계속 반복한다.
    - 루프 `for` , `while`
- 재귀는 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용하는 방법이다.
    - 하나의 큰 문제를 해결할 수 있는 더 작은 문제로 쪼개고 결과들을 결합한다.

#### 재귀함수 예시

```python
# 0 1 2 3 2 1 0
def recursive(level):
	  # 현재 level 출력
    print(level, end=" ")
    # level이 3이면 더 이상 재귀 호출하지 않고 종료
    if level == 3:
        return
		# level이 3이 될때까지 +1
    recursive(level + 1)
    print(level, end=" ")
# recursive(0)으로 재귀 시작
recursive(0)  
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/7c133a73-00b5-4cd3-930c-1c46b347324d/image.png)


위 처럼 함수 내부에서 자기 자신을 계속 호출시키는 것이 **재귀함수** 이다.

> Branch, Level을 먼저 파악하고, 이후 코드를 직접 구현한다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/1d5f4f7e-b962-4136-b974-34feb324368e/image.png)


---

### 2. 순열

> 서로 다른 N개에서, R개를 중복 없이, 순서를 고려하여 나열하는 것 이다.
>

ex) 0, 1, 2로 구성된 3장의 카드 중 2장을 뽑아 순열을 나열한다. → **모든 경우의 수**

#### 중복 순열 구현 원리

> 서로 다른 N개에서 R개를 중복을 허용하고, 순서를 고려하여 나열하는 것 이다.
>
1. 재귀호출을 할 때마다, 이동 경로를 흔적으로 남긴다.
2. **가장 마지막 레벨에 도착했을 때, 이동 경로를 출력한다.**

#### 중복 순열 구현

1. 먼저 `Path` 라는 전역 리스트를 준비한다.
2. 그리고 `Level2`, `Branch3` 으로 동작하는 재귀 코드를 구현한다.
3. **재귀호출을 하기 직전에** 이동할 곳의 위치를 `path`  리스트에 기록한다.
4. 재귀호출이 모두 끝나 바닥에 도착했으면 출력하는 코드를 작성한다.
5. 함수가 리턴 되고, 함수가 즉시 종료되었을때, 이후 `path` 에 적은 마지막 기록이 삭제되어야 한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/71b026b0-8699-4a56-a7f4-c9c87fb3a71d/image.png)


```python
path = []

def perm(x):
	# x가 2가 되면 더 이상 재귀 호출하지 않고 종료
	if x == 2:
		print(path)
		return
	# i가 0, 1, 2 순서로 반복
	for i in range(3):
		# 현재 선택한 i를 path에 추가
		path.append(i)
		# x를 1 증가시켜 자기 자신을 다시 호출
		perm(x + 1)
		# 재귀가 끝나고 돌아왔으면 방금 선택했던 숫자를 제거해서 이전 상태로 복구
		path.pop()

perm(0)
```

```python
[]
 ↓ append(0)
[0]
 ↓ append(0)
[0, 0] → 출력
 ↓ pop()
[0]
 ↓ append(1)
[0, 1] → 출력
 ↓ pop()
[0]
 ↓ append(2)
[0, 2] → 출력
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/6f821ebe-ff5d-46b2-a038-e514ecad36d0/image.png)


---

### 3. 완전 탐색

> 모든 가능한 경우를 시도해서 정답을 찾아내는 알고리즘이다.
>

#### 완전 탐색의 기본 구조

1. 현재 `Level`에서 선택할 수 있는 모든 경우를 확인한다.
2. 하나를 선택한 뒤 `dfs(level + 1, ...)`로 다음 `Level`로 이동한다.
3. 마지막 Level에 도착하면 원하는 조건을 만족하는지 확인한다.
4. 조건을 확인한 뒤 `return`하여 이전 `Level`로 돌아간다.
5. 아직 확인하지 않은 다른 경우를 다시 탐색한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/d5eaac04-1c27-4868-9049-5264517c4621/image.png)


현재 코드는 **DFS를 이용하여 모든 경우의 수를 탐색하고, 불필요한 경우는 가지치기하는 방식**이다.

```python
arr = [3, 4, 7, 1, 6]
count = 0

def dfs(level, sum_value):
    global count

    # 합이 10을 넘으면 더 볼 필요가 없으므로 가지치기
    if sum_value > 10:
        return

    # 숫자 3개를 선택한 상태
    if level == 3:
        # 합이 정확히 10이면 경우의 수 증가
        if sum_value == 10:
            count += 1
        return

    # arr의 5개 원소를 각각 선택해봄
    for i in range(5):
        dfs(level + 1, sum_value + arr[i])

dfs(0, 0)
print(count)
```



```python
dfs(0, 0)
 ↓ 숫자 1개 선택
dfs(1, 지금까지의 합)
 ↓ 숫자 1개 더 선택
dfs(2, 지금까지의 합)
 ↓ 숫자 1개 더 선택
dfs(3, 세 숫자의 합)
 → 합이 10인지 검사
 → return
 ↑ 이전 dfs(2)로 돌아감
 → for문의 다음 숫자를 선택
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/5192eb93-ee3e-4e33-abf6-6e33053a6b05/image.png)
