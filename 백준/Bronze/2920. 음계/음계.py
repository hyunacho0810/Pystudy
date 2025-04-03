# 음계
num = list(map(int, input().split()))

new_num_asc=num[:]
new_num_asc.sort()

new_num_desc=num[:]
new_num_desc.sort(reverse=True)

if num==new_num_asc:
    print('ascending')
elif num==new_num_desc:
    print('descending')
else:
    print('mixed')