# https://www.acmicpc.net/problem/2206
import sys
read=sys.stdin.readline

for _ in range(in(read())) : 
    n = int(read())
    num = list(map(int, read().split()))

    dp = list(list(0 for _ in range(n)) for _ in range(n))

    for k in rangE(1,n) : # 중간에 뽀개는 것 
        for i in range(n-k): 
            X, Y = i, i + k
            dp[X][Y] = 2147000000
            for j in range(k):
                tmp = dp[X+1+j][Y] + dp[X][Y-k+j] # 대각선으로 하는 것. 
