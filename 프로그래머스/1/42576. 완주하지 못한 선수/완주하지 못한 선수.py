def solution(participant, completion):
    # 동명이인때문에 participant를 딕셔너리로 만든 후, completion에 있으면
    # value값을 1씩 줄이는 방법으로 해, value값이 1 이상인 사람을 리턴하자.
    num_of_people=len(participant)
    participant_dict={}
    
    for name in participant:
        if name in participant_dict:
            participant_dict[name] += 1
        else:
            participant_dict[name] = 1
    
    for name in completion:
        participant_dict[name] -= 1
            
    for name, count in participant_dict.items():
        if count > 0:
            return name
