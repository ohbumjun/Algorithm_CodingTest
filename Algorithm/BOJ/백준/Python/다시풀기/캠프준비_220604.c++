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

int N, L, R, X;
std::vector<int> vecProblems;

void Input()
{
    cin >> N >> L >> R >> X;
    vecProblems.reserve(N);

    for (int i = 0; i < N; ++i)
    {
        int Input;
        cin >> Input;
        vecProblems.push_back(Input);
    }
}


void Solve()
{
    int answer = 0;

	for (int bit = 0; bit < (1 << N); ++bit)
	{
        int maxP = -1, minP = INF, sumP = 0;

        for (int i = 0; i < N; ++i)
        {
	        if ((1 << i) & bit)
	        {
                sumP += vecProblems[i];
                if (maxP < vecProblems[i])
                    maxP = vecProblems[i];
                if (minP > vecProblems[i])
                    minP = vecProblems[i];
	        }
        }

        int dif = maxP - minP;

        if (dif < X)
            continue;

        if (sumP < L || sumP > R)
            continue;

        answer += 1;
	}

    cout << answer << endl;
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