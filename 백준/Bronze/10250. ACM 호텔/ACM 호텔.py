# ACM 호텔
T=int(input())
for tc in range(1,T+1):
    H,W,N=map(int,input().split())

    floor=N % H

    if floor==0:
        floor=H
        room=N//H
        if room>=10:
            print(f'{floor}{room}')
        else:
            print(f'{floor}0{room}')

    else:
        floor = N % H
        room = N // H + 1
        if room>=10:
            print(f'{floor}{room}')
        else:
            print(f'{floor}0{room}')


