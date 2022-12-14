# https://programmers.co.kr/learn/courses/30/lessons/81302

# 첫번째 풀이
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(places): #
    answer = []
    rlen = len(places)
    clen = len(places[0])
    # 대기실별 2차원 문자열 배열
    for place in places:
        print()
        # place : 2차원 배열 --> 한개의 대기실
        # 2차원 배열 탐색 --> 사람 발견
        # 사람 발견 --> bfs : 거리 2 이하
        # 거리 1 이하 다른 응시자 발견 : 바로 false
        # 거리 2 이하 --> 이전 위치가 빈테이블일 경우 false
        # 거리 3 넘어가면 break
        # 즉, bfs 를 실행할 때, 그 이전위치들도 고려하면서 진행하기
        ans = False
        ch = [[0]*clen for _ in range(rlen)]
        for i in range(rlen):
            for j in range(clen):
                if place[i][j] == "P":
                    # bfs
                    q = deque()
                    q.append((i, j, "P", 0))
                    searchCp = 0
                    ch[i][j] = 1
                    while q:
                        x, y, item, d = q.popleft()
                        if d == 2:
                            break
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if 0 <= nx < rlen and 0 <= ny < clen and ch[nx][ny] == 0:
                                if place[nx][ny] == "P" and d == 0:
                                    ans = True
                                    break
                                if place[nx][ny] == "P" and d == 1 and item != "X":
                                    ans = True
                                    break
                                q.append((nx, ny, place[nx][ny], d+1))
                                ch[nx][ny] = 1
                        if ans:
                            break
                if ans:
                    break
            if ans:
                break
        if ans:
            answer.append(0)
        else:
            answer.append(1)

    return answer


# 2번째 풀이
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(places):
    answer = []
    rlen = len(places)
    clen = len(places[0])
    # 대기실별 2차원 문자열 배열
    for place in places:
        print()
        # place : 2차원 배열 --> 한개의 대기실
        # 2차원 배열 탐색 --> 사람 발견
        # 사람 발견 --> bfs : 거리 2 이하
        # 거리 1 이하 다른 응시자 발견 : 바로 false
        # 거리 2 이하 --> 이전 위치가 빈테이블일 경우 false
        # 거리 3 넘어가면 break
        # 즉, bfs 를 실행할 때, 그 이전위치들도 고려하면서 진행하기
        ans = False
        for i in range(rlen):
            for j in range(clen):
                if place[i][j] == "P":
                    # bfs
                    ch = [[0]*clen for _ in range(rlen)]
                    q = deque()
                    q.append((i, j, "P", 0))
                    ch[i][j] = 1
                    while q:
                        x, y, item, d = q.popleft()
                        if d == 2:
                            break
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if 0 <= nx < rlen and 0 <= ny < clen and place[nx][ny] != "X":
                                if ch[nx][ny]:
                                    continue
                                if nx == i and ny == j:
                                    continue
                                if place[nx][ny] == "P":
                                    ans = True
                                    break
                                q.append((nx, ny, place[nx][ny], d+1))
                                ch[nx][ny] = 1
                        if ans:
                            break
                if ans:
                    break
            if ans:
                break
        if ans:
            answer.append(0)
        else:
            answer.append(1)

    return answer


'''
풀이 : 관건은 거리가 2 이내 이되, X를 사이에 두는지를 검사하는 것이었다
정말 깔끔하게 애초에 거리 2이내만을 조사하는 상황에서
X를 거쳐가는 경우에는, 무조건 조건을 만족하게 되는 것

따라서, X를 거쳐가지 않으면서
거리가 2 이내인 경우가 있는지만 조사하면
정말 깔끔하게 문제를 풀어낼 수 있다 

s
'''
