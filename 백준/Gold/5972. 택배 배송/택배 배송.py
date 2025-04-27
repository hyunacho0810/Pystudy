# 택배 배송
# 1부터 N까지 가는데 드는 최소 여물-> 다익스트라
def dijkstra(start):
    pq=[(0,start)]
    INF = int(21e9)
    dists=[INF]*(N+1)
    dists[start]=0

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

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    A,B,C=map(int,input().split())
    graph[A].append((C,B))
    graph[B].append((C,A))

import heapq
result=dijkstra(1)
print(result[N])

