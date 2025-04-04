# 분해합
N=int(input())

# N의 가장 작은 생성자를 구해라..
# 자릿수를 더하는 가장 좋은 방법은 문자열로 변환한 다음에 더하기
# 다만 더할 때는 int를 꼭 붙여야한다.

# 시간을 줄이기 위해 시작점을 꽤 높은 숫자로 시작
# M=1000인 경우, 각 자기수의 최대합은9*4이다. 따라서 시작점이 1000-9*4
start=max(1,N-9*len(str(N)))

for num in range(start,N):
    digits = len(str(num))
    result=num
    for digit in str(num):
        result+=int(digit)
    if result==N:
        print(num)
        break
else:
    print(0)