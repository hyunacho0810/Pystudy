def solution(arr):
    answer = []
    N=len(arr)
    # 그냥 리스트 순회 방법
    last=-1
    for i in range(N):
        if arr[i]==last:
            continue
        else:
            last=arr[i]
            answer.append(arr[i])
    return answer
    