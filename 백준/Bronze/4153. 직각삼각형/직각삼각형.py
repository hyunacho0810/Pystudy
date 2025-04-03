# 직각 삼각형
# 인풋이 몇줄인지 몰라서 try except방법으로
while True:
    try:
        num = list(map(int, input().split()))

        # 입력이 0 0 0인 경우 종료 (문제에 따라 종료 조건이 다를 수 있음)
        if num == [0, 0, 0]:
            break

        num.sort()
        if (num[0] ** 2 + num[1] ** 2) == num[2] ** 2:
            print('right')
        else:
            print('wrong')
    except EOFError:
        break