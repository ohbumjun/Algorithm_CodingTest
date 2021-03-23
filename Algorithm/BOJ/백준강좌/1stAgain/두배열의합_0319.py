# https://www.acmicpc.net/problem/2143

'''
부분배열과 부배열은 다르다 !

부배열은, 계속 원소들이 서로
이어붙어져 있어야 한다. 

부배열은 처음 시작점 i, 끝점 j로 정해지기 때문에
총 n ^ 2 개의 부배열이 존재할 것이다.

A의 부배열의 합
B의 부배열의 합 

둘다 100만개씩의 부배열이 존재할 수 있다 ( 1000개가 최대이므로 )

'''
import sys
import heapq
from collections import Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

T = int(input())
aLen = int(input())
aArr = list(map(int, input().split()))
bLen = int(input())
bArr = list(map(int, input().split()))
res = 0

aSumArr = []
bSumArr = []

# 부배열의 경우 i번째 부터 j번째 까지의 합이다.
# 부분배열을 만들어줄 때는 1 << n 형태를 사용했다
# 하지만, 여기서는, 일반 for문2개를 돈다 ( 그래야만 서로 붙어있는 원소들끼리의 합을 구한다 )
for i in range(aLen):
    sum = 0
    for j in range(i, aLen):
        sum += aArr[j]
        aSumArr.append(sum)

for j in range(bLen):
    sum = 0
    for j in range(j, bLen):
        sum += bArr[j]
        bSumArr.append(sum)


aSumArr.sort()
bSumArr.sort()

# aSumArr 을 앞에서부터 순회하면서 aSumArr[i]
# bSumArr 중에서 T - aSumArr[i]의 개수를  더한다
# 특정 배열에서, 특정 숫자를 찾는 방법은
# 1) 배열 전체 순회 ( 시간 초과 문제 )
# 2) 이분 탐색
# 3) Hash 사용 ( 여기서 Counter를 통해 제작 )

c = Counter(bSumArr)
res = 0

for i in range(len(aSumArr)):
    res += c[T-aSumArr[i]]

print(res)
