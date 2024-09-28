// https://www.acmicpc.net/problem/14890

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

int N, L;
vector<vector<int>> Map;

void Input()
{
	cin >> N >> L;
	Map.resize(N, vector<int>(N, 0));

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < N; ++c)
			cin >> Map[r][c];
}

void Solve()
{
	int ans = 0;
	// 행 단위 검사
	for (int r = 0; r < N; ++r)
	{
		// 행을 아예 복사
		// v 자던, max - min 이 2개 차이전 상관없음.
		// check 도 필요없음.
		// for 문이 아니라 while 문 사용해야 한다.
		int c = 0;
		int checkC = -2;
		bool enable = true;
		vector<int> curRow = Map[r];
		while (c + 1 < N)
		{
			int cH = curRow[c];
			int nH = curRow[c + 1];
			if (abs(cH - nH) >= 2)
			{
				enable = false;
				break;
			}
			if (cH == nH)
			{
				c += 1;
				continue;
			}
			if (cH > nH)
			{
				// c + (L-1) 범위까지 조사
				for (int l = 0; l < L; ++l)
				{
					if (c + 1 + l >= N || curRow[c+1+l] != nH)
					{
						enable = false;
						break;
					}
				}
				if (enable == false)
					break;
				int oldC = c;
				c = c + L;
				checkC = oldC + L; // 해당 지점까지는 검사 끝
			}
			else if (cH < nH)
			{
				int cH = curRow[c];
				int nH = curRow[c + 1];
				if (abs(cH - nH) >= 2)
				{
					enable = false;
					break;
				}
				for (int l = 0; l < L; ++l)
				{
					if (c - l < 0 || c - l <= checkC || curRow[c - l] != cH)
					{
						enable = false;
						break;
					}
				}
				if (enable == false)
					break;
				checkC = c;
				c += 1;
			}
		}

		if (!enable)
			continue;
		ans += 1;
	}

	// 열 단위 검사
	for (int c = 0; c < N; ++c)
	{
		// 행을 아예 복사
		// v 자던, max - min 이 2개 차이전 상관없음.
		// check 도 필요없음.
		// for 문이 아니라 while 문 사용해야 한다.
		int r = 0;
		int checkR = -2;
		bool enable = true;
		vector<int> curCol(N ,0);
		for (int r = 0; r < N; ++r)
			curCol[r] = Map[r][c];
		while (r + 1 < N)
		{
			int cH = curCol[r];
			int nH = curCol[r + 1];
			if (abs(cH - nH) >= 2)
			{
				enable = false;
				break;
			}
			if (cH == nH)
			{
				r += 1;
				continue;
			}
			if (cH > nH)
			{
				// c + (L-1) 범위까지 조사
				for (int l = 0; l < L; ++l)
				{
					if (r + l + 1 >= N || curCol[r + l + 1] != nH)
					{
						enable = false;
						break;
					}
				}
				if (enable == false)
					break;
				int oldR = r;
				r = r + L;
				checkR = oldR + L; // 해당 지점까지는 검사 끝
			}
			else if (cH < nH)
			{
				int cH = curCol[r];
				int nH = curCol[r + 1];
				if (abs(cH - nH) >= 2)
				{
					enable = false;
					break;
				}
				for (int l = 0; l < L; ++l)
				{
					if (r - l < 0 || r - l <= checkR || curCol[r - l] != cH)
					{
						enable = false;
						break;
					}
				}
				if (enable == false)
					break;
				checkR = r;
				r += 1;
			}
		}
		if (!enable)
			continue;
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


