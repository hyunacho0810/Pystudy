# 연결 요소의 개수
# union-find에서 조상의 개수를 찾으면 되겠다.
def make_set(x):
    parents=[i for i in range(N+1)]
    return parents

def find_set(x):
    if parents[x]==x:
        return x
    parents[x]=find_set(parents[x])
    return parents[x]

def union(x,y):
    ref_x=find_set(x)
    ref_y=find_set(y)
    if ref_x==ref_y:
        return
    if ref_x<ref_y:
        parents[ref_y]=ref_x
    else:
        parents[ref_x]=ref_y

N,M=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(M)]
parents=make_set(N)

for i in range(M):
    union(arr[i][0],arr[i][1])

grand_grand=set()
for i in range(1,N+1):
    grand_grand.add(find_set(i))
result=len(grand_grand)
print(result)
