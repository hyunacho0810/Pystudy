# 영화감독 숌
N=int(input())
num=0
start=665

# 딱히 뚜렷한 패턴이 보이지 않아 완전 탐색으로 구현
while True:
    start+=1 # 만약 조건에 걸리지 않는다면 값을 하나씩 증가시키면서 확인 
    str_num=str(start)
    length=len(str(start))

    for i in range(length-2):
        # 3개의 6이 연속되어 있음
        if str_num[i]=='6' and str_num[i+1]=='6' and str_num[i+2]=='6':
            num+=1
            break # 6이 3개 있는거를 찾았으면 break

    if num==N:
        print(start)
        break






