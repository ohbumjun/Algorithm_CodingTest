# https://www.acmicpc.net/problem/9663

import collections
import heapq
from collections import deque, Counter
import sys
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


'''
상태트리를 가지치기 할때
그 다음 요소가 promisiing 한지 아닌지를
판단해야 한다.

row만으로 state tree 만들고
각 레벨마다
col, diagnal이 promising 한지 아닌지를 판별해보자

즉, 2개의 퀸, 이전 퀸과 현재 퀸이
같은 열 , 혹은
같은 대각선상.
에 위치하는지를
확인해야 한다. 


col[i] == col[k]

col[i]  : ith row에 있는 column
col[k]  : kth row에 있는 column

// 대각선을 체크하는 방법은 ?
abs( col[i] - col[k] ) == abs( i - k )

< sudo-code 는 다음과 같다 >

void checknode( node v ){ // v : row 에 해당한다.

    node u ;
    if ( promising(v) ) :
        if( v에 해답이 있다면 ) :
            해답 출력
        else:
            for v의 모든 자식 노드 v에 대해 :
                checknode(u)
}

'''

n = int(input())
col = [0] * (n + 1)
cnt = 0


def promising(i, col):
    # 첫번째 행부터 검사
    flag = True
    k = 1
    # for문이 아니라, while문을 통해서 구현해야 한다는 점 !
    while k < i and flag:
        # and가 아니라, or 이라는 점 !!!
        if col[i] == col[k] or abs(col[i] - col[k]) == abs(i - k):
            flag = False
        k += 1
    return flag


def n_queens(i, col):
    global cnt
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            cnt += 1
            return
        else:
            for j in range(1, n + 1):  # 열에 값 배치하기
                col[i+1] = j
                n_queens(i + 1, col)


'''
이제 중요한 것이다.
시작 row를 0으로 한다는 것.
사실상 row 0, col 0은 사용하지 않는다

row를 0 값으로 시작하는 이유는, 
이후 row 1 에다가 , 모든 값들을 setting 하여
시작하기 위한 발판의 역할이다 

'''
n_queens(0, col)
print(cnt)


# 백준 문제풀이 1번째

# 백준 문제풀이 2번째 ( 검사 단계 간소화 )

# check ~  : 해당 열, 대각선에 값이 존재하는지 안하는지 > 존재하면, 거기에 퀸을 두면 안된다
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)


# queen 함수 : 해당 row에서 queen을 놓기
# check 함수 : 해당 row, col에 queen을 놓을 수 있는지 없는지 검사하기

def queen(row):
    if row == n:
        global res
        res += 1
        return
    # 우선, 모든 열에 배치 해보기
    # 그 다음에, 해당 row, col에 위치시킬 수 있는지를 검사
    # 아래로 내려갈 때에는 우선, 방문 체크
    # 해당 start지점 이후에 대해 검사가 끝나면, 다시 올라와서
    # 다른 지점들도 검사해주어야 하기 때문에 방문 해제
    for col in range(n):
        if check(row, col):
            check_col[col] = 1
            check_digL[n+row-col-1] = 1
            check_digR[row+col] = 1
            arr[row][col] = 1

            queen(row + 1)

            check_col[col] = 0
            check_digL[n+row-col-1] = 0
            check_digR[row+col] = 0
            arr[row][col] = 0
    return


def check(row, col):
    global n
    if check_col[col]:
        return False
    # 해당 좌표의 왼쪽 대각선 목록 : n + 행 - 열 -1( 오른쪽 상단이 첫번째 idx )
    if check_digL[n+row-col-1]:
        return False
    if check_digR[row+col]:  # 해당 좌표의 오른쪽 대각선 목록 : 행 + 열
        return False

    return True


n = int(input())
res = 0
arr = [[0] * n for _ in range(n)]
check_col = [False] * n
check_digL = [False] * (2 * n - 1)
check_digR = [False] * (2 * n - 1)
queen(0)
print(res)
