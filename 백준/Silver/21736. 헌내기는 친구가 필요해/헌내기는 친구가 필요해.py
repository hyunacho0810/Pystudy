# 헌내기는 친구가 필요해
# 처음에는 도연이가 위치 이동을 하지 않는다고 생각을 하고 매우 간단한 델타인줄 알았으나
# 자세히 보니 미로찾기랑(DFS) 비슷한 문제이다.

# 도연이를 찾는
def find_me(arr,N,M):
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='I':
                return i,j

def DFS(i,j,N,M):
    global count
    visited=[[0]*M for _ in range(N)]
    stack=[]

    while True:
        visited[i][j]=1
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj]!='X' and visited[ni][nj]==0:
                if arr[ni][nj]=='P':
                    count+=1
                stack.append((i,j))
                i,j=ni,nj
                break
        else:
            if stack:
                i,j=stack.pop()
            else:
                break
    return 0

count=0
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
me_i,me_j=find_me(arr,N,M)
DFS(me_i,me_j,N,M)

if count==0:
    print('TT')
else:
    print(count)

