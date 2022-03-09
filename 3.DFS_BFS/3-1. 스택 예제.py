"""
탐색(Search)란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미
자료구조(Data Structure)란 데이터를 표현하고 관리하고 처리하기 위한 구조
스택과 큐
- 삽입(Push): 데이터를 삽입한다.
- 삭제(Pop) : 데이터를 삭제한다.
오버플로(Overflow) : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할때 발생
언더플로(Underflow) : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태일때 발생

"""
#스택(Stack) : 선입후출(First in Last Out) 구조 또는 후입 선출(Last in First Out) 구조라고 한다.
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) -삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력 / 음의 간격 스탭 리스트를 뒤집는 것과 같은 결과

"""
슬라이싱 참고자료
https://codetorial.net/tips_and_examples/list_slicing.html
"""

#정렬
stack.sort() # 오름차순 정렬
print(stack)

stack.sort(reverse=True) # 내림차순 정렬
print(stack)

stack.reverse() # 단순히 현재 상태에서 뒤집는다. 즉 정렬이 실행되지 않고 현재 상태에서 그대로 순서를 뒤집어줌
print(stack)