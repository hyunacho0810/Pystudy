# 팩토리얼 0의 개수
# def find_number(num):
#     global cnt
#     length = len(str(factorial))
#     cnt = 0
#     # 뒤에서부터 하나씩 살펴본다.
#     for i in range(length - 1, -1, -1):
#         # 숫자를 문자열로 변환해서 하나씩 살펴본다.
#         if str(factorial)[i] == '0':
#             cnt += 1
#             continue
#         else:
#             # 처음으로 0이 아닌 값이 나오면 출력하고 break
#             return True
#     return False
#
#
# N=int(input())
# num=N
# factorial=1
# while True:
#     if num==1:
#         if find_number(factorial):
#             print(cnt)
#     factorial*=num
#     num-=1

# 위의 코드가 시간초과가 나서, 5의 개수로 판단하기
N=int(input())
cnt=0
cnt+=N//5
cnt+=N//25
cnt+=N//125
print(cnt)