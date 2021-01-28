#https://www.acmicpc.net/problem/1021

# 첫번째 풀이....오답...?
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)
import heapq as hq

# 매번 idx로 찾으면 되지 않을까 ?
size , num = map(int,input().split())
arr = deque(list(range(1,size+1)))
targets = list(map(int, sys.stdin.readline().strip().split()))
sec = 0
thr = 0

for i in range(len(targets)) :
    print("sec + thr",sec + thr)
    print("deq", arr )
    # 왼쪽 이동
    if arr.index(targets[i]) < size // 2 :
        while True:
            cur = arr.popleft()
            if cur == targets[i] :
                break
            else:
                arr.append(cur)
                sec += 1
                
    # 오른쪽 이동
    elif arr.index(targets[i]) >= size // 2 :
        while True:
            cur = arr.pop()
            if cur == targets[i]:
                break
            else:
                arr.appendleft(cur)
                thr += 1

        
print( sec + thr )       
            
'''
문제를 잘못 이해했다.
뒤에서는 pop을 할 수 없다.
pop연산은, 첫번째 종류의 연산,

즉, 앞에서의 pop만이 가능하기 때문에
오른쪽 이동을 하더라도
queue 맨 앞에 값이 놓이도록 해야 한다.
'''


## 정답 ----------------------------------------------
#https://www.acmicpc.net/problem/1021

# 첫번째 풀이....오답...?
import sys
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
sys.setrecursionlimit(100000)
import heapq as hq

# 매번 idx로 찾으면 되지 않을까 ?
size , num = map(int,input().split())
arr = list(range(1,size+1))
targets = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0

for i in range(len(targets)) :
    Length = len(arr)
    idx = arr.index(targets[i])
    # 왼쪽 이동

    ## 여기서 Length // 2라는 조건이 아니라
    ## 이런식으로, 좌우를 확실히 비교하는 것이 핵심이다
    ## idx < Length // 2 
    if idx < Length - idx :
        while True:
            if arr[0] == targets[i]:
                del arr[0]
                break
            else:
                arr.append(arr[0])
                del arr[0]
                cnt += 1
                
    # 오른쪽 이동
    else :
        while True:
            if arr[0] == targets[i]:
                del arr[0]
                break
            else:
                arr.insert( 0, arr[-1])
                del arr[-1]
                cnt += 1
        
print(cnt)       
            

