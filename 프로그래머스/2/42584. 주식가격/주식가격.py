def solution(prices):
    N=len(prices)
    answer = [0]*N
    stack=[]
    for i in range(N):
        # 가격이 떨어진 경우 
        while stack and prices[stack[-1]]>prices[i]:
            top=stack.pop()
            answer[top]=i-top
        stack.append(i)
            
    # 끝까지 가격이 떨어지지 않은 경우 
    while stack:
        top=stack.pop()
        answer[top]=N-1-top
    
        
    return answer