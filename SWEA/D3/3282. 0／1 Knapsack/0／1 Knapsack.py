T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split()) # N개의 물건, K의 부피
    V=[0]*(N+1) # 부피 Vi,
    C=[0]*(N+1) # 가치 Ci
    for i in range(1,N+1):
        V[i],C[i]=map(int,input().split())
 
    # dp[i][j]: i물건까지 고려해 부피 j를 채웠을 때의 최대 가치
    dp=[[0]*(K+1) for _ in range(N+1)]
    # 행(i): 고려하는 물건의 번호 (0~N)
    # 열(j): 배낭의 현재 부피 (0~K)
    for i in range(1,N+1):
        for j in range(1,K+1):
            if V[i]>j: # 베낭보다 물건이 큰 경우
                dp[i][j]=dp[i-1][j] # 이전 상태(i-1)의 최대 가치 가져오기
            else:
                # 현재 물건을 배낭에 넣을 수 있는 경우
                # 이전 상태의 최대 가치 VS 현재 물건을 넣는 경우의 최대가치
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-V[i]]+C[i])
    print(f'#{tc} {dp[N][K]}')