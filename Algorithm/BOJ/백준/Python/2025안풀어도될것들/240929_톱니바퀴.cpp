// https://www.acmicpc.net/problem/14891


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

// vector<int> : topni
// 0 ~ 8 : 시계방향값
// 2 ~ 6 (맞닿은 위치들)
vector<vector<char>> topnis;
int K;

void rotateTopni(vector<char>& origin, int dir)
{
	vector<char> newTopni = origin;

	// 시계 방향
	if (dir == 1)
	{
		int cache = origin[7];
		// 오른쪽으로 한칸씩 이동시키기
		for (int i = 7; i >= 1; --i)
		{
			int prevI = i - 1;
			newTopni[i] = origin[prevI];
		}
		newTopni[0] = cache;
	}
	else
	{
		// 왼쪽으로 한칸씩 이동시키기
		int cache = origin[0];
		for (int i = 0; i < 7; ++i)
		{
			int nextI = i + 1;
			newTopni[i] = origin[nextI];
		}
		newTopni[7] = cache;
	}
	origin = newTopni;
}

void Input()
{
	topnis.resize(4);

	for (int i = 0; i < 4; ++i)
	{
		string input;
		cin >> input;
		for (int k = 0; k < 8; ++k)
		{
			topnis[i].push_back(input[k] == '1' ? 'S' : 'N');
		}
	}

	cin >> K;
}

void Solve()
{
	int ans = 0;

	for (int k = 0; k < K; ++k)
	{
		vector<vector<char>> originNis = topnis;

		// 1 : 시계 , -1 : 반시계
		int idx, dir;
		cin >> idx >> dir;
		idx -= 1;

		// 왼쪽으로 가며 검사
		int curIdx = idx;
		int leftDir = -1 * dir;
		int leftIdx = idx - 1;
		
		while (leftIdx >= 0)
		{
			// curIdx 6, leftIdx 2 비교
			char curLeft		= originNis[curIdx][6];
			char leftRight	= originNis[leftIdx][2];

			if (curLeft == leftRight)
				break;

			// left 회전
			rotateTopni(topnis[leftIdx], leftDir);

			curIdx = leftIdx;
			leftIdx -= 1;
			leftDir = leftDir * -1;
		}

		// 오른쪽으로 가며 검사
		int rightIdx = idx + 1;
		int rightDir = dir * -1;
		curIdx = idx;

		while (rightIdx < 4)
		{
			// curIdx 2, rightIdx 6 비교
			char curRight = originNis[curIdx][2];
			char rightLeft = originNis[rightIdx][6];

			if (curRight == rightLeft)
				break;

			// right 회전
			rotateTopni(topnis[rightIdx], rightDir);

			curIdx = rightIdx;
			rightIdx += 1;
			rightDir = rightDir * -1;
		}

		// 마지막에 현재 톱니바퀴 회전
		rotateTopni(topnis[idx], dir);
	}

	for (int i = 0; i < 4; ++i)
	{
		if (i == 0 && topnis[i][0] == 'S')
			ans += 1;
		if (i == 1 && topnis[i][0] == 'S')
			ans += 2;
		if (i == 2 && topnis[i][0] == 'S')
			ans += 4;
		if (i == 3 && topnis[i][0] == 'S')
			ans += 8;
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


