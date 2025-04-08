# 단어 정렬
N=int(input())
str_list=[]
for _ in range(N):
    word=input()
    if word in str_list:
        continue
    else:
        # 아얘 입력을 받을 때 부터 중복된 값은 저장하지 않음
        str_list.append(word)
# 첫번째 기준은 단어의 길이, 두번째 기준은 알파벳 순서 
str_list.sort(key=lambda x:(len(x),x))
N=len(str_list)
for i in range(N):
    print(str_list[i])

