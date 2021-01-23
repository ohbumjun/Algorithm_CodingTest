# https://www.acmicpc.net/problem/1003
# 기본 원리 : 각 숫자에 대한 0,1 출력 횟수도 피보나치 수열을 따른다
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

num = int(input())

zero = [1,0,1]
one  = [0,1,1]

def cal(k):
    length = len(zero)
    if k >=  length:
        for i in range(length, k + 1):
            zero.append( zero[i-1] + zero[i-2] )
            one.append( one[i-1] + one[i-2] )
        
    print(zero[k], one[k])

for i in range(num):
    N = int(input())

    cal(N)
        
    
