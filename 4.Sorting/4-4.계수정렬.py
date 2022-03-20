"""
계수 정렬(Count Sort) : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.

모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대값의 크기를 K라고 할 때,
계수 정렬의 시간 복잡도는 O(N + K) 이다.
계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할 때 적합하다.
계수 정렬은 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을 수록 유리하며 항상 사용할 수는 없다.

- 문제에서 별도의 요구가 없다면 단순히 정렬해야 하는 상황에서는 기본 정렬 라이브러리를 사용,
데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬을 사용한다.

- 코딩 테스트에서의 정렬 알고리즘
1. 정렬 라이브러리로 풀 수 있는 문제
  -> 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본정렬 라이브러리 사용
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제
  -> 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
3. 더 빠른 정렬이 필요한 문제
  -> 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나
     문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.

출력 : 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
"""

# 파이썬 sorted 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# 파이썬 sort 소스코드

array.sort()
print(array)
--------------------------------------------------------
# 정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

---------------------------------------------------------
# 계수 정렬(Count Sort)

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)
print(count) # 배열안에서 가장 큰데이터는 9이다. 즉 크기가 10인 리스트로 초기화한다.

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력