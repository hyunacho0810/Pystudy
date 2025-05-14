# 백트래킹,메모이제이션(시간초과 나서)
def solution(info, n, m):
    num = len(info)
    memo = {}
    
    max_num = 10**9
    
    def dfs(index, sum_A, sum_B):
        # 이미 계산한 상태면 재사용
        if (index, sum_A, sum_B) in memo:
            return memo[(index, sum_A, sum_B)]
            
        # 조건 위반
        if sum_A >= n or sum_B >= m:
            return max_num
            
        # 도둑 다 살펴봄
        if index == num:
            return sum_A
            
        a, b = info[index]
        
        # 두 가지 선택의 최소값
        result = min(
            dfs(index + 1, sum_A + a, sum_B),  # A 도둑 선택
            dfs(index + 1, sum_A, sum_B + b)   # B 도둑 선택
        )
        
        memo[(index, sum_A, sum_B)] = result
        return result
    
    result = dfs(0, 0, 0)
    
    if result == max_num:
        return -1
    else:
        return result




# 이렇게 하면 테케 35개중 33개가 맞는데 최적해를 보장하지 않음
# def solution(info, n, m):
#     answer_A = 0
#     answer_B=0
# #     A 도둑 기준으로 최소값을 구하면 되므로, A기준으로 info를 sort하자
# #     A(x[0])를 내림차순으로 정렬하고, A가 같을 경우 B(x[1])를 오름차순으로 정렬
#     info.sort(key=lambda x: (-x[0], x[1]))
#     print(info)
#     num=len(info)
#     for i in range(num):
#         if info[i][1]+answer_B<m:
#             answer_B+=info[i][1]
#             continue
#         else:
#             answer_A+=info[i][0]
#     if answer_A>=n or answer_B>=m:
#         return -1
#     else:
#         return answer_A