# https://programmers.co.kr/learn/courses/30/lessons/42883

# 최초 시도 : 비트마스크를 활용한 brute force --> 시간초과
def solution(number, k):
    answer = ''
    len_num = len(number)
    # 모든 경우의 수를 다 구하는 방법은 무리가 있지 않을까 ?
    # 비트마스크를 통해서, 구할 수는 있을 것 같다
    # 우선 모든 부분집합 경우의 수를 다 구하고
    # 구한 이후, len이 3인 애들만 남기고
    # 그 중에서 sort 시켜서
    # 최대값 뽑아보자
    candidates = []
    for i in range(1 << len_num):
        res = []
        for j in range(len(number)):
            if i & (1 << j):
                res.append(number[j])
        candidates.append(res)
    threes = []
    for cand in candidates:
        if len(cand) == len_num - k:
            threes.append(int(''.join(cand)))
    threes.sort(reverse=True)

    return str(threes[0])

# 해결 코드
# 특정 숫자가, 오른쪽에서 왼쪽으로 가면서, 큰 숫자만을 남기는 원리를 생각하면 된다


def solution(number, k):

    max_nums = []
    # 앞에서부터 탐색해가면서, 현재 만난 숫자가 더 크면, stack을 빼고, 넣어주는 과정을 반복한다
    # 뺄때마다 k를 감소시켜준다
    # k가 0이 되면 max_nums 배열 + number 배열 안에 있는 숫자들을 return
    # k가 0 이 되지 않은 상태에서, 모든 숫자를 순회하면 남은 k만큼 뒤에서 빼준다
    for i in range(len(number)):
        allRemv = False
        if not max_nums:
            max_nums.append(number[i])
            continue
        while max_nums and max_nums[-1] < number[i]:
            max_nums.pop()
            k -= 1
            if k == 0:
                max_nums += number[i:]
                return ''.join(max_nums)
        max_nums.append(number[i])
    for i in range(k):
        max_nums.pop()
    return ''.join(max_nums)
