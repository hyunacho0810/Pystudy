# 큐
N=int(input())
command=[]
# 명령어를 입력받는 과정
for _ in range(N):
    command.append(input())

# 명령에 따라 큐를 규현하는 과정
queue=[0]*100000
front=rear=-1

for i in range(N):
    # 인큐
    if command[i]=='pop':
        if front!=rear:
            front+=1
            print(queue[front])
        else:
            print('-1')
    # 디큐
    if command[i][0:4]=='push':
        num=int(command[i][5:])
        rear+=1
        queue[rear]=num
    if command[i]=='size':
        print(rear-front)
    if command[i]=='empty':
        if front!=rear:
            print(0)
        else:
            print(1)
    if command[i]=='front':
        if front!=rear:
            print(queue[front+1])
        else:
            print(-1)
    if command[i]=='back':
        if front!=rear:
            print(queue[rear])
        else:
            print(-1)
