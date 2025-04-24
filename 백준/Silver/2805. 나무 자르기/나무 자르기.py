# 나무 자르기
N,M=map(int,input().split())
trees=list(map(int,input().split()))

# 시간 초과를 방지하기 위해 이진탐색
start=0
end=max(trees)
answer=0
while start<=end:
    mid=(start+end)//2
    result=0

    for j in range(N):
        if trees[j]>mid:
            result+=(trees[j]-mid)
    if result>=M:
        answer=mid # 가능한 결과 저장 후
        # 더 높은 높이 탐색
        start=mid+1
    else:
        end=mid-1
print(answer)
