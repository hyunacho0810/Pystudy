# 국회의원 선거
def vote(numbers,N):
    for i in range(1,N):
        if numbers[0]<=numbers[i]:
            # 다른 사람이 더 큰 득표수를 가지면 False반환
            return False
    # 아니면 True 반환
    return True

N=int(input())
numbers=[]
for _ in range(N):
    num=int(input())
    numbers.append(num)

count=0
result = vote(numbers, N)

while not result:
    max_idx=1 # 초기화
    for i in range(1,N):
        if numbers[i]>numbers[max_idx]:
            max_idx=i
    numbers[0] += 1
    numbers[max_idx] -= 1
    count += 1

    result = vote(numbers, N)

print(count)