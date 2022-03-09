"""
재귀함수 (Recursive Function) : 자기 자신을 다시 호출하는 함수를 의미

"""
#재귀 함수 예제
def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()

recursive_function()

"""
RecursionError: maximum recursion depth exceeded while calling a Python object

위 함수를 실행하면 '재귀 함수를 호출합니다'라는 문자열 무한히 출력
어느정도 출력하다가 위의 오류 발생
이 오류 메세지는 재귀(recursion)의 최대 깊이를 초과했다는 내용이다.
"""

# 재귀 함수 종료 예제
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

# 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

"""
팩토리얼을 수학적 점화식으로 표현
1. n이 0 혹은 1일 때 : factorial(n) = 1 
 -> 팩토리얼은 n이 양의 정수일 때에만 유효하기 때문에 n이 1 이하인 경우 1을 반환할 수 있도록 작성
 -> n이 1 이하인 경우를 고려하지 않으면 재귀 함수가 무한히 반복되어 결과를 출력하지 못할 것이다.
 -> 또한, n의 값이 음수가 들어왔을 때는 입력 범위 오류로, 오류 메시지를 띄우도록 코드를 작성할 수도 있다.
 -> 재귀 함수 내에서 특정 조건일 때 더 이상 재귀적으로 함수를 호출하지 않고 종료하도록 if문을 이용하여 꼭 종료조건을 구현
2. n이 1보다 클 때 : factorial(n) = n x factorial(n-1)
"""