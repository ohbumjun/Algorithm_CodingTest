# https://programmers.co.kr/learn/courses/30/lessons/49191

# 1) 파이썬 dfs --> stack을 활용한 dfs
import sys
from collections import deque
from collections import defaultdict


def solution(n, results):
    chart = [[0] * n for _ in range(n)]  # 승패표
    WIN, LOSE = 1, -1
    for i, j in results:  # 내입장 win = 상대방 lose
        chart[i-1][j-1], chart[j-1][i-1] = WIN, LOSE
    for me in range(n):
        wins = [opp for opp, rst in enumerate(chart[me]) if rst == WIN]
        while wins:
            loser = wins.pop()
            for opp, rst in enumerate(chart[loser]):
                # 왜 chart[me][opp] == 0 이라는 조건이 주어진 것일까 ?
                # 왜냐하면, 중복 방지를 위해서
                # me 가 winner 이고, me 에게 진 요소들은
                # 이미 wins 배열에 들어가 있다
                # 그리고 여기 for문에서는, 그 진 애들에게, 진 사람들 ,
                # 즉, 새롭게 진 사람들을 구하는 과정인 것이다
                if rst == WIN and chart[me][opp] == 0:
                    # A 가 B를 이겼다면, B가 이긴 C는, A 에게 무조건 진다
                    # 위 코드의 조건이, 아래 코드에 적용된 것이다
                    # 하지만, 왜 이러한 코드를 적용해야 하는 것일까 ??
                    # 분실된 경기결과에 대한 내용을 우선 모두 반영해놓고
                    # 나중에 가서, 이김, 짐에 대한 결과가 모두 반영된 결과물을 얻기 위함이다
                    chart[me][opp], chart[opp][me] = WIN, LOSE
                    wins.append(opp)
    # -1,1을 제외한 0(자기자신과의 결과)가 1개인 경우만 답을 구할 수 있다고 할 수 있다
    return len(['know' for x in chart if x.count(0) == 1])


# 2) 딕셔너리 활용하기
def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    loses = defaultdict(set)

    for a, b in results:
        wins[a].add(b)
        loses[b].add(a)

    for i in range(1, n+1):
        for loser in wins[i]:
            # |= : set 간에 accumulate function으로 활용될 수 있다
            loses[loser] |= loses[i]
        for winner in loses[i]:
            wins[winner] |= wins[i]

    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer


# 3) DFS
#sys.stdin = open("input.txt","rt")
cnt = 0


def DFS(graph, ch, vertex, flag, n):
    global cnt
    ch[vertex] = 1
    if flag == 1:
        for i in range(1, n+1):
            if graph[vertex][i] == 1 and ch[i] == 0:
                cnt += 1
                DFS(graph, ch, i, flag, n)
    elif flag == -1:
        for i in range(1, n+1):
            if graph[vertex][i] == -1 and ch[i] == 0:
                cnt += 1
                DFS(graph, ch, i, flag, n)


def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1)
    global cnt

    # 입력 값으로 그래프 만들기
    for result in results:
        graph[result[0]][result[1]] = 1
        graph[result[1]][result[0]] = -1

    for i in range(1, n+1):
        for j in range(1, n+1):
            ch[j] = 0
        cnt = 0
        # 승 수 계산
        DFS(graph, ch, i, 1, n)
        # 패 수 계산
        DFS(graph, ch, i, -1, n)
        # 승수와 패수를 모두 계산한
        if cnt == n-1:
            answer += 1

    return answer
