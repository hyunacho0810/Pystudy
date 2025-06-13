# N과M (5)
def recur(cnt):
    if cnt==M:
        print(*path)
        return
    for i in range(N):
        if used[i] is True:
            continue
        used[i]=True
        path.append(nums[i])
        recur(cnt+1)
        path.pop()
        used[i] = False

N,M=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
path=[]
used=[False]*N
recur(0)