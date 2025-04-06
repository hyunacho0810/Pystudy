# 누울 자리를 찾아라
N=int(input())
arr=[list(input()) for _ in range(N)]

# 가로
num_x=0
for i in range(N):
    last_x=0
    for j in range(N):
        if arr[i][j]=='X':
            if j-last_x>=2:
                num_x+=1
            last_x=j+1
    # 행의 마지막
    if N - last_x >= 2:  # 마지막 X 이후로 2칸 이상 빈 공간이 있는지
        num_x += 1   
        

# 세로
num_y=0
for j in range(N): # 매 열마다 체크
    last_y=0
    for i in range(N):
        if arr[i][j]=='X':
            if i-last_y>=2:
                num_y+=1
            last_y=i+1
    # 열의 마지막
    if N - last_y >= 2:
        num_y += 1  

print(num_x,end=' ')
print(num_y)
