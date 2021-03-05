# https://codeforces.com/problemset/problem/1399/C

# 첫번째 풀이 : BruteForce __ 시간 초과 
import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

n = int(input())

for _ in range(n) :
    
    m = int(input())
    arr = Counter( list(map(int,sys.stdin.readline().split())) )
    res = 0

    # 사실 2부터 100까지 숫자가 가능하다
    # 결과적으로 2개의 for문을 도는 원리이다
    # i를 2 ~ 100 이라고 하면
    # j는 counter에 저장된 key값들에 해당할 것이다
    # i - j 라는 값은 0보다는 커야 한다.
    # 또한  i - j  에 해당하는 내용이 ocunter에 key로서 존재해야 한다
    # 결국, arr[i], arr[i-j]의 최소값을 total에 더해준다 ( 둘의 합의 경우의 수이므로 ) 
    # 이렇게 한번 i,j 2개 for문 set를 돌게 되면
    # 해당 i ( total ) 의 개수가 나올 것이다
    # 그런데 우리는 /2 를 해주어야 한다. 중복해서 더해지기 때문이다 
    # 그리고 이러한 total 값들 중에서 max 값들로 계속 갱신해나가야 한다
    for total in range( 2 , 2 * m + 1 ):
        totalVal = 0
        for i in arr.keys():
            other = total - i
            if other > 0 and arr[other]:
                totalVal += min( arr[i], arr[other] )
        totalVal //= 2
        res = max(res, totalVal)

    print(res)
                

    
# 두번째 풀이 : 
import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
import collections
sys.setrecursionlimit(100000)

# 기본원리는 brute force와 동일

'''
첫번째 풀이에서는 ,
나올 수 있는 모든 합을 기준으로 for문을 시작

문제는, 애초부터 나올 수 없는 합의 경우에도
for문을 돌리므로, 불필요한 시간이 걸렸다

< 다른 점 >
여기서는 나올 수 있는 합의 경우의 수에 대해서만 고려하는 원리이다
나올 수 있는 합의 경우의 수를 bruteforce 형태로
이중 for문을 돌리면서 구해나가는 것이다

그렇다면, 나올 수 있는 합의 경우의 수들을 모두 구한다음
그 중 최대를 구하면 되는 것인데

이것을 어떻게 구현할까 ?
조금 낯설지만
a라는 result에 대한 value로 list를 만든다
그리고 그 list안에는 a라는 합을 구성하는 원소들을 넣는다

그 원소들은 중복될 수 없다
예를 들어
1 2 3 4 라는 배열이 주어지고
합이 4를 만드는 원소 구성들을 살펴보면
1 3 이다

1 1 3 이렇게 2개다 둘어갈 수 없으며
set 단위이므로, list 원소개수는 짝수일 것이다

그렇다면 result 에대한 list들을 모두 구한 다음
len(result) // 2가 결국 해당 result가 나오는 경우의 수이다
len(result) // 2 의 최댓값을 구하면 되는 것이다

'''
t = int(input())

for _ in range(t) :
    m = int(input())
    arr = list(map(int,sys.stdin.readline().split()))

    result = collections.defaultdict(list)

    for i , a in enumerate(arr) :
        for j in range(i+1, len(arr)):
            if i not in result[a + arr[j]] and j not in result[a + arr[j]] :
                result[a+arr[j]].append(i)
                result[a+arr[j]].append(j)

    minSum = 0
    for i in result.items():
        tmp = len(i[1]) // 2
        if tmp > minSum :
            minSum = tmp
    print(minSum)
    
    

