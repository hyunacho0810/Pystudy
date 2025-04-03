# 웰컴 키트
N=int(input())
size=list(map(int,input().split()))
T,P=map(int,input().split())
cnt=0
for i in range(6):
    if size[i]%T==0:
        cnt+=size[i]//T
    else:
        cnt+=((size[i]//T)+1)
print(cnt)
print(N//P, end=' ')
print(N%P)