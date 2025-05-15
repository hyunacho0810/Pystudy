def solution(array, commands):
    answer = []
    n=len(commands)
    for i in range(n):
        start=commands[i][0]-1
        end=commands[i][1]
        goal=commands[i][2]-1
        new_arr=array[start:end]
        new_arr.sort()
        new_num=new_arr[goal]
        answer.append(new_num)
    return answer