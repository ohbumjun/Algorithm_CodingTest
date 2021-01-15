# https://codeforces.com/problemset/problem/313/B

import sys
sys.stdin = open("input.txt", "rt")
import heapq as hq

def Count(st, ed):
    res = 0
    print("st,ed", st, ed )
    for i in range( st, ed ) :
        if arr[i] == arr[i+1] :
            res += 1
    return res

arr   = list(sys.stdin.readline())
res   = [0] * ( len(arr) + 1 )
cnt   =  0
Count = int(input())

for i in range(1, len(arr)  ) :
    '''
    if arr[i] ==  arr[i-1] :
        res[i+1] = res[i] + 1
    else: 
        res[i+1] = res[i]

    이거보다, 아래의 방법을 해야 time limit이 안걸린다 
    '''
    if arr[i] ==  arr[i-1] :
        cnt += 1

    res[i+1] = cnt
    

for _ in range(Count):
    m, n = map(int,input().split())
    print(res[n] - res[m])


    
