# https://www.acmicpc.net/problem/1655

import sys
sys.stdin = open("input.txt", "rt")
import heapq as hq

n = int(sys.stdin.readline())

maxHeap = []
minHeap = []

for i in range(n):
    
    num = int(sys.stdin.readline())

    # 현재 개수가 같다면
    if len(maxHeap) == len(minHeap) :
        # maxHeap에 넣는다
        hq.heappush(maxHeap,[-num, num])

    # 현재 개수가 다르다면
    else:
        # minHeap에 넣는다
        hq.heappush(minHeap, [num,num])


    # maxHeap의 최대값이 더 크다면 교체
    if len(minHeap) > 0 and maxHeap[0][1] > minHeap[0][1] :
        tmp_max = hq.heappop(maxHeap)[1]
        tmp_min = hq.heappop(minHeap)[1]
        hq.heappush( minHeap , [tmp_max, tmp_max] )
        hq.heappush( maxHeap , [tmp_min, - tmp_min] )

    # 출력
    print(maxHeap[0][1])
