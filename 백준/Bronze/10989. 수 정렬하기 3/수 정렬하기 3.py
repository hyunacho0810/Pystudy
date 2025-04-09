# 수 정렬하기 3
# 메모리 사용량을 줄이기 위해 각 수의 등장 횟수만 저장
N=int(input())
number=[0]*10001
for _ in range(N):
    num=int(input())
    number[num]+=1
for i in range(1, 10001):
    if number[i] > 0:  # 1번 이상 등장
        for _ in range(number[i]):  # 등장한 횟수만큼 출력
            print(i)