# 이 방법은 클로드가 알려줬는데...오우 쉽지 않네요
def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    
    # numbers는 1000이하. 최대 4자리까지 가능.
    # 따라서 어떤 두 숫자를 비교할 때 최소 3번이상 반복해야 한다.
    # 예: 3->333
    # 예:30-?>303030
    # ['9', '10', '4']->['999','101010','444']
    # 이때 문자열 비교의 경우 앞 자리수부터 비교. 999>101010이다.
    # 따라서 이 방법이 가능. 
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = ''.join(numbers)
    
    return str(int(answer))


# # 재귀로 순열을 생성하니까 시간초과
# def solution(numbers):
#     n=len(numbers)
#     answer=0
    
#     # 모든 순열을 저장할 리스트 
#     answer_set=[]
    
#     # 일단 다 문자로 바꾸고
#     numbers = list(map(str, numbers))
    
#     # 모든 조합을 확인해본다.(재귀)
#     def dfs(string,count, visited):
#         if count==n:
#             answer_set.append(string)
#             return
#         for i in range(n):
#             if not visited[i]:
#                 new_visited=visited[:]
#                 new_visited[i]=True
#                 dfs(string+numbers[i],count+1,new_visited)
    
#     dfs('',0,[False]*n)
    
#     answer_set = list(map(int, answer_set))
#     print(answer_set)
#     answer=max(answer_set)
#     answer=str(answer)

    
#     return answer