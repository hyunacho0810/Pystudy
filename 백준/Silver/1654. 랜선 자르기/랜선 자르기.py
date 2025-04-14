# 랜선 자르기
K,N=map(int,input().split())
cable=[]
for _ in range(K):
    cable.append(int(input()))

# 시간초과를 해결하기 위해 이진탐색
start=1
end=max(cable)
result=0

while start<=end:
    mid=(start+end)//2
    count=0

    for i in range(K):
        count+=(cable[i]//mid)
    if count>=N:
        result=mid # 현재 길이 저장
        start=mid+1 # 더 긴 길이 시도
    else:
        end=mid-1 # 더 짧은 길이 시도
print(result)
