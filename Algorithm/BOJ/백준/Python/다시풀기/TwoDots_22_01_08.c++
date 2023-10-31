#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int dx[4] = { 0,0,-1,1 };
int dy[4] = { 1,-1,0,0 };

vector<vector<int>> ColorMaps;
vector<vector<bool>> CheckMaps;

int ROW, COL;
int ANS = 0;

// 싸이클을 찾는 원리는
// 상하좌우 방향으로 탐색을 진행한다
// 단, 색상이 다르면 진행하지 않고, 같은 색상이라면, 현재까지 같은 색상정보에 대한 정보도 가지고 온다
// 그리고 처음 시작 위치에 대한 정보도 계속 유지한다.
// 이전 위치도 기록해서, 해당 방향으로는 검사하지 않게 세팅한다.
// 그리고 지금까지 거쳐온 정점 위치들도 vector에 저장하면서 온다.
// 만약, 다음 갈 위치가 처음 위치와 동일하고, 현재까지 온 개수가 3이상이라면 싸이클
// 전역 변수 ans에 더해준다
// 그리고 vector 에 들어있는 idx에 해당하는 정점들을 모두 check true로 세팅해준다.
void findCycle(int curRow, int curCol, int initRow, int initCol, vector<pair<int, int>> vecIdx, int curNum)
{
    for (int k = 0; k < 4; k++)
    {
        int nxtRow = curRow + dx[k];
        int nxtCol = curCol + dy[k];

        // 범위 제한 
        if (nxtRow < 0 || nxtRow >= ROW || nxtCol < 0 || nxtCol >= COL)
            continue;

        // 색상이 다르면 제한
        if (ColorMaps[nxtRow][nxtCol] != ColorMaps[curRow][curCol])
            continue;

        // 색상이 같다면 
        if (ColorMaps[nxtRow][nxtCol] == ColorMaps[curRow][curCol])
        {
            // 시작점이라면 ( 즉, 싸이클로 판명이 난다면 )
            if (curNum >= 3 && (nxtRow == initRow && nxtCol == initCol))
            {
                cout << "Yes";
                exit(0);
            }

            // 같은 색이되 방문한 적이 있다면 Pass
            pair<int, int> tempP;
            tempP = make_pair(nxtRow, nxtCol);
            if (find(vecIdx.begin(), vecIdx.end(), tempP) != vecIdx.end())
            {
                continue;
            }

            // 그외 진행 
            std::vector<pair<int, int>> nvecIdx;
            nvecIdx.resize(vecIdx.size());
            std::copy(vecIdx.begin(), vecIdx.end(), nvecIdx.begin());
            nvecIdx.push_back(std::make_pair(curRow, curCol));

            // 방문 처리 
            findCycle(nxtRow, nxtCol, initRow, initCol, nvecIdx, curNum + 1);

        }
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    cin >> ROW >> COL;

    ColorMaps = vector<vector<int>>(ROW, vector<int>(COL, 0));

    for (int i = 0; i < ROW; i++)
    {
        string chars;
        cin >> chars;
        for (int j = 0; j < COL; j++)
        {
            ColorMaps[i][j] = chars[j];
        }
    }

    for (int row = 0; row < ROW; row++)
    {
        for (int col = 0; col < COL; col++)
        {
            vector<pair<int, int>> vecIdx;
            vecIdx.push_back(make_pair(row, col));
            findCycle(row, col, row, col, vecIdx, 1);
        }
    }

    string Answer = ANS == 0 ? "No" : "Yes";
    cout << Answer;

    return 0;
}


