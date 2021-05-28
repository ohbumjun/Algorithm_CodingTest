# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq as hq


def solution(scoville, K):
    # 매번 heapq 에서 가장 작은 음식 2개를 골라야 한다
    # 둘다 k보다 작은 것이 아니면 break
    foodHeap = []
    time = 0
    for s in scoville:
        hq.heappush(foodHeap, s)
    while True:
        # 섞고
        # 모든 요소가 K 이상인지 검사
        # 지속 및 break 여부 결정
        s1 = hq.heappop(foodHeap)
        # 최소가 K보다 크다라는 것은, 모든 요소가 K보다 크다는 것을 의미한다
        if s1 > K:
            return time
        elif len(foodHeap) == 0:
            return -1
        s2 = hq.heappop(foodHeap)
        newS = s1 + s2*2
        hq.heappush(foodHeap, newS)
        time += 1
