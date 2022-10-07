// https://www.acmicpc.net/problem/20040

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
#include <string>

#define endl "\n"
#define MAX 500 + 1
#define INF int(1e9)

using namespace std;

int N, M;
vector<int> vecParent;

int find_parent(vector<int>& vecParent, int child) //
{
    if (vecParent[child] != child)
        return find_parent(vecParent, vecParent[child]);

    return vecParent[child];
}

void union_parent(vector<int>& vecParent, int a, int b)
{
    int pA = find_parent(vecParent, a);
    int pB = find_parent(vecParent, b);

    if (pA < pB)
        vecParent[pB] = pA;
    else
        vecParent[pA] = pB;
}

void Input()
{
    cin >> N >> M;
}

void Solve()
{
    vecParent.resize(N + 1);

    for (int i = 1; i <= N; ++i)
        vecParent[i] = i;

    int P1, P2;

    for (int i = 0; i < M; ++i)
    {
        cin >> P1 >> P2;

        int pP1 = find_parent(vecParent, P1);
        int pP2 = find_parent(vecParent, P2);

        if (pP1 == pP2)
        {
            cout << i + 1 << endl;
            exit(0);
        }
        else
        {
            union_parent(vecParent, P1, P2);
        }
    }

    cout << 0;
}

// 2.28, 4.25
// 4 12, 6 5
// 6 3, 6 15
// 6 15, 9 27
// 9 14, 12 24

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();
    Solve();

    return 0;
}