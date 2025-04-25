# 구간 한 구하기 4
N,M=map(int,input().split())
nums=list(map(int,input().split()))

# 시간초과를 잡기 위해 중간 계산 값을 저장
calculated_sum=[0]*(N+1)
for i in range(N):
    calculated_sum[i+1]=calculated_sum[i]+nums[i]

for _ in range(M):
    start,end=map(int,input().split())
    print(calculated_sum[end]-calculated_sum[start-1])