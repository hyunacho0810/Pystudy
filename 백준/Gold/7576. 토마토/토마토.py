# 토마토
# 최소 일수를 구하는 문제이므로 BFS
def bfs(queue, arr, ripe, yes_tomato):
    count_days = 0

    while queue:  # 익은 토마토가 주위의 것을 다 익게 할때까지
        i, j, days = queue.popleft()
        count_days = max(count_days, days)

        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            # 범위 내에 있고 익지 않으면
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                arr[ni][nj] = 1  # 익음 처리
                queue.append((ni, nj, days + 1))
                ripe += 1  # 하나씩 익음 처리

    return count_days, ripe


from collections import deque

M,N=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

# 익은 토마토의 위치를 큐에 넣기
queue=deque()
yes_tomato=0
ripe=0
count_days=0
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            queue.append((i,j,0)) # 위치, 일수
            ripe+=1
        if arr[i][j]!=-1: # 빈칸을 제외하고 토마토가 있는 칸
            yes_tomato+=1

# 모든 칸의 토마토가 익은 경우
if ripe==yes_tomato:
    print(0) # 0일 걸림
else: # 그러지 않은 경우
    count_days, ripe = bfs(queue, arr, ripe, yes_tomato)
    if ripe == yes_tomato:  # 모든 토마토가 익은 경우
        print(count_days)
    else:
        print(-1)
