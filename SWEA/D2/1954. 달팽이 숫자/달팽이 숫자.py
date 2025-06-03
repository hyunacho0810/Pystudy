T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 오른쪽, 아래, 왼쪽, 위 
    answer = [[0] * N for _ in range(N)]
    num = 1
    idx = 0
    i, j = 0, -1
    
    while num <= (N * N):
        ni, nj = i + dir[idx][0], j + dir[idx][1]
        if 0 <= ni < N and 0 <= nj < N and answer[ni][nj] == 0:
            answer[ni][nj] = num
            i, j = ni, nj
            num += 1
        else:
            idx = (idx + 1) % 4    
    
    print(f"#{test_case}")
    for row in answer:
        print(*row)