### 그래프를 탐색하는 방법

그래프를 탐색하는 방법에는 두가지가 있다. *너비 우선탐색과 깊이 우선 탐색*이 있다.

![](https://velog.velcdn.com/images/king-dong-gun/post/fea4f790-29e9-4675-8501-ab56dd7c6683/image.png)


### 너비 우선 탐색 (BFS, Breadth First Search)

> 탐색 시작 정점에 인접한 정점들을 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식이다.
>

### BFS 탐색 순서

![](https://velog.velcdn.com/images/king-dong-gun/post/3dcd1bd6-873d-4a94-8375-900a4809a488/image.png)


#### BFS 알고리즘

- 입력 파라미터: 그래프 G와 탐색 시작점 v

```python
def bfs(G, v, n):             # 그래프 G, 탐색 시작점 v
	visited = [0] * (n + 1)     # n: 정점의 갯수
	queue = []                  # 큐 생성
	queue.append(v)             # 시작점 v를 큐에 삽입
	
	while queue:                # 큐가 비어있지 않은 경우
		t = queue.pop(0)          # 큐의 첫 번째 원소 반환
		visited(t)                # 정점 t에서 할 일
			
			for i in G[t]:          # t와 연결된 모든 정점에 대해
				if not visited[i]:    # 방문하지 않은 곳이면
					queue.append(i)     # 큐에 넣는다
					visited[i] = visited[t] + 1 # n으로부터 1만큼 이동
```

즉 아래와 같이 요구사항에 맞게 코드를 짜자

```python
시작점 큐에 넣기
→ 시작점 방문 처리
→ 큐에서 하나 꺼내기
→ 연결된 곳 확인
→ 방문 안 했으면 큐에 넣기 + 방문 처리
→ 큐가 빌 때까지 반복
```