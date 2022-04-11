"""
서로소 집합(Disjoint Sets) : 공통 원소가 없는 두 집합
예) {1, 2}와 {3, 4} 서로소 관계이다.

서로소 집합 계산 알고리즘
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.
 1-1. A와 B의 루트노드 A, B를 각각 찾는다.
 1-2. A를 B의 부모노드로 설정한다(B가 A를 가리키도록 한다.)

2. 모든 union(합집합) 연사을 처리할 때까지 1번 과정을 반복한다.

"""

# 기본적인 서로소 집합 알고리즘 소스

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력하기
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
