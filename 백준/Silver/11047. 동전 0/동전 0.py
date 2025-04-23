# 동전 0
N,K=map(int,input().split())
coin=[]
for _ in range(N):
    coin.append(int(input()))

# 동전의 숫자가 다 배수를 이루고 있으므로
# 간단하게 가장 큰 수부터 살펴보면 되겠다
count=0
for i in range(N-1,-1,-1):
    count+=K//coin[i]
    K-=coin[i]*(K//coin[i])
print(count)