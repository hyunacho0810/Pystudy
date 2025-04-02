def num_check(x, row, col, arr):
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

def sudoku(arr):
    # 비어있는 칸 찾기
    empty_found = False
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                row, col = i, j
                empty_found = True
                break
        if empty_found:
            break
    
    # 모든 칸이 채워져 있으면 완성된 것
    if not empty_found:
        return True
    
    # 1부터 9까지 시도
    for num in range(1, 10):
        # 해당 위치에 num이 유효한지 확인
        if num_check(num, row, col, arr):
            # 유효하면 값 할당
            arr[row][col] = num
            
            # 재귀적으로 다음 빈 칸 채우기
            if sudoku(arr):
                return True
            
            # 이 숫자로는 해결할 수 없으면 다시 0으로 되돌리기 (백트래킹)
            arr[row][col] = 0
    
    # 1-9 중 어떤 숫자도 유효하지 않으면 이전 단계로 백트래킹
    return False

# 입력 받기
arr = [list(map(int, input().split())) for _ in range(9)]

# 스도쿠 풀기
sudoku(arr)

# 결과 출력
for row in arr:
    print(*row)