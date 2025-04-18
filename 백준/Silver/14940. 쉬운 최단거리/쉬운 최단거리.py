# 쉬운 최단거리
# 각 지점에서 목표지점까지의 거리를 출력하기 ->BFS
# 모든 지점에서 계산하기에는 시간초과가 날 것 같으니 중간값을 visited에  저장해서 사용하는 방향으로
def find_goal(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j]==2:
                return i,j

def BFS(start_i,start_j):
    global visited
    queue=deque()
    queue.append((start_i,start_j))
    visited[start_i][start_j]=0

    while queue:
        i,j=queue.popleft()
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni,nj=i+di,j+dj
            # 범위 내에 있고 갈 수 있으며 아직 방문하지 않은 곳
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==1 and visited[ni][nj]==-1:
                queue.append((ni,nj))
                visited[ni][nj]=visited[i][j]+1  # 이전 위치의 거리 + 1

    for i in range(N):
        for j in range(M):
            if arr[i][j]==0: # 벽
                visited[i][j]=0


from collections import deque
N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
# 그냥 반대로 목표지점에서 각 좌표까지의 거리라고 하면 되겠다.
visited=[[-1]*M for _ in range(N)]

goal_i,goal_j=find_goal(arr)
BFS(goal_i,goal_j)

for i in range(N):
    print(*visited[i])  # 각 행을 공백으로 구분하여 출력