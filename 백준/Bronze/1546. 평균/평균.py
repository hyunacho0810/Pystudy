# 평균을 조작하는 문제
N = int(input())                              # N은 과목 개수
score = list(map(int, input().split()))       # 점수들 입력받기
M = score[0]                                  # 첫 번째 점수를 최댓값 초기값으로
result = 0

# 최댓값 찾기
for i in range(N):
    if score[i] > M:
        M = score[i]

# 점수 변환
for i in range(N):
    score[i] = (score[i]/M) * 100

# 평균 계산
for i in range(N):
    result += score[i]
print(result/N)