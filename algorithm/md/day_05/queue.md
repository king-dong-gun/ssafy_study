### 1. 큐 (Queue)

> 먼저 들어온 데이터가 먼저 나가는 선형 자료구조
>

#### 큐의 구조

**선입선출, FIFO (First In First Out), 가장 먼저 넣은 자료가 가장 먼저 나오는 것이다.**

![](https://velog.velcdn.com/images/king-dong-gun/post/2553bc9d-5bd8-4525-b4f6-48a2362b6547/image.png)


#### 큐의 기본 연산

- 삽입은 `enqueue()` , 삭제는 `dequeue()` 라고 한다.

---

### 2. 선형 큐 (Linear Queue)

> 데이터를 일렬로 저장하며, 앞에서 꺼내고 뒤에 넣는 기본 큐 구조이다.
>

#### 상태표현

1. 초기 상태: `front = rear = -1`
2. 공백 상태: `front == rear`
3. 포화 상태: `rear == n-1` (배열의 크기 n, 배열의 마지막 인덱스 n-1)

#### 구현

1. 배열이나 연결 리스트로 구현한다.
2. 배열로 구현한 경우 큐의 크기는 배열의 크기와 같다.
3. `front` : 가장 최근에 삭제된 원소의 인덱스다.
4. `rear` : 마지막에 저장된 원소의 인덱스다.

```python
# 초기 공백 큐 생성
# create_queue()
q = [0] * n
front = -1
rear = -1

# 삽입 enqueue
def enqueue(item):
	global rear
	if is_full():
		print("Queue_Full")
	else:
		rear = rear + 1
		q[rear] = item
		
# 삭제 dequeue
def dequeue():
	global front
	if is_empty():
		print("Queue_Empty")
	else:
		front = front + 1
		return q[front]
		
# 공백 상태 및 포화 상태 검사 is_empty(), is_full()
def is_empty():
	return front == rear

def is_full():
	return rear == len(q) - 1

# 검색 qpeek()
def fqpeek():
	if is_empty():
		print("Queue_Empty")
	else:
		return q[front + 1]
```

#### 선형 큐 사용시 문제점

***선형 큐를 이용해 원소 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, `rear == n-1` 인 상태, 포화상태로 인식해 더 이상 삽입을 수행하지 않게 된다.***

#### 해결 방법

1. 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동한다.
    - 많은 시간이 소요되어 큐의 효율성이 떨어진다.
2. 1차원 배열을 사용한다.
    - 배열의 처음과 끝이 연결되어 원형 형태를 이룬다고 가정하고 사용한다. → **원형 큐**

---

### 3. 원형 큐  (Circualr Queue)

> 선형 큐의 공간 낭비를 막기 위해 처음과 끝이 연결된 구조이다.
>

#### 원형 큐의 구조

![](https://velog.velcdn.com/images/king-dong-gun/post/98d76cd3-154b-4809-952b-bae8ac066431/image.png)



#### 원형 큐 구현

```python
# 초기 공백 큐 생성
cq = [0] * n
front = rear = 0

# 삽입 enqueue(item)
def enqueue(item):
	global rear
	if is_full():
		print("Queue_Full")
	else:
		rear = (rear + 1) % len(cq)
		cq[rear] = item
	
# 삭제 dequeue()
def dequeue():
	global front
	if is_empty():
		print("Queue_Empty")
	else:
		front = (front + 1) % len(cq)
		return cq[front]
	
# 공백상태 및 포화상태 검사 is_empty(), is_full()
def is_empty():
	return front == rear

def is_full():
	return (rear + 1) % len(cq) == front
```

---

### 4. 연결 큐 (Linked Queue)

> 연결 리스트를 이용해 구현한 큐 이다.
>

#### 상태 표현

1. 초기 상태: `front == rear == NULL`
2. 공백 상태: `front == rear == NULL`

#### 연결 큐의 구조

단순 연결 리스트를 이용한 큐

1. 큐의 원소: 단순 연결 리스트의 노드이다.
2. 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있다.
3. `front` : 첫번째 노드를 가리키는 링크이다.
4. `rear` : 마지막 노드를 가리키는 링크이다.

![](https://velog.velcdn.com/images/king-dong-gun/post/e2701cc2-966f-49c9-9d7c-2626c4b6f963/image.png)


#### 구현

`deque (덱)` : 이미 구현되어 있는 자료구조를 가져와서 `append()`, `popleft()`만 사용한다.

```python
from collections import deque

q = deque()
q.append(1)     # enqueue()
t =q.popleft()  # dequeue()
```

```python
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n
front = None
rear = None

# 연결 큐 삽입 연산
def enqueue(item):
    global front, rear
    newNode = Node(item)   # 새 노드 생성
    if front == None:      # 큐가 비어 있으면
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

# 연결 큐가 비어 있는지 검사
def is_empty():
    return front == None
    
# 연결 큐 삭제 연산
def dequeue():
    global front, rear
    if is_empty():
        print("Queue_Empty")
        return None
    item = front.item      # 맨 앞 데이터 저장
    front = front.next     # front를 다음 노드로 이동
    if front == None:      # 마지막 원소까지 삭제했다면
        rear = None
    return item
```

---

### 5. 우선 순위 큐 (Priority Queue)

> 우선순위를 가진 항목들을 저장하는 큐 이다.
>

![](https://velog.velcdn.com/images/king-dong-gun/post/8284c3e9-7c7a-479b-9297-b2757c504987/image.png)


#### 배열을 이용한 우선순위 큐

1. 배열을 이용해 자료를 저장한다.
2. 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조이다.
3. 가장 앞에 최고 우선순위의 원소가 위치한다.

#### 문제점

1. 배열을 사용하므로, 삽입이나, 삭제 연산이 일어날 때 원소의 재배치가 발생한다.
2. 소요되는 시간이나 메모리 낭비가 크다.

---

### 6. 큐의 활용

#### 버퍼 (Buffer)

> 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역이다.
>

#### 버퍼의 자료구조

- 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용된다.
- 순서대로 입/출력/전달이 되야하므로 `FIFO` 방식의 자료구조인 큐가 활용된다.

---
## 실습) 마이쮸 나눠주기

마이쮸를 받기 위해 사람들이 한 줄로 줄을 선다.

처음에는 **1번 사람**이 줄을 서서 마이쮸 **1개**를 받는다.

마이쮸를 받은 사람은 다시 줄의 맨 뒤로 이동하며, 다음번 자신의 차례에는 **이전에 받은 개수보다 1개 더 많은 마이쮸**를 받는다.

또한 한 사람이 마이쮸를 받고 다시 줄을 설 때마다 **새로운 사람이 1명씩 줄의 맨 뒤에 들어온다.**

진행 과정은 다음과 같다.

```python
1번이 줄을 선다.
1번이 마이쮸 1개를 받는다.

1번이 다시 줄을 선다.
새로운 2번이 줄을 선다.

1번이 마이쮸 2개를 받는다.
1번이 다시 줄을 선다.
새로운 3번이 줄을 선다.

2번이 마이쮸 1개를 받는다.
2번이 다시 줄을 선다.
새로운 4번이 줄을 선다.

1번이 마이쮸 3개를 받는다.
1번이 다시 줄을 선다.
새로운 5번이 줄을 선다.

3번이 마이쮸 1개를 받는다.

...
```

```python
from collections import deque

next_person = 1              # 새로 줄을 설 사람 번호
queue = deque()              # 대기 줄

total_candy = 1000000        # 전체 마이쮸 개수
given_candy = 0              # 지금까지 나눠준 마이쮸 개수

current_person = 0           # 현재 마이쮸를 받는 사람 번호

while given_candy < total_candy:

    # 새로운 사람이 처음 줄을 선다.
    # 처음 받을 개수는 1개, 지금까지 받은 개수는 0개
    queue.append((next_person, 1, 0))

    # 가장 먼저 줄을 선 사람을 꺼낸다.
    current_person, candy_count, received_candy = queue.popleft()

    # 현재 사람에게 마이쮸를 나눠준다.
    given_candy += candy_count

    # 받은 사람은 다시 줄의 맨 뒤로 간다.
    # 다음에는 이전보다 1개 더 받는다.
    queue.append((
        current_person,
        candy_count + 1,
        received_candy + candy_count
    ))

    # 다음에 새로 줄을 설 사람 번호
    next_person += 1

print(f'마지막 받은 사람 : {current_person}')
```

### 코드 흐름

1. `deque`를 이용해 사람들의 대기 줄을 만든다.
2. 새로운 사람은 항상 처음에 마이쮸 **1개를 받을 상태**로 큐의 뒤에 들어간다.
3. `popleft()`로 줄의 맨 앞 사람을 꺼낸다.
4. 그 사람이 받을 마이쮸 개수만큼 `given_candy`에 더한다.
5. 마이쮸를 받은 사람은 **다음에 받을 개수를 1 증가**시켜 다시 큐의 뒤에 들어간다.
6. 새로운 사람 번호를 1 증가시킨다.
7. 전체 마이쮸가 모두 나눠질 때까지 위 과정을 반복한다.
8. 반복이 끝났을 때 `current_person`이 마지막으로 마이쮸를 받은 사람이다.

핵심은 아래 두 줄이다.

```
queue.append(...)# 줄의 맨 뒤에 들어감queue.popleft()# 줄의 맨 앞 사람이 나옴
```

즉, **먼저 줄을 선 사람이 먼저 마이쮸를 받는 FIFO 구조를 `deque`로 구현한 시뮬레이션 문제**이다.