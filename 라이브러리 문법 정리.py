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

