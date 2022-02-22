// 입력 값 4 2

// 1) 중복 조합 
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

void DFS(int Index, int PrevNum)
{
	if (Index == M)
	{
        for (const auto& ball : Balls)
            cout << ball << " ";
        cout << endl;
        return;
	}

    for (int i = PrevNum; i <= N; i++)
    {
        Balls[Index] = i;
        DFS(Index + 1, i);
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

    DFS(0, 1);

	
    return 0;
}




// 2) 조합
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

void DFS(int Index, int PrevNum)
{
	if (Index == M)
	{
        for (const auto& ball : Balls)
            cout << ball << " ";
        cout << endl;
        return;
	}

    for (int i = PrevNum + 1; i <= N; i++)
    {
        Balls[Index] = i;
        DFS(Index + 1, i);
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

    DFS(0, 0);

	
    return 0;
}


