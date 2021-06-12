# https://programmers.co.kr/learn/courses/30/lessons/43164
# dfs ---
from collections import defaultdict

# 1) dictionary 를 이용하여 인접리스트 형태의 dict를 만든다
# 2) stack을 활용한 dfs를 이용할 것이다.
# 각 route 배열에서 맨 뒤의 것을 뽑는 형태를 택할 것이다
# 따라서, 각 route 배열을 내림차순 정렬한다
# 3) 경로가 존재할 때까지 stack에 쌓아가고
# 4) 더이상 경로가 없게되는 순간 ,stack 뒤에서 부터 뽑아서 ans 배열에 넣고
# 5) ans 에는, 경로의 반대순서가 저장되므로 reverse 시켜서 return 해준다


def solution(tickets):
    # 1) 경로 세팅, 2) sort< 내림차순 >, 3) stack을 이용한 dfs
    route = defaultdict(list)
    for key, val in tickets:
        route[key].append(val)
    # 모든 route 배열 순회하기
    for key, val in route.items():
        val.sort(reverse=True)  # 내림 차순 정렬 : stack을 이용해서 뒤에서 부터 뽑아갈 것이다

    flights = []
    flights.append("ICN")

    answer = []
    while flights:
        flight = flights[-1]
        if flight not in route or len(route[flight]) == 0:  # 그 다음 갈 경로가 더이상 없음
            answer.append(flights.pop())
        else:  # 경로가 존재한다면
            flights.append(route[flight].pop())

    answer.reverse()

    return answer
