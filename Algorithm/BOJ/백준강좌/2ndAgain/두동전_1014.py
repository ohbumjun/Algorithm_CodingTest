# https://www.acmicpc.net/problem/16197

'''
중요한 점은 
1) 한번 이동시, 두 동전은 '같은' 방향으로 이동한다는 것이다
2) 최대 이동 10번으로 제한

이에 근거할 때,
총 4 ^ 10 까지의 경우가 있을 것이다
왜냐하면, 한번의 이동으로 움직일 수 있는 방향이
총 4가지이기 때문이다.

" 함수를 구현하기 위해 필요한 정보 "
1. 몇번째 버튼을 누르는 것인가 ?
즉, 버튼을 누른 횟수

2. 버튼을 누르면, 무엇이 변하는가 ?
- 동전의 위치가 이동한다
- 보드의 상태가 변하는 것

여기서 중요한 점은,
보드의 상태를 넣을 때 
보드 전체를 넣으면 안된다.
우리는 brute force 형태로
반복 진행을 할 것인데 ,

보드 상태 전체가
계속 반복되어 넘어가게 되면
문제가 될 수 있다

공간이 비효율적이다.
왜 비효율적 ?
왜냐하면, 변하지 않는 값의 저장.이 일어나기 때문이다

매 상태마다 변하는 값은
4칸이다 ( 2개 동전 이동 전, 후)

'''

'''
go( step x1, y1, x2, y2 )

- step       : 버튼을 누른 횟수
- (x1, y1)   : 한 동전의 위치
- ( x2, y2 ) : 다른 동전의 위치 

일반적으로는
'범위에 대한 검사'를 하고나서
'이동'을 했다

하지만, 이번에는 다르다.
일단 이동을 하고

그 다음 범위 검사를 할것이다.
왜 ? 우리는 떨어졌는지를 봐야한다

그래서, 일단 이동해보고,
떨어졌는지 안떨어졌는지를 
검사해볼 것이다

'''


'''
재귀 함수를 구현시 

1) 정답을 찾은 경우 : 하나만 떨어짐
2) 불가능한 경우    : 둘다 떨어진 경우 or STEP == 11
3) 다음 경우        : 4번 이동 ( 4방향 이동 )  >> step + 1 


'''


'''
로직

1) 일단 2개 동전 위치를 찾는다
2) x1,y1  // x2,y2 에 넣어준다
3) 그리고 해당 영역을 빈칸으로 만들어준다 
- 왜 빈칸으로 만들어주는 것일까 ?
어차피 동전이 있는 곳으로도 이동할 수 있다.
더이상 이동에 있어, 2차원 배열 상에서의
동전 정보는 더이상 필요 없다
- 동전 이동 전,후의 정보를 비교하기 위해서
그저 현재 동전을 다른 칸으로 이동만 시켜준다면
기존 칸을 빈칸으로 만들어주는 불필요한
작업을 할 필요가 없다....??


함수 로직
1) step 이 11일때 return
떨어졌는지 검사 : fail1, fail2 
2) 둘다 -1 떨어짐 ? fail
3) 하나만 떨어짐 ? return step

이동하지 않는다. 를 처리하기
4개 방향의 새 x,y 좌표를 받는다
각각 범위안 + 그다음 # : 기존 nx, ny는
다시 세팅

새로운 애로 go 실행,
리턴값 받는다 

해당 리턴값이 1이라면, continue
어떤 작업 혹은 비교도 하지 않고

왜 ? 
우리는 '가능한 경우' 중에서
'최소 step'을 찾고 싶은것

처음 ans를 -1로 설정하기

if( ans == -1 || anx > tmp ) :
    ans = tmp

return tmp
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def go(step, x1, y1, x2, y2):
    # 최대 10번만 이동가능하기 때문에 아래와 같은 처리해주기
    if step == 11:
        return -1
    fall1 = False
    fall2 = False
    # 떨어짐 처리 : 둘다 떨어짐 fail // 하나만 떨어짐 : 정답 !
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step
    ans = -1
    # 현재 좌표에서도 답을 못구한 경우이므로 4개 방향 고려
    for k in range(4):
        nx1, ny1 = x1+dx[k], y1+dy[k]
        nx2, ny2 = x2+dx[k], y2+dy[k]
        # 범위 안에 존재  + 벽 : 이동x 처리
        if 0 <= nx1 < n and 0 <= ny1 < m and a[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if 0 <= nx2 < n and 0 <= ny2 < m and a[nx2][ny2] == '#':
            nx2, ny2 = x2, y2
        # 그 다음 이동값이 -1이면 무시
        # 우리가 구하고자 하는 값은 '최소 이동 횟수', -1은 고려 x
        # 이렇게 위에서 ( if fall1 or fall2 :  ) 에서 비교하는 것이 아니라
        # 이와 같이, return을 받은 형태로 작성하는 코드
        temp = go(step+1, nx1, ny1, nx2, ny2)
        if temp == -1:
            continue
        # 비교하고자 하는 값 : 떨어지는 값 중, 최소 이동 횟수
        # 1) ans == -1  : 답이 없는 경우
        # 2) ans > temp : 최소 값
        if ans == -1 or ans > temp:
            ans = temp
    return ans


n, m = map(int, input().split())
x1 = y1 = x2 = y2 = -1
a = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            a[i][j] = '.'  # 빈칸으로 만들어주면 깔끔해지니까 !!
print(go(0, x1, y1, x2, y2))

'''
C++  -------------------------
#include <iostream>
using namespace std;
int n, m;
string a[20];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int go(int step, int x1, int y1, int x2, int y2) {
    if (step == 11) return -1;
    bool fall1=false, fall2=false;
    if (x1 < 0 || x1 >= n || y1 < 0 || y1 >= m) fall1 = true;
    if (x2 < 0 || x2 >= n || y2 < 0 || y2 >= m) fall2 = true;
    if (fall1 && fall2) return -1;
    if (fall1 || fall2) return step;
    int ans = -1;
    for (int k=0; k<4; k++) {
        int nx1 = x1+dx[k];
        int ny1 = y1+dy[k];
        int nx2 = x2+dx[k];
        int ny2 = y2+dy[k];
        if (0 <= nx1 && nx1 < n && 0 <= ny1 && ny1 < m && a[nx1][ny1] == '#') {
            nx1 = x1;
            ny1 = y1;
        }
        if (0 <= nx2 && nx2 < n && 0 <= ny2 && ny2 < m && a[nx2][ny2] == '#') {
            nx2 = x2;
            ny2 = y2;
        }
        
        int temp = go(step+1, nx1, ny1, nx2, ny2);
        if (temp == -1) continue;
        if (ans == -1 || ans > temp) {
            ans = temp;
        }
    }
    return ans;
}
int main() {
    cin >> n >> m;
    int x1,y1,x2,y2;
    x1=y1=x2=y2=-1;
    for (int i=0; i<n; i++) {
        cin >> a[i];
        for (int j=0; j<m; j++) {
            if (a[i][j] == 'o') {
                if (x1 == -1) {
                    x1 = i;
                    y1 = j;
                } else {
                    x2 = i;
                    y2 = j;
                }
                a[i][j] = '.';
            }
        }
    }
    cout << go(0,x1,y1,x2,y2) << '\n'; 
    return 0;
}

'''
