# https://www.acmicpc.net/problem/12100

import sys
sys.setrecursionlimit(100000)

'''
구슬 탈출2 와 비슷한 유형이지만,
여기서 다른 점은,
구슬 탈출2의 경우, 같은 방향으로 이동시키는 것이
의미를 지니지 못했지만,

2048(easy)의 경우,
같은 방향으로 이동시키는 것이 의미를 갖는다.

즉, 첫번째 왼쪽 이동과, 2번째 왼쪽 이동은 다른 의미를 지닌다는 것이다 

'''

dx = [0, 0, 1, -1]
dy = [-1, -1, 0, 0]

# 최대 5번 이동
LIMIT = 5

# 4진법으로 바꾸는 부분 ( 2빈법 bitmask를 )
# 10자리수를, 5자리수로 바꿀 것이다.


def gen(k):
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = (k & 3)
        k >>= 2
    return a

# 보드 a를 dirs 방향대로 이동시키서, 최대값을 리턴한다


def check(a, dirs):
    n = len(a)
    d = [row[:] for row in a]

    for dir in dirs:
        ok = False

        # 합쳐졌음 여부를 표시하는 merged 배열 : 초기화는, 우선 합쳐진 적이 없다라고 표시한다.
        # merges[i][j] : 이번 이동에 해당 칸이 합쳐졌는지 아닌지를 표시해주기
        # 처음에는 우선 합쳐진 적이 없는 경우들이므로, 아래와 같이 초기화 해준다
        merged = [[False] * n for _ in range(n)]

        # 계속 해당 방향으로 쭈~~욱 보내는 것이다
        while True:

            ok = False

            # 아래 방향으로 이동하기( dir == 0 )
            if dir == 0:
                # 응 ?? 방향은 아래로 이동하는 것인데, 검사 순서는 아래에서 위로 올라오고 있다
                # 제일 밑에서부터 확인을 하면서, 바로 위에 숫자랑 합쳐질 수 있는지를 검사하면서 위로 차근차근 이동한다
                '''
                2
                2
                2
                를 아래로 이동한다고 할때

                0
                2
                4
                로 만들어주기 위해서는

                맨아래 2부터 위로 접근하면서 합쳐주어야 한다
                즉, 맨 아래 2에서 시작하여 한칸 위를 보게 되면 2가 위치해 있다

                그러면, 아래에서 2번째 2를 한칸 아래로 이동시켜서 합쳐주는 개념이다

                아래 반복문에서 n-1 이 아니라, n-2부터 시작하는 이유도,
                어차피 맨 아래 2같은 수는, 그 아래로 이동하지 못하기 때문이다 

                2
                2
                2

                위에서부터 아래로 내려가면서 합쳐주게 되면

                0
                4
                2 라는 오답이 나올 수 있는 것이다 


                '''
                # n-1 이 아니라, n-2부터 시작한다
                for i in range(n-2, -1, -1):
                    for j in range(n):
                        # 현재 수가 없다면, 그냥 pass
                        if d[i][j] == 0:
                            continue
                        # 한칸 아래에 수가 없다면
                        if d[i+1][j] == 0:
                            # 현재 칸을, 현재 아래 칸에 대입시킨다
                            d[i+1][j] = d[i][j]
                            # 현재 칸의 합쳐진 정보를, 아래 칸의 합쳐진 정보란에 대입해준다
                            # 예를 들어, 현재 d[i][j]에는 값이 있고
                            # 그값은, 위에서 내려오면서 합쳐져서 만들어진 수일 수도 , 아닐 수도 있다
                            # 그런데, 아래칸은 수가 없다.그리고 현재 칸을 아래에 넣는 것이다
                            # 그렇다면, 현재 칸의 합쳐짐 여부에 대한 정보도, 아래칸에 넣어줘야 하는 것이다
                            merged[i+1][j] = merged[i][j]
                            # 그리고 원래 칸에는 수가 없다고 표시해준다
                            d[i][j] = 0
                            ok = True
                        # 한칸 아래에 수가 있고, 현재 칸과 같을 때 == 합쳐주자 !
                        elif d[i+1][j] == d[i][j]:
                            # 왜 아래줄과 같은 코드가 존재하는 것일까 ??
                            '''
                            2
                            2
                            2
                            2 라는 코드가 있다고 해보자

                            이것을 한번 아래로 내리면
                            0
                            0
                            4
                            4

                            가 되어야 한다.

                            그 이후에 한번 '더' 화살표 아래 키를 누르게 되면

                            0
                            0
                            0
                            8
                            이 되는 것이다

                            그런데, 잘 생각해보면, merged[][]라는 정보를 쓰지 않게 되면
                            한번의 클릭으로

                            0
                            0
                            4
                            4
                            에 그치는 것이 아니라

                            0
                            0
                            0
                            8 로 쭉 내려가 버린다. 이것은 우리가 원하는 것이 아니다.

                            4를 만났을 때, 즉, for문을 돌면서 계속 아래로 내려갈 텐데
                            2와2가 합쳐진 4를 만났을 때, 설령 그 아래의 4와 합쳐질 수 있다고 하더라도
                            이미 2개의 4는 해당 턴에서 합쳐졌기 때문에
                            더이상 합쳐지는 것을 막는 것이다 


                            '''
                            if not merged[i][j] and not merged[i+1][j]:
                                d[i+1][j] *= 2
                                merged[i+1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 1:  # 위로 이동 시키기( 1번째 행 부터 보는 것 )
                for i in range(1, n):
                    for j in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i-1][j] == 0:
                            d[i-1][j] = d[i][j]
                            merged[i-1][j] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i-1][j] == d[i][j]:
                            if not merged[i][j] and not merged[i-1][j]:
                                d[i-1][j] *= 2
                                merged[i-1][j] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 2:  # 왼쪽으로 이동시키기
                for j in range(1, n):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j-1] == 0:
                            d[i][j-1] = d[i][j]
                            merged[i][j-1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j-1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j-1]:
                                d[i][j-1] *= 2
                                merged[i][j-1] = True
                                d[i][j] = 0
                                ok = True
            elif dir == 3:  # 오른쪽으로 이동시키기
                for j in range(n-2, -1, -1):
                    for i in range(n):
                        if d[i][j] == 0:
                            continue
                        if d[i][j+1] == 0:
                            d[i][j+1] = d[i][j]
                            merged[i][j+1] = merged[i][j]
                            d[i][j] = 0
                            ok = True
                        elif d[i][j+1] == d[i][j]:
                            if not merged[i][j] and not merged[i][j+1]:
                                d[i][j+1] *= 2
                                merged[i][j+1] = True
                                d[i][j] = 0
                                ok = True

            # 더이상 이동하지 않는다면, break
            # 즉, 더이상 이동할 공간이 없다면, 이동시켜도 아무런 변화가 없다면
            if not ok:
                break

    ans = max([max(row) for row in d])
    return ans


n = int(input())

# 해당 정보를 입력받는다.
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 이동할 수 있는 모든 경우의 수를 for문 돌려 순회한다
for k in range(1 << (LIMIT * 2)):
    # 우리가 사용할 수 있는 4진법 형태로 만들어준다
    dirs = gen(k)
    # cur : 만들어낼 수 있는 최댓값 ( 보드에 존재하는 최댓값 )
    # 만약 해당 방향으로 이동시켜도 변화가 없다면, -1이 return될 것이다
    cur = check(a, dirs)
    if ans < cur:
        ans = cur

print(ans)
