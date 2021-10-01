# 가장 긴 증가하는 부분 수열 4
# https://www.acmicpc.net/problem/14002
# help : https://www.crocus.co.kr/680

'''
여기서는 dp로 풀어보는데,

우리가 dp 배열에 저장하는 값들이,
실제, 최대부분 증가수열은 아니다.

ex
dp  : 1 2 2 3 4 3 4 5
arr : 1 6 2 5 7 3 5 6

그러면, 우리가 실제
구해지는 최대부분 증가수열을 구하기 위해서는
dp 기준 뒤에서부터
조사해오면 되는 것이다. 

즉, 최댓값을 만나면, 그때부터
-1 씩해주면서 오는 것이다.

그렇게 뒤에서부터 오면서
res 라는 배열에 append 해주고,
출력은 뒤집어서 출력해주면 되는 것이다. 

'''
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

def lower_bound( st, ed ,num ):
    while st < ed :
        mid = ( st + ed ) // 2
        if arr[mid] < num :
            st = mid + 1
        elif arr[mid] > num :
            ed = mid
        elif arr[mid] == num:
            ed = mid
    return ed       
    

n = int(input())
arr = list(map(int,input().split()))
dp = [0] * ( n )
dp[0]= 1
res = 0
resArr = []

for i in range(len(arr) ) :
    maxLen = 0
    for j in range( i ):
        if arr[i] > arr[j] and dp[j] > maxLen :
            maxLen = dp[j]
    dp[i] = maxLen + 1
    res = max(res, dp[i])

print(res)

for i in range( len(arr) -1 , -1, -1 ) :
    if dp[i] == res:
        resArr.append(arr[i])
        res -= 1

print(' '.join(list(map(str, reversed(resArr)))))
        
    

