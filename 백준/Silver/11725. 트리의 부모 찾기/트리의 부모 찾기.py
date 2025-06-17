# 트리의 부모 찾기
# BFS로 순회하면서 부모 찾기
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
parent = [0] * (N+1)
# 시작점 덱에 넣기
queue = deque([1])
visited[1] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            queue.append(neighbor)

# 2번 노드부터 부모 출력
for i in range(2, N+1):
    print(parent[i])
