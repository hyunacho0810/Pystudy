# 나는야 포케몬 마스터 이다솜
N,M=map(int,input().split())
pokemon_dict={}
pokemon_dict_by_name = {}
for i in range(N):
    name = input()
    pokemon_dict[i + 1] = name
    pokemon_dict_by_name[name] = i + 1
for i in range(M):
    order=input()
    # 문자열로 인풋받고 있으므로 order.type()해도 항상 str로 나온다.
    if order.isdigit():
        print(pokemon_dict[int(order)])
    else:
        print(pokemon_dict_by_name[order])