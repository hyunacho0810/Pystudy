# N과 M(2)
# 재귀?
def recur(cnt,start):
    if cnt==M:
        print(*path)
        return
    for i in range(start,N+1):
        path.append(i)
        recur(cnt+1,i+1)
        path.pop()

N,M=map(int,input().split())
path=[]
recur(0,1)

