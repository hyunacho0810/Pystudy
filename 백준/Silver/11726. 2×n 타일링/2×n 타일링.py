# 이거는 SWEA에서 본 재귀문제!
# n이 1000이지만, 연습 겸, 재귀의 결과를 저장하기
def recur(n):
    # 해당 값을 구하지 않았으면
    if memo[n]!=0:
        return memo[n]

    memo[n]=(recur(n-1)+recur(n-2))%10007
    return memo[n]

    
N=int(input())
memo=[0]*(N+1)
if N >= 1:
    memo[1] = 1
if N >= 2:
    memo[2] = 2
print(recur(N))