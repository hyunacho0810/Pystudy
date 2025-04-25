# 피보나치 함수
# 제한시간이 0.25초로 매우 짧다.
# 재위로 하면 시간초과가 나기에 O(2^n) DP로 해야한다.
# 한번 구한 값은 다시 계산하지 않고 저장. (메모이제이션?)

def fibo(n):
    # 이미 구한 값이면
    if n < len(memo) and memo[n] != (0, 0):
        return memo[n]
    if n==0:
        # (0의 횟수,1의 횟수)
        memo[n]=(1,0)
    elif n==1:
        memo[n]=(0,1)
    else:
        a = fibo(n - 1)
        b = fibo(n - 2)
        # 0 호출 횟수의 합, 1호출 횟수의 합
        memo[n] = (a[0] + b[0], a[1] + b[1])
    return memo[n]

# 시간초과를 줄이기 위해 입출력도 효율적인 방법으로 수정
import sys
T=int(sys.stdin.readline())
for tc in range(1,T+1):
    N=int(sys.stdin.readline())
    memo=[(0,0)]*(N+1) # 값, 횟수를 저장할 리스트 생성
    memo[0] = (1, 0)
    if N >= 1:
        memo[1] = (0, 1)

    result=fibo(N)
    print(f'{result[0]} {result[1]}')
