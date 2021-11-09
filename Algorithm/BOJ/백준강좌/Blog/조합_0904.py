

from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

# 분모의 m 팩토리얼을 dp로 구한다
fact = [1]*(n+1)
for i in range(1, n+1):
    fact[i] = fact[i-1] * i

# 분자 구하기
s = 1
for i in range(m):
    s *= (n-i)

print(s//fact[m])
