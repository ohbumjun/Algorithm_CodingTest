# https://www.acmicpc.net/problem/11780

# 모든 점에서, 다른 모든점까지의 최소 거리 = 플로이드 와샬 //
n = int(input())
m = int(input())

INT_MAX = int(1e9)
dp     = [[INT_MAX] * n for _ in range(n)]
cities = [[[] for _ in range(n)] for _ in range(n)]

# 자기 자신으로의 거리 0
for i in range(n):
    dp[i][i] = 0
    
for _ in range(m):
    st,ed,cst  = map(int,input().split())
    st,ed      = st-1,ed-1
    if cst < dp[st][ed] : 
        dp[st][ed] = cst
        cities[st][ed] = []
        cities[st][ed].append(st + 1) #

# for d in dp : print(d)

# 플로이드 와샬을 이용해서, 한 도시에서 다른 도시로 가는 비용 계산
for k in range(n):
    for r in range(n):  #
        for c in range(n):
            if dp[r][c] > dp[r][k] + dp[k][c] :
                dp[r][c] = dp[r][k] + dp[k][c]
                cities[r][c] = cities[r][k] + cities[k][c] 
                

# 경로없는 경우 비용 0으로
for r in range(n):
    for c in range(n):
        if dp[r][c] == INT_MAX :
            dp[r][c] = 0
        else :
            cities[r][c].append(c+1)
# 비용 출력 
for d in dp : print(' '.join(map(str,d)))
# 경로 출력
for r in range(n):
    for c in range(n):
        if dp[r][c] == 0 :
            print(0)
        else :
            print(len(cities[r][c]), end = ' ')
            print(' '.join(map(str,cities[r][c])))