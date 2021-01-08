import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

n = int(input())
arr = list()
for i in range(n):
    string = input()
    strL = len(string)
    arr.append((strL,string))

# 중복 삭제
arr = list(set(arr))

# 길이 > 알파벳
arr = sorted(arr, key = lambda elem : ( elem[0] , elem[1] ) )

for x in arr :
    print(x[1])
