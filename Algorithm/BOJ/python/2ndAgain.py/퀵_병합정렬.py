# 퀵정렬 1번째 버전
# 전위순회 : 자기 본연의 일을 먼저한다
'''
자기 본연의 일을 먼저한다니 ....?
무슨 말이냐면, 
1) 자신을 일정 기준을 갖고 정렬을 하고
2) 왼쪽 자식 정렬
3) 오른쪽 자식 정렬
을 실시한다는 것이다.

그렇다면, 1) 의 과정을 살펴보자
pivot값을 맨 오른쪽으로 두고
pos를 맨 왼쪽 값
i도 맨왼쪽값

자. 이제 우리가 할일은 i를 통해서
배열 전체를 돌면서 정렬을 실시할 것이다.

그렇다면 어떻게 정렬을 실시할 것이냐 !
내 목표는
정렬을 마친 이후에 !

pivot 값. 맨 오른쪽 값을 기준으로
왼쪽에는 pivot보다 작은 값
오른쪽에는 pivot보다 큰 값.
을 정렬할 것이다.

i를 통해 배열을 돌면서 ,
pivot보다 작은 값을 search 할 것이다.

만약 pivot보다 작은 값을 발견하게 되면 
pos가 가리키고 있는 값과 i를 바꿔주고
pos는 1 증가시켜준다. 

만일 22 33 66 44 55 였다고 해보자
22 = pos
22 = i
55 = pivot

이제 i를 보면, pivot보다 작으니까
pos와 바꿔주는데 지금은 pos 와 i 가 같은 위치에 있다.
뭐 바꿔준 것이라고 치면 되니까

이제 pos도 1증가, i도 1증가 시켜준다.
33은 pivot보다 작다. 그래서 pos ~ i를 바꿔주는데
지금도 둘다 같은 값에 있으므로 변화가 없다

이제 i, pos를 또 1 증가시켜준다.
66은 pivot보다 크다. 그러면 pos는 그대로 두고
i를 1증가시킨다.
44 = i
66 = pos

44는 pivot보다 작다. 
그러면 pos와 44를 바꿔서 정렬한 이후

22 33 44 66 55
pos와 1을 둘다 증가시켜준다. 
이제 i는 55, 
pos는 66 를 가리킨다.

이렇게 i가 모든 값을 돌았을 때, 
55와 66을 교체한다.

그러면 결과적으로
22 33 44 55 66
이 된다. 


'''
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


def quickSort(arr, lt, rt):
    if lt >= rt:  # 원소 개수 1개인 경우 혹은, 아예 partition 내에 원소 없는 경우 종료
        return
    pos = lt
    pivot = arr[rt]

    for i in range(lt, rt):
        if arr[i] <= pivot:
            arr[i], arr[pos] = arr[pos], arr[i]
            pos += 1

    arr[pos], arr[rt] = arr[rt], arr[pos]

    quickSort(arr, 0, pos - 1)
    quickSort(arr, pos + 1, rt)


n = int(input())
arr = [int(input()) for _ in range(n)]

# 퀵 정렬 : pivot은 맨 마지막 값을 잡았다.
quickSort(arr, 0, len(arr) - 1)

for x in arr:
    print(x)

# 퀵정렬 2번째 버전 -------------------------------------------------
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)

n = int(input())
arr = [int(input()) for _ in range(n)]
print(arr)


def quickSort(arr, low, high):
    if low < high:
        pivotpoint = partition(arr, low, high)
        quickSort(arr, low, pivotpoint - 1)
        quickSort(arr, pivotpoint + 1, high)


def partition(arr, low, high):
    pivotitem = arr[low]  # 맨 앞의 값을 pivot으로 잡는다
    i = low + 1
    j = high

    while i <= j:
        while arr[i] < pivotitem:
            i += 1
        while arr[j] > pivotitem:
            j -= 1
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]  # swap

    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]

    return pivotpoint


quickSort(arr, 0, len(arr) - 1)
print(arr)


# 병합정렬
'''
병합정렬은 기본적으로 후위순회.이다.
1) 왼쪽 나누고
2) 오른쪽 나누고
3) 그 다음에 본연의 일

우선 나누는 과정을 먼저 한다
lt , rt ( 처음 , 끝 )
mid = ( lt + rt ) // 2

1) DSort( lt , mid )
2) DSort( mid + 1, rt )
3) 합치기 

'''
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10000)


def MergeSort(st, ed):
    '''
    병합정렬의 경우 , 후위순회 이다
    왼쪽 자식의 일을 진행
    오른쪽 자식의 일을 진행
    자기 본연의 일

    위와 같은 3단계의 일로 진행한다.
    왼쪽 자식의 일이라는 것은,
    왼쪽 일부 자식도 마찬가지로 MereSort를 진행하고
    오른쪽 일부 자식도 마찬가지로 MergeSort를 진행하는 것이다.

    자기 본연의 일이라는 것은,
    정렬되어 돌아온, 왼쪽, 오른쪽 자식애들을
    또 다시 정렬하는 것이다

    11 34 ~ 22 66
    이렇게 각각의 왼쪽, 오른쪽 자식이 정렬되어 올라왔다면
    그것을 다시 정렬하는 것
    계속 반복하면서 올라온다고 생각하면 된다.

    그렇다면 정렬하는 것은 어떻게 ?
    임시의 tmp 배열을 만들고
    거기에 올라온 왼쪽, 자식을 정렬해서 넣은 다음
    원래 origin arr에 tmp값들을 복사해서 넣는다.

    단, 조건이 있다 lt  < rt 이어야 한다는 것이다.
    무슨 말이냐면, 원소의 개수가 1이 되면
    정렬을 할 필요가 없다.
    원소 1개 자체가, 이미 정렬된 상태이기 때문이다.

    그래서 lt == rt일때가 원소 1개일 때이고
    lt < rt 가 , 적어도 원소가 2개이상이고
    정렬이 필요할 때이기 때문에
    lt < rt 일때만 정렬을 수행하는 것이다. 
    '''

    # 원소 개수가 1개라면, st == ed가 될 것이다. 이때는 그냥 바로 리턴

    if st < ed:
        # 후위순회 개념이다
        mid = (st + ed) // 2
        # 1) 왼쪽 아래 : 분할시 앞쪽 정렬
        MergeSort(st, mid)
        # 2) 오른쪽 아래 : 분할시 뒤쪽 정렬
        MergeSort(mid + 1, ed)

        # 다 끝난 이후, 본연의 일, 정렬된 앞,뒤쪽 배열 정렬
        p1 = st
        p2 = mid + 1
        tmp = []

        while p1 <= mid and p2 <= ed:
            # 왼쪽 오른쪽 비교
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1 += 1
            else:
                tmp.append(arr[p2])
                p2 += 1

        # 왼쪽이 남았다면
        if p1 <= mid:
            tmp += arr[p1: mid + 1]

        # 오른쪽이 남았다면
        if p2 <= ed:
            tmp += arr[p2: ed + 1]

        # tmp를 원래 arr idx에 붙여넣기
        for i in range(len(tmp)):
            arr[st+i] = tmp[i]


n = int(input())

arr = [int(input()) for _ in range(n)]


# 퀵 정렬 : pivot은 맨 처음 값을 잡았다.
MergeSort(0, len(arr) - 1)

for x in arr:
    print(x)

# 병합정렬 bottom up --------------------------------------
