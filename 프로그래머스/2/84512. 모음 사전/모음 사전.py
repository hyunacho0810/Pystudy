def solution(word):
    answer = 0
    n=len(word)
    vowel_list=['A','E','I','O','U']
    
    first=1
    second=5+first
    third=5*5 +second
    fourth=5*5*5+third
    fifth=5*5*5*5+fourth
    # 각 자리에서 하나 바뀔때 있는 단어의 수
    # A____->E____은 사이에 fifth만큼의 단어가 있다. 
    weights=[fifth,fourth,third,second,first]
    
    for i in range(n):
        # 맨 앞부터 어떤 알파벳인지 
        letter=word[i]
        for j in range(5):
            if letter==vowel_list[j]:
                count=j
        answer+=count*weights[i]+1
        
    return answer