# 카드 2
# 시간초과를 해결하기 위해 덱 사용
from collections import deque
N=int(input())
numbers=deque()
for i in range(1,N+1):
    numbers.append(i)
while len(numbers)>1: # 한장 남을 때 까지
    numbers.popleft() # 가장 위의 카드 버리기
    first=numbers[0]
    numbers.popleft() # 두번째 카드도 버리고
    numbers.append(first) # 이거는 뒤에 붙이기
print(*numbers)
