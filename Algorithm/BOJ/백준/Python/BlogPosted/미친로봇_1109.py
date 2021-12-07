# https://www.acmicpc.net/problem/1405

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 각 가는 경로마다, check 배열 세팅
# path 개념으로, 만약, N 만큼 이동할시
# 해당 path 에 대한 확률을 계산한다.
num, E, W, S, N = map(int, input().split())
probs = [float(N/100), float(S/100), float(W/100), float(E/100)]
check = [[False]*30 for _ in range(30)]
tPaths = 0


def findPath(path, number, x, y):
    global check, tPaths
    if number == num:
        tPaths += path
        return
    for k in range(4):
        nx, ny = x + dx[k], y+dy[k]
        if probs[k] == 0:
            continue
        if check[nx][ny]:
            continue
        check[nx][ny] = True
        findPath(path * probs[k], number+1, nx, ny)
        check[nx][ny] = False


check[15][15] = True
findPath(1.0, 0, 15, 15)

print(tPaths)
