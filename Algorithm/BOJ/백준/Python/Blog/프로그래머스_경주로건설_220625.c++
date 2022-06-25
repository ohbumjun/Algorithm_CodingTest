// 주의할점 : 위치별 최소값이 아니라, 방향별 최소값을 구해야 한다.

#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <iostream>

using namespace std;

#define INF 999999

// 0 (빈칸 이동 가능)
// 1 (벽 이동 불가능)
// 직선 하나당 100
// 코너 하나당 500

int answer = 0;
int dRow[] = {-1, 0, 1, 0}; // 상, 좌, 하, 우
int dCol[] = {0, -1, 0, 1}; //

int vecDist[26][26][4];

int BFS(vector<vector<int>>& board)
{
    int N = board.size();
    
    for (int r = 0; r < N; ++r)
    {
        for (int c = 0; c < N; ++c)
        {
            for (int k = 0; k < 4; ++k)
                vecDist[r][c][k] = INF;
        }
    }
    
    // row, col, cost, prevD
    queue<tuple<int, int, int, int>> Queue;
    
    for (int k = 0; k < 4; ++k)
        vecDist[0][0][k] = 0;
    
    Queue.push(make_tuple(0,0,0,-1));
    
    
    while (!Queue.empty())
    {
        auto [cRow, cCol, cCost, prevD] = Queue.front();
        Queue.pop();
        
        // 4방향 조사
        for (int k = 0; k < 4; ++k)
        {
            int nRow = cRow + dRow[k];
            int nCol = cCol + dCol[k];
            
            // 범위 조사
            if (nRow >= N || nRow < 0 || nCol >= N || nCol < 0)
                continue;
            // 벽, 빈칸 여부 조사
            if (board[nRow][nCol] == 1)
                continue;
            // 비용 조사
            int addCost = 0;
            // 맨 처음 시작 or 같은 방향
            if (prevD == -1 || k == prevD)
                addCost = 100;
            else 
                addCost = 600;
            
            // 비용 비교
            int nxtCost = cCost + addCost;
            if (vecDist[nRow][nCol][k] >= nxtCost)
            {
                vecDist[nRow][nCol][k] = nxtCost;
                Queue.push(make_tuple(nRow,nCol,nxtCost,k));
            }
        }
    }
    
    /*
    for (int r = 0; r < N; ++r)
    {
        for (int c = 0; c < N; ++c)
        {
            for (int k = 0; k < 4; ++k)
                cout << vecDist[r][c][k] << ".";
            cout << " ";
        }
        cout << endl;
    }
    */
    
    // 4방향 이동 중 최소값 조사
    int minN = INF;
    for (int k = 0; k < 4; ++k)
    {
        if (minN > vecDist[N-1][N-1][k])
            minN = vecDist[N-1][N-1][k];
    }
    return minN;
}

int solution(vector<vector<int>> board) {

    return BFS(board);
}