#

# 첫번째 풀이 : 시간초과
'''
1. b가 들어갈 수 있는 idx의 조합을 구한다.
오름차순으로 idx가 정렬될 것이다.

2. tmp = ['a'] * ( n + 1 ) 을 선언해두고
b가 들어가는 조합에 근거하여 'b'를 넣은 후
정렬한다

ex [0,1] ... >> bbaaa ( 1번째로 만들어진다 )

하지만, 중요한 점은 실제 b가 정렬되는 순서는
b의 idx가 [0,1] 일때는 맨 마지막으로 와야 한다

그러므로, 만들어진 문자열들에 대해서
오름차순 정렬하도록 한다.

3. 입력받은 , 순서 정보 를 통해
해당 숫자의 문자열 출력

< 시간 초과 >


'''
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

def dfs(L, val, res, ch, IdxArr):

    if L == 2 :
        IdxArr.append([res[0],res[1]])
        return
    else:
        for i in range( val ,  len(ch) - 1):
            if ch[i] == 0 :
                # 방문 처리
                ch[i] = 1
                res.append(i)
                dfs( L + 1, i , res , ch, IdxArr )
                res.pop()
                ch[i] = 0
          
def makeCases(n) :
    ch = [0] * ( n + 1 )
    IdxArr = []
    resArr = []

    dfs( 0, 0 ,[], ch ,IdxArr )

    for idx in IdxArr:
        tmp = ['a'] * n
        tmp[ idx[0] ] = 'b'
        tmp[ idx[1] ] = 'b'
        resArr.append(tmp)

    resArr.sort()
    return resArr

k = int(input())

for _ in range(k):
    n , order = map(int, sys.stdin.readline().split())
    madeCase = makeCases(n)
    print(''.join( madeCase[order-1] ))


# 두번째 : 시간초과
'''
> 같은 원리이지만, 
조합이 만들어지는 idx순서가 다르다

1번째에서는
[0,1] .... 이런식으로 만들어지지만,

여기서는
[5,4] ... 이런식으로 만들어진다.

이런 시도를 한 이유는
1번째에서 문자열 후보를 만들고
sort 하는데에 걸리는 최소 시간 복잡도가
O ( n log n) 이기때문에
이마저도 절약하고 싶었다

'''
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

def dfs(L, val, res, ch, IdxArr):

    if L == 2 :
        IdxArr.append([res[0],res[1]])
        return
    else:
        for i in range( len(ch) - 2 , val -1 , -1 ):
            if ch[i] == 0 :
                # 방문 처리
                ch[i] = 1
                res.append(i)
                dfs( L + 1, i , res , ch, IdxArr )
                res.pop()
                ch[i] = 0
          
def makeCases(n) :
    ch = [0] * ( n + 1 )
    IdxArr = []
    resArr = []

    dfs( 0, 0 ,[], ch ,IdxArr )

    for idx in IdxArr:
        tmp = ['a'] * n
        tmp[ idx[0] ] = 'b'
        tmp[ idx[1] ] = 'b'
        resArr.append(tmp)

    
    return resArr

k = int(input())

for _ in range(k):
    n , order = map(int, sys.stdin.readline().split())
    madeCase = makeCases(n)
    print(''.join( madeCase[order-1] ))


# 세번째 :  
'''
# https://www.youtube.com/watch?v=bZQDRArWYeI

이해하기 매우 어렵다.
우선, 2개의 b , 가 들어갈
idx를 찾는 과정을 먼저 한다

그렇다면, 어떻게 2개의 b가 들어갈 idx를 찾는다는 것일까 ?
우선, 왼쪽에 오는 b가 올 경우의 수를 본다

aaabb
aabab
aabba
abaab
ababa
abbaa
baaab
baaba
babaa
bbaaa

왼쪽 b의 위치를 보면
str의 길이를 n이라고 하면

n-2에 1개
n-3에 2개
n-4에 3개

이런 식으로 나아가는 것을 확인할 수 있다.
즉, 
for( let i = n -2 ; i >=0 ; i--)
라고 하면

n-1-i 번째에 왼쪽 b가 오는 경우가
i 개 라는 것이다.

그렇다면 우리가 할일은
입력받은 k를

특정 idx에 가능한 왼쪽 b의 경우수를
세트로 빼가는 것이다

예를 들어, k가 5라면

n-2에 1개
n-3에 2개 인 경우는 지나올 것이고

n-4 에 3개 , 이 경우 3개 중 하나에 속할 것이다.
이렇게 k가 들어갈 세트에 도달하면,
그 idx에 왼쪽 b를 넣어준다

자. 이제 왼쪽으로 찾았으니
오른쪽으로 찾아보자

k = 5이면
ababa 이다.

n-4번째에 b 가 오는 경우 수에 해당했으므로
n-2번째에 1개
n-3번재에 2개 인 경우는 지나쳐왔을 것이며,

k를 계속 빼왔으므로
k = 2 인 상태이다.

그런데 오른쪽 b의 위치를 보니
ababa
즉, str길이 n에서 -2 만큼의 idx에 위치한다

즉, 왼쪽 b를 찾고 난 이후에는
( N - 2 ) 번째 위치에 
알파벳이 존재한다는 의미가 된다 !!

즉, 왼쪽 b 배치이후
N - K 번째 idx에 오른쪽 b를 배치하면 되는 것이다


'''

import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)

n = int(input())

for _ in range(n):
    
    N, K = map(int, sys.stdin.readline().split())
    ch = ['a'] * N
    
    for i in range(N-2,-1,-1) :
        
        numOfLeftInIPos = N - 1 - i

        if K <= numOfLeftInIPos :
            # 현재 여기서 이제 오른쪽 찾기
            # 우선 왼쪽 대입
            ch[i] = 'b'

            # 오른쪽 대입 : 오른쪽 idx = n ( str length ) - k
            ch[ N - K ] = 'b'
            print(''.join(ch))
            break

        K -= numOfLeftInIPos

    
            
            
