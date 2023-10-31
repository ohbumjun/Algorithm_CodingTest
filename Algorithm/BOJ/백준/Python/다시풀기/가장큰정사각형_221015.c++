// https://www.acmicpc.net/problem/1915

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

int dRow[] = {-1, 1, 0,0};
int dCol[] =  {0, 0, -1,1};

int N, M;

vector<vector<int>> vecInput;
vector<vector<int>> vecDP;

void Input()
{
	cin >> N >> M; // N이 행, M이 열

	vecInput.resize(N);
	vecDP.resize(N);

	for (int i = 0; i < N; ++i)
	{
		vecInput[i].resize(M);
		vecDP[i].resize(M);
	}

	for (int r = 0; r < N; ++r)
	{
		string Input;
		cin >> Input;
		
		for (int c = 0; c < Input.length(); ++c)
		{
			vecInput[r][c] = Input[c] - '0';
		}
	}

	//for (int r = 0; r < N; ++r)
	//{
	//	for (int c = 0; c < M; ++c)
	//	{
	//		cout << vecInput[r][c] << ".";
	//	}
	//	cout << endl;
	//}
}

void Solve()
{
	int Answer = 0;

	for (int r = 0; r < N; ++r)
	{
		for (int c = 0; c < M; ++c)
		{
			// 0 이면 Skip
			if (vecInput[r][c] == 0)
				continue;

			// 맨 위 , 혹은 맨 왼쪽
			if (r < 1 || c < 1)
				vecDP[r][c] = 1;

			// 대각선 위가 0 일 때 
			else  if (vecInput[r-1][c-1] == 0)
				vecDP[r][c] = 1;

			else
			{
				// 이때는 위, 왼쪽으로 모두 1인지 검사
				// 1) 대각선 위의 vecDP 값 + 1 인지 여부를 파악하기 
				// 2) 그렇지 않다면 
				// 만약 맞다면 vecDP[r - 1][c - 1] + 1로 세팅
				// 그렇지 않다면 1로 세팅

				vecDP[r][c] = 1;

				int prevVal = vecDP[r - 1][c - 1];

				bool IsAllOne = true;

				int noOneR = r - prevVal;
				int noOneC = c - prevVal;

				// for (int rIdx = r - prevVal; rIdx < r; rIdx++)
				for (int rIdx = r; rIdx >= r - prevVal; rIdx--)
				{
					if (vecInput[rIdx][c] != 1)
					{
						noOneR = rIdx;
						IsAllOne = false;
						break;
					}
				}

				// for (int cIdx = c - prevVal; cIdx < c; cIdx++)
				for (int cIdx = c; cIdx >= c - prevVal; cIdx--)
				{
					if (vecInput[r][cIdx] != 1)
					{
						noOneC = cIdx;
						IsAllOne = false;
						break;
					}
				}

				if (IsAllOne)
					vecDP[r][c] = prevVal + 1;
				else
				{
					int minV = min(c - noOneC, r - noOneR);
					vecDP[r][c] = minV;
				}
			}

			if (Answer < vecDP[r][c] * vecDP[r][c])
				Answer = vecDP[r][c] * vecDP[r][c];
		}
	}

	/*
	<에지 케이스>
	4 4
	1100
	1111
	0111
	0111
	*/

	cout << Answer << endl;
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
