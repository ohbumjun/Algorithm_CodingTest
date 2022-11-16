# https://www.acmicpc.net/problem/16954
import sys
from collections import deque
import heapq as hq
sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(1001*1001)

'''
< 캐릭터 관점 >
이동할 수 있는 9가지 조건

- 상하좌우
- 대각선 4방향
- 제자리

여기서 중요한 것이 있다
1) 이동할 칸에 벽이 있으면 이동할 수 없다
2) 뿐만 아니라, ( ex) 오른쪽으로 이동한다고 했을 때 )오른쪽 위에 벽이 있으면 이동할 수 없다
왜 ? 1초후에, 현재 캐릭터 기준 오른쪽으로 내려올 것이기 때문이다 

< 지도 >
1번째 방법
- 지도는 8*8 이다
그리고 각 벽은 1초에 한칸씩 내려온다

다시 말하면 8초후에는, 모든 칸이 빈칸이 된다는 것

따라서, 0초,1초, ... 8초. 후의 지도
총 9가지 지도의 개수를 고려할 수 있다는 것이다

----------------------------------------------------------------

자. 그래서 우리는 캐릭터의 이동정보를 표시할 때
( x, y, t ) : 위치 + 시간
을 통해 표시한다

왜 ??
초마다 지도를 다르게 표시한다고 했다.
즉, 해당 위치 + 언제 거기에 캐릭터가 있는지가
더 중요한 정보이기 때문이다 

즉 몇초 후에, 해당 위치에 있는 것이냐 !!
여기서 고려할 점은, t가 8이상이 될때부터는, 다 같게 취급한다는 것
어차피 지도에는 8초 이후부터는 벽이 없는, 동일한 지도 정보로 존재할 것이기 때문이다

----------------------------------------------------------------

그런데, 사실은 지도를 9개나 표시할 이유는 없다.
하나만 사용해도 된다

특정 시점 t초 후에, 벽이 있는지 없는지를 알아낼 수 있기 때문이다

현재 3초, 그리고 (r,c) 에 벽이 있다는 것은
3초 이전에, 즉, ( r-3,c )에 벽이 있다는 얘기이기 때문이다

----------------------------------------------------------------
자. 이제 캐릭터가 이동한다고 해보자.

현재 t초  , ( r,c ) 에서
다음 t+1초, ( nr, nc ) 로 이동한다고 했을 때, 

1) 현재 같은 시간 시점에 이동할 칸에 벽이 있는 경우 : A[nr-t][nc] == '#'
2) 이동한 이후, 해당 칸으로 벽이 이동할 경우 ( t + 1 을 고려 ) : A[nr-(t+1)][nc] == '#'

이게 되면, 이동할 수 없게 되는 것이다 

'''
dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

arr = [list(input()) for _ in range(8)]
# 특정 t에, 해당 위치에 있는 것인가 ! => 즉, 정점의 정의는 x,y,t 라는 3가지 정보에 의해 정의된다
# 즉, t초 후의 Map 에서 x,y 를 방문한 적이 있는가 !
# 어차피, 같은 곳은 두번 방문할 필요가 없으니까, 같은 시간에
# 또한, check[x][y][8 ~ infinite] 부터는, 사실, 같은 Map이다. 즉, 벽이 없는 Map
# 그 상태에서는, 그냥 이후 모든 값을, 벽이 없는 Map 에서 해당 x,y에 도달한 적이 있는가.를 조사하면 된다.
check = [[[0] * 9 for _ in range(8)]for _ in range(8)]


ans = -1
check[7][0][0] = 1
queue = deque([(7, 0, 0)])

while queue:
    x, y, t = queue.popleft()
    if x == 7 and y == 7:
        ans = 1
        break
    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or 8 <= nx or ny < 0 or 8 <= ny:
            continue
        nt = min(8, t+1)
        # 현재 시점에 이동하려는 곳에 벽이 있는가
        if nx - t >= 0 and arr[nx-t][ny] == '#':
            continue
        # 1초후에, 이동하려는 곳 , 한칸 행 위에 벽이 있는가
        if nx - (t+1) >= 0 and arr[nx-(t+1)][ny] == '#':
            continue

        if check[nx][ny][nt] == 0:
            check[nx][ny][nt] = 1
            queue.append((nx, ny, nt))
print(1 if ans else 0)


