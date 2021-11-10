# https://www.acmicpc.net/problem/14888

import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
< 재귀 >
여기서 중요한 점은,
연산자를 어디에 넣는지이다.

즉, 여기서도 마찬가지로, 
모든 연산자를 넣어야 하는데, 그 순서를 바꿔서 넣어야 하는 경우인 것이다

그렇다면, 모든 연산자를 다 넣어야 하는건가 ?
너무 많은 경우의 수가 있으면 어떡하지 ?

이 문제의 경우,
우리가 넣을 수 있는 연산자는 딱 정해져 있다

예를 들어, 10개가 주어졌다고 하면
우리는 10개의 구간에다가 넣으면 된다.

그렇다면, 4 ^ 10 인 것일까 ?

아니다. + 4개를 만약 연속해서 삽입한다고 하면
그것은 중복되게 인식해야 한다.

어떻게 ?
다음과 같은 식을 사용하면 된다
10개의 연산자를 넣는 경우,
각각의 연산자 개수가 2, 2, 3, 3 이라고 할때

10C2 * 8C2 * 6C3 * 3C3 = !
이와 같은 과정을 겪으면 된다.
왜 ?? 
10개가 들어갈 수 있는 공간 중에서
+ 2개가 들어갈 공간 선택

이후 8개가 들어갈 수 있는 공간 중에서
- 2개가 들어갈 공간 선택

그리고 실제 이 경우,
4 ^ 10 보다는 훨씬 더 적은 경우의 수를 얻을 수 있다

다음과 같은 식을 사용하여 구해보자
go( arr , idx, cur, plus, minus, mul, div )

// arr  : 주어진 값arr
// idx  : 현재 계산에 포함시켜야 하는 연산자의 idx
// cur  : 지금까지 누적된 연산결과값
// plus : 남은 +  연산자 개수
// minus: 남은 -  연산자 개수
// mul  : 남은 *  연산자 개수
// div  : 남은 // 연산자 개수

이후, 재귀적으로 함수를 구현

return 값은 [cur,cur]

각 단계에서
res라는 임의의 배열을 두고

각 단계, 4단계로 분리 이후 return되는 값들에서의
최대, 최소를 각각 구하고

해당 (최대, 최소)를 return 해오는 방식을 취한

'''

n = int(input())
numArr = list(map(int, input().split()))
calNum = list(map(int, input().split()))

resMin = 123242132
resMax = 0
resArr = []


def go(arr, idx, cur,  plus, minus, mul, div):

    n = len(arr)

    if idx == n:
        return (cur, cur)

    res = []
    if plus > 0:
        res.append(
            go(arr, idx + 1, cur + arr[idx],  plus - 1, minus, mul, div))
    if minus > 0:
        res.append(
            go(arr, idx + 1, cur - arr[idx],  plus, minus - 1, mul, div))
    if mul > 0:
        res.append(
            go(arr, idx + 1, cur * arr[idx],  plus, minus, mul - 1, div))
    if div > 0:
        if cur >= 0:
            res.append(
                go(arr, idx + 1, cur // arr[idx], plus, minus, mul, div - 1))
        else:
            res.append(
                go(arr, idx + 1, - (cur // arr[idx]), plus, minus, mul, div - 1))
    ans = (max([t[0] for t in res]), min([t[1] for t in res]))

    return ans


ans = go(numArr, 1, numArr[0],  calNum[0], calNum[1], calNum[2], calNum[3])

print(ans[0])
print(ans[1])
