# 제로
K=int(input())
numbers=[]
for _ in range(K):
    number=int(input())
    numbers.append(number)
sum=0
stack=[]
for i in range(K):
    if numbers[i] !=0:
        stack.append(numbers[i])
    else: # 0이면
        # 0은 항상 첫번째로 오지 않는다고 하므로 추가 조건 필요 없음.
        stack.pop()

for i in range(len(stack)):
    sum+=stack[i]
# print(stack)
print(sum)
