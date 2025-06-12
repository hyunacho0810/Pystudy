def find_length(arr,N):
    count=0
    heart_i,heart_j=0,0
    count_left_arm,count_right_arm=0,0
    count_body = 0
    count_left_leg,count_right_leg = 0,0
    i=0

    while i < N:
        if count == 0:
            # 머리 위치로부터 심장의 위치 도출
            for j in range(N):
                if arr[i][j] == '*':
                    heart_j = j + 1
                    i += 1
                    count += 1
                    break
            else:
                i += 1  # *가 없으면 다음 행으로 이동
        # 팔 길이 도출
        elif count==1:
            heart_i = i+1
            for j in range(N):
                if j<heart_j-1 and arr[i][j]=='*':
                    count_left_arm+=1
                elif j>heart_j-1 and arr[i][j]=='*':
                    count_right_arm+=1
            i+=1
            count+=1
        # 몸통 길이 도출. 심장 아래 *이 있는 개수
        elif count>1:
            if arr[i][heart_j - 1] == '*':
                count_body += 1
            if arr[i][heart_j-2]=='*':
                count_left_leg+=1
            if arr[i][heart_j]=='*':
                count_right_leg+=1



            i += 1
            count += 1



    # 심장의 위치 출력
    print(heart_i,heart_j)
    # 팔,몸통,다리 등등
    print(count_left_arm, count_right_arm, count_body, count_left_leg, count_right_leg)


N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(input()))  # 각 행을 리스트로 변환하여 추가
find_length(arr,N)

