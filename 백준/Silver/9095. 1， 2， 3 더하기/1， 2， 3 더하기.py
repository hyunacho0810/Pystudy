# 1,2,3 더하기
# 조합??
# n이 11보다 작으므로 그렇게까지 시간초과를 고려하진 않아도 되겠다.
def find_case(N,sum):

    if sum==N:
        return 1
    if sum>N:
        return 0
    
    count=0
    for i in range(1,4):
        count+=find_case(N,sum+i)
    return count


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    count=0
    result=find_case(n,0)
    print(result)


