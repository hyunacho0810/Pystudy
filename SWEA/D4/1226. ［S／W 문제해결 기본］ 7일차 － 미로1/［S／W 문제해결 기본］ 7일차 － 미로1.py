# 미로 1
# 시작점 찾는 함수
def start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j]==2:
                return i,j


def dfs(i,j):
    visited=[[0]*16 for _ in range(16)]
    stack=[]

    while True:
        visited[i][j]=1 # 시작점 방문표시
        if arr[i][j]==3:
            return 1 # 방문할 수 있음을 프린트
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj=i+di,j+dj
            # 범위 내에서 이동하며 길이고 방문한적 없으면
            if 0<=ni<16 and 0<=nj<16 and arr[ni][nj]!=1 and visited[ni][nj]==0:
                stack.append((ni,nj))
                i,j=ni,nj # 다음 위치로 이동
                break
        else: # 더 이상 갈 수 없을 때
            if stack:
                i,j=stack.pop() # 백트래킹 
            else:
                break
    return 0 # 도착점에 도달할 수 없는 경우

T=10
for tc in range(1,11):
    test_case_num=int(input())
    arr=[]
    for _ in range(16):
        line=input() # 문자열로 입력받기
        row=[int(num) for num in line]
        arr.append(row)

    # 시작점에서 도착점까지 갈 수 있는지를 판단하는 문제이므로 DFS 사용
    sti,stj=start(arr)
    result=dfs(sti,stj)
    print(f'#{tc} {result}')