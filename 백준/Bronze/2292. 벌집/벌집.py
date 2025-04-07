# 벌집
N = int(input())
dist = 1

if N == 1:
    print(1)
else:
    count = 1
    while count < N:
        count += 6 * dist
        dist += 1
    print(dist)