'''
C++


# include <iostream>
# include <tuple>
# include <vector>
# include <string>
# include <queue>
using namespace std
bool check[8][8][9]
int dx[] = {0, 0, 1, -1, 1, -1, 1, -1, 0}
int dy[] = {1, -1, 0, 0, 1, 1, -1, -1, 0}
int main() {
    int n = 8
    vector < string > a(n)
    for (int i=0
         i < n
         i++) {
        cin >> a[i]
    }
    queue < tuple < int, int, int >> q
    check[7][0][0] = true
    q.push(make_tuple(7, 0, 0))
    bool ans = false
    while (!q.empty()) {
        int x, y, t
        tie(x, y, t) = q.front()
        q.pop()
        if (x == 0 & & y == 7) ans = true
        for (int k=0
             k < 9
             k++) {
            int nx = x+dx[k]
            int ny = y+dy[k]
            int nt = min(t+1, 8)
            if (0 <= nx & & nx < n & & 0 <= ny & & ny < n) {
                if (nx-t >= 0 & & a[nx-t][ny] == '#') continue
                if (nx-t-1 >= 0 & & a[nx-t-1][ny] == '#') continue
                if (check[nx][ny][nt] == false) {
                    check[nx][ny][nt] = true
                    q.push(make_tuple(nx, ny, nt))
                }
            }
        }
    }
    cout << (ans ? 1: 0) << '\n'
    return 0
}

'''
''' 자체 풀이 버전
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <algorithm>
#include <unordered_map>

#define endl "\n"

using namespace std;

vector<vector<char>> mapChess;
vector<vector<bool>> mapCheck;

int dRow[] = {-1,1,0,0, -1,-1,1, 1,0 };
int dCol[] = { 0,0,1,-1,-1, 1,-1,1,0 };

void Input()
{
    mapChess.resize(8);
    mapCheck.resize(8);

    for (int i = 0; i < 8; ++i)
    {
        mapChess[i].resize(8);
        mapCheck[i].resize(8);
    }

    for (int r = 7; r >= 0; --r)
    {
        for (int c = 0; c < 8; ++c)
        {
            char input;
            cin >> input;
            // 아래행에서부터 시작하기
            mapChess[r][c] = input;

            // 방문 여부
            mapCheck[r][c] = false;
        }
    }

    // Init Map
    //cout << "Init Map" << endl;
    //for (int r = 7; r >=0; --r)
    //{
    //    for (int c = 0; c < 8; ++c)
    //    {
    //        cout << mapChess[r][c] << ",";
    //    }
    //    cout << endl;
    //}
};

void DEBUGMap(vector<vector<bool>>& curCheck, int curRow, int curCol)
{
    cout << "curR, curC : " << curRow << "," << curCol << endl;
    cout << "check" << endl;
    for (int r = 7; r >= 0; --r)
    {
        for (int c = 0; c < 8; ++c)
        {
            cout << curCheck[r][c] << ".";
        }
        cout << endl;
    }
    cout << endl;
}

void Solve()
{
    // Queue : r,c, map
    queue<tuple<int, int, vector<vector<char>>, vector<vector<bool>>>> Queue;
    Queue.push(make_tuple(0, 0, mapChess, mapCheck));

    while (!Queue.empty())
    {
        auto [curRow, curCol, curMap, curCheck] = Queue.front();
        Queue.pop();

        curCheck[curRow][curCol] = true;

        vector<pair<int, int>> vNxtPoses;

        // 현재 위치에서 이동 가능한 새로운 위치 정보를 vector 에 모아둔다
        for (int k = 0; k < 9; ++k)
        {
            int nxtRow = curRow + dRow[k];
            int nxtCol  = curCol + dCol[k];

            // 범위
            if (nxtRow < 0 || nxtRow >= 8 || nxtCol < 0 || nxtCol >= 8)
                continue;

            // 벽 X
            if (curMap[nxtRow][nxtCol] == '#')
                continue;

            // 이미 방문 ? X (But 제자리인 경우는 예외)
            if (k != 8 && curCheck[nxtRow][nxtCol])
                continue;

            // 조사하던 와중 목적지에 도달하면 1 을 출력하고 break
            if (nxtRow == 7 && nxtCol == 7)
            {
                cout << 1 << endl;
                exit(0);
            }

            vNxtPoses.push_back(make_pair(nxtRow, nxtCol));
        }

        // 무한 루프를 어떻게 해결해야 하는가.

        vector<vector<char>> newMap = curMap;

        // 현재 벽들을 한칸 내린다
        // 아래서부터 내린다.
        for (int r = 0; r < 8; r++)
        {
            for (int c = 0; c < 8; ++c)
            {
                if (curMap[r][c] == '#')
                {
                    // 현재 위치는 벽 X
                    newMap[r][c] = '.';

                    // 맨 아래에 있던 벽은 사라짐
                    if (r == 0)
                        continue;

                    // 아래칸을 벽으로 세팅
                    newMap[r - 1][c] = '#';
                }
            }
        }

        // 새로운 위치 정보 중에서 벽과 부딪히는 부분들을 제외시킨다.
        for (const auto& [nR, nC] : vNxtPoses)
        {
            // 그 다음에 벽이라면 이동 X
            if (newMap[nR][nC] == '#')
                continue;

            // 새로운 위치 정보와 함께 새롭게 Queue 에 추가한다.
            Queue.push(make_tuple(nR, nC, newMap, curCheck));
        }
    }


    cout << 0 << endl;
};

int main() {
    ios::sync_with_stdio(false);

    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();

    Solve();
    
    return 0;
}


'''