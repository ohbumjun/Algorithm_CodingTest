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
vector<int> vecDist;
vector<bool> vecSnake;
vector<bool> vecLadder;
unordered_map<int, int> mapSnake;
unordered_map<int, int> mapLadder;


void Input()
{
    cin >> N >> M;

    vecSnake = vector<bool>(101, false);
    vecLadder = vector<bool>(101, false);
    vecDist = vector<int>(101, INF);

    int st, ed;
	for (int i = 0; i < N; ++i)
	{
        cin >> st >> ed;
        vecLadder[st] = true;
        mapLadder[st] = ed;
	}

    for (int i = 0; i < M; ++i)
    {
        cin >> st >> ed;
        vecSnake[st] = true;
        mapSnake[st] = ed;
    }
}


void Solve()
{
    queue<int> Queue;
    vecDist[1] = 0;
    Queue.push(1);

    while (!Queue.empty())
    {
        int cur = Queue.front();
        Queue.pop();

        for (int i = 1; i <= 6; ++i)
        {
            int nxt = cur + i;

            if (nxt > 100)
                break;

            // 사다리
            if (vecSnake[nxt])
                nxt = mapSnake[nxt];

            // 뱀
            else if (vecLadder[nxt])
                nxt = mapLadder[nxt];

            if (vecDist[nxt] != INF)
                continue;;

            if (vecDist[nxt] > vecDist[cur] + 1)
            {
                vecDist[nxt] = vecDist[cur] + 1;
                Queue.push(nxt);
            }
        }
    }

    cout << vecDist[100] << endl;
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