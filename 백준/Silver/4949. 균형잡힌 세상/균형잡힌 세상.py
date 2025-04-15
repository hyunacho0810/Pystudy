# 균현잡힌 세상
lines=[]
while True:
    line=input()
    if line=='.':
        break
    lines.append(line)

N=len(lines)
for i in range(N):
    result='yes' # 결과값 초기화
    top=-1
    stack=[] # 새로운 문장을 시작할 때마다 스택 초기화
    for letter in lines[i]:
        if letter=='(' or letter=='[':
            top+=1
            stack.append(letter)
        elif letter==')':
            if top==-1:
                result='no'
            elif stack[top]=='(':
                top-=1
                stack.pop()
            else:
                result='no'
        elif letter==']':
            if top==-1:
                result='no'
            elif stack[top]=='[':
                top-=1
                stack.pop()
            else:
                result='no'
    # 끝까지 다 봤는데 스택에 괄호가 남아있는 경우
    if top>-1:
        result='no'
    print(result)
