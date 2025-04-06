# 행복한지 슬픈지
letter=input() # 문자열로 인풋받기
num_happy=0 # 행복한 이모티콘의 개수
num_sad=0 # 슬픈 이모티콘의 새우
N=len(letter)

for i in range(N-2):
    if letter[i]==':' and letter[i+1]=='-' and letter[i+2]==')':
        num_happy+=1
    if letter[i]==':' and letter[i+1]=='-' and letter[i+2]=='(':
        num_sad+=1
if (num_happy+num_sad)==0:
    print('none')
elif num_happy==num_sad:
    print('unsure')
elif num_happy>num_sad:
    print('happy')
else:
    print('sad')
