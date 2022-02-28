#1-2 1이 될 때까지

#단순하게 푸는 답안 예시

n, k = map(int, input().split())
result = 0

#N이 K 이상이라면 K로 계속 나누기
while n >= k:
    #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    #K로 나누기
    n //= k #나눈 후 정수 부분만 할당
    result += 1

    #마지막으로 남은 수에 대하여 1씩 빼기
    while n > 1:
        n -= 1
        result += 1
    print(result)

# 로그 시간 복잡도를 활용한 효율적인 풀이
n, k = map(int, input().split())
result = 0

while True:
    #(N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    print('n//k :', n//k) # 정수 부분만 구하기
    print('n과k :', n, k)
    target = (n//k) * k
    print("target : ", target)
    print("n first :", n)
    result += (n-target)
    print("result :", result)
    n = target
    print('n :', n)
    print()
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 달출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k
    print('update n :', n)

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

