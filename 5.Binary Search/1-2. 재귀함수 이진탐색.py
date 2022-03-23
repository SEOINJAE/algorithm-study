"""
# 재귀 함수로 구현한 이진 탐색 소스코드

# 이진 탐색을 구현하는 방법에는 2가지가 있다.
1. 재귀함수 활용
2. 단순하게 반복문 활용

# 입력 예시 1
10 7
1 3 5 7 9 11 13 15 17 19

출력 예시 : 4

# 입력 예시 2
10 7
1 3 5 6 9 11 13 15 17 19

출력 예시 : 원소가 존재하지 않습니다.
"""

# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2 # 몫만을 가져온다.

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) # 위치 인덱스 출력
