# 체스판 다시 칠하기
# 왼쪽 위가 흰색인 경우
def chess_1(arr):
    count=0
    for i in range(8):
        for j in range(8):
            if i%2==0 and j%2==0 and arr[i][j]=='B':
                count+=1
            elif i%2==0 and j%2==1 and arr[i][j]=='W':
                count+=1
            elif i%2==1 and j%2==0 and arr[i][j]=='W':
                count+=1
            elif i%2==1 and j%2==1 and arr[i][j]=='B':
                count+=1
    return count

# 왼쪽 위가 검정색이 경우
def chess_2(arr):
    count = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0 and j % 2 == 0 and arr[i][j] == 'W':
                count += 1
            elif i % 2 == 0 and j % 2 == 1 and arr[i][j] == 'B':
                count += 1
            elif i % 2 == 1 and j % 2 == 0 and arr[i][j] == 'B':
                count += 1
            elif i % 2 == 1 and j % 2 == 1 and arr[i][j] == 'W':
                count += 1
    return count

N,M=map(int,input().split())
chess=[list(input()) for _ in range(N)]
min_change=50*50
for i in range(N-7):
    for j in range(M-7):
        new_arr = [row[j:j+8] for row in chess[i:i+8]]
        result1,result2=chess_1(new_arr),chess_2(new_arr)
        min_change=min(min_change,result1,result2)
print(min_change)
