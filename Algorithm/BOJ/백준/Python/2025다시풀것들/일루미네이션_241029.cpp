// https://www.acmicpc.net/problem/5547

// 최초 풀이
// 1 인 애들 찾아서 + 6 
// 1 인 애들, 인접도 1 이면 -1
// 0 인 애들 주변 모두가 1 이면, -6

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

using namespace std;

int W, H; // W : col / H : row
vector<vector<int>> map;
int answer = 0;

// 앞 : w, 뒤 : h
// even : H 가 짝수, odd : H 가 홀수
// 오, 오위, 위, 왼위, 왼, 왼아, 아, 오아
// int evenRow[6] = {1}
int evenCol[6] = {};

int oddRow[6];
int oddCol[6];

void Input()
{
    cin >> W >> H;
    map.resize(H + 1);
    for (int i = 0; i < H + 1; i++) map[i].resize(W + 1);

    for (int r = 1; r < H+1; r++)
        for (int c= 1; c < W+1; c++)
			cin >> map[r][c];
};

void Solve()
{
    // 일단 1 인 건물 주위에 벽 6 개를 전부 칠한다.

    for (int h = 1; h < H + 1; ++h)
        for (int w = 1; w < W + 1; ++w)
        {
            if (map[h][w] == 1) answer += 6;
        }

    // 26(-6) + 38 == 64
    // cout << "init answer : " << answer << endl;

    // 각 1 인 건물을 순회. 인접이 건물이면 -2 
    for (int h = 1; h <= H; ++h)
    {
        for (int w = 1; w <= W; ++w)
        {
            int minusCnt = 0;

            // 앞 : w, 뒤 : h
            if (map[h][w] != 1) continue;

            // cout << "w,h : " << w << ", " << h << endl;

            // 오
            if (w + 1 <= W && map[h][w + 1] == 1) minusCnt += 1;

            // 왼
            if (w - 1 >= 1 && map[h][w - 1] == 1) minusCnt += 1;

            if ((h + 1) % 2 != 1)   // 홀수
            {
                // 왼 위
                if (h - 1 >= 1 && map[h - 1][w] == 1) minusCnt += 1;
                // 오 위
                if (h - 1 >= 1 && w + 1 < W && map[h - 1][w+1] == 1) minusCnt += 1;
                // 오 아
                if (h + 1 <= H && w + 1 < W && map[h + 1][w + 1] == 1) minusCnt += 1;
                // 왼 아
                if (h + 1 <= H && map[h + 1][w] == 1) minusCnt += 1;
            }
            else                            // 짝수  
            {
                // 왼 위
                if (h - 1 >= 1 && w - 1 >= 0 && map[h - 1][w - 1] == 1) minusCnt += 1;
                // 오 위
                if (h - 1 >= 1 && map[h - 1][w] == 1) minusCnt += 1;
                // 오 아
                if (h + 1 <= H && map[h + 1][w] == 1) minusCnt += 1;
                // 왼 아
                if (h + 1 <= H && w - 1 >= 1 && map[h + 1][w - 1] == 1) minusCnt += 1;
            }

            // cout << "minusCnt : " << minusCnt << endl;
            answer -= minusCnt;
        }
    }

    // 0 인 건물 순회. 주변이 모두 건물이면 -1 * 6
     // 각 1 인 건물을 순회. 인접이 건물이면 -2 
    for (int h = 0; h < H; ++h)
    {
        for (int w = 0; w < W; ++w)
        {
            // 앞 : w, 뒤 : h
            if (map[h][w] != 0) continue;

            // 오
            if (w + 1 <= W && map[h][w + 1] == 0) continue;

            // 왼
            if (w - 1 >= 1 && map[h][w - 1] == 0) continue;

            if (h + 1 % 2 != 1)   // 홀수
            {
                // 이 부분 다시 작성해야 한다.
                // 왼 위
                if (h - 1 >= 1 && map[h - 1][w] == 0) continue;
                // 오 위
                if (h - 1 >= 1 && w + 1 <= W && map[h - 1][w + 1] == 0) continue;
                // 오 아
                if (h + 1 <= H && w + 1 <= W && map[h + 1][w + 1] == 0) continue;
                // 왼 아
                if (h + 1 <= H && map[h + 1][w] == 0) continue;
            }
            else                        // 짝수  
            {
                // 왼 위
                if (h - 1 >= 1 && w - 1 >= 0 && map[h - 1][w - 1] == 0) continue;
                // 오 위
                if (h - 1 >= 1 && map[h - 1][w] == 0) continue;
                // 오 아
                if (h + 1 <= H && map[h + 1][w] == 0) continue;
                // 왼 아
                if (h + 1 <= H && w - 1 >= 0 && map[h + 1][w - 1] == 0) continue;
            }

            // cout << "hello " << endl;
            answer -= 6;
        }
    }

    cout << answer << endl;
}

