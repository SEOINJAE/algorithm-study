"""
DFS는 Depth-First Search 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

인접 행렬 (Adjacency Matrix 방식)은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.
인접 리스트(Adjacency List 방식)은 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다.
"""
# 인접 행렬 방식 예제
INF = 9999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
print(type(graph))
print(len(graph))
print(graph[0])

# 인접 리스트 방식 예제
# 행(ROW)이 3개인 2차원 리스트로 인접 리스트 표현
graph2 = [[] for _ in range(3)]
print(graph2)

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph2[0].append((1, 7))
graph2[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph2[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph2[2].append((0, 5))

print(graph2)

"""
DFS는 탐색을 수행함에 있어서 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다는 특징이 있다.
DFS는 스택을 이용하는 알고리즘이기 때문에 실제 구현은 재귀 함수를 이용했을 때 간결하게 구현할 수 있다.
"""

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

print(graph)
print(visited)