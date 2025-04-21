# 로봇 청소기
N,M=map(int,input().split())
i,j,d=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]

# 현재 칸이 청소되지 않은 경우, 현재 칸 정소
# 현재 칸의 주변 4 방향이 모두 청소 된 경우 바라보는 방향을 유지한 채로 뒤로 한칸 후진
# 뒤쪽 칸이 벽이라서 후진을 못하면 끝
# 4 방향중 청소되지 않은 칸이 있는 경우, 반시계 방향으로 90도 회전한 후, 해당 방향으로 간다.

clean=0 # 청소한 칸 수

# 북, 동, 남, 서 순서로
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

while True:
    # 만약 청소되지 않은 빈칸이면 청소를 한다.
    if arr[i][j]==0:
        arr[i][j]=2 # 청소 완료 표시
        clean+=1

    # 만약 현재 위치는 깨끗하다면 주변의 4 칸을 확인한다. (반시계 방향으로)
    cleaned=True
    for m in range(4):
        # 반시계 방향으로 확인
        nd = (d + 3 -m) % 4
        ni,nj=i+di[nd],j+dj[nd]
        # 범위 내에 있고, 청소하지 않은 칸이면 
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
            # 청소 할 칸이 있으면
            # 반시계 방향으로 회전
            d=nd
            i,j=ni,nj
            cleaned=False
            break

    # 4방향에 청소할 칸이 없으면(break문에 걸리지 않는 경우)
    if cleaned:
        # 후진 방향
        back_d=(d+2)%4
        ni,nj=i+di[back_d],j+dj[back_d]

        # 후진할 수 있는 경우(범위 내에 있고 벽이 아니면)
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]!=1:
            i,j=ni,nj
        else:
            break
print(clean)