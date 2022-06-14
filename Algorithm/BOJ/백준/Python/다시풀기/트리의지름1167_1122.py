# https://www.acmicpc.net/problem/1167

from collections import deque, Counter
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100001)
#

# bfs : 임의의 한점에서 가장 먼점과 그 거리를 리턴하는 함수


def bfs(num):
    maxDist, node = 0, num
    queue = deque()
    queue.append((num, 0))
    ch[num] = 1

    while queue:
        q = queue.popleft() #
        print("q", q)
        nowDist = q[1]
        nowNode = q[0]

        for n in adj[nowNode]:
            if ch[n[0]] == 0:
                ch[n[0]] = 1
                print("append", (n[0], nowDist + n[1]))
                queue.append((n[0], nowDist + n[1]))
                if maxDist < nowDist + n[1]:
                    maxDist = nowDist + n[1]
                    node = n[0]

    return node, maxDist


# 인접리스트 생성
n = int(sys.stdin.readline())
adj = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(tmp) - 1, 2):
        adj[tmp[0]].append((tmp[j], tmp[j+1]))

N, D = bfs(1)

# 체크리스트 초기화
for i in range(len(ch)):
    ch[i] = 0
print("N", D)
print(bfs(N)[1])
