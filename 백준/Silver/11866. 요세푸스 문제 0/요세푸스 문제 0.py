# 요세푸스 문제 0
N,K=map(int,input().split())
circle=[]
for i in range(1,N+1):
    circle.append(i)

result=[]
count=0
idx=0
while circle: # 원이 비어있지 않은 동안
    idx=(idx+K-1)%len(circle)
    result.append(circle[idx])
    circle.remove(circle[idx])
print('<',end='')
for i in range(N):
    if i !=N-1:
        print(result[i],end=', ')
    else:
        print(result[i],end='')
print('>')
