# 듣보잡
N,M=map(int,input().split())
# 시간초과가 나서 리스트가 아닌 셋으로 접근했어요
no_listen=set()
no_look=set()

for _ in range(N):
    no_listen.add(input())
for _ in range(M):
    no_look.add(input())

# 교집합
result = list(no_listen.intersection(no_look))
# 찾아보니까 sort가 문자열도 사전순으로 정렬해준다고 하네요
result.sort()  # 사전 순 정렬

print(len(result))
for name in result:
    print(name)
