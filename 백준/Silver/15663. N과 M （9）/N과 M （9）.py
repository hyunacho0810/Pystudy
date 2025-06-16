# N과 M(9)
def recur(cnt):
    if cnt == M:
        print(*path)
        return

    prev = -1  # 이전에 사용한 값을 기록
    for i in range(N):
        # 이전과 같으면 안된다. 
        if visited[i] or num_list[i] == prev:
            continue

        visited[i] = True
        path.append(num_list[i])
        prev = num_list[i] # 업데이트
        recur(cnt + 1)
        path.pop()
        visited[i] = False

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
path = []
visited = [False] * N
recur(0)