def postfix_expression(n, arr):
    stack = []
    # icp: 토큰의 우선순위 (입력될 때)
    # isp: 스택 내부에서의 우선순위
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

    result = ''

    for i in range(n):
        word = arr[i]

        # 알파벳일때 
        if word.isalpha():
            result += word
        elif word == '(':
            stack.append(word)
        elif word == ')':
            # 여는 괄호가 나올 때까지 pop
            while stack and stack[-1] != '(':
                result += stack.pop()
            # 여는 괄호 제거
            if stack:
                stack.pop()
        # 연산자인 경우
        else:
            # 스택의 top이 현재 토큰보다 우선순위가 높거나 같으면 pop
            while stack and isp[stack[-1]] >= icp[word]:
                result += stack.pop()
            stack.append(word)

    # 남아있는 연산자들 모두 pop
    while stack:
        result += stack.pop()
    return result

equation = input().strip()
N = len(equation)
result = postfix_expression(N, equation)
print(result)