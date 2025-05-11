# 예산
def find_sum():
    global sum_total
    for i in range(N):
        sum_total += num_list[i]

def find_max_num():
    start = 1
    end = num_list[N-1]
    answer = 0
    while start<=end:
        mid=(start+end)//2
        result=0 # 중간 결과 값 저장용
        for j in range(N):
            if num_list[j]>mid:
                result+=mid
            else:
                result+=num_list[j]
        if result>M:
            # 더 작은 값을 찾아야한다.
            end=mid-1
        else:
            # 더 큰 값을 찾아도 되는 경우
            answer=mid # 중간저장
            start=mid+1
    return answer

N=int(input())
num_list=list(map(int,input().split()))
M=int(input())

# 일단 오름차순으로 정렬
num_list.sort()
sum_total=0
find_sum()

if sum_total<=M:
    print(num_list[N-1])
else:
    # 만약, 정수 상한액을 계산하여야 하는 경우
    # 빠르게 상한액을 구하기 위해 이진검색으로 구하기
    final_result=find_max_num()
    print(final_result)

