import itertools
from copy import deepcopy
import heapq
import sys
from collections import deque, defaultdict, Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

# 한 기차당 20명이 쭈르륵
# 총 N개의 기차
# 1,2,3,4 총 4개의 명령
# 건널시, 같은 기록의 칸은 못건넌다
N, M = map(int, input().split())
trains = [0]*N

# 총 M개의 명령 동안 반복한다
for _ in range(M):
    orders = list(map(int, input().split()))
    # 원소 추가
    if orders[0] == 1:
        order, tN, sN = orders
        tN, sN = tN-1, sN-1
        trains[tN] |= 1 << sN  # sN 번째칸 1 추가
    # 원소 제거
    elif orders[0] == 2:
        '''
        # 1<<k는 k번째 bit만 켜진 상태이며, 여기에 NOT을 씌우면 k번째 bit만 꺼진 상태가 된다. 
        # 그러므로 AND 연산을 적용하면 k번째 bit만 0이 되고 나머지 bit는 변함이 없다. 

        '''
        order, tN, sN = orders
        tN, sN = tN-1, sN-1
        trains[tN] &= ~(1 << sN)  # sN번째 칸 1 제거
    elif orders[0] == 3:  # 모두 한칸씩 뒤로 (비트마스크 <<)
        order, tN = orders
        tN -= 1
        trains[tN] = trains[tN] << 1
        # print("3rd train", bin(trains[tN]))
        # print("3rd comp" , bin(((1<<20)-1)))
        # print("3rd",bin(trains[tN] & (((1<<20)-1))) )
        trains[tN] = trains[tN] & (((1 << 20)-1))
    elif orders[0] == 4:  # 모두 한칸씩 앞으로 (비트마스크 >>)
        order, tN = orders
        tN -= 1
        trains[tN] >>= 1
    # for t in trains : print(bin(t))
    # print()

trains = set(trains)
print(len(trains))
