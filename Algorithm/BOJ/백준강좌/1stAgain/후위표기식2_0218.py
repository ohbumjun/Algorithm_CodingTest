# https://www.acmicpc.net/problem/1935

import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
import collections
sys.setrecursionlimit(100000)


'''

아래 코드에서 매우 효율적인 부분은

바로 알파벳 피연산자를, 해당 요소에 맞는
숫자로 바꿔넣는 다는 것이다

'''

n = int(input()) # 피연산자의 개수 
arr = input() # 후위 표기식
nums = [int(input()) for _ in range(n) ]
stack = [] # 스택 선언 

# 후위 표기식 숫자 배치
for i in arr :
    if 'A' <= i <= 'Z' : # 피연산자를 만나면
        stack.append(nums[ord(i) - ord('A')]) # 스택에 저장 
    else : # 연산자 이면
        str2 = stack.pop() # 스택에 저장되어 있던 피연산자 2개 pop
        str1 = stack.pop()

        if i == '+' :
            stack.append( str1 + str2 )
        elif i == '-' :
            stack.append( str1 - str2 )
        elif i == '*' :
            stack.append( str1 * str2 )
        elif i == '/' :
            stack.append(str1 / str2)

# 마지막에 스택에 남아있는 값 소수점 둘째자리 까지 출력
print('%.2f' %stack[0])
