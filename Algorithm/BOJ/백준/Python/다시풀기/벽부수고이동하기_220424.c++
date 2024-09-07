#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>
#include <string>
#include <cmath>
#include <climits>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N, M;

// ex) vecDist[1][0][0] -> 벽을 1개 부수고, (0,0) 까지의 최소 거리
std::vector<std::vector<std::vector<int>>> vecDist;

// 행렬로 표현되는 맵이 존재한다.
std::vector<std::vector<int>> vecMap;

// 방향 정보
int dRow[4] = { 0 , 0, -1, 1 };
int dCol[4]  = { -1, 1, -0, 0 };

void Input()
{
    cin >> N >> M;

    // Map 정보 세팅하기
    vecMap.reserve(N);

    for (int i = 0; i < N; ++i)
    {
        vecMap.push_back(std::vector<int>(M, 0));
    }

    for (int row = 0; row < N; ++row)
    {
        std::string nString;
        cin >> nString;

	    for (int col = 0; col < M; ++col)
	    {
            vecMap[row][col] = nString[col] - '0';
	    }
    }

    // 거리 정보 세팅하기
    vecDist.resize(2);

    for (int i = 0; i < 2; ++i)
    {
        vecDist[i].reserve(N);

        for (int j = 0; j < N; ++j)
        {
            vecDist[i].push_back(std::vector<int>(M, INF));
        }
    }
}

void BFS()
{
    /*
    // Map 정보 출력
    for (int r = 0; r < N; ++r)
    {
	    for (int c = 0; c < M; ++c)
	    {
            cout << vecMap[r][c] << ".";
	    }
        cout << endl;
    }
    */

    // Queue
    queue<tuple<int, int, int>> Queue;

    // 시작점 Queue 추가
    // 부순 벽 개수, row, col
    Queue.push(make_tuple(0, 0, 0));

    // 거리 세팅
    vecDist[0][0][0] = 1;

    while (!Queue.empty())
    {
        tuple<int, int, int> Info = Queue.front();

        Queue.pop();

        int wallN    = std::get<0>(Info);
        int curRow = std::get<1>(Info);
        int curCol  = std::get<2>(Info);

        // 4방향 탐색
        for (int k = 0; k < 4; ++k)
        {
            int nRow = curRow + dRow[k];
            int nCol  = curCol + dCol[k];

            // 범위 조사
            if (nRow >= N || nRow < 0 || nCol >= M || nCol < 0)
                continue;

            // 1) 벽이 아닐 경우
            if (vecMap[nRow][nCol] == 0)
            {
	            // 방문 되지 않은 곳이라면
                if (vecDist[wallN][nRow][nCol] == INF)
                {
                    // BFS 를 지속한다.
                    vecDist[wallN][nRow][nCol] = vecDist[wallN][curRow][curCol] + 1;

                    Queue.push(make_tuple(wallN, nRow, nCol));
                }
            }

            // 2) 벽일 경우
            if (vecMap[nRow][nCol] == 1)
            {
                // 아직 벽을 한번도 깨부신적이 없다면, 깨고 표시한다.
                if (wallN == 0)
                {
                    int nDist = vecDist[wallN][curRow][curCol] + 1;

                    // 방문된 곳이라면 거리 비교하기
                    if (vecDist[wallN + 1][nRow][nCol] < nDist)
                        continue;

                    vecDist[wallN + 1][nRow][nCol] = nDist;

                    Queue.push(make_tuple(wallN + 1, nRow, nCol));
                }
            }
        }
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();

    BFS();

    int Answer = -1;

    int NBreakDist = vecDist[0][N - 1][M - 1];
    int YBreakDist = vecDist[1][N - 1][M - 1];

    if (NBreakDist == INF && YBreakDist == INF)
        Answer = -1;
    else
    {
	    Answer = NBreakDist < YBreakDist ? NBreakDist : YBreakDist;
    }

    cout << Answer;

    return 0;
}