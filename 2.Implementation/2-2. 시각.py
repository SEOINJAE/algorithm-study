"""
시각 문제 : 완전 탐색(Brute Forcing) 유형으로 분류되기도 한다.
 ->  가능한 모든 경우의 수를 모두 검사해보는 탐색 방법.
입력 예시 : 5
출력 예시 : 11475

확인(탐색) 해야할 데이터 전체 데이터의 개수가 100만개 이하일 때 완전 탐색을 사용하면 적절.
"""

#H를 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    # print(i)
    for j in range(60):
        for k in range(60):
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)