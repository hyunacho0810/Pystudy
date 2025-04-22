# 적록색약
# 유기농 배추와 매우 유사
# 런타임에러를 해결하기 위해 재귀가 아닌 스택 이용하기
import copy
def DFS1(start_i, start_j, arr):
    stack = [(start_i, start_j)]
    color = arr[start_i][start_j]  # 시작 위치의 색상
    arr[start_i][start_j] = 'X'  # 방문 표시

    while stack:
        i, j = stack.pop()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color:
                stack.append((ni, nj))
                arr[ni][nj] = 'X'  # 방문할 때 바로 표시


def DFS2(start_i, start_j, arr):
    stack = [(start_i, start_j)]
    color = arr[start_i][start_j]  # 시작 위치의 색상
    arr[start_i][start_j] = 'X'  # 방문 표시

    while stack:
        i, j = stack.pop()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # 적록색약 처리
                if ((color == 'R' or color == 'G') and
                        (arr[ni][nj] == 'R' or arr[ni][nj] == 'G')):
                    stack.append((ni, nj))
                    arr[ni][nj] = 'X'  # 방문할 때 바로 표시
                # 파란색 처리
                elif color == 'B' and arr[ni][nj] == 'B':
                    stack.append((ni, nj))
                    arr[ni][nj] = 'X'  # 방문할 때 바로 표시


N = int(input())
arr = [list(input()) for _ in range(N)]

# 일반인이 보는 구역 수
arr1 = [row[:] for row in arr]  # 2차원 리스트 깊은 복사 (deepcopy보다 빠름)
count_1 = 0

for i in range(N):
    for j in range(N):
        if arr1[i][j] != 'X':
            count_1 += 1
            DFS1(i, j, arr1)

# 적록색약이 보는 구역 수
arr2 = [row[:] for row in arr]  # 2차원 리스트 깊은 복사
count_2 = 0

for i in range(N):
    for j in range(N):
        if arr2[i][j] != 'X':
            count_2 += 1
            DFS2(i, j, arr2)

print(f'{count_1} {count_2}')

# DFS함수를 2개 만들어서 처리하기. 아직도 런타임에러
# import copy
# def DFS1(i,j,arr):
#     now=arr[i][j] # 현재 영역의 색
#     arr[i][j]='X' # 해당 칸을 세었다
#     for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#         ni,nj=i+di,j+dj
#         if 0<=ni<N and 0<=nj<N and arr[ni][nj]==now:
#             DFS1(ni,nj,arr)
#
# def DFS2(i,j,arr):
#     now=arr[i][j] # 현재 영역의 색
#     arr[i][j]='X' # 해당 칸을 세었다
#     for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#         ni,nj=i+di,j+dj
#         if 0 <= ni < N and 0 <= nj < N:
#             # 적록색약은 R과 G를 구분하지 못함
#             if (now == 'R' or now == 'G') and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
#                 DFS2(ni, nj, arr)
#             # B는 정상적으로 처리
#             elif now == 'B' and arr[ni][nj] == 'B':
#                 DFS2(ni, nj, arr)
#
# N=int(input())
# arr=[list(input()) for _ in range(N)]
#
# # 일반인이 보는 구역 수
# arr1 = copy.deepcopy(arr)
# count_1 = 0
#
# for i in range(N):
#     for j in range(N):
#         if arr1[i][j] != 'X':
#             count_1 += 1
#             DFS1(i, j, arr1)
#
# # 적록색약이 보는 구역 수
# arr2 = copy.deepcopy(arr)
# count_2 = 0
#
# for i in range(N):
#     for j in range(N):
#         if arr2[i][j] != 'X':
#             count_2 += 1
#             DFS2(i, j, arr2)
#
# print(f'{count_1} {count_2}')



# 아래처럼 푸니까 답은 정확한데 런타임에러
# import copy
# def DFS(i,j,arr):
#     now=arr[i][j] # 현재 영역의 색
#     arr[i][j]='X' # 해당 칸을 세었다
#     for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#         ni,nj=i+di,j+dj
#         if 0<=ni<N and 0<=nj<N and arr[ni][nj]==now:
#             DFS(ni,nj,arr)
#
#
#
# N=int(input())
# arr_1=[list(input()) for _ in range(N)]
# arr_2=copy.deepcopy(arr_1) # 적록색약
#
# # 초록색인 칸을 빨간색으로 바꾸기
# for i in range(N):
#     for j in range(N):
#         if arr_2[i][j]=='G':
#             arr_2[i][j]='R'
#
# count_1=0
# count_2=0
#
# for i in range(N):
#     for j in range(N):
#         if arr_1[i][j]!='X':
#             count_1+=1
#             DFS(i,j,arr_1)
#
#         if arr_2[i][j]!='X':
#             count_2+=1
#             DFS(i,j,arr_2)
#
# print(f'{count_1} {count_2}')