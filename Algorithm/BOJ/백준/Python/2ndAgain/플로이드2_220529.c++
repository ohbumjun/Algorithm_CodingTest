#define _CRT_SECURE_NO_WARNINGS

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

int N, M;
vector<vector<int>> Graph;
vector<vector<list<int>>> vecPath;

void Input()
{
    cin >> N;
	cin >> M;

    Graph = vector<vector<int>>(N + 1,vector<int>(N + 1, INF));
    vecPath = vector<vector<list<int>>>(N + 1, vector<list<int>>(N + 1, list<int>(0)));

    // 자기 자신으로 거리는 0
    for (int i = 1; i <= N; ++i)
    {
        Graph[i][i] = 0;
        // vecPath[i][i].push_back(i);
    }

    // Graph 정보 세팅
    for (int i = 0; i < M; ++i)
    {
        int st, ed, cost;
        cin >> st >> ed >> cost;

        if (Graph[st][ed] > cost)
    		Graph[st][ed] = cost;

        // vecPath[st][ed].push_back(st);
        // vecPath[st][ed].push_back(ed);

        // cout << st << ". " << ed << ". " << cost << endl;
    }
}

void Solve()
{
    for (int k = 1; k <= N; ++k)
    {
	    for (int st = 1; st <= N; ++st)
	    {
		    for (int ed = 1; ed <= N; ++ed)
		    {
                if (k == st || k == ed)
                    continue;

                if (Graph[st][k] + Graph[k][ed] > Graph[st][ed])
                    continue;

                // 거리 정보 Update
                Graph[st][ed] = Graph[st][k] + Graph[k][ed];

                // Path 정보 Update
                // 해당 Path 정보를 지워준다.
                vecPath[st][ed].clear();

                // 첫번째 Path 정보를 넣어준다.
                {
                    auto iter = vecPath[st][k].begin();
                    auto iterEnd = vecPath[st][k].end();

                    for (; iter != iterEnd; ++iter)
                    {
                        vecPath[st][ed].push_back((*iter));
                    }
                }

                vecPath[st][ed].push_back(k);

                // 두번째 Path 정보를 넣어준다.
                {
                    int Cnt = 0;

                    auto iter = vecPath[k][ed].begin();
                    auto iterEnd = vecPath[k][ed].end();

                    for (; iter != iterEnd; ++iter)
                    {
                        vecPath[st][ed].push_back((*iter));
                    }
                }
		    }
	    }
    }

    for (int r = 1; r <= N; ++r)
    {
        for (int c = 1; c <= N; ++c)
        {
            cout << Graph[r][c] << " ";
        }
        cout << endl;
    }
    for (int i = 1; i <= N; ++i)
    {
	    for (int j = 1; j <= N; ++j)
	    {
            auto iter = vecPath[i][j].begin();
            auto iterEnd = vecPath[i][j].end();

            if (Graph[i][j] == INF || Graph[i][j] == 0)
            {
                cout << 0 << endl;
            }
            else
            {
                cout << vecPath[i][j].size() + 2 << " ";
                cout << i << " ";
                for (; iter != iterEnd; ++iter)
                    cout << (*iter) << " ";
                cout << j;
                cout << endl;
            }
	    }
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input_c.txt", "r", stdin);

    Input();

    Solve();
    
    return 0;
}