def solution(n, w, num):
    answer = 0
    row_num=n//w+1
    arr=[[0]*w for _ in range(row_num)]
    
    count=1
    i,j=row_num-1,-1 # 처음을 우로 이동할 것이므로 
    dir=[[0, 1], [-1, 0], [0, -1], [-1, 0]] # 우, 상, 좌, 상
    idx=0
    
    while count<=n:
        ni,nj=i+dir[idx][0],j+dir[idx][1]
        if 0<=ni<row_num and 0<=nj<w and arr[ni][nj]==0:
            arr[ni][nj]=count
            i,j=ni,nj
            count+=1
            # 상은 한번만 해야한다. 
            if idx==1 or idx==3:
                idx=(idx+1)%4
                
        else:
            idx=(idx+1)%4
    
    final_i,final_j=0,0        
    for i in range(row_num):
        for j in range(w):
            if arr[i][j]==num:
                final_i,final_j=i,j
                answer=i+1
                for k in range(final_i):
                    if arr[k][final_j]==0:
                        answer-=1
                        print(answer)
                        return answer
                return answer  

    return answer 
            
            
        
