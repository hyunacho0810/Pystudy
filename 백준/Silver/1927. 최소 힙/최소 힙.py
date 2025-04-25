# 최소 힙
N=int(input())
nums=[int(input()) for _ in range(N)]

import heapq
min_heap=[]
for num in nums:
    if num!=0:
        heapq.heappush(min_heap,num)
    else:
        if len(min_heap)==0:
            print(0)
        else:
            result=heapq.heappop(min_heap)
            print(result)