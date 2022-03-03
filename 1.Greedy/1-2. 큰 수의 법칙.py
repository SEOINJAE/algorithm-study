"""
1-2 큰 수의 법칙
입력예시
5 8 3
2 4 5 4 6

"""

import time

start_time = time.time()

#N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

#N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬하기, 오름차순 정렬하기
# data.sort(reverse = True) #내림차순 정렬하기
# print(data)

first = data[n-1] #가장 큰 수
second = data[n-2] #두 번째로 큰 수

# print(first, second)

result = 0

while True:
    for i in range(k): #가장 큰 수를 K번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 #더하기 할때마다 1씩 빼기
    if m == 0: #m이 0이라면 반복문 탈출
        break
    result += second #두 번째로 큰 수를 한 번 더하기
    m -= 1 #더할 때마다 1씩 빼기

print(result)

end_time = time.time()

print("time :", end_time - start_time)