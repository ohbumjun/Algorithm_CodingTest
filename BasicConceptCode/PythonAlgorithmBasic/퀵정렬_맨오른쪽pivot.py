'''
퀵 정렬은 
하나의 '전위 순회 방식'이라고도 할 수 있다

즉, 자기 본연의 일을 먼저 한 다음에

그 이후에, 왼쪽, 오른쪽 역할을 하는 방식인 것이다 

'''
import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)


def quicksort(low, high):
    # low 부터 high 까지의 원소를 정렬하겠다 !
    # 따라서 low < high 일 경우에만, 정렬하는 경우에 해닫하는 것이므로
    # 아래와 같이 if low < high 라는 조건을 준 것이다
    if low < high:
        # 오른쪽 설정
        pivot = arr[high]
        pos = low
        i = low
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[pos], arr[high] = arr[high], arr[pos]
        quicksort(low, pos - 1)
        quicksort(pos + 1, high)


arr = [2, 5, 9, 3, 7, 5]
quicksort(0, len(arr) - 1)
print(arr)
