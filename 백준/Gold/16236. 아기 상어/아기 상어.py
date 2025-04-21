# 아기상어
# A형 대비. 최종 코드. 예전에 비해 훨씬 코드가 깔끔해져서 매우 뿌듯하다. 

# 비어있거나, 자기보다 크기가 작거나 같은 칸을 지나갈 수 있다.
# 자기보다 크기가 작은 물고기만 먹을 수 있다.
# 먹을 수 있는 물고기가 한마리라면 그 물고기를 먹으러 간다
# 1마리 이상이라면 그 중 가장 가까운(BFS) 물고기를 먹으러 간다.
# 같은 거리인 물고기가 여러개라면 가장 위, 가장 왼쪽 물고기를 먹으러 간다. (i,j)
# 아기 상어는 자신의 크기만큼 물고기를 먹으면 크기가 1 증가한다.
# 더 이상 먹을 수 있는 물고기가 없으면 엄마상어에게 도움 요청
# 0:빈칸, 1~6: 물고기의 크기, 9:아기 상어의 위치
def find_shark(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j]=0 # 해당 위치를 0으로 변경
                return i, j


def find_fish(i,j,size,arr, N):
    # 현재 위치로부터 가장 가까운 순서대로 먹을 수 있는 물고기를 리스트? 스택에 입력
    queue = deque()
    visited=[[False]*N for _ in range(N)]
    queue.append((i,j,0)) # 행, 열, 거리
    visited[i][j]=True
    can_eat=[] # 먹을 수 있는 물고기 후보군
    min_dist = None

    while queue:
        i,j,dist=queue.popleft()

        # 왼쪽 위부터 시계방향
        for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
            ni,nj=i+di,j+dj
            # 범위 안에 있고 방문한 적 없으면
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                # 지나갈 수 있으면
                if arr[ni][nj]<=size:
                    visited[ni][nj]=True
                    # 먹을 수 있으면
                    if 0<arr[ni][nj]<size:
                        can_eat.append((dist+1,ni,nj)) # 먹을 수 있는 물고기 후보군에 추가
                    else:
                        # 먹을 수 없는 경우에만 경로에 추가
                        queue.append((ni, nj, dist + 1))

    # 먹을 수 있는 물고기가 있는 경우
    if can_eat:
        can_eat.sort() # 거리, 행, 열 순으로
        return can_eat[0] # 제일 빨리 먹을 수 있는 물고기 리턴
    # 먹을 수 있는 물고기가 없는 경우
    else:
        return None

# 위의 두 함수를 합쳐서
def eat(N,arr):
    sti,stj=find_shark(arr,N)
    size=2 # 초기 사이즈
    count=0 # 먹은 물고기 수
    time=0 # 총 이동한 시간

    while True:
        result=find_fish(sti,stj,size,arr,N)
        # 먹을 수 있는 물고기가 없으면
        if result is None:
            break
        # 먹을 수 있는 물고기가 있으면 물고기를 먹으러 이동
        dist,next_i,next_j=result
        time+=dist
        arr[next_i][next_j]=0 # 해당 위치를 0으로 초기화
        count+=1

        if size==count:
            size+=1 # 사이즈는 커지고
            count=0 # count는 초기화

        sti,stj=next_i,next_j
    return time


from collections import deque
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
print(eat(N,arr))