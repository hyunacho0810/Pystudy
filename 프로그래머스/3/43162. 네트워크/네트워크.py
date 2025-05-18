def solution(n, computers):
    answer = 0
    visited=[False]*n
    
    def DFS(node):
        visited[node]=True
        # 인접노드 확인
        for i in range(n):
            if computers[node][i]==1 and not visited[i]:
                DFS(i) # 해당 노드로 dfs 수행
    
    # 모든 노드에 대해 dfs 수행
    for i in range(n):
        # 아직 방문하지 않은 노드라면
        if not visited[i]:
            DFS(i) 
            answer+=1
            
    return answer