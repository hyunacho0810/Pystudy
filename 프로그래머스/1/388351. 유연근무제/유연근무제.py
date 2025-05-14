def solution(schedules, timelogs, startday):
    answer = 0
    goal_min = 0
    # 시작일부터 일주일이므로 3(수)의 경우 인덱스 기준 주말 3,4을 제외하고 다시 1,2
    # 시간 계산이 헷갈리므로 그냥 다 분으로 바꾸기 
    for worker in range(len(schedules)):
        goal_min = (schedules[worker]//100)*60+(schedules[worker]%100)
        success = 0
        for day in range(7):
            check_in_min = (timelogs[worker][day]//100)*60+(timelogs[worker][day]%100)
            
            if (day+startday)%7==6 or (day+startday)%7==0:
                success += 1
            elif check_in_min <= goal_min+10:
                success += 1
        if success == 7:
            answer += 1
    return answer