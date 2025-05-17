# 큰 수 만들기
N=int(input())
num_list=list(input().split())

num_list.sort(key=lambda x:x*9,reverse=True)

answer=''.join(num_list)

# 모든 숫자가 0인 경우 00000이 아닌 0이 나와야 한다.
count=0
for i in range(N):
    if num_list[i]=='0':
        count+=1
if count==N:
    answer='0'
    
print(answer)