# https://programmers.co.kr/learn/courses/30/lessons/43238

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
    minT = 1
    maxT = max(times) * n
    ans = int(1e9)
    while minT < maxT:
        mid = (minT + maxT) // 2
        nums = 0
        for time in times:
            nums += (mid//time)
        if nums < n:
            minT = mid + 1
        else:
            ans = mid
            maxT = mid
    return ans


# 부등호 변환 버전
def solution(n, times):
    minT = 1
    maxT = max(times) * n
    ans = int(1e9)
    while minT <= maxT:
        mid = (minT + maxT) // 2
        nums = 0
        for time in times:
            nums += (mid//time)
        if nums < n:
            minT = mid + 1
        else:
            ans = mid
            maxT = mid - 1
    return ans
