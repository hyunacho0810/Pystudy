# 주사위 굴리기
# 1: 동쪽(동), 2: 서쪽(서), 3: 북쪽(북), 4: 남쪽(남)
def roll_dice(direction):
    global dice
    temp = dice[:]

    # 동쪽으로 굴리기
    if direction == 1:
        dice[0] = temp[3]
        dice[2] = temp[0]
        dice[5] = temp[2]
        dice[3] = temp[5]

    # 서쪽으로 굴리기
    elif direction == 2:
        dice[0] = temp[2]
        dice[3] = temp[0]
        dice[5] = temp[3]
        dice[2] = temp[5]

    # 북쪽으로 굴리기
    elif direction == 3:
        dice[0] = temp[4]
        dice[1] = temp[0]
        dice[5] = temp[1]
        dice[4] = temp[5]

    # 남쪽으로 굴리기
    elif direction == 4:
        dice[0] = temp[1]
        dice[4] = temp[0]
        dice[5] = temp[4]
        dice[1] = temp[5]


N,M,x,y,K=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
order=list(map(int,input().split()))

# 0(윗면), 1(북쪽면), 2(동쪽면), 3(서쪽면), 4(남쪽면), 5(바닥면)
dice=[0]*6 # 주사위의 6개 면

for i in range(K):
    nx, ny = x, y
    if order[i]==1: # 동
        ny=y+1
    elif order[i]==2: # 서
        ny=y-1
    elif order[i]==3: # 북
        nx=x-1
    else: # 남
        nx=x+1

    # 범위를 벗어나면
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    # 범위 내에 있으면
    x, y = nx, ny
    roll_dice(order[i])

    # 칸의 값이 0이면 주사위 바닥면의 값을 칸에 복사
    if arr[x][y]==0:
        arr[x][y] = dice[5]
    # 아니면
    else:
        dice[5] = arr[x][y]
        arr[x][y]=0

    print(dice[0])

