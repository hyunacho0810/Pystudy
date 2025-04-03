# O/X 퀴즈
T=int(input())
for tc in range(1,T+1):
    result=input()
    num=len(result)
    cnt=0
    last=0
    for i in range(num):
        if result[i]=='O':
            cnt+=(1+last)
            last+=1
        else:
            last = 0
            cnt+=0
    print(cnt)

    