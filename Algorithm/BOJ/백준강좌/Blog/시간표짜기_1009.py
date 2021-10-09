# https://www.acmicpc.net/problem/14569

import itertools
from copy import deepcopy
import heapq
import sys
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(100000)

# 비어있는 시간에
# 추가로 신청할 수 있는 과목의 후보 개수
# 겹치더라도 모두 세야 한다 ( 후보이므로 )
# 1 << 50 (하나의 비트는 수업)

N = int(input())
classes = []

# 수업 비트마스크 제작
for _ in range(N):
    c = list(map(int, input().split()))
    num = 0
    for i in range(1, len(c)):
        num |= 1 << (c[i]-1)
    classes.append(num)
    # print(bin(num))

# 각 학생 비트마스크 제작
M = int(input())
studs = []
for _ in range(M):
    stud_n = 0
    stud = list(map(int, input().split()))
    for i in range(1, len(stud)):
        stud_n |= 1 << (stud[i]-1)
    studs.append(stud_n)

for stud_n in studs:
    ans = 0
    for class_n in classes:
        # 비트마스크로 비교해서,
        # class 의 1 자리가, stud_n 에서도 1자리이면 된다
        # 1) 둘을 & 연산 처리한다
        # 2) class_n 까지 잘라서, class_n과 비교한다
        # 3) 비교기준은 class
        # - 비교 연산 결과 ~ class 가 동일하면 된다
        # - 왜냐하면, class 가 들어가면 되는 것이기 때문이다
        l_class = len(bin(class_n)) - 2
        stud_class_len = stud_n & ((1 << l_class) - 1)
        comp = stud_class_len & class_n
        # print("comp           ",bin(comp))
        # print("stud_n         ",bin(stud_n))
        # print("class_n        ",bin(class_n))
        # print("stud_class_len ",bin(stud_class_len))
        if class_n == comp:
            ans += 1
    print(ans)
