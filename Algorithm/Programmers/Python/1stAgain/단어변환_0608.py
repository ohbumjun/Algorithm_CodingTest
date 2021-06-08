# https://programmers.co.kr/learn/courses/30/lessons/43163

# bfs
from collections import deque


def bfs(begin, length, words, target):
    # 최소 거리 : 한번의 변환 set를 묶어서 생각한다
    # 즉 정점의 정의는 : 각 알파벳
    # 간선의 정의는, 한번의 알파벳 변환이다
    check = [0] * length
    queue = deque()
    queue.append(begin)
    answer = 0
    while queue:
        for cur in queue:
            if cur == target:
                return answer
            tmp = deque()
            for w in range(len(words)):
                if len([i for i in range(len(words[w])) if words[w][i] != cur[i]]) == 1:
                    if check[w] == 0:
                        check[w] = 1
                        tmp.append(words[w])
        queue = tmp
        answer += 1
    return answer


def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, len(words), words, target)

# dfs
# 스택을 활용한 dfs


def dfs(begin, words, check, target):
    stack = []
    stack.append(begin)
    answer = 0
    while stack:
        word = stack.pop()
        if word == target:
            return answer
        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i] != word[i]]) == 1:
                if check[w] == 1:
                    continue
                check[w] = 1
                stack.append(words[w])
        answer += 1


'''
의문점 : 이게 무조건 최소거리를 리턴하는 것인가 ?
사실 bfs 랑 원리는 똑같다. 
계속 같은 거리,
같은 횟수으 변환이 필요한 알파벳들을
세트로 묶어가는 과정이다

예를 들어
stack, ans
hit     0
hot     1
dot,lot 2
lot,dog 3
dog,log 4

이러한 과정으로 진행된다

여기서 주목할점은 dot을 뽑은 이후, 
'''


def solution(begin, target, words):
    if target not in words:
        return 0
    check = [0] * len(words)
    return dfs(begin, words, check, target)
