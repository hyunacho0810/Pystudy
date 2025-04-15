# 소수 구하기
M,N=map(int,input().split())

for j in range(M,N+1):
    if j==1: # 1은 소수가 아님
        continue
    is_prime=True
    # 소수를 판별하려면 2부터 해당 숫자의 제곱근까지 살펴보면 된다.
    for k in range(2,int(j**0.5)+1):
        if j%k ==0: # 하나라도 나누어 떨어지면 소수가 아님
            is_prime=False
            break
    if is_prime:
        print(j)


