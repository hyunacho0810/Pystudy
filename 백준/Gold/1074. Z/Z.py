# Z
# 하나씩 다 탐색하기에는 시간이 0.5초로 매우 짧다. 따라서, 수학적 규칙을 파악하는 것이 좋겠다
# 이 문제가 분할정복?

def find_order(n, r, c):
    # 재귀로 영역을 쪼개면서 하기
    # 기저 조건
    if n == 0:
        return 0

    half = 2**(n-1) # 현재 사각형의 절반 크기

    # 어느 사분면인지 확인
    if r < half and c < half:  # 왼쪽 위
        return find_order(n - 1, r, c)
    elif r < half and c >= half:  # 오른쪽 위
        return (half * half) + find_order(n - 1, r, c - half)
    elif r >= half and c < half:  # 왼쪽 아래
        return 2 * (half * half) + find_order(n - 1, r - half, c)
    else:  # 오른쪽 아래
        return 3 * (half * half) + find_order(n - 1, r - half, c - half)


n, r, c = map(int, input().split())
print(find_order(n, r, c))
