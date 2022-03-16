"""
정렬(Sorting) : 연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘
오름차순 정렬을 기준으로 연습.
내림차순은 결과를 반대로 Reverse하면 된다.

- 선택 정렬
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
"""

# 선택 정렬 소스코드(가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬 완료
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
print(array)

# 파이썬 스와프(Swap) 소스코드
# 0 인덱스와 1 인덱스의 원소 교체하기
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array)

