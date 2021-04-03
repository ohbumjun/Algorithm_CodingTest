'''
우리가 기존의 quick sort에서는 2가지 집단으로 분류했다

pivot보다 작은애

pivot보다 큰 애

그런데, 만약 우리가 정렬하려는 배열에 

pivot과 같은 애가 있다면 ??

예를 들어, 1 라는 pivot을 설정했고

0 2 2 1 0 2 1 1 

이라는 배열을 정렬하려고 한다면 ??

이 경우에는 pivot 을 기준으로 3가지 집단으로 나누는

partitioning을 진행해야 한다

1) pivot보다 작은 애

2) pivot과 같은 애

3) pivot 보다 큰 애

그러면, 어떻게 하느냐 ??

linear 한 시간복잡도.

를 지니는.

정렬을

2번 진행해야 한다

첫번째 정렬에서는, 

배열 앞에서부터 시작하여, 

pivot보다 작은 애들을, 배열 앞쪽으로 정렬시켜서

pivot보다 작은 집단을 모아두는 정렬

두번째 정렬에서는, 

배열 뒤쪽에서 시작하여, 

pivot보다 큰 애들을, 배열 뒤쪽으로 정렬 시켜서

pivot 보다 큰 집단을 모아두는 정렬

이렇게 2번의 정렬을 실시하게 되면

배열을 기준으로

 

0 2 2 1 0 2 1 1 

0 0 / 1 1 1 / 2 2 2

로 정렬이 될 것이다

'''

import sys
from collections import deque
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

arr = [0, 2, 1, 0, 2, 2, 1, 1, 0]

'''
< 첫번째 정렬 >
앞에서부터 시작
i, pos 라는 point 2개를 사용한다

pos 가 가리키는 애가 pivot보다 작다면
pos를 1 증가시킨다

만약 pos가 pivot 보다 크거나 같고
i는 pivot보다 작은 값이라면

pos ~ i를 바꾸고
pos를 1증가 시킨다 

'''

pos = 0
pivot = 1
for i in range(len(arr)):
    if arr[pos] >= pivot and arr[i] < pivot:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
    elif arr[pos] < pivot:
        pos += 1

print(arr)

'''
< 두번째 정렬 >
뒤에서부터 시작
i, pos라는 2개의 point 를 사용

pos 가 가리키는 애가
pivot 보다 크다면
pos를 1 감소시킨다

pos가 pivot 보다 작거나 같고
i는 pivot 보다 큰 값이라면

둘을 바꿔준다 

'''
pos = len(arr) - 1
for j in range(len(arr) - 1, -1, -1):
    if arr[pos] <= pivot and arr[j] > pivot:
        arr[pos], arr[j] = arr[j], arr[pos]
        pos -= 1
    elif arr[pos] > pivot:
        pos -= 1
print(arr)
