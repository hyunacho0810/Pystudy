# 인덱스로 접근한 방법
N=int(input())
T=int(input())
hand = list(map(int, input().split()))
call=list(map(int,input().split()))
i=0

for c in call:
    # 참가자가 손을 빼지 않으므로 누가 패배하는지만 알면 된다.
    # i에 값은 누적해서 이전 게임에서부터 연속해서 진행함을 구현
    i+=(c-1) # 몇 번 이동해야하는지
    if i>=len(hand):
        i%=len(hand)
        print(hand[i],end=' ')
    else:
        print(hand[i],end=' ')