# 그냥 피보나치 ㅜㄴ제가 아니고 행렬의 곱셈을 이용해야 메모리 초과나 안나네..
# DP->O(N)
# 행렬->O(logN)
# def fibo(N):
#     if N == 0:
#         return 0
#     elif N == 1:
#         return 1
#
#     # 효율적인 재귀를 위해 메모이제이션 사용
#     memo = [0] * (N + 1)
#     memo[0] = 0
#     memo[1] = 1
#
#     for i in range(2, N + 1):
#         memo[i] = memo[i - 1] + memo[i - 2]
#
#     return memo[N]
#
# N=int(input())
# print(fibo(N)%1000000007)

# 분할정복 방법
def mat_mult(A, B):
    # 2x2 행렬 곱셈
    # F(n)=F(n-1)+F(n-2)를 행렬로 하는 과정
    # 이후 해당 값을 MOD로 나눈다.
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

# 거듭제곱을 빠르게 구하기
# 16의 경우 2^4이므로 이런 숫자를 쪼개서 간단하게 계산하기 위함
def mat_pow(mat, n):
    # 단위행렬로 초기화
    result = [[1, 0], [0, 1]]
    base = mat

    while n > 0:
        if n % 2 == 1:  # n이 홀수면
            result = mat_mult(result, base)
        base = mat_mult(base, base)  # base를 제곱
        n //= 2

    return result


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    base = [[1, 1], [1, 0]]
    result = mat_pow(base, n)
    return result[0][1]


N = int(input())
MOD = 1000000007
print(fibo(N))
