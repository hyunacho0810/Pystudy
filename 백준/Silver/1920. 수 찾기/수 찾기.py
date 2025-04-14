# 수 찾기
N=int(input())
# 시간초과를 방지하기 위해 세트로 
numbers=set(map(int,input().split()))
M=int(input())
goal=list(map(int,input().split()))

for j in range(M):
    if goal[j] in numbers:
        print(1)
    else:
        print(0)