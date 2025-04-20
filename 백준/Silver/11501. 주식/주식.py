# 주식
# 뒤에서 앞으로 오면서 최댓값 찾기
def stock(price,N):
    earn=0 # 초기화
    max_price = price[N - 1]  # 마지막 날을 최대값으로 초기화

    for i in range(N - 2, -1, -1):
        if price[i] < max_price:
            # 현재 가격이 최대값보다 작으면 이익 추가
            earn += (max_price - price[i])
        elif price[i] > max_price:
            # 현재 가격이 더 크면 최대값 갱신
            max_price = price[i]
    return earn


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    price=list(map(int,input().split()))
    result_earn=stock(price,N)
    print(result_earn)
