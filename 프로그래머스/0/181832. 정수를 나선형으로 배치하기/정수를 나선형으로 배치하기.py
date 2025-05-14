def solution(n):
    dir=[[0,1],[1,0],[0,-1],[-1,0]] # 오른쪽, 아래, 왼쪽, 위 
    answer = [[0]*n for _ in range(n)]
    num=1
    idx=0
    i,j=0,-1
    while num<=(n*n):
        ni,nj=i+dir[idx][0],j+dir[idx][1]
        if 0<=ni<n and 0<=nj<n and answer[ni][nj]==0:
            answer[ni][nj]=num
            i,j=ni,nj
            num+=1
        else:
            idx=(idx+1)%4    
    return answer