int main() {
    ios::sync_with_stdio(false);

    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();

    Solve();
    
    return 0;
}


// 정답 풀이
// https://velog.io/@i_am_gr00t/%EB%B0%B1%EC%A4%80-5547-%EC%9D%BC%EB%A3%A8%EB%AF%B8%EB%84%A4%EC%9D%B4%EC%85%98-C
// 기본적으로 벽이 아니라, 빈 공간을 중심으로 BFS
// BFS 로 공간들의 그룹을 만든다.
// BFS 한 호출이 곧 한 공간의 그룹
// 탐색하면서 인접 건물을 만나면 + 1
// 만약 oob 를 만나면, 둘러쌓이지 않은 것이므로
// wallcnt 를 리턴
// 만약 둘러쌓인 것이라면 0 을 리턴
// 한편, 가장 자리 건물들의 벽도 cnt 해야 하므로
// 해당 부분은 별도로 처리

// https://velog.io/@nnnyeong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%92%80%EC%9D%B4-%EB%B6%84%EC%84%9D-BOJ-5547-%EC%9D%BC%EB%A3%A8%EB%AF%B8%EB%84%A4%EC%9D%B4%EC%85%98
// 혹은 해당 방법과 같이 행,열을 늘려서 고려하는 방법도 있다.

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Pos {
    int x;
    int y;

    bool operator==(Pos input){
        return x == input.x && y == input.y;
    }
    Pos operator+(Pos input){
        Pos res;
        res.x = this->x + input.x;
        res.y = this->y + input.y;
        return res;
    }
};

int w, h;
vector<vector<int>> matrix;
vector<vector<Pos>> nextDir { // 아니 이게 문제에서는 1부터 시작인데 실제 인덱스는 0부터 시작이라 좀 바뀜;
    { {-1, 1}, {0, -1}, {-1, 0}, {1, 0}, {0, 1}, {1, 1} },  // even
    { {-1, -1}, {0, -1}, {-1, 0}, {1, 0}, {0, 1}, {1, -1} } // odd
};
vector<vector<int>> visited;

bool OOB(Pos input){
    return 0 > input.x || input.x >= h || 0 > input.y || input.y >= w;
}

int bfs(Pos start){
    bool isOut = false;
    int wallCnt = 0;

    queue<Pos> q;
    q.push(start);
    visited[start.x][start.y] = true;

    while (!q.empty()){
        Pos cur = q.front();
        q.pop();
        for (Pos d : nextDir[cur.x % 2]){
            Pos next = cur + d;
            if (OOB(next)) isOut = true;
            else if (matrix[next.x][next.y] == 1) wallCnt++;
            else if (!visited[next.x][next.y]){
                visited[next.x][next.y] = true;
                q.push(next);
            }
        }
    }

    if (isOut) return wallCnt;
    else return 0;
}

int main () {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    cin >> w >> h;
    int wallCnt = 0;
    matrix = vector<vector<int>> (h, vector<int>(w, 0));
    visited = vector<vector<int>> (h, vector<int>(w, false));
    for (int i=0; i < h; i++){
        for (int j=0; j < w; j++){
            cin >> matrix[i][j];
        }
    }
    for (int i=0; i < h; i++){
        for (int j=0; j < w; j++){
            if (matrix[i][j] == 1) {
                if (i == 0 || i == h-1 || j == 0 || j == w-1){ // 가장자리인 경우 OOB 체크해서 wallCnt++
                    for (Pos d : nextDir[i%2]){
                        Pos next = Pos{i, j} + d;
                        if (OOB(next)) wallCnt++;
                    }
                }
            }
            else {
                if (!visited[i][j]) wallCnt += bfs({i, j});
            }
        }
    }
    cout << wallCnt << endl;
    
    return 0;
}