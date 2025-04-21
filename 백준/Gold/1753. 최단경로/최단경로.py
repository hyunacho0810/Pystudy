# 최단경로
# 다익스트라=가중치가 있는 그래프에서 출발점부터 도착점까지 최단경로를 찾는 알고리즘
def dijkstra(start_node):
    pq=[(0,start_node)]
    INT=int(21e8)
    dists=[INT]*(V+1)
    dists[start_node]=0

    while pq:
        dist,node=heapq.heappop(pq)
        if dists[node]<dist:
            continue
        for next_info in graph[node]:
            next_dist=next_info[0]
            next_node=next_info[1]

            new_dist=dist+next_dist
            if dists[next_node]<=new_dist:
                continue
            dists[next_node]=new_dist
            heapq.heappush(pq,(new_dist,next_node))
    return dists

import heapq
V,E=map(int,input().split()) # V개의 정점과 E개의 간선
K=int(input()) # 시작 정점 번호
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
result=dijkstra(K)
for i in range(1,V+1):
    if result[i]==int(21e8):
        print('INF')
    else:
        print(result[i])


