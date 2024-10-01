// https://www.acmicpc.net/problem/16235

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

int dRow[4] = { 0, 0, 1, -1 };
int dCol[4] = { 1, -1, 0, 0 };
int N, L, R;
int ppl[51][51];
vector<vector<bool>> check(51, vector<bool>(51, false));
int ans = 0;

bool bfs(int stRow, int stCol)
{
	vector<pair<int, int>> openCountry;
	queue<pair<int, int>> q;
	q.push({ stRow, stCol });

	check[stRow][stCol] = true;

	while (!q.empty())
	{
		int curRow = q.front().first;
		int curCol = q.front().second;
		openCountry.push_back({ curRow, curCol });
		q.pop();

		for (int d = 0; d < 4; ++d)
		{
			int nextRow = curRow + dRow[d];
			int nextCol = curCol + dCol[d];
			if (nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= N)
				continue;
			if (check[nextRow][nextCol])
				continue;
			int diff = abs(ppl[curRow][curCol] - ppl[nextRow][nextCol]);
			if (diff >= L && diff <= R)
			{
				check[nextRow][nextCol] = true;
				q.push({ nextRow, nextCol });
			}
		}
	}

	if (openCountry.size() == 1)
		return false;

	int sum = 0;

	for (int i = 0; i < openCountry.size(); ++i)
		sum += ppl[openCountry[i].first][openCountry[i].second];

	int avg = sum / openCountry.size();

	for (int i = 0; i < openCountry.size(); ++i)
		ppl[openCountry[i].first][openCountry[i].second] = avg;

	return true;
}

void Input()
{
	// N*N 개의 땅. 각 땅에 사람들이 살고 있음
	// 인접 나라끼리 인구차이 L명 이상, R 명 이하 -> 모든 국경을 연다.
	// 인구 이동 시작
	// 인접칸만 이동. 국경 열려서 인접한 국가는 연합

	// 매번 BFS 로 각 칸을 기준으로 연합 국가를 계속해서 찾아가야 할 것 같다.
	cin >> N >> L >> R;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> ppl[i][j];

}

void Solve()
{
	
	while (true)
	{
		// reset check
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				check[i][j] = false;

		bool isOpen = false;

		// 각 칸을 기준으로 bfs 진행해보기
		for (int r = 0; r < N; ++r)
		{
			for (int c = 0; c < N; ++c)
			{
				if (check[r][c])
					continue;
				if (bfs(r, c))
					isOpen = true;
			}
		}

		if (!isOpen)
			break;

		ans += 1;
	}

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


