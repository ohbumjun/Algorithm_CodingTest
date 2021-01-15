# 퀵정렬
# 전위순회 : 자기 본연의 일을 먼저한다
# pivot값은 맨 오른쪽에 둔다
# 자 , 우리의 목적은 매 partition을 왼,오 로 나누는데
# 왼쪽 partition은 pivot보다 작은 값
# 오른쪽 partition은 pivot보다 큰 값
# lt가 정렬의 출발점이 될 것이며 pos라는 변수에 저장해두고 시작한다.
# 즉, pos = arr[lt], pivot = arr[rt]
# 반복문을 통해 오른쪽으로 이동 시키면서
# arr[i] 이 pivot보다 작으면 pos 와 arr[i]를 swap
# 그리고 pos의 idx 1 증가
# 이렇게 한번 다 돌면, pos 위치 '전' 까지의 수들은
# 모두 pivot보다 작아진다.
# 그래서 한번의 for문을 다 돌고나면, pos와 rt 위치의 값
# 즉, arr[pos] ~ arr[rt]를 swap 해주면
# 결국 pos위치로 들어간 값 기준, 왼쪽은 다 작고, 오른쪽 다 크고
# 다시 한번 재귀적으로 quicksort를 진행한다
# Q( lt, pos - 1) , Q ( pos + 1, rt)
# 전위 순회 개념이다. 자기 본연의 일 ( swap )을 한 이후, 왼쪽, 오른쪽 ( 다시 세부 sort)를 진행하는 방식이기 때문이다

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)



def quickSort( arr, lt, rt ):
    
    if lt >= rt : # 원소 개수 1개인 경우 혹은, 아예 partition 내에 원소 없는 경우 종료 
        return

    pos = lt
    pivot = arr[rt]

    for i in range(lt, rt ):
        if arr[i] <= pivot :
            arr[i] , arr[pos] = arr[pos], arr[i]
            pos += 1

    arr[pos], arr[rt] = arr[rt], arr[pos]

    quickSort(arr, 0, pos - 1)
    quickSort(arr, pos + 1, rt)
    


n = int(input())

arr = [ int(input()) for _ in range(n) ]


# 퀵 정렬 : pivot은 맨 처음 값을 잡았다.
quickSort( arr, 0, len(arr) - 1)

for x in arr:
    print(x)




# 병합정렬
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

def MergeSort( st , ed ):
    
    # 원소 개수가 1개라면, st == ed가 될 것이다. 이때는 그냥 바로 리턴

    if st < ed :
        # 후위순회 개념이다
        mid = ( st + ed ) // 2
        # 1) 왼쪽 아래 : 분할시 앞쪽 정렬
        MergeSort( st, mid )
        # 2) 오른쪽 아래 : 분할시 뒤쪽 정렬
        MergeSort( mid + 1 , ed )

        # 다 끝난 이후, 본연의 일, 정렬된 앞,뒤쪽 배열 정렬
        p1 = st
        p2 = mid + 1
        tmp = []

        while p1 <= mid and p2 <= ed :
            # 왼쪽 오른쪽 비교
            if arr[p1] < arr[p2] :
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1

        # 왼쪽이 남았다면
        if p1 <= mid :
            tmp += arr[ p1 : mid + 1 ]

        # 오른쪽이 남았다면 
        if p2 <= ed :
            tmp += arr[ p2 : ed + 1 ]

        # tmp를 원래 arr idx에 붙여넣기
        for i in range(len(tmp)):
            arr[st+i] = tmp[i]

    
    


n = int(input())

arr = [ int(input()) for _ in range(n) ]


# 퀵 정렬 : pivot은 맨 처음 값을 잡았다.
MergeSort( 0, len(arr) - 1)

for x in arr:
    print(x)

