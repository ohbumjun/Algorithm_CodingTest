# 

# 첫번째 풀이 : 시간 초과
'''
매번 새로운 idx마다 새로운 합들을 구해주면
그때그때마다 최댓값을 갱신
'''
import sys
sys.setrecursionlimit(100000)

arrLen , m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
lt = 0
rt = m - 1
res = 0

while rt < len(arr) :
    res = max( res, sum(arr[ lt : rt + 1 ]) )
    lt += 1
    rt += 1

print(res)
