### 1. 최소 신장 트리

> 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 **최소**인 신장 트리이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/a215efaf-afed-4cbc-b08b-bd565f50b070/image.png)



#### 대표적인 트리 문제

보통 **최소 신장 트리(MST)** 문제는 아래 형태로 많이 나온다.

1. **모든 정점을 최소 비용으로 연결**
    - 도시들을 도로로 연결 문제
    - 컴퓨터들을 네트워크로 연결 문제
2. **섬 연결**
    - 여러 섬을 다리로 연결하면서 건설 비용 최소화 문제
3. **통신망 / 전기망 구축**
    - 모든 지역을 연결하면서 케이블 설치 비용 최소화 문제
4. **기존 연결망에서 최소 비용 구하기**
    - 여러 연결 방법 중 전체를 연결할 수 있는 최소 비용 선택 문제

---

### 2. Prim 알고리즘

> 하나의 정점에 연결된 간선들 중에서, 하나씩 선택하면서 MST를 만들어 가는 방식이다.
>
1. 임의 정점 하나를 선택해서 시작한다.
2. 선택한 정점과 인접하는 정점들 중의 최소비용의 간선이 존재하는 정점을 선택한다.
3. 모든 정점이 선택될 때까지 앞의 과정을 반복한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/1e6fe781-098d-4d1e-a7ff-1396b9a3d6ae/image.png)


#### 우선 순위 큐

> Prim 알고리즘에서는 **현재 선택 가능한 간선 중 가장 가중치가 작은 간선**을 계속 찾아야 한다.
>

그래서 최소값을 빠르게 꺼낼 수 있는 **우선순위 큐(Priority Queue)**를 사용한다.

파이썬에서는 `heapq`를 이용한다.

#### 최소 힙

```python
import heapq

arr = []

heapq.heappush(arr, 13)
heapq.heappush(arr, 5)
heapq.heappush(arr, 17)
heapq.heappush(arr, 9)

print(arr)

for i in range(len(arr)):
    print(heapq.heappop(arr))

print(arr)
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/0c09e36f-e662-4151-a8d8-bbcef75568f4/image.png)


#### 최대 힙

```python
import heapq
arr = [3, 234, 23, 12, 31]
heap = []
for i in range(len(arr)):
		# 음수로 바꿔서 넣으면 최대 힙처럼 사용
		# 음수 중에서는 가장 작은 값이 원래 값으로 보면 가장 큰 값
    heapq.heappush(heap, -arr[i])

for i in range(len(arr)):
    print(heapq.heappop(heap)*-1)
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/5344f306-a239-4432-a426-21514e4ec918/image.png)


Prim → 최소 비용 간선을 반복해서 선택 → 우선순위 큐 사용의 흐름으로 연결된다.

---

### 3. Kruskal 알고리즘

> 간선을 하나씩 선택해서 MST를 찾는 알고리즘이다.
>
1. 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬한다.
2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킨다.
    - 사이클이 존재하면 다음으로 가중치가 낮은 간선을 선택한다.
3. `n - 1` 개의 간선이 선택될 때까지 2를 반복한다.

![](https://velog.velcdn.com/images/king-dong-gun/post/9eaa138c-997e-4d7c-a15e-af2d3ef06312/image.png)



```python
# (가중치, 시작 정점, 끝 정점)
edges = [
    (1, 1, 2),
    (2, 1, 3),
    (3, 2, 3),
    (4, 2, 4),
    (5, 3, 4)
]

edges.sort()

parent = [0, 1, 2, 3, 4]

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])

    return parent[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x != y:
        parent[y] = x

total = 0

for cost, x, y in edges:
    # 서로 다른 집합이면 사이클이 발생하지 않음
    if find_set(x) != find_set(y):
        union(x, y)
        total += cost

        print(x, y, cost)

print("최소 비용:", total)
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/5bbe4b66-8e60-44a2-9fd1-1aef5f3e1b53/image.png)

가중치가 작은 간선부터 확인하면서 **사이클이 없는 간선만 선택**한다.

---

### 4. Dijkstra 알고리즘

#### 최단 경로

> 가중치가 있는 그래프에서 두 정점 사이의 경로 중 가중치 합이 최소인 경로이다.
>

#### Dijkstra 알고리즘

> 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 알고리즘이다.
>
1. 시작 정점(s)에서 끝 정점(t)까지의 최단 경로에 정점 x가 존재한다.
2. 최단 경로는 s에서 x까지의 최단 경로와 x에서 t까지의 최단 경로로 구성된다.
3. 탐욕 기법을 사용한 알고리즘으로 MST의 Prim 알고리즘과 유사하다.

![](https://velog.velcdn.com/images/king-dong-gun/post/c1302096-2cae-4f4c-ba30-8bffb08d082e/image.png)



```python
import heapq

# 그래프 정보
# graph[정점] = [(가중치, 연결된 정점), ...]
graph = [
    [],
    [(2, 2), (5, 3)],   # 1번 정점 -> 2번(비용 2), 3번(비용 5)
    [(1, 3), (4, 4)],   # 2번 정점 -> 3번(비용 1), 4번(비용 4)
    [(1, 4)],           # 3번 정점 -> 4번(비용 1)
    []
]

# 무한대 값
INF = int(1e9)

# 각 정점까지의 최단 거리 저장
# 처음에는 아직 최단 거리를 모르기 때문에 무한대로 초기화
distance = [INF] * 5

# 우선순위 큐
pq = []

# 시작 정점은 1번
# 자기 자신까지의 거리는 0
distance[1] = 0

# (거리, 정점) 형태로 우선순위 큐에 저장
heapq.heappush(pq, (0, 1))

while pq:
    # 현재 가장 거리가 짧은 정점을 꺼냄
    dist, node = heapq.heappop(pq)

    # 이미 더 짧은 경로가 저장되어 있다면 무시
    if distance[node] < dist:
        continue

    # 현재 정점과 연결된 정점 확인
    for cost, next_node in graph[node]:

        # 현재 정점을 거쳐 다음 정점으로 가는 거리
        new_dist = dist + cost

        # 기존에 저장된 거리보다 더 짧다면 갱신
        if new_dist < distance[next_node]:
            distance[next_node] = new_dist

            # 갱신된 거리와 정점을 우선순위 큐에 추가
            heapq.heappush(pq, (new_dist, next_node))

# 1번 정점에서 각 정점까지의 최단 거리 출력
for i in range(1, 5):
    print(i, distance[i])
```

#### 출력

![](https://velog.velcdn.com/images/king-dong-gun/post/f8bd1df4-1984-469e-9dd3-c19f6995899d/image.png)


시작 정점이 `1`이므로:

```
1 → 1 : 0
1 → 2 : 2
1 → 3 : 3
1 → 4 : 4
```

처럼 **1번 정점에서 각 정점까지의 최소 비용**이 출력된다.