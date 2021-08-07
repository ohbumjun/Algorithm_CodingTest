# https://programmers.co.kr/learn/courses/30/lessons/60059

import copy


def rotate(key, m): 
    # rotate 변경사항 저장할 배열
    rst = [[0] * m for _ in range(m)]
    # 원래 애를 갖다가 쭉 돌면서 ( key 배열 )
    for i in range(m):
        for j in range(m):
            # 행은, 위에서, 아래로 // 열은 , 왼쪽에서, 오른쪽으로
            # ---
            # 열.을 기준으로 생각한다면, 회전 후 위치의 관점에서는 위에서 아래로
            # 따라서 key의 j가 rst의 i로 간다고 생각하면 된다
            # ---
            # 행.을 기준으로 생각한다면,
            # 회전 후 위치의 관점에서는, 오른쪽에서 왼쪽으로
            # 따라서 key의 m-1-i가 , rst의 행이 된다
            rst[j][m-1-i] = key[i][j]
    return rst


def test(key, lock, i, j, m, n):
    dump = copy.deepcopy(lock)
    # i,j는 음수일 수 있다
    # i : key 배열 기준, 맨 왼쪽 윗칸
    for p in range(i, i+m):
        if 0 <= p < n:
            for q in range(j, j+m):
                if 0 <= q < n:
                    # lock의 임장에서 key의 위치가 - 일 수 있다
                    # 하지만 key의 관점에서는 0 부터 m-1 까지만 돈다
                    dump[p][q] += key[p-i][q-j]
    # 각각의 값 모두가 1이 되어야만, 암호가 풀린 것으로 인식될 수 있다
    for line in dump:
        for item in line:
            if item != 1:
                return False
    return True


def solution(key, lock):
    # 벗어난 부분에 대한 고려  ---
    # key의 오른쪽 아래 부분이, Lock의 왼쪽 위 부분에 오는 지점에서 시작
    # key의 왼쪽 위 부분이, Lock의 오른쪽 아래 부분에 오는 지점에서 끝
    # 즉, 최소 한개씩만 겹치게 설정하면 된다는 것이다

    # lock이 풀렸는지에 대한 검사 ---
    # 왼쪽 위부터, 오른쪽 아래까지
    # 각 칸의 합이 더해서 1이라면, 답이 될 것이다
    m, n = len(key), len(lock)
    for _ in range(4):
        # i,j는 lock의 맨왼쪽위 idx
        for i in range(-m+1, n):
            for j in range(-m+1, n):
                if test(key, lock, i, j, m, n):
                    return True
        key = rotate(key, m)

    '''
    헷갈리는 부분이 있을 수도 있다
    왜 4번만 돌리느냐 !
    반대로 생각하면, 각 key의 위치에서 4번씩 돌리고,
    그것을 가능한 위치 모두에 대해 적용한다고 생각하면 된다
    즉
    1st: 각 회전마다 모든 위치 조사하가
    2nd: 모든 위치마다 4번씩 회전시켜 조사하가
    둘다 같은 개념으로 접근할 수 있다는 것이다 
    '''
    return False
