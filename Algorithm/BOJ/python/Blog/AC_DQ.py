# https://www.acmicpc.net/problem/5430

import sys
from collections import deque
t = int(input())

for _ in range(t):
    p = list(sys.stdin.readline())
    n = int(input())
    x = sys.stdin.readline()

    di = 1
    try:
        if n == 0:
            x = []
        else:
            x = deque(list(map(int, x.strip()[1:-1].split(','))))

        for i in p:
            if i == 'R':
                di *= -1
            elif i == 'D':
                if x:
                    if di == 1:
                        x.popleft()
                    else:
                        x.pop()
                else:
                    raise ValueError
    except ValueError:
        print("error")
    else:
        if di == -1:
            x = reversed(x)
        print("[" + ",".join(list(map(str, x))) + "]")


'''
2가지를 주목해야 한다
1) 무조건 수가 없다고, 무조건 error가 아니라는 것
왜냐하면 명령어 중에서 D가 없고 R만 있을 수 있으니

2) flag 변수 활용까지는 좋았다.
하지만, 결국 -1 일때는
마지막에 출력시 뒤집어 주어야 한다는 것.

'''