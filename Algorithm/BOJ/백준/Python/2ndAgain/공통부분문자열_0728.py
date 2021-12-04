# https://www.acmicpc.net/status?user_id=dhsys112&problem_id=5582&from_mine=1

# 첫번째 풀이 : 시간초과 ----
import sys
import heapq
import math
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
가장 긴것부터 해서,
sliding window
방식으로 구현하면 되지 않을까 ?

가장 긴 길이부터, 차례대로 줄여가면서
sliding window 방식으로 비교해가기 
'''
s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
slen, blen, sStr, bStr = -1, -1, '', ''

if l1 <= l2:
    slen, blen, sStr, bStr = l1, l2, s1, s2
else:
    slen, blen, sStr, bStr = l2, l1, s2, s1
res = 0
# 모든 종류의 길이에 대해서 --> i : 길이
for i in range(slen, 0, -1):
    # 해당 길이의 모든 부분문자열에 대해서 --> j : 문자열 시작위치
    for j in range(slen-i+1):
        strs = sStr[j: j+i]
        # 다른 비교 문자열에 대해서 --> k는 비교분자열 시작위치
        for k in range(blen-i+1):
            cstrs = bStr[k:k+i]
            if cstrs == strs:
                res = len(strs)
                print(res)
                exit(0)

# dp ---------
'''
이 문제는 'substring'을 구하는 문제이다
즉, 반드시 '연속성'을 만족시켜야 한다 

우리가 앞의 subsequence를 구할 때
d[i][j] : string1 의 i번째까지, string2의 j번째까지의 문자열, 까지의
공통 subsequence 를 의미했다 

string1 의 i번째 문자와
string2 의 j번째 문자가 같다면 ,
d[i][j] = d[i-1][j-1] + 1을 의미했고

그렇지 않다면 
d[i][j] = max(d[i][j-1],d[i-1][j]) 를 의미했다 
그런데, 이경우는 무슨 말이냐면, 현재 같지는 않으니
현재 만난 문자는 고려하지 않지만
앞에서 있었던 공통 subsequence 는 고려하겠다 !! 라는 의미이다
즉, 연속성을 만족하지 않아도 되기 때문에
이러한 식을 세울 수 있었던 것이다

하지만, substring 문제의 경우, 
반드시 '연속성'을 만족시켜야 한다
다른 말로 하면 ,
string1의 i번째 문자
string2의 j번째 문자가 같지 않게 된다면, 

연속성이 끊어진 것, 
substring이 끊어진 것

따라서 d[i][j] = 0을 만들어주면 되는 것이다 

'''
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
가장 긴것부터 해서,
sliding window
방식으로 구현하면 되지 않을까 ?
'''
a = input()
b = input()
n = len(a)
m = len(b)
a = " " + a
b = " " + b
d = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i] == b[j]:
            d[i][j] = d[i-1][j-1] + 1
        else:
            d[i][j] = 0
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if ans < d[i][j]:
            ans = d[i][j]
print(ans)
