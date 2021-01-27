# https://www.acmicpc.net/problem/8979

# 1번째 풀이 : 오답 ------------------------------------------------------------------------------------------
import sys
n, k = map(int,input().split())
hash = dict()

arr = sorted([list(map(int, sys.stdin.readline().strip().split() )) for _ in range(n)], reverse = True, key = lambda x : [ x[1], x[2], x[3]])
hash[arr[0][0]] = 1


for i in range( 1, len(arr) ) :
    if arr[i][1] == arr[i-1][1] and arr[i][2] == arr[i-1][2] and arr[i][3] == arr[i-1][3] :
        hash[arr[i][0]] = hash[arr[i-1][0]]
    else:
        hash[arr[i][0]] = hash[arr[i-1][0]] + 1

print(hash[k])
'''
원리는 2가지이다
1. 금메달, 은매달, 동메달 순 정렬
2. 정렬된 배열 앞에서부터, 금메달, 은메달, 동메달 수에 따른 hash 값 생성
3. 나중에 hash의 key값으로 k를 넣어서 값을 찾는다 

답이 틀렸다고 한다.
왜그런지 모르겠다

'''

# 2번째 풀이 ------------------------------------------------------------------------------------------------
'''
정렬가지는 똑같지만, 해당 순위를 찾는데에 있어 다른 접근을 했다.
사실, 포인트는, 내가 찾는 나라의 등수를 찾는 것인데,
해당 나라와 같은 등수이면서, 
배열 상 앞에 위치한 나라가 있을 수 있으니

배열 상 
1) 앞에 있으면서
2) 해당 나라와 같은 등수
를 갖는 나라를 찾으면된다.


그렇다면, 그저 배열 앞에서부터 값을 보면서
해당 나라의 등수와 같은 나라,의 idx + 1을 출력해주면 되는 것이다. 
'''
import sys
n, k = map(int,input().split())
hash = dict()

arr = sorted([list(map(int, sys.stdin.readline().strip().split() )) for _ in range(n)], reverse = True, key = lambda x : [ x[1], x[2], x[3]])
hash[arr[0][0]] = 1


# 정렬된 배열상에서 k 나라 정보를 찾는다
for i in range(len(arr)) :
    if arr[i][0] == k :
        index = i

# 정렬된 배열 상에서, k나라와 정보는 같으면서, 제일 앞에 위치한 정보를 찾는다
for i in range(len(arr)) :
    if arr[index][1:] == arr[i][1:] :
        print(i+1)
        break
