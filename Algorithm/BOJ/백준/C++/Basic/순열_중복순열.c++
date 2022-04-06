// 입력값 4 2

// 1) 중복 순열 : 중복을 허락하여 순열 구성하기
#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <stack>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 100000 + 1
#define INF int(1e9)

using namespace std;

std::vector<int> Balls;

int N, M;

void DFS(int Index)
{
	if (Index == M)
	{
        for (const auto& ball : Balls)
            cout << ball << " ";
        cout << endl;
        return;
	}

    for (int i = 1; i <= N; i++)
    {
        Balls[Index] = i;
        DFS(Index + 1);
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

	cin >> N >> M;
    
    Balls.resize(M);

    DFS(0);

	
    return 0;
}


// 2) 순열
#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <array>
#include <stack>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 100000 + 1
#define INF int(1e9)

using namespace std;

std::vector<int> Balls;

int N, M;

void DFS(int Index)
{
	if (Index == M)
	{
        for (const auto& ball : Balls)
            cout << ball << " ";
        cout << endl;
        return;
	}

    for (int i = Index + 1; i <= N; i++)
    {
        Balls[Index] = i;
        DFS(Index + 1);
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

	cin >> N >> M;
    
    Balls.resize(M);

    DFS(0);

	
    return 0;
}


