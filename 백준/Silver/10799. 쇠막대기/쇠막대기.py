# 쇠막대기
stick=input()
N=len(stick)
top=0
# stack=[0]*100001 # 스택 개념만 필요한 것이지 스택 자체는 필요 없음
result=0

i=0
while i<N:
    if stick[i]=='(' and stick[i+1]==')': # 레이저이면
        result+=top
        i+=2 # 다다음칸으로 이동
    elif stick[i]=='(': # 레이저가 아니고 그냥 막대 시작이면
        top+=1
        i+=1
    else: # 막대가 끝나는 지점이면 1 추가 
        result+=1
        top-=1
        i+=1

print(result)
