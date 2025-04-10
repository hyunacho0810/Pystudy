# 펠린드롬수
num_set=[]
# 0이 나오기 전까지의 숫자 입력이 인풋
while True:
    num = input()
    if int(num)==0:
        break
    num_set.append(num)
    N=len(num_set)

    # 이 밑에 수 확인
    result=''
    for tc in range(N):
        if num_set[tc][0]=='0':
            result='no'
        # 슬라이싱을 이용해 펠린드롬 수 검사 
        elif num_set[tc][::]!=num_set[tc][::-1]:
            result='no'
        elif num_set[tc][::]==num_set[tc][::-1]:
            result='yes'
    print(result)