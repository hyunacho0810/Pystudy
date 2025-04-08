# 미세먼지 안녕!
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]


def device():
    idx = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                idx.append(i)
    # 항상 1열에 있으므로 행 위치만 반환
    return idx[0], idx[1]


def runmachine():
    up, down = device()

    # 위쪽 공기청정기(반시계)
    # 직사각형의 왼쪽 선분
    for i in range(up - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    # 직사각형의 윗쪽 선분
    for j in range(0, C - 1):
        arr[0][j] = arr[0][j + 1]
    # 직사각형의 오른쪽 선분
    for i in range(0, up):
        arr[i][C - 1] = arr[i + 1][C - 1]
    # 직사각형의 아래쪽 선분
    for j in range(C - 1, 1, -1):
        arr[up][j] = arr[up][j - 1]
    arr[up][1] = 0  # 공기청정기에서 나오는 바람

    # 아래쪽 공기청정기(시계)
    # 1. 왼쪽 선분
    for i in range(down + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    # 2. 아래쪽 선분
    for j in range(0, C - 1):
        arr[R - 1][j] = arr[R - 1][j + 1]
    # 3. 오른쪽 선분
    for i in range(R - 1, down, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    # 4. 위쪽 선분
    for j in range(C - 1, 1, -1):
        arr[down][j] = arr[down][j - 1]
    arr[down][1] = 0  # 공기청정기에서 나오는 바람


time = 0
while time < T:
    # 새로운 배열
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                temp[i][j] = -1  # 새로운 배열에 공기 청정기 위치 저장

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                spread_count = 0
                spread_amount = arr[i][j] // 5
                # 확산될 수 있는 방향으로 확산하기.
                for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        temp[ni][nj] += spread_amount  # 확산 된 값 더하기
                        spread_count += 1
                temp[i][j] += arr[i][j] - (spread_amount * spread_count)  # 남은 양

    arr = temp  # 배열 업데이트
    runmachine()
    time += 1

# 결과 출력
result = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            result += arr[i][j]

print(result)