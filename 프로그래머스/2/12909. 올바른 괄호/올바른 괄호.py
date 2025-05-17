def solution(s):
    N=len(s)
    stack=['']*N # top으로 접근하려면 충분한 크기의 스택을 생성
    top=-1
    result=True
    
    for char in s:
        if char=='(':
            top+=1
            stack[top]=char
        else:
            if top==-1:
                result=False
                break
            else:
                top-=1
                
    # 모든 문자를 다 확인했는데도 스택에 괄호가 남아있으면
    if top!=-1:
        result=False
    return result
