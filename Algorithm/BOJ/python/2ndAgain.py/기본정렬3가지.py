# 문제 : https://www.acmicpc.net/problem/2750

# 버블 정렬
# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


n = int(input())

arr = [int(input()) for _ in range(n)]

# 버블 정렬
# 한번 정렬될때마다, 맨 뒤에는 가장 큰 값이 들어가있다
# 원소 개수만큼 반복
# 비교는, 정렬된 뒤쪽 원소 제외

for i in range(n):
    for j in range((n - 1) - i):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp

for x in arr:
    print(x)


# 선택 정렬
# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


n = int(input())

arr = [int(input()) for _ in range(n)]
minIdx = 0

# 선택 정렬
# 작은 것을 앞으로 보낸다
# 현재 자신 이후 원소들 중 가장 작은 값과, 자신을 교체
# 이러면서, 가장 작은 값들을 계속 차근차근 앞으로 보낸다
# 만약 현재 자신이 가장 작은 원소라면 ( 이후 원소들과 비교했을 때) 그때는 그저 pass


# 원소 개수만큼 반복
for i in range(n):
    min = 12391239
    for j in range(i, n):
        if min > arr[j]:
            min = arr[j]
            minIdx = j

    # 자신과 자신 이후 최소값 비교 및 교체
    tmp = arr[i]
    arr[i] = arr[minIdx]
    arr[minIdx] = tmp


for x in arr:
    print(x)


# 삽입 정렬
# 재귀함수 호출시 Memoization을 할 수 있는지를 물어본 문제
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


n = int(input())
arr = [int(input()) for _ in range(n)]

# 삽입정렬
# 자기와 왼쪽에 있는 값을 비교한다
# 만약 자기보다 왼쪽 값이 크다면, 왼쪽으로 가면서, 자신이 들어갈 위치를 찾아 삽입된다.
# 이렇게 원소 하나하나를 접근할 때마다, 왼쪽으로 원소들은 계속 정렬되어 간다
# 삽입정렬의 장점은, 왼쪽에 있는 것은 항상 정렬이 되어 있다고 가정한다는 점이다.

for i in range(n-1):
    # 현재 정렬한 원소를 선택해서, 적절한 위치에 넣어주기 위함이다.
    j = i
    while arr[j] > arr[j+1]:
        # j를 1씩 빼가면서, 왼쪽에 있는 값이 더 크면 바꿔주는 원리를 적용한다.
        tmp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = tmp
        j -= 1
        if j < 0:
            break

for elem in arr:
    print(elem)
