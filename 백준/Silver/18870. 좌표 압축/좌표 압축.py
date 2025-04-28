# 좌표 압축
N=int(input())
nums=list(map(int,input().split()))

new_num=nums.copy()
# 같은 번호는 하나만 남겨두고, 오름차순으로 정렬
# 이 순서가 답이 된다.
new_num=sorted(list(set(new_num)))

order_dict={}
for i in range(len(new_num)):
    key=new_num[i]
    value=i
    order_dict[key]=value

for i in nums:
    print(order_dict[i],end=' ')