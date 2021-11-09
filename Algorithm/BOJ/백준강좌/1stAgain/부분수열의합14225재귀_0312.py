# https://www.acmicpc.net/problem/14225

'''
부분 수열의 개수 ?
ex) [1,2,3] => []/ 1/ 2/  3/ 1 2/ 1 3/ 2 3/ 1 2 3 /

2 ^ ( 배열 길이 ) = 8 개 !

n의 최대길이는 20

즉, 우리가 구할 수 있는 부분수열의 최대 개수 : 2 ^ 20

1억보다 작기 때문에

모든 부분수열들을 구하고, 그것들의 합을 조사한 다음

가장 작은 자연수를 구하면 된다

특정 set을 두고, 더해진 합을 set에 더해간다.

1) 1 ~ 까지 조사하면서
중간에 없는 값 출력

2) 만약 다 연속적으로 있다면,
set의 최대값 + 1을 출력
'''

import sys
sys.setrecursionlimit(100000)

'''
목표하는 합을 만드는 숫자 조합의 수는 1개일 수도 ...n개일 수도 있다.

1개 ~ n개 로 만들어지는 모든 조합들을 다 조사하고

그 조합들 중에서 조건을 만족시키는 경우를 발견하면

그때 ans += 1을 해준다

( 사실상 이중 for문 개념 ) 

'''

n = int(input())
arr = list(map(int, input().split()))
ans = set([])


def dfs(L, idx, c, res):
    global ans
    if L == c:
        ans.add(res)
        return
    else:
        for i in range(idx, n):
            if select[i] == 0:
                select[i] = 1
                dfs(L+1, i, c, res + arr[i])
                select[i] = 0


for i in range(1, n+1):
    select = [0] * (n + 1)
    dfs(0, 0, i, 0)

ans = list(ans)
ans.sort()
flag = -1
for i in range(1, len(ans) + 1):
    if i != ans[i-1]:
        flag = 1
        print(i)
        break
if flag == -1:
    print(ans[-1] + 1)
