"""
실전문제 : 효율적인 화폐 구성

입력 예시 1
2 15 # (화폐 종류수, 화폐 가치)
2 # 2원
3 # 3원

출력 조건
첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
불가능할 때는 -1 을 출력한다.

출력 예시 : 5


입력 예시 2
3 4
3
5
7

출력 예시 2: -1
"""

# 정수 N, M을 입력받기
n, m = map(int, input().split())

# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))


# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우, 실제 구현시에는 필요없긴함, 아래의 min에서 처리됨.
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])