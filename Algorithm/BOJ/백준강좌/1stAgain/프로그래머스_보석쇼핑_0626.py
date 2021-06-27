# https://programmers.co.kr/learn/courses/30/lessons/67258

# 투포인터 알고리즘
from collections import defaultdict

# 완전탐색으로 하면 정답은 구하지만, 틀리게 될 것이다


def solution(gems):
    # 투포인터 알고리즘
    # 시작, 끝
    st, ed = 0, 0
    # break 조건
    # - ed가 len + 1 이 될 때(범위 : ed  - 1 까지 )
    # - st가 len 이 될 때
    ans, info = [0, int(1e9)], dict()
    l_all = len(set(gems))
    info[gems[st]] = 1
    l_gems = len(gems)
    while True:
        # info가 모두 포함하는지 확인하기
        if len(info.keys()) == l_all:
            if ed - st + 1 < ans[1] - ans[0] + 1:
                ans = [st, ed]
            info[gems[st]] -= 1
            if info[gems[st]] == 0:
                del info[gems[st]]
            st += 1
            if st == l_gems:
                break
        elif len(info.keys()) < l_all:
            ed += 1
            if ed == l_gems:
                break
            if gems[ed] not in info:
                info[gems[ed]] = 1
            else:
                info[gems[ed]] += 1

    return [ans[0]+1, ans[1]+1]
