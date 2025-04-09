# 수 정렬하기
N=int(input())
num=[]
for _ in range(N):
    number=int(input())
    num.append(number)
num.sort()
for i in range(N):
    print(num[i])