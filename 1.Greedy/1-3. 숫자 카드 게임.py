"""
1-3. 숫자 카드 게임
입력 예시 1
3 3
3 1 2
4 1 4
2 2 2

출력 예시 1
2

입력 예시 2
2 4
7 3 1 8
3 3 3 4

출력예시 2
3
"""

#min 함수를 이용하는 답안
# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    #현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # print("min_value :", min_value)

    #'가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

#---------------------------------------------
# 2중 반복문 구조를 이용하는 답안
# N, M을 공백으로 구분하여 입력받기
k, p = map(int, input().split())

result2 = 0

#한 줄씩 입력받아 확인
for i in range(k):
    data = list(map(int, input().split()))

    #현재 줄에서 '가장 작은 수' 찾기
    min_value2 = 10001 #문제의 조건에 있는 1만 이하의 자연수
    for a in data:
        min_value2 = min(min_value2, a)
        print(min_value2, result2)
    result2 = max(result2, min_value2)
    #큰 루프가 돌면서 result2가 업데이트됨, 새롭게 들어온 각 행의 데이터와 이전 행의 데이터 중에서 큰 수찾기

print(result2)