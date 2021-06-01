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

왜냐하면, 꼭 1,3,5,6,9 이렇게 저장되어 있을때
1을 처리한다음 바로 3으로 간다는 보장이 없기 때문이다
9 idx가 거리상 가까우면 9로 넘어가야 하는 것인데
현재 내 코드는 그냥 순서대로 앞에서부터 
뒤로 가는 원리를 적용했기 때문에
틀리다고 할 수 있다 

'''

# 해결 코드


def solution(name):
    # 처음부터 각 알파벳에 대한 상하 이동 횟수를 저장한다
    make_name = [min(ord(n)-ord('A'), ord('Z')-ord(n)+1) for n in name]
    idx, answer = 0, 0

    while True:
        # 상하 이동
        answer += make_name[idx]
        make_name[idx] = 0

        # break 조건
        if sum(make_name) == 0:
            break

        # 좌,우 이동
        left, right = 1, 1
        while make_name[idx-left] == 0:
            left += 1
        while make_name[idx+right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right
    return answer


'''
자. 사실 여기서의 핵심은 
[idx-left] 혹은 [idx+right] 하는 과정에서
범위를 넘어서면 어떡하냐는 것이다

그리고 해당 코드가 올바르게 실행되기 위해서는
idx가 반드시 0으로 시작되어야 한다

------------------------------------------

1) left
left 부터 살펴보자 
idx-left가 - 가 되면 어떡하냐고 ?
python 문법상 배열에서 -1,-2는
자연스럽게 오른쪽 끝으로 이동하게 된다
따라서 이는 문제가 없다


2) right
사실 이 right이 문제다

왜냐하면 idx + right 이 len(name)을 벗어난다고
0부터 시작하는 원리는 아니기 때문이다 

예를 들어, 아래와 같은 문자열이 있었다고 해보자
J A A A B A C

이 경우, J를 처리한 다음
C로 갈건데
C에서 idx + right을 하는 순간 범위를 벗어나는 것이 아닌가 ?
라고 생각할 수도 있다

하지만, 이때의 idx 값을 살펴봐야 한다
J에서 바로 C로 갔다는 얘기는 left로 갔다는 것이고
0 idx에서 왼쪽으로 가면 -1 이다

즉, C 에 도착했을 때 idx는 len(name) -1 이 아니라
-1 이기 때문에 idx + right을 해도 범위에서 
벗어나는 일은 생기지 않는다는 것이다 
------------------------------------------


'''
