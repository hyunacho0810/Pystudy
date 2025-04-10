# 블랙잭
N,M=map(int,input().split())
arr=list(map(int,input().split()))

# 3개의 카드를 골라서 M가 최대한 가까운 큰 수를 만들기
# 일단 큰 순서대로 sort하기
arr.sort(reverse=True)

result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum=arr[i]+arr[j]+arr[k]
            if sum>M:
                continue
            if sum<=M and sum>result:
                result=sum
print(result)




