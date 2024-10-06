// https://www.acmicpc.net/problem/17779

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

int N;
vector<vector<int>> Map;

void Input()
{
	cin >> N;
	Map.resize(N, vector<int>(N, 0));

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < N; ++c)
			cin >> Map[r][c];
}

void Solve()
{
	// 5개 선거구로 만들기
	// 1개 선거구는 적어도 1개의 구역 포함
	// 1 선거구 내 구역은 모두 연결(인접)

	// d1, d2 는 1 이상
	// 최소 범위 : r 은 1 이상, y 도 1 이상, N - 2 이하

	// r,c 하나하나에 대해서 계산
	// 이때 d1, d2 도 모든 케이스 계산
	// 당연히 경계 범위 고려해서
	// 그 안에서 범위 모두 나누고
	// 인구 차이 계산
	// 최소값 구하기
	// x : 행, y : 열
	int ans = INT_MAX;
	for (int x = 1; x < N - 1; ++x)
	{
		for (int y = 1; y < N - 1; ++y)
		{
			for (int d1 = 1; d1 < N; ++d1)
			{
				for (int d2 = 1; d2 < N; ++d2)
				{
					vector<vector<int>> debug;
					vector<int> areas(5,0);
					debug.resize(N, vector<int>(N, 0));
					if (x + d1 + d2 >= N)
						continue;
					if (y - d1 <= 0)
						continue;
					if (y + d2 >= N)
						continue;

					// 일단 5번 말고 기본 범위로 모두 세팅하기
					for (int cR = 0; cR < N; ++cR)
					{
						for (int cC = 0; cC < N; ++cC)
						{
							if (cR < x + d1 && cC <= y)
								debug[cR][cC] = 1;
							else if (cR <= x + d2 && cC > y)
								debug[cR][cC] = 2;
							else if (cR >= x + d1 && cC < y - d1 + d2)
								debug[cR][cC] = 3;
							else if (cR > x + d2 && cC >= y - d1 + d2)
								debug[cR][cC] = 4;
						}
					}

					// std::cout << "---------bef----------" << endl;
					// for (int a = 0; a < N; ++a)
					// {
					// 	for (int b = 0; b < N; ++b)
					// 		std::cout << debug[a][b] << ".";
					// 	std::cout << endl;
					// }

					// 경계선 표기하고
					// 이후 5 ~ 5 사이의 값들도 모두 0 으로 변경해서 표기하기
					for (int t = 0; t <= d1; ++t)
					{
						// 1
						debug[x+t][y - t] = 5; // 5
						// 4
						debug[x + d2 + t][y + d2 - t] = 5; // 5
					}

					for (int t = 0; t <= d2; ++t)
					{
						// 2
						debug[x + t][y + t] = 5; // 5
						// 3
						debug[x + d1 + t][y - d1 + t] = 5; // 5
					}

					for (int cR = 0; cR < N; ++cR)
					{
						for (int cC = 0; cC < N; ++cC)
						{
							if (debug[cR][cC] != 5)
								continue;
							int nC = cC + 1;
							bool nxtFiveFound = false;
							while (nC < N)
							{
								if (debug[cR][nC] == 5)
								{
									nxtFiveFound = true;
									break;
								}
								nC += 1;
							}
							if (nxtFiveFound == false)
								continue;
							for (int tmpC = cC + 1; tmpC < nC; ++tmpC)
								debug[cR][tmpC] = 5;
							cC = nC + 1;
						}
					}

					// std::cout << "---------aft----------" << endl;
					// for (int a = 0; a < N; ++a)
					// {
					// 	for (int b = 0; b < N; ++b)
					// 		std::cout << debug[a][b] << ".";
					// 	std::cout << endl;
					// }

					for (int a = 0; a < N; ++a)
					{
						for (int b = 0; b < N; ++b)
						{
							if (debug[a][b] == 0)
								debug[a][b] = 5;
							areas[debug[a][b] - 1] += Map[a][b];
						}
					}

					int maxNum = 0;
					int minNum = INT_MAX;
					for (int i = 0; i < 5; ++i)
					{
						if (areas[i] > maxNum)
							maxNum = areas[i];
						if (areas[i] < minNum)
							minNum = areas[i];
					}

					if (maxNum - minNum == 19)
					{
						bool h = true;
					}
					ans = min(ans, maxNum - minNum);
				}
			}
		}
	}

	std::cout << ans << endl;
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


