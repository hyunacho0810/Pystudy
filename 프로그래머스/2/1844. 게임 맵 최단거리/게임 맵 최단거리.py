def solution(maps):
    from collections import deque
    answer = 0
    N=len(maps) # 행
    M=len(maps[0]) # 열
    
    def BFS(i,j,N,M):
        dq=deque([(i,j)]) # 첫번째 좌표 입력
        visited=[[0]*M for _ in range(N)]
        visited[i][j]=1
        
        while dq:
            ti,tj=dq.popleft()
            if ti==N-1 and tj==M-1:
                return visited[ti][tj]
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni,nj=ti+di,tj+dj
                if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and maps[ni][nj]==1:
                    dq.append((ni,nj))
                    visited[ni][nj]=visited[ti][tj]+1
        return -1
    
    answer=BFS(0,0,N,M)    
        
    return answer