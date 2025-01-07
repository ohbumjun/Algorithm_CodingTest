// https://softeer.ai/app/assessment/index.html?xid=350601&xsrfToken=XspWIOw1nE27EfS0AeOGTqXYGqHDd5G2&testType=practice

// 1번째 풀이 : 25/100
// >> 문제 이해 부족 : '순서대로' 방문을 해야 한다.
// 나의 경우에는 그저, 모든 지점을 방문했는가에 대한 풀이만 존재했다
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

// #define DEBUG 1

int dRow[] = {-1, 1, 0, 0};
int dCol[] = {0, 0, -1, 1};

int M, N;

// m 개 지점 방문
// 상하좌우
// 벽 지나갈 수 x
// 한번만 방문
// start : 출발 지점 -> end : 마지막 지점

// 1) st, ed 모든 경우의 수 만들기
// 각각에 대해서 bfs 진행하기
// 만약 도달 ed map 이 유효한 값이면 answer += 1
// (4 * 4) * (4 * 3)

int map[4][4];
vector<pair<int,int>> targets;

void dfs(int curR, int curC, vector<vector<bool>>& visit, const pair<int,int>& ed, int& totCnt, int visitCnt)
{
    if (curR == ed.first && curC == ed.second)
    {
        if (visitCnt == M)
            totCnt += 1;
        return;
    }
    
    visit[curR][curC] = true;

    #ifdef DEBUG
    // cout << "curR, curC, visitCnt : " << curR << "," << curC << "," << visitCnt << endl;
    #endif
    for (int d = 0; d < 4; ++d)
    {
        int nxtR = curR + dRow[d];
        int nxtC = curC + dCol[d];
        if (nxtR < 0 || nxtR >= N || nxtC < 0 || nxtC >= N)
            continue;
        if (map[nxtR][nxtC] == 1) // 벽
            continue;
        if (visit[nxtR][nxtC])
            continue;
        int nxtVisit = map[nxtR][nxtC] == 2 ? visitCnt + 1 : visitCnt;
        dfs(nxtR, nxtC, visit, ed, totCnt, nxtVisit);
    }
    visit[curR][curC] = false;
}

int canVisit(const pair<int,int>& st, const pair<int,int>& ed)
{
    #ifdef DEBUG
    cout << "----------------------" << endl;
    cout << "st : " << st.first << "," << st.second << endl;
    cout << "ed : " << ed.first << "," << ed.second << endl;
    #endif
    vector<vector<bool>> visit(N, vector<bool>(N, false));
    visit[st.first][st.second] = true;
    int totCnt = 0;
    int visitCnt = 1;
    dfs(st.first, st.second, visit, ed, totCnt, visitCnt);
    #ifdef DEBUG
    cout << "totCnt : " << totCnt << endl;
    #endif
    return totCnt;
}

int main(int argc, char** argv)
{
    cin >> N >> M;

    #ifdef DEBUG
    cout << "N, M : " << N << "," << M << endl;
    #endif
    
    int answer = 0;
    
    for (int r = 0; r < N; ++r)
        for (int c = 0; c < N; ++c)
            cin >> map[r][c];

    for (int m = 0; m < M; ++m)
    {
        int r, c;
        cin >> r >> c;
        r -= 1; c -= 1;
        targets.push_back({r, c});
        map[r][c] = 2;
    }

    #ifdef DEBUG
        for (int r = 0; r < N; ++r)
        {
            for (int c = 0; c < N; ++c)
                cout << map[r][c] << ".";
            cout << endl;
        }
            
    #endif
    const pair<int,int>& start = targets[0];
    const pair<int,int>& end = targets[targets.size() - 1];
    answer += canVisit(start, end);

    cout << answer << endl;

    return 0;
}

// 2번째 풀이 : 순서대로 방문 풀이 과정으로 수정
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

// #define DEBUG 1

int dRow[] = {-1, 1, 0, 0};
int dCol[] = {0, 0, -1, 1};

int M, N;

// m 개 지점 방문
// 상하좌우
// 벽 지나갈 수 x
// 한번만 방문
// start : 출발 지점 -> end : 마지막 지점

// 1) st, ed 모든 경우의 수 만들기
// 각각에 대해서 bfs 진행하기
// 만약 도달 ed map 이 유효한 값이면 answer += 1
// (4 * 4) * (4 * 3)

int map[4][4];
vector<pair<int,int>> targets;

void dfs(int curR, int curC, vector<vector<bool>>& visit, int nxtIndex, int& totCnt, int debugCnt)
{
    const pair<int,int>& ed = targets[nxtIndex];

    if (curR == ed.first && curC == ed.second)
    {
        if (nxtIndex == M - 1)
            totCnt += 1;
        else 
        {
            dfs(ed.first, ed.second, visit, nxtIndex + 1, totCnt, debugCnt);
        }
        return;
    }

    visit[curR][curC] = true;

    #ifdef DEBUG
    cout << "curR, curC, visitCnt : " << curR << "," << curC << "," << visitCnt << endl;
    #endif

    if (debugCnt > 20)
        return;
    
    for (int d = 0; d < 4; ++d)
    {
        int nxtR = curR + dRow[d];
        int nxtC = curC + dCol[d];
        if (nxtR < 0 || nxtR >= N || nxtC < 0 || nxtC >= N)
            continue;
        if (map[nxtR][nxtC] == 1) // 벽
            continue;
        if (visit[nxtR][nxtC])
            continue;
        dfs(nxtR, nxtC, visit, nxtIndex, totCnt, debugCnt + 1);
    }
    visit[curR][curC] = false;
}

int main(int argc, char** argv)
{
    cin >> N >> M;

    #ifdef DEBUG
    cout << "N, M : " << N << "," << M << endl;
    #endif
    
    int answer = 0;
    
    for (int r = 0; r < N; ++r)
        for (int c = 0; c < N; ++c)
            cin >> map[r][c];

    for (int m = 0; m < M; ++m)
    {
        int r, c;
        cin >> r >> c;
        r -= 1; c -= 1;
        targets.push_back({r, c});
        map[r][c] = 2;
    }

    #ifdef DEBUG
        for (int r = 0; r < N; ++r)
        {
            for (int c = 0; c < N; ++c)
                cout << map[r][c] << ".";
            cout << endl;
        }
            
    #endif
    const pair<int,int>& start = targets[0];
    const pair<int,int>& end = targets[targets.size() - 1];
    vector<vector<bool>> visit(N, vector<bool>(N, false));
    int totCnt = 0;
    int debugCnt = 0;
    dfs(start.first, start.second, visit, 1, totCnt, debugCnt);

    cout << totCnt << endl;

    return 0;
}