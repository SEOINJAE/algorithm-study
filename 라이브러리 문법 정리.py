"""
자주 사용하는 라이브러리 함수 정리
"""

# 내장 함수
result = sum([1, 2, 3, 4, 5])
print(result)

# min, max 가장 작은 값과 큰 값 반환
result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

# eval() 함수는 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환.
result = eval("(3+5) * 7")
print(result)

# sorted
result = sorted([9, 1, 8, 5, 4]) # 오름차순으로 정렬
print(result)

result = sorted([9, 1, 8, 5, 4], reverse = True) # 내림차순으로 정렬
print(result)

# 원소를 튜플의 두 번째 원소(나이)를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse =True)
print(result)

# 리스트와 같은 iterable 객체는 기본으로 sort() 함수를 내장하고 있다.
data = [9, 1, 8, 5, 4]
data.sort()
print(data)


# itertools
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)


from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)


from itertools import combinations_with_replacement
data = ['A', 'B', 'C'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
print(result)


# heapq
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)



# 최대 힙(Max Heap)
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 동작원리 파악해보기
test = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
h = []
value = []
# 모든 원소를 차례대로 힙에 삽입
for value in test:
    heapq.heappush(h, -value)
    print(h, value)

result = []
for i in range(len(h)):
    result.append(-heapq.heappop(h))
    print(result)

# bisect
"""
bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a, x): 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
"""

from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


from bisect import bisect_left, bisect_right

# 값이[left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))


# collections
from collections import deque

data = deque([2, 3, 4])
print(data)
data.appendleft(1)
data.append(5)

print(data)
print(list(data)) # 리스트 자료형으로 변환

# collections Counter는 등장 횟수를 세는 기능을 제공
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환

# math 라이브러리
import math

print(math.factorial(5)) # 5! 팩토리얼을 출력

print(math.sqrt(7)) # 7의 제곱근을 출력

print(math.gcd(21, 14)) # 최대 공약수

print(math.pi) # 파이(pi) 출력

print(math.e) # 자연상수 e 출력

