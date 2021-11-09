# https://www.acmicpc.net/status?user_id=dhsys112&problem_id=2212&from_mine=1

# 애초에 수신국을 어디로 정하냐는, 메인 point가 아니다
# 우리가 구해야 하는 것은, 각각의 수신가능영역의
# 최소거리값들의 합이 되어야 하는 것이다
# 수신가능영역은 말그대로 수신이 가능한 전체 영역.
# 수신가능영역의 길이는 반지름이 아니라 말그대로 수신이 가능한 전체 영역의 길이
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
pos = sorted(list(map(int, sys.stdin.readline().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n):
    dist.append(pos[i] - pos[i-1])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))
