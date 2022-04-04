"""
개선된 다익스트라 알고리즘
개선된 다익스트라 알고리즘에서는 힙(Heap) 자료구조를 사용한다.

힙 설명
힙 자료구조는 우선순위 큐(Priority Queue)를 구현하기 위하여 사용하는 자료구조 중 하나다.
우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제한다는 점이 특징이다.

스택(Stack) : 가장 나중에 삽입된 데이터 추출
큐(Queue): 가장 먼저 삽입된 데이터 추출
우선순위 큐(Priority Queue) : 가장 우선순위가 높은 데이터 추출

파이썬 우선순위 큐 구현 : PriorityQueue, heapq 사용 가능
파이썬 라이브러리는 최소 힙(Min Heap)으로 구현되어 있다. : 값이 낮은 데이터가 먼저 삭제

최단 거리를 저장하기 위한 1차원 리스트(최단 거리 테이블)는 그대로 사용하고,
현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 읨하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호를 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달 할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[1] == INF:
        print("INFINITY")
    # 도달 할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

print('savepoint')