# 시간 초과를 해결하기 위해 이분탐색 사용 
def solution(n,times):
    answer=0
    # 최소시간
    left=1
    # 최대시간
    right=max(times)*n # 가장 오래걸리는 심사관이 모든 사람을 처리할 경우
    
    while left<=right:
        mid=(left+right)//2
        people=0 # 처리한 사람 명 수 
        
        # 각 심사관이 mid 시간동안 몇 명을 심사할 수 있는지 계산
        for time in times:
            people+=mid//time 
        
        # n명 이상 심사 가능하면 시간을 줄여본다.
        if people>=n:
            # 중간 결과값 저장 
            answer=mid
            right=mid-1
        # 만약에n명 미만 가능하면, 시간을 늘려본다.
        else:
            left=mid+1
        
    return answer



# 아래 방법이 테케는 맞는데 시간초과가 남
# def solution(n, times):
#     answer = 0
#     person=1
#     screen=len(times)
    
    
#     # 각 심사대의 심사 시간 
#     screen_times=[0] * screen
    
#     # 모든 사람을 다 탐색할 때까지 
#     while person<=n:
#         min_idx=0
#         min_time=screen_times[0] + times[0]
#         # 각 사람마다 가장 시간이 적게 걸리는 심사대 고르기
#         for i in range(1,screen):
#             if screen_times[i]+times[i]<min_time:
#                 min_time=screen_times[i]+times[i]
#                 min_idx=i
#         screen_times[min_idx]+=times[min_idx]
#         person+=1
            
#     answer=max(screen_times)
                
#     # print(screen_times)
#     return answer