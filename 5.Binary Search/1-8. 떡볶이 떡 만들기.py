"""
실습 3: 떡볶이 떡 만들기

파라메트릭 서치(Parametric Search)
최적화 문제를 결정 문제로 바꾸어 해결하는 기법.
원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제

입력 예시
4 6
19 15 10 17

출력 예시 : 15
"""

# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, input().split(' ')))

# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in array:
        # 잘랐을 때의 떡의 양 계산
            if x > mid:
                total += x - mid
        # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        if total < m:
            end = mid - 1
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1

# 정답 출력
print(result)