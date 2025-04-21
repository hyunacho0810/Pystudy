# 수영장
# 아마도 DP?
T=int(input())
for tc in range(1,T+1):
    day,month,three_month,year=map(int,input().split())
    plan=[0]+list(map(int,input().split())) # 12개월 이용 계획

    # 모든 경우의 수를 살펴보자
    # 1. 1일 이용권 사용
    # 2. 한달 이용권 사용
    # 3. 3달 이용권 사용(현재 달 부터)
    # 4. 1년 이용권 사용

    price=0 # 변수 초기화
    dp=[0]*13 # 배열 생성 
    
    # bottom-up으로 가장 작은 문제로부터 큰 문제 구하기 
    for i in range(1,13):
        # 1. 현재 달을 1일권으로 할지 한달 권으로 할지
        dp[i]=dp[i-1]+min(plan[i]*day,month)
        # 2. 3달 이용권을 사용하는 경우
        if i>=3:
            # dp[i]=1일권, 1달권의 조합과 3달권을 비교
            dp[i]=min(dp[i],dp[i-3]+three_month)
        # 3. 1년 이용권 사용
        if i==12:
            dp[i]=min(dp[i],year)

    print(f'#{tc} {dp[12]}')
