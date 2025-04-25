# 1로 만들기
# 시간이 0.15초로 매우 짧다
def bfs(start,end):
    q=deque([(start,0)]) # 숫자, 연산 횟수
    visited=[0]*(end * 3 + 1)
    visited[start] = 1

    while q:
        loc,cnt=q.popleft()
        if loc==end:
            return cnt
        # 해당 숫자를 계산한 적 있으면 패스
        # 3곱하기
        next_loc=loc*3
        if next_loc<=end and visited[next_loc]!=1:
            visited[next_loc]=1
            q.append((next_loc,cnt+1))

        # 2곱하기
        next_loc = loc * 2
        if next_loc<=end and visited[next_loc]!=1:
            visited[next_loc]=1
            q.append((next_loc,cnt+1))

        # 1더하기
        next_loc = loc +1
        if next_loc<=end and visited[next_loc]!=1:
            visited[next_loc]=1
            q.append((next_loc,cnt+1))




from collections import deque
import sys
N=int(sys.stdin.readline())

# BFS 방법으로 풀어보기
result=bfs(1,N)
print(result)

