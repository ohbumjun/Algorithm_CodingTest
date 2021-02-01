# https://www.acmicpc.net/problem/9663

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
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
col = [0] * ( n + 1 )
cnt = 0

def promising( i, col ):
    # 첫번째 행부터 검사
    flag = True
    k = 1

    while k < i and flag :
        # and가 아니라, or 이라는 점 !!! 
        if col[i] == col[k] or abs(col[i] - col[k]) == abs( i - k ):
            flag = False
        k += 1
    return flag


def n_queens( i, col ) :
    global cnt
    n = len(col) - 1
    if promising(i, col) :
        if i == n :
            cnt += 1
            return
        else:
            for j in range( 1 , n + 1) : # 열에 값 배치하기
                col[i+1] = j
                n_queens( i + 1, col )

n_queens( 0 , col)
print(cnt)
