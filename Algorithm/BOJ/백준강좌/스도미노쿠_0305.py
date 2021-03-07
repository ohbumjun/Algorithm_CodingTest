# https://www.acmicpc.net/problem/4574

'''
스도쿠 문제와의 차이점은. 수를 놓는 방식.이다

1. 행 검사 배열
2. 열 검사 배열
3. 블록 검사 배열
4. 새로 놓는 도미노 배열
5. 수를 놓는 방식 세팅을 위한 2가지 배열
- dx[] : {0,1}
- dy[] : {1,0}
'''

n = 9
# 스도쿠 정보를 놓기 위한 dx,dy 정보 ( 오른쪽, 아래 )
dx = [0, 1]
dy = [1, 0]


# B2, 이렇게 들어온 정보를, 유효한 숫자 형태의 row, col로 바꿔준다
def convert(s):
    return (ord(s[0])-ord('A'), ord(s[1])-ord('1'))


def square(x, y):
    return (x//3)*3+(y//3)

# 해당 칸에 숫자를 넣을 수 있는지 없는지 검사( 행,열,블록 정보  )


def can(x, y, num):
    return not c[x][num] and not c2[y][num] and not c3[square(x, y)][num]

# 행,열,블록 정보에 해당 숫자가 쓰였음/안쓰였음 을 표시


def check(x, y, num, what):
    c[x][num] = what
    c2[y][num] = what
    c3[square(x, y)][num] = what

# 올바른 범위안에 있는지 검사


def check_range(x, y):
    return 0 <= x < n and 0 <= y < n


def go(z):
    if z == 81:
        for i in range(n):
            print(''.join(map(str, a[i])))
        return True
    x = z//n
    y = z % n
    if a[x][y] != 0:
        return go(z+1)
    else:
        for k in range(2):
            nx, ny = x+dx[k], y+dy[k]
            # 유효한 범위가 아니라면 pass
            if not check_range(nx, ny):
                continue
            # 빈칸이 아니라면 그냥 pass
            if a[nx][ny] != 0:
                continue
            # 아래의 2중 for문은 domino i, j를 만드는 코드
            # 즉, 새로운 domino 판을 짜는 것이다
            # 처음부터 끝까지 !
            for i in range(1, 10):
                for j in range(1, 10):
                    # 인접한 도미노끼리는 같은 숫자가 될 수 없다
                    if i == j:
                        continue
                    # 이미 그 domino를 사용한 적이 있어도 건너뛴다
                    if domino[i][j]:
                        continue
                    # 2개의 숫자를 배치해야 한다. 2개 숫자 모두 사용가능하다면
                    if can(x, y, i) and can(nx, ny, j):
                        # 행, 열, 블록 정보에 사용여부 표시
                        check(x, y, i, True)
                        check(nx, ny, j, True)
                        # domino 배치 ,실제 a배열에도 실질적인 정보 표시
                        domino[i][j] = domino[j][i] = True
                        a[x][y] = i
                        a[nx][ny] = j
                        if go(z+1):
                            return True
                        # 원상태 복귀
                        check(x, y, i, False)
                        check(nx, ny, j, False)

                        domino[i][j] = domino[j][i] = False
                        a[x][y] = 0
                        a[nx][ny] = 0
    return False


tc = 1
while True:
    # 한번의 while문이 바로, 하나의 퍼즐을 푸는 프로그램
    c = [[False]*10 for _ in range(10)]
    c2 = [[False]*10 for _ in range(10)]
    c3 = [[False]*10 for _ in range(10)]
    domino = [[False]*10 for _ in range(10)]
    a = [[0]*9 for _ in range(9)]
    m = int(input())
    # 입력의 마지막 줄에는 0이 하나 주어진다
    # 0을 만나면, 퍼즐 맞추기를 종료한다
    if m == 0:
        break
    for i in range(m):
        n1, s1, n2, s2 = input().split()
        # n1, n2는 도미노에 쓰여진 숫자
        n1 = int(n1)
        n2 = int(n2)
        # s1, s2는 도미노 숫자의 address( 주소 )
        x1, y1 = convert(s1)
        x2, y2 = convert(s2)
        # a 라는 실제 배열에 넣는다
        # 우리는 '빈칸'에 도미노를 채워넣을 것이기 때문에
        # '빈칸'이 아닌 경우를 채워준다
        a[x1][y1] = n1
        a[x2][y2] = n2

        # 해당 위치의 도미노를 사용했다고 표시
        # 이게 필요한 이유는, 어느 시점에서 인접한 곳에 숫자를 배치 후
        # 도미노를 사용하려 할 때
        # 해당 위치에 도미노가 이미 사용되었다고 표시하는 것이다
        domino[n1][n2] = domino[n2][n1] = True

        # 가로, 세로 블록배열에 표시
        check(x1, y1, n1, True)
        check(x2, y2, n2, True)

    # 미리 배치된 숫자 정보 입력하기
    temp = input().split()
    for i in range(1, 10):
        s = temp[i-1]
        x, y = convert(s)
        a[x][y] = i
        check(x, y, i, True)
    print('Puzzle %d' % tc)
    go(0)
    tc += 1
