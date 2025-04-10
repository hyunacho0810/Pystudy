# 스택 수열
N=int(input())
num=[]
for _ in range(N):
    num.append(int(input()))

signs=[]
i=0
top=-1
stack=[0]*100000
last=0
possible=True

while i < N and possible:
    # 종료조건 (스택의 맨 위에 수가 더 큰 경우)
    if stack[top]>num[i]:
        possible=False
        print('NO')
        break
    elif stack[top]<num[i]:
        top+=1
        stack[top]=last+1
        signs.append('+')
        last+=1
    elif stack[top]==num[i]:
        top-=1
        signs.append('-')
        i+=1

# NO인 경우, 위의 부호들이 뜨면 안되므로, 리스트에 저장을 한 후 프린트 
if possible:
    for sign in signs:
        print(sign)