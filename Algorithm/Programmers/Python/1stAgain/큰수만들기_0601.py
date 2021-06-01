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


def solution(name):
    # 처음부터 각 알파벳에 대한 상하 이동 횟수를 저장한다
    make_name = [min(ord(n)-ord('A'), ord('Z')-ord(n)+1) for n in name]
    idx, answer = 0, 0

    while True:
        # 상하 이동
        answer += make_name[idx]
        make_name[idx] = 0

        # break 조건
        if sum(make_name) == 0:
            break

        # 좌,우 이동
        left, right = 1, 1
        while make_name[idx-left] == 0:
            left += 1
        while make_name[idx+right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
    return answer


'''
자. 사실 여기서의 핵심은 
[idx-left] 혹은 [idx+right] 하는 과정에서
범위를 넘어서면 어떡하냐는 것이다

그리고 해당 코드가 올바르게 실행되기 위해서는
idx가 반드시 0으로 시작되어야 한다

------------------------------------------

1) left
left 부터 살펴보자 
idx-left가 - 가 되면 어떡하냐고 ?
python 문법상 배열에서 -1,-2는
자연스럽게 오른쪽 끝으로 이동하게 된다
따라서 이는 문제가 없다


2) right
사실 이 right이 문제다

왜냐하면 idx + right 이 len(name)을 벗어난다고
0부터 시작하는 원리는 아니기 때문이다 

예를 들어, 아래와 같은 문자열이 있었다고 해보자
J A A A B A C

이 경우, J를 처리한 다음
C로 갈건데
C에서 idx + right을 하는 순간 범위를 벗어나는 것이 아닌가 ?
라고 생각할 수도 있다

하지만, 이때의 idx 값을 살펴봐야 한다
J에서 바로 C로 갔다는 얘기는 left로 갔다는 것이고
0 idx에서 왼쪽으로 가면 -1 이다

즉, C 에 도착했을 때 idx는 len(name) -1 이 아니라
-1 이기 때문에 idx + right을 해도 범위에서 
벗어나는 일은 생기지 않는다는 것이다 
------------------------------------------


'''
