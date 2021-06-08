# https://programmers.co.kr/learn/courses/30/lessons/43238

def binary(st, ed, times, n):
    ans = int(1e9)
    while st <= ed:
        mid = (st+ed) // 2
        if isPassed(n, mid, times):
            # 어차피 mid값이 가장 이상적인 값이 되어갈 것이기 때문이다
            ans = mid
            ed = mid - 1
        else:
            st = mid + 1
    return ans


def isPassed(n, mid, times):
    ans = 0
    for i in range(len(times)):
        ans += mid // times[i]
    if ans >= n:
        return True
    else:
        return False


def solution(n, times):
    # 이진 탐색을 수행하기 위해서는 먼저 정렬을 해야 한다
    # pb 1)
    # 제일 처음에 헷갈렸던 것은, 이분탐색을 실시하려면
    # 특정 target이 있어야 하는것 아닌가 ? 였다
    # 하지만, 아니다. 특정 조건을 만족시키는 최대, 최소 범위를 구하는 방식이 존재한다
    # pb 2)
    # 이분탐색을 위해서는 먼저 정렬을 해주어야 한다
    # pb 3)
    # 최대 최소 범위를, 사람의 수가 아니라, '시간'으로 둬야 한다
    times.sort()
    st = 1
    ed = n * times[-1]
    return binary(st, ed, times, n)
