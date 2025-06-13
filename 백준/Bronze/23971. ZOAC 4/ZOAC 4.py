# ZOAC 4
H,W,N,M=map(int,input().split())
# H=행의 수, W=열의 수
# N=행의 방향으로 비워야 하는 칸, M=열의 방향

# 가로 곱하기 세로를 하면 된다
if H%(N+1)==0:
    y=H//(N+1)
else:
    y = (H // (N + 1))+1

if W%(M+1)==0:
    x=W//(M+1)
else:
    x=(W//(M+1))+1

answer=y*x
print(answer)