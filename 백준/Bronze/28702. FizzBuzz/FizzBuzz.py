# FizzBuzz
sent1=input()
sent2=input()
sent3=input()

num=None
idx=0

# 셋중하나는 분명히 숫자
for i,sent in enumerate([sent1, sent2, sent3]): # 값과 인덱스를 반환하는 함수
    try:
        num = int(sent)  # 숫자로 변환 가능한지 시도
        idx=i
        break # 만약 숫자면
    except ValueError:
        continue

# 숫자를 찾았을 경우
if num is not None:
    next_num=num+(3-idx)
    if next_num % 3 == 0 and next_num % 5 == 0:
        print('FizzBuzz')
    elif next_num % 3 == 0:
        print('Fizz')
    elif next_num % 5 == 0:
        print('Buzz')
    else:
        print(next_num)