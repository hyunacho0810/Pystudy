# 차윤이의 RC 카
# 상(0), 우(1), 하(2), 좌(3)
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 상, 우, 하, 좌

def start_end(grid, N):
    sx, sy, ex, ey = -1, -1, -1, -1
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'X':
                sx, sy = i, j
            if grid[i][j] == 'Y':
                ex, ey = i, j
    return sx, sy, ex, ey

def turn_left(d):
    return (d-1)%4

def turn_right(d):
    return (d+1)%4

def move_car(arr,N,sti,stj,endi,endj,command):
    x,y=sti,stj
    d=0 # 처음은 상

    # 명령어 시퀀스를 모두 수행
    for c in command:
        if c == 'L':
            d = turn_left(d)
        elif c == 'R':
            d = turn_right(d)
        elif c == 'A':
            nx = x + directions[d][0]
            ny = y + directions[d][1]
            # 영역 안에 있고 나무가 아니면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 'T':
                x, y = nx, ny  # 새로운 좌표 설정

    # 목적지에 도달했는지 확인
    if x == endi and y == endj:
        return 1
    return 0 # 도착지에 도달하지 못한경우


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    Q=int(input()) # 조종을 한 횟수
    commands = []
    for _ in range(Q):
        line=input()
        commands.append(line[2:]) # 명령어 알파벳만 리스트에 저장

    sti,stj,endi,endj=start_end(arr,N)
    print(f'#{tc}',end=' ')
    for cmd in range(Q):
        current_command=commands[cmd]
        result=move_car(arr,N,sti,stj,endi,endj,current_command)
        print(result, end=' ')
    print() # 한 테케가 씉나면 줄바꿈 