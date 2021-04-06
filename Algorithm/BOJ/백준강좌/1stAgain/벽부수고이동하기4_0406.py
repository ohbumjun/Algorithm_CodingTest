# https://www.acmicpc.net/problem/16946

# 처음 코드 : 시간 초과 --------------------------------------------------------------
import sys
from collections import deque
import heapq as hq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

N, M = map(int, input().split())
Map = [list(map(int, input())) for _ in range(N)]
arr = [[0] * M for _ in range(N)]


'''
모든 벽에 대해서 해당 경우수를 수행해 봐야 한다
= Brute Force


'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    res = 1
    bfsA = [[0] * M for _ in range(N)]

    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 0 and bfsA[nx][ny] == 0:
                res += 1
                bfsA[x][y] = 1
                queue.append((nx, ny))
    return res


for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            arr[i][j] = 0
        else:
            arr[i][j] = bfs(i, j)

for a in arr:
    print(''.join(map(str, a)))


# 해설 : 시간 초과 --------------------------------------------------------------
'''
크게 2가지 부분으로 나뉜다
1) 각각의 벽을 빈칸으로 바꾸기 = Brute Force => O(NM)
2) 그 칸에서 이동해보기 = BFS, DFS : O(NM) => 왜 ? 최대 전체칸을 이동해볼 수 있기 때문이다 

O(NM) * O(NM) = ( O(NM) ) ^ 2  = 1000 ^ 4

시간이 오래 걸려서 이 방법으로는 불가능하다



'''
