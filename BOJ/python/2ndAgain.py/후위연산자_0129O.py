# https://www.acmicpc.net/problem/1918

# 첫번째 풀이 : 오답 -----------------------------------
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)
import heapq as hq

'''
비연산자의 경우, 바로 배열로 넘겨버린다.

연산자 스택이 이제 중요한대,

/, * 는 + , - 위에 올 수 있지만,
+ , - 는 /, * 위에 올 수 없다.

같은 우선순위의 경우, 기존 것을 배열로 보내고,
그 다음 쌓는다

그렇다면 괄호는 어떻게 해야 하는 것인가 ??

----------------------------------------------

소괄호를 만나면, 우선, 새로운 바닥을 만드는 것이다.
여는 소괄호를 만나면, 우선 쌓는다.

쌓는 규칙은 기존의 방식과 동일하게 진행한다.
다만, 닫는 괄호를 만나게 된다면, 
그때는 소괄호를 만날 때까지, 모든 연산자를 빼서, 스택에 넣는다.
'''

arr     = list(input())
res     = []
stack   = []
Cal     = ['+','-','*','/','(',')']
lowCal  = ['+','-']
highCal = ['/','*']

for x in arr :
    if x not in Cal :
        res.append(x)
    elif x in lowCal :
        if stack and stack[-1] != '(':
            res.append(stack.pop())
            stack.append(x)
        else:
            stack.append(x)
    elif x in highCal:
        if stack and stack[-1] in highCal :
            res.append(stack.pop())
            stack.append(x)
        else:
            stack.append(x)
    elif x == '(':
        stack.append(x)
    elif x == ')' :
        while True:
            if stack and stack[-1] == '(':
                stack.pop()
                break
            else:
                res.append(stack.pop())

if stack:
    while len(stack) > 0 :
        res.append(stack.pop())

print(''.join(res))
            
        
# 두번째 풀이 -------------------------------------------------


arr     = list(input())
res     = []
stack   = []
Cal     = ['+','-','*','/','(',')']
lowCal  = ['+','-']
highCal = ['/','*']

for x in arr :
    if x not in Cal :
        res.append(x)
    elif x in lowCal :
        # while !!! 즉, if가 아니다 !! 계속 아래의 pop, append과정을 반복해야 하는 것이다
        while stack and stack[-1] != '(':
            res.append(stack.pop())
        stack.append(x)
    elif x in highCal:
        # while !!! 즉, if가 아니다 !! 계속 아래의 pop, append과정을 반복해야 하는 것이다
        while stack and stack[-1] in highCal :
            res.append(stack.pop())
        stack.append(x)
    elif x == '(':
        stack.append(x)
    elif x == ')' :
        while True:
            if stack and stack[-1] == '(':
                stack.pop()
                break
            res.append(stack.pop())

if stack:
    while len(stack) > 0 :
        res.append(stack.pop())

print(''.join(res))
            
        
    