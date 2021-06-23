# https://programmers.co.kr/learn/courses/30/lessons/42884

# 1번째 풀이 : checked 라는 배열을 두고, 이중 for문
from collections import deque


def solution(routes):
    routes.sort(key=lambda x: x[1])
    length = len(routes)
    checked = [False] * length
    camera = 0
    res = 0
    for i in range(length):
        if checked[i] == False:
            checked[i] = True
            camera = routes[i][1]
            res += 1
        for j in range(i+1, length):
            if routes[j][0] <= camera and camera <= routes[j][1] and checked[j] == False:
                checked[j] = True
    return res

# 2번째 풀이
# 1) routes[1] 기준 오른차순 정렬
# 2) camera를 -30,001 로 설정하기
# 3) for문을 돌면서 camera가 routes[0] 보다 작다는 것은, 해당 범위 안에 없다는 것
# 4) 우리는, 끝나는 시점에, 또 다른 도로가 포함되는지를 생각해야 하므로, camera를 routes[1]에 세팅


def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    res = 0
    for i in range(len(routes)):
        if camera < routes[i][0]:
            camera = routes[i][1]
            res += 1
    return res
