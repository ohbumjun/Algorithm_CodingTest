// https://www.acmicpc.net/problem/3055 

#define _CRT_SECURE_NO_WARNINGS //

#include<iostream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int dRow[4] = {-1, 1, 0, 0};
int dCol[4] = {0, 0, 1, -1};

int R, C;
vector<vector<char>> vecMap;
vector<vector<int>> vecDistMap;
queue<pair<int, int>> Queue;
queue<pair<int, int>> WaterQueue;
int AnimalTurn = 0;
int WaterTurn = 0;

int edR = -1, edC = -1;

void Input()
{
    // "S" 는 빈칸으로 만들어주기
    cin >> R >> C;

    vecMap = vector<vector<char>>(R, vector<char>(C));
    vecDistMap = vector<vector<int>>(R, vector<int>(C, INF));

    for (int r = 0; r < R; ++r)
    {
        for (int c = 0; c < C; ++c)
        {
            char Input;
            cin >> Input;
            vecMap[r][c] = Input;

            if (Input == 'S')
            {
                Queue.push(make_pair(r, c));
				vecMap[r][c] = '.';
                vecDistMap[r][c] = 0;
                AnimalTurn = 1;
            }
            else if (Input == 'D')
            {
                edR = r, edC = c;
            }
            else if (vecMap[r][c] == '*')
            {
                WaterQueue.push(make_pair(r, c));
                WaterTurn += 1;
            }
        }
    }
}

void Solve()
{
    // map
    // distMap

    // while문 큰거 한번
    while (!Queue.empty())
    {
        int AddedPath = 0;

        // cout << "AnimTurn : " << AnimalTurn << endl;
        // cout << "Queue Size : " << Queue.size() << endl;
        // cout << "WaterTurn : " << WaterTurn << endl;
        // cout << "WaterQueue Size : " << WaterQueue.size() << endl;
        // cout << endl;

        while (AnimalTurn > 0)
        {
		    // - 물, 돌 X 이동
		    // - 꺼냈는데, 현재 위치가 물이면 continue
		    // - 해당 queue 에 아무것도 없으면 break;
	        // - 최소 이동 값 Update
            pair<int, int> Animal = Queue.front();

            Queue.pop();
            AnimalTurn -= 1;

            int row = Animal.first;
            int col = Animal.second;

            // 현재 위치가 이미 물에 찼다면
            if (vecMap[row][col] == '*')
                continue;

            for (int k = 0; k < 4; ++k)
            {
                int nRow = row + dRow[k];
                int nCol = col + dCol[k];

                // 범위
                if (nRow < 0 || nRow >= R || nCol < 0 || nCol >= C)
                    continue;

                // 돌, 물
                if (vecMap[nRow][nCol] == '*' ||
                    vecMap[nRow][nCol] == 'X')
                    continue;

                if (vecDistMap[nRow][nCol] <= vecDistMap[row][col] + 1)
                    continue;

                vecDistMap[nRow][nCol] = vecDistMap[row][col] + 1;

                Queue.push(make_pair(nRow, nCol));
                AddedPath += 1;
            }
        }

        AnimalTurn = AddedPath;

        int NewWaterPath = 0;

        while (WaterTurn > 0)
        {
            pair<int, int> waterPos = WaterQueue.front();

            WaterQueue.pop();
            WaterTurn -= 1;

            int row = waterPos.first;
            int col = waterPos.second;

            for (int k = 0; k < 4; ++k)
            {
                int nRow = row + dRow[k];
                int nCol = col + dCol[k];

                // 범위
                if (nRow < 0 || nRow >= R || nCol < 0 || nCol >= C)
                    continue;

                // 돌, 물, 비버굴
                if (vecMap[nRow][nCol] == 'X' ||
                    vecMap[nRow][nCol] == 'D' ||
                    vecMap[nRow][nCol] == '*')
                    continue;

                vecMap[nRow][nCol] = '*';

                WaterQueue.push(make_pair(nRow, nCol));

                NewWaterPath += 1;
            }
        }

        WaterTurn = NewWaterPath;
    }

    // 최종적으로 D 에 있는 칸 
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input_c.txt", "r", stdin);

    Input();

    Solve();

    if (vecDistMap[edR][edC] == INF)
        cout << "KAKTUS" << endl;
    else
        cout << vecDistMap[edR][edC] << endl;

    return 0;
}