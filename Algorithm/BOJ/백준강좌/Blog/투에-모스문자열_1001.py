# https://www.acmicpc.net/problem/18222

import sys
from collections import deque, defaultdict,Counter
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)
from copy import deepcopy
import itertools

k = int(input())

# 첫번째 , 2번째라면, 바로 return
if k == 1 :
    print(0)
    exit(0)
if k == 2 :
    print(1)
    exit(0)

# 1) 해당 k라는 숫자가, 몇번째 문자를 만드는데 쓰이는가.를 찾기 
# 1,1,2,4,8,16,32
# dp[i]  = i번째 문자의 길이 = 2^(i-1)
# tot[i] = i번째 문자까지의 총길이
# 10**18은 2^60 ~ 2^61 사이에 존재한다 

def findOrder(num):
    res = 0
    while num > 0 :
        num //= 2
        res += 1
    return res

# 2) 그 다음 부터, 구체적으로 문자를 찾기 
order = findOrder(k)

def changeNum(n):
    if n == 0 : return 1
    if n == 1 : return 0

# 원리는 다소 어렵다
# 여기서 order란, 2로 나눈 몫 + 1 이다.
# 0번째 : '0'
# 1번째 : '01'
# 2번째 : '0110'
# 즉, order 가 짝수면, 끝이 0, 아니면 1이다
# 이렇게 order를 구하고, 끝 숫자를 endN 에 세팅하고 시작한다

# 0110 1001 1001 0110 의 문자열 , num이 만약 12라고 할때
# endN은 0이다
# 이제 이분탐색을 실시할 것인데,
# mid보다 num이 왼쪽에 있게 되면, edN이 바뀐다
# mid보다 num이 오른족에 있다면, edN은 그대로다
# mid와 num이 같을 때에도, 사실상, 왼쪽 영역에 속하는 것이므로
# endN이 바뀐다

# 이러한 과정을 반복하여, 최종 endN을 출
def findText(num,order):
    endN = 0 if order % 2 == 0 else 1
    st   = 2**(order-1)
    ed   = 2**order
    while st < ed :
        mid = (st+ed)//2
        if num <= mid :
            ed = mid
            endN = changeNum(endN)
        else : # num >= mid
            st = mid + 1
    return endN
print(findText(k,order))




    
    

