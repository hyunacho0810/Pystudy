# 스도구
def num_check(x,row,col,arr):
    # 행 체크
    for i in range(9):
        if arr[row][i] == x:
            return False
    # 열 체크
    for i in range(9):
        if arr[i][col] == x:
            return False
    # 3*3 상자 체크
    box_row = (row // 3) * 3  # 3x3 박스의 시작 행 인덱스
    box_col = (col // 3) * 3  # 3x3 박스의 시작 열 인덱스
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if arr[i][j] == x:
                return False
    # 위의 세 조건에 걸리지 않으면
    return True


def find_empty(array):
    for i in range(9):
        for j in range(9):
            if array[i][j]==0:
                return (i,j) # 좌표 넘기기
    return None


def sudoku(array):
    empty=find_empty(array)
    if not empty:
        return True

    row,col=empty
    for num in range(1, 10):
        if num_check(num, row, col, array): # true면
            array[row][col] = num # 해당 값 배치
            if sudoku(array): # 다음 값 재귀로 넘기기 
                return True
            # 안되면 백트래킹
            array[row][col] = 0
    return False




arr=[list(map(int,input().split())) for _ in range(9)]
sudoku(arr)
for row in arr:
    print(*row)


