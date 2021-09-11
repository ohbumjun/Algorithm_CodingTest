# https://www.acmicpc.net/problem/1790
from copy import deepcopy
import sys
from functools import reduce
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

n, k = map(int, input().split())
length = 0

# 특정 숫자까지의 자리수 구하기


def calLen(num):
    start, end, length, ans = 1, 10, 1, 0
    while True:
        end, start = end-1, start-1
        if start >= num:
            break
        if end > num:
            end = num
        ans += (end - start) * length
        end, start = (end+1) * 10, (start+1) * 10
        length += 1
    return ans


ans = 0
left = 1
right = n

# 문제 조건
if calLen(n) < k:
    print(-1)
    exit()

# 이분 탐색을 통해 k 근접의 총자릿수를 갖는 ans 찾기
while True:
    if left <= right:
        mid = (left+right)//2
        length = calLen(mid)
        if length < k:
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    else:
        break

c_len = calLen(ans)
s_len = len(str(ans))

# 해당 차이만큼 끝에서부터 빼주기
print(str(ans)[s_len-1-(c_len-k)])
