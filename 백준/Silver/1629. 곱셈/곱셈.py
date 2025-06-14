# 곱셈
# 이게 분할정복을 이용한 거듭제곱 처리?
# A를 B번 곱해야 하는데, B가 짝수면 이를 나눠서 구할 수 있음
def divide(A,B,C):
    if B==0:
        return 1
    if B%2==0:
        half=divide(A,B//2,C)
        return (half*half)%C
    else:
        return (A*divide(A,B-1,C))%C

A,B,C=map(int,input().split())
print(divide(A,B,C))