# DFS와 BFS
def dfs(S,N): # 시작점, 정점의 개수
    visited=[0]*(N+1)
    stack=[]
    route = [S]  # 시작 노드를 경로에 추가

    while True:
        visited[S]=1
        for w in adj_list[S]:
            if visited[w]==0:
                stack.append(S)
                S=w
                route.append(S)
                break
        else:
            if stack:
                S=stack.pop()
            else:
                return route

def bfs(S,N):
    visited = [0] * (N + 1)
    queue=[]
    queue.append(S)
    visited[S]=1
    route=[S]

    while queue:
        t=queue.pop(0)
        for w in adj_list[t]:
            if visited[w]==0:
                queue.append(w)
                route.append(w)
                visited[w]=1
    return route


N,M,V=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(M)]
adj_list=[[] for _ in range(N+1)] # 2차원 배열로 저장
for i in range(M):
    start,end=graph[i][0],graph[i][1]
    adj_list[start].append(end) # 양방향 간선이므로
    adj_list[end].append(start)

# 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in range(1, N+1):
    adj_list[i].sort()

print(*dfs(V,N))
print(*bfs(V,N))
