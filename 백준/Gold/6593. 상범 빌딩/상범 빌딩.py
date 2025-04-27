# 상벙빌딩
# 3차원 델타? 동서남북상하
def BFS(h,i,j): # 층, 행, 열
    global eh,ei,ej
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    queue=deque()
    queue.append((h,i,j))
    visited[h][i][j]=1

    while queue:
        th,ti,tj=queue.popleft()
        if th==eh and ti==ei and tj==ej:
            return visited[th][ti][tj]-1 # 시작점을 1초로 두었으므로 
        # 이제 델타를 돌려야 하는데 동서남북 따로 위아래 따로 해야한다.
        # 동서남북
        for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            wi,wj=ti+di,tj+dj
            if 0<=wi<R and 0<=wj<C and building[th][wi][wj]!='#' and visited[th][wi][wj] ==0:
                queue.append((th,wi,wj))
                visited[th][wi][wj]=visited[th][ti][tj]+1

        # 상하
        for dh in [1,-1]:
            wh=th+dh
            if 0 <= wh < L and building[wh][ti][tj] != '#' and visited[wh][ti][tj] == 0:
                queue.append((wh, ti, tj))
                visited[wh][ti][tj] = visited[th][ti][tj] + 1
    return 0



# 테스트 케이스를 주지 않으므로 while문 이용
while True:
    L,R,C=map(int,input().split())
    sh,si,sj=0,0,0
    # 0 0 0이 나오면 빠져나와야 하므로
    if L==0 and R==0 and C==0:
        break
    building=[]
    for height in range(L): # 각 층수마다
        floor=[]
        for row in range(R): # 각 열마다
            r=input()
            floor.append(r)
            # 시작점과 끝점 찾기
            if 'S' in r:
                sh,si,sj=height,row,r.index('S')
            if 'E' in r:
                eh,ei,ej=height,row,r.index('E')
        building.append(floor)
        input() # 층 사이의 공백

    from collections import deque
    # 이제 여기서부터 3차원 BFS 시작
    result=BFS(sh,si,sj)
    if result==0:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')


