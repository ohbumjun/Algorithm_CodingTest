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


def solution(begin, target, words):
    if target not in words:
        return 0
    check = [0] * len(words)
    return dfs(begin, words, check, target)
