# 미로 탐색
# 시작점에서 도착점까지 이동해야할 때 거쳐가야하는 최소한의 칸 수
# -> BFS

def BFS(start_i,start_j):
    queue=deque()
    visited=[[0]*M for _ in range(N)]
    # 시작점도 한칸이라고 고려
    queue.append((start_i,start_j,1)) # 시작점과, 이동한 칸 수

    while queue: # 큐에 원소가 있는 동안
        i,j,count=queue.popleft()

        if i==N-1 and j==M-1:
            return count

        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni,nj=i+di,j+dj
            # 범위 내에 있고 이동할 수 있는 칸이면
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='1' and visited[ni][nj]==0:
                queue.append((ni,nj,count+1))
                visited[ni][nj]=1

    return 0


from collections import deque

N,M=map(int,input().split())
# 수들이 붙어서 나오므로 그냥 문자열로 간주
arr=[list(input()) for _ in range(N)]
print(BFS(0,0))