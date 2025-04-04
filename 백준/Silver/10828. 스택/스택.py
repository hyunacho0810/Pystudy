# 스택
N=int(input())
arr = [input() for _ in range(N)]
# print(arr)
stack=[0]*10000 # 일단 매우 큰 스택을 만든다.
top=-1

for i in range(N):
    if arr[i]=='top':
        if top==-1:
            print(-1)
        else:
            print(stack[top])

    if arr[i]=='pop':
        if top==-1:
            print(-1)
        else:
            print(stack[top])
            top-=1

    if arr[i]=='size':
        print(top+1)

    if arr[i]=='empty':
        if top==-1:
            print(1)
        else:
            print(0)

    if arr[i][0:4]=='push':
        top+=1
        stack[top]=arr[i][5:]
