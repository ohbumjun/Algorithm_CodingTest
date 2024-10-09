# https://www.acmicpc.net/problem/12015

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000) ##

# 이진 탐색
def findPlace(tmp, val):
    lt = 1 # 어차피 tmp 맨 앞 0은 고려하지 않기 때문이
    rt = len(tmp) -1
    res = 0

    # 기존 이진 탐색과 다소 다르다
    # 일반적으로 이진 탐색은 tmp[mid] == val을 향해 찾아가지만
    # 여기는 tmp라는 배열 안에 정확한 val 값이 없을 수 있고
    # 현재 val이 들어갈 위치를 찾는 것이다. 그리고 그 위치는 lt, rt가 같은 
    while lt < rt :
        mid = ( lt + rt ) // 2
        if tmp[mid] < val : # val보다 작다면, 오른쪽 탐색
            lt = mid + 1
        elif tmp[mid] > val : # val보다 크다면, 왼쪽 탐색
            rt = mid 
        else : # lt와 rt가 가리키는 값이 똑같을 경우, 그곳이 새로운 val이 들어갈 위치
            lt = rt = mid
            break

    return lt
        

if __name__ == "__main__" :
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = [0]
 
    # 탐색하면서, 현재 마지막 값보다 크면 맨 끝에 넣는다
    # 만약, 맨 끝값보다 작거나 같은 값이 나온다면
    # 이진탐색을 통해, 새로 만난 값이 위치를 찾은 다음
    # 해당 위치에 넣는다
    # 마지막에는 총 배열 길이 - 1 ( 0 을 처음에 임의로 추가했기 때문이다 ) 

    for i in range(len(arr)):
        if arr[i] > tmp[-1] : # tmp에 0을 미리 넣어주고 시작해야 tmp[-1]이 out of idx 에러 안뜬다 
            tmp.append(arr[i])
        else:
            newIdx = findPlace(tmp,arr[i])
            tmp[newIdx] = arr[i]

    print(len(tmp) - 1)
            

