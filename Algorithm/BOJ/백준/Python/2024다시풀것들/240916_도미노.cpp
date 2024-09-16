// https://www.acmicpc.net/problem/1552

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <thread>
#include <vector>
#include <string>
#include <cstring>
#include <set>
#include <queue>
#include <math.h>
#include <stack>
#include <algorithm>
#include <unordered_map>

#define endl "\n"
#define INT_MAX int(1e9)
#define MAX 10001

using namespace std;

int N;
int maxNum = 0, minNum = INT_MAX;
vector<vector<int>> nums;
vector<bool> rowCheck;
vector<bool> colCheck;

int getCycleCount(vector<pair<int, int>>& dominos);

// 인자로 들어온 최초 domino 를 이용하여, 모든 경로 경우의 수를 구한다.
// 그리고 각각에 대해서 cycle cnt 를 구해보고, 최대 cnt 를 리턴하면 된다.
void caculateCycle(int& maxVal, int cIdx, vector<bool>& visit, const vector<pair<int, int>>& dominos, vector<pair<int, int>>& temp)
{
	visit[cIdx] = true;
	
	if (temp.size() == N)
	{
		int cycleSize = getCycleCount(temp);
		if (cycleSize > maxVal)
			maxVal = cycleSize;
		return;
	}

	for (int i = 0; i < N; i++)
	{
		if (visit[i])
			continue;
		temp.push_back(dominos[i]);
		caculateCycle(maxVal, i, visit, dominos, temp);
		temp.pop_back();
		visit[i] = false;
	}
}

// 하나의 경로에 1) 사이클 o 경로 2) 사이클 x 경로. 가 존재할 수 있다.
int getCycleCount(vector<pair<int, int>>& dominos)
{
	vector<pair<int, int>> cycleGroup;
	cycleGroup.reserve(dominos.size());

	int dominosSize = dominos.size();
	int cycleCount = 0;
	int prevR = dominos[0].first;
	int prevC = dominos[0].second;

	cycleGroup.push_back({ prevR, prevC });

	for (int i = 1; i < dominosSize; i++)
	{
		int r = dominos[i].first;
		int c = dominos[i].second;

		if (r != prevC)
		{
			if (cycleGroup.size() > 1)
			{
				// 맨 처음 first, 맨 마지막 second 비교
				if (cycleGroup[0].first == cycleGroup[cycleGroup.size() - 1].second)
					cycleCount += 1;
			}
			else
			{
				if (cycleGroup[0].first == cycleGroup[0].second)
					cycleCount += 1;
			}

			cycleGroup.clear();
			cycleGroup.push_back({ r, c });
		}
		else
			cycleGroup.push_back({ r, c });

		prevR = r;
		prevC = c;
	}

	if (cycleGroup.size() > 1)
	{
		// 맨 처음 first, 맨 마지막 second 비교
		if (cycleGroup[0].first == cycleGroup[cycleGroup.size() - 1].second)
			cycleCount += 1;
	}
	else
	{
		if (cycleGroup[0].first == cycleGroup[0].second)
			cycleCount += 1;
	}

	return cycleCount;
}

void dfs(int stR, int curR, int curC, vector<pair<int, int>>& dominos)
{
	int dominosSize = dominos.size();

	if (dominosSize == N)
	{
		int n = 1;
		// cout << "--- dominos --- " << endl;
		for (int i = 0; i < dominosSize; i++)
		{
			int r = dominos[i].first;
			int c = dominos[i].second;
			// cout << "r,c,num : " << r << " " << c << " " << nums[r][c] << endl;
			n *= nums[r][c];
		}

		int cycleGroupCnt = 0;
		for (int i = 0; i < N; ++i)
		{
			vector<bool> visit(N, false);
			vector<pair<int, int>> temp;
			temp.push_back(dominos[i]);
			caculateCycle(cycleGroupCnt, 0, visit, dominos, temp);
		}

		// cout << "cycleCount :  " << cycleGroupCnt << endl;

		if (cycleGroupCnt > 1 && cycleGroupCnt % 2 == 0)
			n *= -1;

		if (n < minNum)
			minNum = n;
		if (n > maxNum)
			maxNum = n;

		return;
	}

	for (int r = 0; r < N; ++r)
	{
		if (rowCheck[r]) continue;
		rowCheck[r] = true;
		for (int c = 0; c < N; ++c)
		{
			if (colCheck[c])
				continue;
			colCheck[c] = true;
			dominos.push_back({ r, c });
			dfs(stR, r, c, dominos);
			dominos.pop_back();
			colCheck[c] = false;
		}
		rowCheck[r] = false;
	}
}

void Input()
{
	cin >> N;
	nums.resize(N, vector<int>(N));

	rowCheck.resize(N, false);
	colCheck.resize(N, false);

	for (int r = 0; r < N; ++r)
	{
		string n;
		int c = 0;
		cin >> n;
		for (int c = 0; c < N; ++c)
		{
			bool isAlpha = false;
			auto ch = n[c];
			if (ch >= 'A' && ch <= 'I')
			{
				isAlpha = true;
			}

			if (isAlpha == false)
				nums[r][c] = n[c] - '0';
			else
				nums[r][c] = -1 - (ch - 'A');
		}
	}
};

void resetCheck()
{
	for (int i = 0; i < N; ++i)
		rowCheck[i] = false;

	for (int i = 0; i < N; ++i)
		colCheck[i] = false;
}

void Solve()
{
	// 같은 행, 같은 열 X
	// 1,1 도 하나의 사이클
	// 모든 사이클 모두 구하기 -> 사이클 이루면 지금까지의 숫자 뒷편 값 모두 구하기
	// 단, 짝수라면 결과값 - 1

	for (int r = 0; r < N; ++r)
	{
		for (int c = 0; c < N; ++c)
		{
			resetCheck();
			vector<pair<int, int>> dominos;
			dominos.push_back({ r, c });
			rowCheck[r] = true;
			colCheck[c] = true;
			dfs(r, r, c, dominos);

			rowCheck[r] = false;
			colCheck[c] = false;
		}
	}

	cout << minNum << endl;
	cout << maxNum << endl;
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
