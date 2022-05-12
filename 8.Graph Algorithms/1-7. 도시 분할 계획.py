"""
도시 분할 계획

입력 예시
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
6 4 1
6 5 3
4 5 3
6 7 4

출력 예시 : 8
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
계속 예정