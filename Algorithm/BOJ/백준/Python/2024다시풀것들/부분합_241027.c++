// https://www.acmicpc.net/problem/1806

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <functional>
#include <algorithm>
#include <unordered_map>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N, S;
vector<int> vecNums;
int Answer = INF;

void Input()
{
    cin >> N >> S;
    vecNums.reserve(N);

    int Input;

    for (int i = 0; i < N; ++i)
    {
        cin >> Input;
        vecNums.push_back(Input);
    }
}

void Solve()
{
    int interval_sum = 0;
    int edP = 0;

    for (int stP = 0; stP < N; ++stP)
    {
	    while (interval_sum < S && edP < N)
	    {
            interval_sum += vecNums[edP];
            edP += 1;
	    }

        if (interval_sum >= S)
        {
            // cout << "stP : " << stP << endl;
            // cout << "edP : " << edP << endl;
            // cout << "interval_sum : " << interval_sum << endl;
            // cout << endl;
            if (edP - stP < Answer)
            {
                Answer = edP - stP;
            }
        }

        interval_sum -= vecNums[stP];
    }
}


int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_c.txt", "r", stdin);

    Input();

    Solve();

    if (Answer == INF)
        cout << 0;
    else
        cout << Answer;

    return 0;
}