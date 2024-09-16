

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
#define MAX 100000+1
#define INF int(1e9)

using namespace std;

int N;
vector<vector<int>> domNums;
vector<vector<int>> checks;
vector <vector<pair<int, int>>> cycles;

void getCycle(int initRow, int pRow, int pCol, vector<pair<int, int>>& pairs)
{
	// 이전 pCol, pRow 에서는 선택 X
	// 그 다음 row 가 pCol 과 같은 녀석을 선택해서 pairs 에 넣기
	// check 
	// 그 다음 check 해제
	// pairs 에서 빼주고
	
	// 한편 현재 pCol 이 맨 처음과 동일하다면, 이제 cycles 목록에 추가
}

void Input()
{
	cin >> N;

	checks.resize(N + 1, vector<int>(N + 1));
	domNums.resize(N + 1, vector<int>(N + 1));

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> domNums[i+1][j+1];
}

void Solve()
{
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input_c.txt", "r", stdin);

	Input();
	Solve();

	return 0;
}
