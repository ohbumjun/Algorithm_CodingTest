# https://www.acmicpc.net/problem/14003

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

def lower_bound( st, ed, target ):
    while st < ed :
        mid = ( st + ed ) // 2
        if res[mid] == target :
            ed = mid
            break
        elif res[mid] < target:
            st = mid + 1
        else : # arr[mid] > target
            ed = mid
    return ed

n = int(input())
arr = [0] +  list(map(int, sys.stdin.readline().split()))
d = [0] * ( n + 1 ) # d[i] : i 숫자가 나올때, 최대 부분 증가수열길이 , i는 arr 상 특정 숫자의 idx , 사실 
res = [-1000000002] # res[i] : 길이값, 즉, res[1] 은, 곧, 최대부분증가수열 길이가 1이라는 것,
# i는 그때의 가장 작은 마지막 값
maxLen = 0 # 최대길이

for i in range( 1,  len(arr) ): # i는 idx 개념이다.
    if arr[i] > res[-1] :
        res.append(arr[i])
        d[i] = len(res) - 1 
        maxLen = d[i]
    else:
        # d[i] : arr[i]이 마지막 증가수열 일때의, 길이 
        d[i]      = lower_bound(1, len(res) - 1, arr[i])
        res[d[i]] = arr[i]

print(maxLen)
stack = []


for i in range( n , 0, -1 ):
    if d[i] == maxLen :
        stack.append(arr[i])
        maxLen -= 1

stack.reverse()
for x in stack:
    print(x , end = ' ')



'''

2가지를 조심해야 한다

1) lower_bound 에서
res를 찾는 것이 아니라, arr 배열을 대상으로 찾는 경우

2) lower_bound(1, len(res) - 1, arr[i]) 에서
시작 idx를 1이 아닌, 0으로 주는 

'''

