# https://programmers.co.kr/learn/courses/30/lessons/67258

# 투포인터 알고리즘
from collections import defaultdict

# 완전탐색으로 하면 정답은 구하지만, 틀리게 될 것이다

# 첫번째 풀이 : set 이용 --> 시간초과
from collections import defaultdict


def solution(gems):
    ans = []
    len_gem = len(gems)
    # 보석들 종류의 갯수를 알아내야 한다.
    set_gems = set(gems)
    prec_len = len(set_gems)

    # 투포인터 알고리즘 --> 시작,시작+1 위치 잡기 ( st ~ ed-1)
    # 만약 개수가 작으면 ed += 1
    # 만약 개수가 같다면
    # 범위가 같다면, 그냥 ans 배열에 추가
    # 만약 범위가 더 작다면, ans 초기화 후에 배열에 추가
    st, ed = 0, 1
    p_gems = gems[st:ed]
    minLen = int(1e9)

    while True:
        if st > ed:
            break
        if ed >= len_gem + 1:
            break
        if st >= len_gem:
            break
        len_p_prec = len(set(p_gems))
        # 보석 길이 비교
        if len_p_prec < prec_len:
            if ed >= len_gem:
                break
            p_gems.append(gems[ed])
            ed += 1
        if len_p_prec == prec_len:
            len_range = ed - st
            if len_range == minLen:
                ans.append((st+1, ed+1))
            if len_range < minLen:
                minLen = len_range
                ans = [(st+1, ed+1)]
            p_gems.pop(0)
            st += 1

    ans.sort()
    print(ans)
    return (ans[0][0], ans[0][1]-1)

# Dictionary 이용 --------------------------------


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
