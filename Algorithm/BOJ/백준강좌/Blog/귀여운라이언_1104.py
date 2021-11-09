# https://www.acmicpc.net/problem/15565

# 첫번째 풀이 : 일반적인 투포인터 문제 > 틀림
import sys
import heapq
sys.stdin = open("input.txt", "rt")
from collections import deque, Counter
import collections
sys.setrecursionlimit(100000)

N ,K = map(int,input().split())
data = list(map(int, sys.stdin.readline().split()))

'''
start와 end 지점은 각각 0 , 1 로 시작
내가 고려하는 것은 end 전까지의 데이터

1) start 지점 잡기 
초기화 : start, end = 0, 1가 아니라
최초 1이 나오는 지점을 start로 잡고,
+ 1 을 한곳에 end를 잡는다

2 라이언 세기 + 탈출 조건 
start ~ end - 1 까지의 수를 보면서
1 ( 라이언 ) 의 개수를 센다

만일 라이언의 개수가 K보다 작다면

현재 end지점을 확인한다
end가 데이터 구간 범위 안에 존재한다면 

    1) 만일 1 이라면, 구간에서의 라이언 개수를 + 1 시켜준다
        만일 라이언의 개수가 K와 같다면
            해당 구간을 res와 비교 res = min( res , end + 1 - start )
            start를 다음 1이 나오는 곳까지 이동시키기
            cnt -= 1
        만일 라이언의 개수가 K보다 작다면
            아무것도 안한다 
        end는 1증가
    2) 만일 1이 아니라면, end를 1증가시켜주기만 한다

벗어낫다면 종료 


'''

start, end = 0,0
res = int(1e9)

while data[start] != 1 :
    start += 1

if start == N :
    print(-1)
else:
    end = start + 1
    cnt = 1

    while True:
        if cnt < K and end < N:
            if data[end] == 1 :
                cnt += 1
                if cnt == K :
                    res = min(res , end + 1 - start )
                    start += 1
                    while data[start] != 1 :
                        start += 1
                    cnt -= 1
                end += 1
            else :
                end += 1
        else:
            break
print(res)

# 두번째 풀리 : 슬라이딩 윈도우


'''
라이언 인형이 딱 K개가 되는 구간만 확인해주면 된다

"항상 K개가 되는 것을 확인해야 하므로, 슬라이딩 윈도우를 활용할 수 있는 것이다"

라이언들의 idx들을 구해놓는다
0 4 6 9

K가 3이라면
0 4 6
4 6 9
라는 2개의 set가 존재하게 되며

처음 idx - 마지막 idx + 1 을 해주면
인형이 포함된 전체 인형의 개수가 된다

윈도우의 크기를 K로 유지하면
한칸씩 뒤로 밀어가며 계속 비교해가면 된

'''


N ,K = map(int,input().split())
dolls = list(map(int, sys.stdin.readline().split()))

lion = [] # 라이언 위치 저장
for i in range(len(dolls)) :
    if dolls[i] == 1 :
        lion.append(i)

if len(lion) < K :
    print(-1)
    exit(0)

start = 0
end = K - 1
res = int(1e9)

while end < len(lion) :
    length = lion[end] - lion[start] + 1
    res = min(length, res)
    start += 1
    end += 1

print(res)
             