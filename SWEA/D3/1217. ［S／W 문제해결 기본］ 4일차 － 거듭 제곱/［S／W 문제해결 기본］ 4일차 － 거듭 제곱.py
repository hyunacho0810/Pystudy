def solve(n, m):
    return n **m
 
for _ in range(10):
    tc = int(input())
    n, m = map(int, input().split())
    print(f'#{tc} {solve(n, m)}')