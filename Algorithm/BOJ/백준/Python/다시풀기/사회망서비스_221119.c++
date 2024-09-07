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
#include <cstring>

#define endl "\n"
#define MAX 1000000+1
#define INF int(1e9)

using namespace std;

int N;

int parent;
vector<int> Graph[MAX];
int Memo[MAX][2]; // 얼리 어댑터인지 아닌지
bool Visit[MAX];
vector<int> Tree[MAX];

void Input()
{
    // 1. 그래프 만들어주기
    cin >> N;

    int u, v;

    for (int i = 0; i < N - 1; ++i)
    {
        cin >> u >> v;
        Graph[u].push_back(v);
        Graph[v].push_back(u);
    }

    memset(Visit, false, sizeof(Visit));
    memset(Memo, -1, sizeof(Memo));

    // F[A][B] = C
    // B 에는 0 혹은 1 만 들어간다
    // 1) F[A][0] = C -> 현재 A 번 정점이고, A번 정점이 얼리어답터가 아닐 때, 최소 얼리어답터의 수는
    //      C개이다.
	// 2) F[A][1] = C -> 현재 A 번 정점이고, A번 정점이 얼리어답터일 때, 최소 얼리어답터의 수는
    //      C개이다. (이 C개 에는 자기 자신도 포함된다..)

    // 처음 호출은 2개 함수를 호출한다.
    // DFS(1,0), DFS(1, 1)
    // 1번 노드가 얼리어댑터인지, 아닌지 2가지가 다른 결과를 낼 수 있기 때문에
    // 2가지를 모두 조사해야 한다.

    // 1) 현재 정점이 얼리어댑터라면,
    // - 현재 정점과 연결되어 있는 정점들은 얼리어댑터 일 수도 있고, 아닐 수도 있고
    // - 따라서 2가지 경우 모두 탐색해야 한다.
    // - 그 중 최소값으로 설정 하기

    // 2) 현재 정점이 얼리어댑터가 아니라면, 현재 정점과 연결되어 있는 모든 정점들은
    // - 얼리어댑터여야 한다.
}

void Make_Tree(int Cur)
{
    Visit[Cur] = true;

    for (int i = 0; i < Graph[Cur].size(); ++i)
    {
        int Next = Graph[Cur][i];

        if (Visit[Next] == false)
        {
            Tree[Cur].push_back(Next);
            Make_Tree(Next);
        }
    }
}

int DFS (int Cur, int State)
{
    if (Memo[Cur][State] != -1)
        return Memo[Cur][State];

    // 현재 Cur 가 얼리어댑터 -> 자식 노드들이 얼리어댑터 일수도, 아닐 수도
    if (State == 1)
    {
        // 자기 자신
        Memo[Cur][State] = 1;

        for (int i = 0; i < Tree[Cur].size(); ++i)
        {
            int Next = Tree[Cur][i];
            Memo[Cur][State] += min(DFS(Next, 0), DFS(Next, 1));
        }
    }
    else
    {
        Memo[Cur][State] = 0;

        for (int i = 0; i < Tree[Cur].size(); ++i)
        {
            int Next = Tree[Cur][i];

            Memo[Cur][State] += DFS(Next, 1);
        }
    }

    return Memo[Cur][State];
}

void Solve()
{
    Make_Tree(1);

    cout << min(DFS(1, 1), DFS(1, 0)) << endl;
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