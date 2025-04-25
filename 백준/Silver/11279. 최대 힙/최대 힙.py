# 최대 힙
N=int(input())
nums=[int(input()) for _ in range(N)]

# 파이썬에서 힙은 최소힙으로 구현이 되어있으므로
# -로 입력한 후 꺼낼때 -를 또 붙이는 방법으로
import heapq
max_heap=[]
for num in nums:
    if num!=0:
        heapq.heappush(max_heap,num*(-1))
    else:
        if len(max_heap)==0:
            print(0)
        else:
            result=heapq.heappop(max_heap)
            print(result*(-1))