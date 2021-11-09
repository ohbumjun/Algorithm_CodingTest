# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3

'''
작동원리는 단순하다고 할 수 있다
1) 현재 작업이 진행중이고, 해당 작업이 끝나는 시점을 기준으로,
그 이전에 시작되는 작업들이 존재한다면 heap에 넣는다

그리고 heap이 다 빌때까지는, 
소요시간이 가장 작은 것들 순서대로 실행한다

2) heap이 다 빈다면, 그 말은, 둘중 하나일 것이다
2_1) 더이상 처리할 작업이 없거나
2_2) 이후 작업들이, 끝나는 시점 이후에 시작한다는 것이다 
'''

import heapq


def solution(jobs):
    jobs.sort()
    # 기다리는 배열(wait)에서 무언가를 꺼낼 때마다, count += 1 --> 다꺼낸다면, len과 같아질 것이다
    count = 0
    last = -1           # 현재 진행되는 작업이 시작된 시간
    wait = []           # 현재 작업이 진행되는 동안, 기다리는 작업들
    time = jobs[0][0]   # 현재 작업이 끝나는 시간
    length = len(jobs)
    answer = 0

    while count < length:
        for s, t in jobs:
            if last < s <= time:
                # 뽑아낼때, 소요시간이 가장 적은 것을 뽑아내기 위해 순서 바꿈
                heapq.heappush(wait, (t, s))
        if len(wait) > 0:
            last = time
            term, start = heapq.heappop(wait)
            count += 1
            time += term
            answer += (time - start)
            print("answer")
        else:  # 1초씩 계속 기다린다
            time += 1
    return answer // length

# 기원님 코드
# https://programmers.co.kr/learn/courses/30/lessons/42627


def solution(jobs):
    answer, now, last = 0, 0, -1
    wait, n, count = [], len(jobs), 0

    while count < n:
        for job in jobs:
            if last < job[0] <= now:
                answer += (now - job[0])
                heapq.heappush(wait, job[1])

        if not wait:
            now += 1
            continue

        t = heapq.heappop(wait)
        answer += len(wait) * t
        last = now
        now += t
        count += 1

    return answer // n
