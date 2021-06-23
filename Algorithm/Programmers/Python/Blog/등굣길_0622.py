# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    # m : 열, n : 행
    row, col = n, m
    # 웅덩이가 있는 공간은 0으로 만들어주면 된다
    # 해당 웅덩이를 0으로 만들어주면, 그 웅덩이에서 오는 경우의 수는 자연스럽게 0으로 만들어질 것이기 때문이다
    dp = [[0]*(col+1) for _ in range(row+1)]
    dp[1][1] = 1
    for i in range(1, row+1):
        for j in range(1,
                       col+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return (dp[row][col]) % 1000000007
