# 프린터 큐
from collections import deque

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    important=list(map(int,input().split()))

    # 덱에 중요도와 위치 저장
    queue = deque([(important[i], i) for i in range(N)])
    count = 0

    while queue:
        first_imp,idx=queue[0]
        max_p = max(item[0] for item in queue)

        if first_imp < max_p:
            # 맨 앞의 것보다 더 중요한게 있으면 현재 것을 맨 뒤로 이동
            queue.append(queue.popleft())
        else:  # 없다면
            # 현재 문서 출력
            printed_doc = queue.popleft()
            count += 1

            if printed_doc[1]==M:
                print(count)
                break

