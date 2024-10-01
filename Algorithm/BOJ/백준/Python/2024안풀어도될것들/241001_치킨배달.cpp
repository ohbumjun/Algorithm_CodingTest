// https://www.acmicpc.net/problem/15686

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <cstring>
#include <climits>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

// #define DEBUG 1

using namespace std;

int N, M; // 크기 N * N
vector<vector<int>> cities; 
// 0  : 빈캄
// 1  : 집
// 2  : 치킨
vector<pair<int, int>> chickens;
vector<pair<int, int>> houses;
int ans = INT_MAX;

// 도시 치킨 거리 구하는 함수
int getDist(const vector<vector<int>>& curCity, vector<bool>& selected)
{
	// 현대 도시에서 치킨집 목록 모아두기
	// houses 에서 각 치킨집을 돌며 최소 치킨집 거리 구하기
	// 이때 selected 가 true 라면 skip
	// 그 거리들의 합
	int cityDist = 0;

	for (int h = 0; h < houses.size(); ++h)
	{
		int chickenDist = INT_MAX;
		for (int c = 0; c < chickens.size(); ++c)
		{
			if (selected[c] == false)
				continue;
			int houseRow = houses[h].first;
			int houseCol = houses[h].second;

			int chickenRow = chickens[c].first;
			int chickenCol = chickens[c].second;

			int dist = abs(houseRow - chickenRow) + abs(houseCol - chickenCol);
			chickenDist = min(chickenDist, dist);
		}
		cityDist += (chickenDist == INT_MAX ? 0 : chickenDist);
	}

	return cityDist;
}

// M 개의 chicken 집 구하는 함수
void selectChicken(int curCnt, vector<bool>& selected, int prevIdx)
{
	if (curCnt == M)
	{
		// 도시 치킨 거리 구하기
		ans = min(ans, getDist(cities, selected));
		return;
	}

	for (int i = prevIdx + 1; i < chickens.size(); ++i)
	{
		if (selected[i] == true)
			continue;
		selected[i] = true;
		selectChicken(curCnt + 1, selected, i);
		selected[i] = false;
	}
}

void Input()
{
	cin >> N >> M;

	cities.resize(N + 1, vector<int>(N + 1, 0));

	for (int r = 0; r < N; ++r)
	{
		for (int c = 0; c < N; ++c)
		{
			cin >> cities[r][c];
			if (cities[r][c] == 2)
				chickens.push_back({ r, c });
			else if (cities[r][c] == 1)
				houses.push_back({ r, c });
		}
	}
}

void Solve()
{
	// 치킨 거리 : 집과 가까운 치킨집 사이의 거리
	// 각 집은 치킨 지님
	// 도시의 치킨 거리는 모든 집의 치킨 거리 합
	// M 개를 택하되, 가장 도시 치킨 거리가 작은 경우 구하기	
	vector<bool> selected(chickens.size(), false);
	selectChicken(0, selected, -1);

	cout << ans << endl;
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


