N=int(input())
num=[]
dict={}
sum=0
# 최대한 한번에 많은 것을 처리
for i in range(N):
    number=int(input())
    num.append(number)
    sum+=number # 합을 구하고
    if number in dict: # 숫자의 개수에 대한 딕셔너리를 만들고
        dict[number]+=1
    else:
        dict[number]=1

# 산술평균
avg=sum/N
rounded_avg = round(avg)  # 정수로 반올림
print(rounded_avg)

# 중앙값
num.sort()
middle=num[N//2]
print(middle)

# 최빈값
# 같은 값이 2번 이상 나온경우
max_cnt=0
max_keys=set()
for key,values in dict.items():
    if values>max_cnt:
        max_cnt=values
        result=key
        max_keys={key}
    if values==max_cnt:
        max_keys.add(key)

sorted_max_values = sorted(max_keys)

if len(sorted_max_values)>=2:
    result=sorted_max_values[1]
else:
    result=sorted_max_values[0]
print(result)

# 범위
range=num[N-1]-num[0]
print(range)
