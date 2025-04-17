# 빵집
# 시작점부터 도착점까지 갈 수 있는 경로의 개수 -> DFS
def dfs(sti,stj):
    stack = [(sti, stj)]

    while stack:
        i, j = stack.pop()
        visited[i][j]=1

        if j == C - 1:
            return 1
        # 오른쪽 위, 오른쪽, 오른쪽 아래 순서
        for di,dj in [[1, 1], [0, 1], [-1, 1]]:
            ni, nj = i + di, j + dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj]=='.' and visited[ni][nj]!=1:
                stack.append((ni,nj))
    return 0



R,C=map(int,input().split())
arr=[list(input()) for _ in range(R)]

result=0 # 경로의 개수 초기화
visited = [[0] * C for _ in range(R)]

# 모든 가능한 시작점 좌표에서 dfs돌리고
for i in range(R):
    if arr[i][0]=='.':
        result+=dfs(i,0)

# 값을 누적해서 더하기
print(result)