# https://www.acmicpc.net/problem/12946

#!/usr/bin/python3

'''
나올 수 있는 후보군의 개수는
0 ~ 3

'X'가 하나도 없으면 0
'X'가 하나라도 있다면 그때는 1, 2, 3

'X'로 표시된 정점을 기준으로 주변을 서치
> 만약 인접한 정점 'X'가 없다 : '1' ( 1가지의 색으로만 칠하기 가능 )
> 만약 인접한 정점중 'X'가 있다
    둘중 하나
    >> 1) '2' 거나 : '이분 그래프'
    >> 2) '3' 거나 : '이분 그래프' 아님 

'''
import sys
sys.setrecursionlimit(1000000)
n = int(input())
a = [input() for _ in range(n)]
color = [[-1]*n for _ in range(n)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [0, 1, -1, 1, -1, 0]
ans = 0


def dfs(x, y, c):
    global ans
    # 여기에 들어왔다는 것은, 적어도 1개의 색은 칠해야 한다는 것
    color[x][y] = c
    ans = max(ans, 1)
    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 'X':
                # 여기에 왔다는 것은, 이웃한 X를 서로 다른 색으로 칠해야 하므로 최소 2개 color필요
                # 이분 그래프인지 판단해보기
                if color[nx][ny] == -1:
                    dfs(nx, ny, 1-c)

                ans = max(ans, 2)
                # 인접한 곳의 색이 같다는 것은, 이분 그래프가 아니라는 것
                # 따라서, 3
                if color[nx][ny] == c:
                    ans = max(ans, 3)


for i in range(n):
    for j in range(n):
        if a[i][j] == 'X' and color[i][j] == -1:
            dfs(i, j, 0)

print(ans)
