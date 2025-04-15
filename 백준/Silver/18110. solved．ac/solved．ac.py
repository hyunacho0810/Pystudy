# solved.ac
# 파이썬의 경우 round함수는 사사오입
# 즉 round 2.5는 2, round 3.5는 4 이렇게 되기 때문에
# 다른 방법이 필요하다. int(num+0.5)
n=int(input())
level=[]
for _ in range(n):
    lev=int(input())
    level.append(lev)

# 일단 오름차순으로 정렬
level.sort()
out=int(n*0.15+0.5) # round함수를 쓰지 않고 수학적으로 처리하는 방법
final_num=n-2*out
sum=0
if final_num==0:
    result=0
else:
    for i in range(out,n-out):
        sum+=level[i]
    result=int((sum/final_num)+0.5)
print(result)
