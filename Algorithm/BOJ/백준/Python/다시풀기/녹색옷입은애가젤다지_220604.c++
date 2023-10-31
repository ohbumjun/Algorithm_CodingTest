#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <array>
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

int N;

int dRow[4] = { 1,-1,0,0 };
int dCol[4] = { 0,0,-1,1 };

void Input()
{
  
}

void Solve()
{
    int Cnt = 1;

    while (true)
    {
        cin >> N;

        if (N == 0)
            break;

        std::vector<std::vector<int>> vecCave;
        vecCave.resize(N);

        std::vector<std::vector<int>> vecMinDist;
        vecMinDist.resize(N);

        // 각 정점 위치 마다 -> 다른 정점, 비용
        std::unordered_map<int, std::vector<pair<int, int>>> vecGraph;

        for (int i = 0; i < N; ++i)
        {
            vecCave[i].resize(N);
            vecMinDist[i] = std::vector<int>(N, INF);
        }

        for (int i = 0; i < N; ++i)
        {
            for (int c = 0; c < N; ++c)
            {
                int Input;
                cin >> Input;
                vecCave[i][c] = Input;
            }
        }

        vecMinDist[0][0] = vecCave[0][0];


        for (int r = 0; r < N; ++r)
        {
            for (int c = 0; c < N; ++c)
            {
                int Key = r * N + c;

                for (int k = 0; k < 4; ++k)
                {
                    int nRow = r + dRow[k];
                    int nCol = c + dCol[k];

                    if (nRow < 0 || nRow >= N || nCol < 0 || nCol >= N)
                        continue;

                    vecGraph[Key].push_back(make_pair(nRow * N + nCol, vecCave[nRow][nCol]));
                }
            }
        }

        // 다익스트라
        priority_queue<pair<int, int>> Queue;

        // 가장 작은 비용의 녀석이 뽑히도록 해야 한다.
        Queue.push(make_pair(vecMinDist[0][0] * -1, 0));

        while (!Queue.empty())
        {
            pair<int, int> minInfo = Queue.top();
            Queue.pop();

            int curIdx = minInfo.second; // row * N + col
            int curDist = minInfo.first * -1;

            if (vecMinDist[curIdx / N][curIdx % N] < curDist)
                continue;

            vecMinDist[curIdx / N][curIdx % N] = curDist;

            size_t Size = vecGraph[curIdx].size();

            for (size_t i = 0; i < Size; ++i)
            {
                int nxtIdx = vecGraph[curIdx][i].first;
                int nxtCost = vecGraph[curIdx][i].second;

                if (vecMinDist[nxtIdx / N][nxtIdx % N] != INF)
                    continue;

                Queue.push(make_pair((nxtCost + curDist) * -1, nxtIdx));
            }
        }
        cout << "Problem " << Cnt << ": " << vecMinDist[N-1][N-1] << endl;
        Cnt++;
    }
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