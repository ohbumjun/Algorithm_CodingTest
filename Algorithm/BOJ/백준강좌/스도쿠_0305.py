import collections
from collections import deque, Counter
import sys
import heapq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(100000)

'''
한번 놓을 때마다
row, col, 주변 9개를 검사해야 한다

어떻게 검사하지 ?
검사하는 방식의 코드는 어떻게 짤거야 ??

각 행 기준, 1 ~ 9 숫자가 있는지
c[i][j] : i행에 숫자가 j가 있으면 true

각 열 기준  1 ~ 9 숫자가 있는지
c2[i][j] : i열에 숫자가 j가 있으면 true 

각 블록기준 1 ~ 9 숫자가 있는지
c3[i][j] : i번 작은 정사각형에 숫자j가 있으면 true
( x, y ) : ( x//3 ) * 3 + ( y // 3 ) 

를 확인해야 한다

go(z) : z 번째 칸을 채우겠다
( x, y ) => 9 * x + y 번째

정답을 찾은 경우 : z = 81
다음 :
1) 빈칸인 경우 : 해당 정보를 채우는 처리 진행 ! 그 다음 넘어가기 
2) 수가 있는 경우 ( 넘어가기 )


각 칸을 채울 때마다 3군데를 봐야 한다
가로, 세로, 해당 블록

1) 각각에 대해 check 배열을 만들어둔다
- 여기서 해당 블록.의 idx 를 계산하는 별도의 로직이 필요하다
0 ~ 8 까지의 idx를 가지는 블록이 차레대로 만들어진다고 할 때,
현재 row, col은 x, y
그러면 ( x // 3 ) * 3 + ( y // 3 ) 을 해주면 0 ~ 8 idx로 설정이 된
블록의 idx가 나올 것이다 

입력을 받고, 2차원 배열을 탐색할 때,
채워져있는 경우와, 채워져있지 않은 경우가 있다

빈칸이 아니라면, 그냥 넘어가고
빈칸이라면, 해당 칸을 채우고 넘어가야 한다

그러면, 채울 때는 어떻게 채워야 하는 걸까?

1) 가로, 세로, 블록이 모두 가능한지를 보고
2) 가능하다면, 가로,세로,블록 check 배열에 체크
3) 그다음 arr[][] 을 해당 값으로 채워준다
4) 여기서중요한 것은, 사실 그 빈칸에 들어갈 수 있는 수가
1개 이상일 수도 있다 즉, 해당 빈칸을 그 숫자로 채우고 쭉 진행한 이후에
다시 다른 숫자로 채우고 진행하는 경우가 생길 수도 있다는 것이다

이러한 경우에 대비하여 ,
체크 하고 , 들어간 다음에
다시 해당 요소들을 해지해주어야 한다는 것이다 


'''


def go(z):
    if z == 81:
        # 출력
        for row in arr:
            print(' '.join(map(str, row)))
        return True  # 만약 여기서 print하고 끝내고, 더이상 다시 재귀뒤로 돌아가지 않으려면
        # exit(0)을 하면 된다

    x = z // n
    y = z % n

    if arr[x][y] != 0:  # 빈칸이 아니라면, 넘어간다
        go(z+1)
    else:  # 빈칸이라면, 채우는 과정을 진행한다
        # 1 ~ 10 으로 설정한 것이 중요하다 ( 실제 1 ,2 라는 값이 들어가있느냐 )
        for i in range(1, 10):
            # 해당 칸에 채울 수 있다면
            if c[x][i] == 0 and c2[y][i] == 0 and c3[square(x, y)][i] == 0:
                # 방문 처리
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = 1
                arr[x][y] = i
                '''
                여기서 중요한 것이 있다
                왜 굳이 if go(z+1) return True
                를 해주는 것일까

                다시 여기로 돌아오기 위한 것이다
                즉, 쭈~~욱 재귀타고 들어가면 z == 81 을 만나게 될것이다

                그러면, 다시 일로 쭉 ~~ 타고 올라올 것이다 
                ??

                그런데 어차피 맨 마지막에 go(z+1)이 true가 된다는 것은 
                결과적으로, go(z) 들이 모두 true가 되니까

                해당 줄 아래로는 안오는 거 아닌가?

                아니지, 왜냐하면 
                저기 위에 if arr[x][y] != 0 에 걸려서
                +2,+3 이렇게 건너뛰어서 갈 수도 있기 때문이다 

                즉, go(z+1)이 true가 되어서 돌아올 때
                go(z)도 빈칸이어서, 해당 칸을 채워야 하는 
                상황이 아닐 수도 있다는 것이다 
                '''
                if go(z+1):
                    return True
                # 방문 처리 해제
                arr[x][y] = 0
                c[x][i] = c2[y][i] = c3[square(x, y)][i] = 0
    return False


def square(x, y):
    return (x // 3) * 3 + (y // 3)


n = 9
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

# 10 ! 이라는 값이 중요하다. 각 col의 idx가 곧, 1,2,3 이 채워졌는지 아닌지가 들어간다
c = [[0] * 10 for _ in range(9)]
c2 = [[0] * 10 for _ in range(9)]
c3 = [[0] * 10 for _ in range(9)]


# 입력을 받으면서, 빈칸이 아닌경우, 처리해주기
for i in range(9):
    for j in range(9):
        if arr[i][j] != 0:
            # 행 정보 추가
            c[i][arr[i][j]] = 1
            # 열 정보 추가
            c2[j][arr[i][j]] = 1
            # 블록 정보 추가
            c3[square(i, j)][arr[i][j]] = 1
go(0)
