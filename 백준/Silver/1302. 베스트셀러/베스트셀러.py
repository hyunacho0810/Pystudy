book={}
N=int(input())
for _ in range(N):
    name=input()
    if name in book:
        book[name]+=1
    else:
        book[name]=1
max_num=0
book_name=''
for key,value in book.items():
    if value > max_num:  
        max_num = value
        book_name = key
    # 이런 방식으로 문자열 간 비교를 할 수 있음음
    elif value == max_num and key < book_name:  # 사전순으로 비교
        book_name = key
print(book_name)