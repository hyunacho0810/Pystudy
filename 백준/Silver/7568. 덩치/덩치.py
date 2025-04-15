# 덩치
N=int(input())
info=[]
for _ in range(N):
    weight,height=map(int,input().split())
    info.append((weight,height))

# 다른 방법이 떠오르지 않아서 완전탐색
# 근데 만약 사람이 엄청 많으면 어떻게 하지..(50명 이하면 괜찮나)
order=[0]*N
for i in range(N):
    count = 1 # 시작점을 1이라고 둔다.
    for j in range(N):
        if i !=j:
            if info[i][0]<info[j][0] and info[i][1]<info[j][1]:
                count+=1
    order[i]=count
print(*order)
