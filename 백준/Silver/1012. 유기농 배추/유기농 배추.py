# 유기농 배추
def DFS(i,j):
    arr[i][j] = 0 # DFS를 돌때마다 해당 칸을 0으로 치환한다.

    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]==1:
            DFS(ni,nj)


T=int(input())
for tc in range(1,T+1):
    M,N,K=map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    for _ in range(K):
        y,x=map(int,input().split())
        arr[x][y]=1

    count_snail=0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:  # 배추를 발견하면
                DFS(i, j)  # 그 배추와 연결된 모든 배추를 방문 처리
                count_snail += 1  # 하나의 그룹 처리 완료, 지렁이 카운트 증가

    print(count_snail)




# 이렇게 하면 거의 모든 테스트케이스에서 맞는데 
# U이런 모양으로 생길경우 2개라고 카운트하는 문제가 있다.
# T=int(input())
# for tc in range(1,T+1):
#     M,N,K=map(int,input().split())
#     arr=[[0]*M for _ in range(N)]
#     for _ in range(K):
#         y,x=map(int,input().split())
#         arr[x][y]=1
#
#     count_snail=0
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j]==1:
#                 # 4방향을 다 탐색했는데 이미 앱벌레를 놓은 영역이다.
#                 for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#                     ni,nj=i+di,j+dj
#                     if 0<=ni<N and 0<=nj<M:
#                         if arr[ni][nj]==9:
#                             arr[i][j]=9
#                             break
#                 # 아직 애벌레를 놓지 못한 영역이다.
#                 else:
#                     count_snail+=1
#                     arr[i][j]=9
#
#     print(count_snail)



