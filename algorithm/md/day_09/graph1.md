### 1. 그래프 기본

> 정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료 구조이다.
>

#### 그래프 유형

1. 무향 (무방향) 그래프
2. 유향 (방향) 그래프
3. 가중치 그래프
4. 사이클 없는 방향 그래프

![](https://velog.velcdn.com/images/king-dong-gun/post/1f586997-6007-4342-9a91-cd1afccafc58/image.png)


#### 그래프 표현

- 간선의 정보를 저장하는 방식, 메모리나 성능을 고려해서 결정한다.
- 인접 행렬
    - `N x N` 크기의 2차원 배열을 이용해서 간선 정보를 저장한다.

```python
graph = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
```

- 인접 리스트
    - 각 정점마다 해당 정점과 인접한 정점 정보를 저장한다.

```python
graph = [
    [1, 2],
    [0],
    [0]
]
```

- 간선의 배열
    - 간선을 배열에 연속적으로 저장한다.

```python
edges = [
    (0, 1),
    (0, 2)
]
```

---

### 2. DFS

> 한 경로를 끝까지 탐색한 뒤, 더 이상 갈 곳이 없으면 이전 갈림길로 돌아가 탐색을 이어간다.
>
>
> 재귀 또는 스택을 이용한다.
>

#### 재귀 방식

```python
def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(next_node)
```

- 현재 정점을 방문 처리한다.
- 연결된 정점 중 방문하지 않은 정점으로 계속 들어간다.

#### 스택 방식

```python
def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        v = stack.pop()
        print(v, end=' ')

        for next_node in graph[v]:
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True
```

---

### 3. BFS

> 시작 정점에서 가까운 정점부터 차례대로 탐색한다.
>
>
> 큐(Queue)를 이용한다.
>

```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for next_node in graph[v]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
```

- 시작 정점을 큐에 넣는다.
- 큐에서 하나씩 꺼내면서 인접 정점을 확인한다.
- 방문하지 않은 정점은 다시 큐에 넣는다.

#### DFS / BFS 차이

| DFS | BFS |
| --- | --- |
| 깊이 우선 탐색 | 너비 우선 탐색 |
| 재귀 / 스택 | 큐 |
| 한 경로를 깊게 탐색 | 가까운 정점부터 탐색 |

---

### 4. Union-Find

> 서로소 집합(Disjoint Set)을 관리하기 위한 자료구조이다.
>
>
> `Make-Set`, `Find-Set`, `Union` 연산을 사용한다.
>

#### Make-Set

각 원소가 자기 **자신을 대표자**로 가지도록 만든다.

```python
N = 5

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i
```

#### Find-Set

해당 원소가 속한 집합의 대표자를 찾는다.

```python
def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])

    return parent[x]
```

`parent[x] = find_set(parent[x])`를 통해 대표자를 직접 가리키도록 변경하는 것을 **경로 압축(Path Compression)**이라고 한다.

#### Union

두 원소가 속한 집합을 하나로 합친다.

```python
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x
```

사용 예시는 다음과 같다.

```python
union(1, 2)
union(2, 3)

print(find_set(1))
print(find_set(2))
print(find_set(3))
```

`1`, `2`, `3`은 같은 대표자를 가지게 된다.

---

### 5. Union-Find 최적화

트리가 한쪽으로 길어지면 `Find-Set` 과정이 오래 걸릴 수 있다.

#### Rank

높이가 낮은 트리를 높은 트리 아래에 붙인다.

```python
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_x] = root_y

        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1
```