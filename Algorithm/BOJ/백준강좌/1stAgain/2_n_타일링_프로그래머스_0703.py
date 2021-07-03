# https://programmers.co.kr/learn/courses/30/lessons/12900

# 첫번째 시도 : 시간 초과
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])
    return dp[n] % 1000000007

# 두번째 시도 : ok


def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]


'''
이것이 왜 맞는 것일까 ? 
왜냐하면, 
여기서는 숫자가 점점 커지는데
거대한 숫자끼리의 연산은 시간이 소요된다

다 더해서 마지막에 1000007 로 나누어주나, 
중간중간 값들을 100007로 나누어주면서 더하나
같은 결과값을 낼 것이기 때문이다 
'''
