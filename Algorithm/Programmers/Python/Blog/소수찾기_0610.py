# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations
import math

from itertools import permutations
import math


def solution(numbers):
    # 해당 경우의 숫자가, 소수에 해당하는지를 찾으면 된다
    # 아니. 모든 경우의 수를 만들어서, 각 수에 대해서, 소수 판별 알고리즘을 적용하면 된다
    len_num = len(numbers)
    numbers = list(numbers)

    answer = 0
    res = set()  # 만들어지는 모든 경우의 수가 들어가는 배열
    for i in range(1, len_num + 1):
        tmp = permutations(numbers, i)
        for t in tmp:
            res.add(int(''.join(t)))
    for r in res:
        if r < 2:
            continue
        # 2,3 도 소수로 포함시켜야 하는 것이 아닐까 ?
        # 아래 코드는 2와 3도 소수로 포함시키게 되는 원리인거 아닌가 ?
        # 맞아, 2,3 도 소수야. 그런데 아래에서 int(math.sqrt(r))+1 를 2,3에 적용하면
        # 애초부터 2를 2로 나누거나, 3을 3으로 나누는 경우의 수가 애초부터 고려가 안되
        # 그래서 자연스럽게 소수로 고려되게 되는 것이다
        decimal = True
        for i in range(2, int(math.sqrt(r))+1):
            if r % i == 0:
                decimal = False
                break
        print("decimal", decimal)
        if decimal:
            answer += 1

    return answer
