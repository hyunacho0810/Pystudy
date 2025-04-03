#소수 찾기
N = int(input())
numbers = list(map(int, input().split()))

# 소수 개수 세기
count = 0
for num in numbers:
    # 1은 소수가 아님
    if num == 1:
        continue

    # 소수 여부 판별
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

# 결과 출력
print(count)