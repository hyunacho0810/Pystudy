# 평범한 베낭
N,K=map(int,input().split())
arr=[]
for _ in range(N):
    W,V=map(int,input().split())
    arr.append((W,V))

# DP를 이용해서 문제 풀기
# 열은 무게, 행은 물건
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 물건 하나하나에 대해 살펴보기
for i in range(1,N+1):
    weight,value=arr[i-1]

    for j in range(1,K+1):
        # 현재 물건을 넣을 수 없는 경우
        if weight>j:
            # 이전 상태의 최대 가치 가져오기
            dp[i][j]=dp[i-1][j]
        # 넣을 수 있는 경우(넣거나 넣지 않거나 중 최댓값 선택)
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)

print(dp[N][K])
