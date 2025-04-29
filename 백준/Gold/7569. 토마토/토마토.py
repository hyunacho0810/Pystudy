# 토마토
# 3차원 인덱스+BFS
def bfs(queue, arr, ripe, yes_tomato):
    count_days = 0

    while queue:  # 익은 토마토가 주위의 것을 다 익게 할때까지
        h,i, j, days = queue.popleft()
        count_days = max(count_days, days)

        # 동서남북
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # 범위 내에 있고 익지 않으면
            if 0 <= ni < N and 0 <= nj < M and arr[h][ni][nj] == 0:
                arr[h][ni][nj] = 1  # 익음 처리
                queue.append((h,ni, nj, days + 1))
                ripe += 1  # 하나씩 익음 처리

        # 상하
        for dh in [1,-1]:
            nh=h+dh
            if 0<=nh<H and arr[nh][i][j] == 0:
                arr[nh][i][j] = 1  # 익음 처리
                queue.append((nh, i, j, days + 1))
                ripe += 1  # 하나씩 익음 처리
    return count_days, ripe


from collections import deque
M,N,H=map(int,input().split())
arr=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
# 가장 낮은 층을 먼저 위치하게 하고 싶어서
# 이렇게 하면 1층->2층-> 3층 이렇게 저장된다.
arr.reverse()

# 익은 토마토의 위치를 큐에
queue=deque()
yes_tomato=0
ripe=0
count_days=0

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j]==1:
                queue.append((h,i,j,0)) # 위치, 일수
                ripe+=1
            if arr[h][i][j]!=-1: # 빈칸을 제외하고 토마토가 있는 칸
                yes_tomato+=1

# 모든 칸의 토마토가 다 익은 경우
if ripe==yes_tomato:
    print(0) # 0일 걸림
else:
    count_days, ripe = bfs(queue, arr, ripe, yes_tomato)
    if ripe == yes_tomato:  # 모든 토마토가 익은 경우
        print(count_days)
    else:
        print(-1)