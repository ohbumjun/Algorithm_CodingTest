# https://programmers.co.kr/learn/courses/30/lessons/12900

# 첫번째 시도 : 시간 초과
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])
    return dp[n] % 1000000007
