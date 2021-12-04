import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)
import heapq as hq

def postOrder( st , ed ):
    if st > ed :
        return
    pivot = ed + 1
    for i in range( st + 1, ed + 1 ):
        if arr[i] > arr[st] :
            pivot = i
            break
    # 왼
    postOrder( st + 1 , pivot - 1 )
    # 오
    postOrder( pivot , ed )
    # 본
    print(arr[st])

arr = []
while True:
    try :
        arr.append(int(input()))
    except:
        break

postOrder( 0 , len(arr) - 1 )

'''
50, 30 24 5 28 45 , 98 52 60

전위순회한 결과이다
전위순회는 본인 + 왼쪽 + 오른쪽. 순서로 출력이 이루어진다.

그런데 자세히 보면,
전위순회 결과를 살펴보면,
루트값, 즉, 맨 처음값을 기준으로

뒤에 가다가 더 큰 숫자들은, 오른쪽 서브트리에 위치한 것,
더 작은 숫자들은 왼쪽 서브트리에 위치한 것 

후위 순회는
왼 > 오 > 루트.

즉, 오른쪽 시작점을 잡고,

왼, 오, 루트 출력
식의 재귀함수를 구현하면 된다 

'''