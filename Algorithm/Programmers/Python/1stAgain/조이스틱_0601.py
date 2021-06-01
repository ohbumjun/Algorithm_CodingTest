# https://programmers.co.kr/learn/courses/30/lessons/42860

# 최초 풀이
def solution(name):
    # 그러면 , 처음부터, 알파벳 AAA 와 다른 위치idx 들을 저장해둬야 하는 것인가
    move = 0
    # 0. 예외 case : 해당 배열에 아무것도 없을 경우 !
    # 이때는 그냥 name의 길이 - 1 을 return 시켜준다
    # 1. 먼저, A가 아닌 알파벳들의 idx를 순서대로 배열에 넣는다
    # 2. 해당 idx에서의 알파벳에 대해 조이스틱(위,아래) 적용한다
    # 단, 당연히, 위가 가까운지, 아래가 가까운지 탐색한다
    # 3. 해당 배열을 탐색하면서, 어떤 idx에 접근해야 하는지를 살핀다 (좌,우)
    # 마찬가지로, 좌우 어디가 더 가까운지를 탐색한다
    diff = []
    for i in range(len(name)):
        if name[i] != 'A':
            diff.append(i)
    if len(name) == 0:
        return name - 1
    idx = 0
    while True:
        # 위,아래 탐색
        if ord(name[diff[idx]]) - ord('A') <= ord('Z') - ord(name[diff[idx]]) + 1:
            move += ord(name[diff[idx]]) - ord('A')
        else:
            move += ord('Z') - ord(name[diff[idx]]) + 1

        if idx == len(diff) - 1:
            break

        # 좌,우 탐색
        if diff[idx+1] - diff[idx] < len(name) - diff[idx+1] + diff[idx]:
            move += (diff[idx+1] - diff[idx])
        else:
            move += (len(name) - diff[idx+1] + diff[idx])

        idx += 1
    return move


'''
왜 이 문제는 틀린 것일까 ?


'''
