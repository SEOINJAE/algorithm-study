# 10의 9제곱 : 0이 9개
a = 1e9
print(a)

b= 2e3
print(b)

# 3.954
c = 3594e-3
print(c)


a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)


a = 0.3 + 0.6
print(a)

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)


print(round(a, 4))


a = list()
print(a)

b = []
print(b)

#  크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

print(a[3])


# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)


# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

array[1][1] = 5
print(array)

summary = 0
for i in range(1, 10):
    summary += i
print(summary)

for _ in range(5):
    print("Hello World")


# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4

array = [[0] * m] * n
print(array)


array[1][1] = 5
print(array)


a = [1, 4, 3]
print("기본 리스트:", a)

a.append(2)
print("삽입:", a)

a.sort()
print("오름차순 정렬:", a)

a.sort(reverse= True)
print("내림차순 정렬:", a)

a.reverse()
print("원소 뒤집기:", a)

a.insert(2, 3)
print("인덱스 2에 3 추가:", a)

print("값이 3인 데이터 개수:", a.count(3))


a.remove(1)
print("값이 1인 데이터 삭제:", a)


a = [1, 2, 3, 4, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)



data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

data

# 키 데이터만 담은 리스트
key_list = data.keys()

print(key_list)

# 값 데이터만 담은 리스트
value_list = data.values()

value_list

print(value_list)

for key in key_list:
    print(data[key])


data = set([1,1,2,3,4,4,5])

print(data)

data = {1, 1, 2, 3, 4, 4, 5}

print(data)


a = 0

def func():
    global a
    a += 1

for i in range(10):
    print(func())
    print(a)

print(a)


def add(a, b):
    return a + b

print(add(3, 7)



print((lambda c, d: c + d)(3, 7))



# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

data.sort

data


n, m, k = map(int, input().split())

print(n, m, k)



import sys
data = sys.stdin.readline().rstrip()

print(data)