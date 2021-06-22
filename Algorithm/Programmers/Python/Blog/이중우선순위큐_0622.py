# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3

import heapq as hq


def solution(operations):
    maxH = []
    minH = []
    for op in operations:
        cmd, num = op.split(' ')
        if cmd == 'I':
            num = int(num)
            hq.heappush(maxH, (-num, num))
            hq.heappush(minH, num)
        else:
            if len(maxH) == 0:
                continue
            # 최대 지우기
            if num == '1':
                out = hq.heappop(maxH)
                minH.remove(out[1])
            # 최소 지우기
            elif num == '-1':
                out = hq.heappop(minH)
                maxH.remove((-out, out))

    if len(maxH) == 0:
        return [0, 0]
    else:
        return [hq.heappop(maxH)[1], hq.heappop(minH)]
