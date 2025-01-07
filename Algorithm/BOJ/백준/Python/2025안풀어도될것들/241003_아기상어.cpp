// https://www.acmicpc.net/problem/16236

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
int stRow, stCol;
vector<vector<int>> Board;
int dRow[4] = { -1, 0, 0, 1 }; // 북,좌,우,남
int dCol[4] = { 0, -1, 1, 0 };

struct Fish
{
	int row;
	int col;
	int mov;
};

void Input()
{
	cin >> N;
	Board.resize(N, vector<int>(N, 0));

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> Board[i][j];
			if (Board[i][j] == 9)
			{
				stRow = i;
				stCol = j;
			}
		}
	}
}

void bfs(int curRow, int curCol, int sharkSize, 
	vector<vector<bool>>& check, vector< Fish>& fishes)
{
	queue <tuple<int, int, int>> q;
	check[curRow][curCol] = true;
	q.push(make_tuple(curRow, curCol, 0));

	while (!q.empty())
	{
		int row = std::get<0>(q.front());
		int col = std::get<1>(q.front());
		int dist = std::get<2>(q.front());
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nextRow = row + dRow[i];
			int nextCol = col + dCol[i];
			if (nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= N)
				continue;
			if (check[nextRow][nextCol])
				continue;
			if (Board[nextRow][nextCol] > sharkSize)
				continue;
			check[nextRow][nextCol] = true;
			q.push(make_tuple(nextRow, nextCol, dist + 1));

			if (Board[nextRow][nextCol] < sharkSize &&
				Board[nextRow][nextCol] != 0)
			{
				Fish fish;
				fish.row = nextRow;
				fish.col = nextCol;
				fish.mov = dist + 1;
				fishes.push_back(fish);
			}
		}
	}
}

void Solve()
{
	// 자기보다 큰 물고기가 있는 공간 외에 모두 지나갈 수 있다.
	// 만약 크기 같으면 지나가기만 할 수 있다.
	// 크기가 더 작으면, 먹고 지나갈 수 있다.

	// 이동 결정 방법.
	// 먹을 수 있는 물고기 없다면, 도움 요청
	// 먹을 수 있는 물고기 1마리 -> 먹으러 간다.
	// 2마리 이상 -> 가장 가까운 물고기 먹으러 간다. ?
	// (즉, 상하 좌우 1칸이 아니라, 쭉 ~~ 조사한다)
	// 거리 가까운 물고기 많다면, 가장 위에 있는 물고기. 그 중에서 가자 왼쪽.
	// (즉, 북. 그 다음 왼쪽)
	// 1칸에 물고기 1마리.
	// 자기 크기만큼 물고기 먹어야 크기 + 1
	int time = 0;
	int curRow = stRow, curCol = stCol;
	Board[curRow][curCol] = 0;
	int eatFishCnt = 0;
	int curSharkSize = 2;
	while (true)
	{
		// 현재 위치에서 bfs 로 먹을 수 있는 모든 물고기 찾기
		// 크기, 위치, 이동 거리를 리턴해야 한다.
		// vector 로 모아두고, row 와 col 단위로 정렬
		vector<Fish> fishes;
		vector<vector<bool>> check(N, vector<bool>(N, false));
		bfs(curRow, curCol, curSharkSize, check, fishes);
		if (fishes.empty())
			break;
		std::sort(fishes.begin(), fishes.end(), [](Fish& a, Fish& b) {
			if (a.mov == b.mov)
			{
				if (a.row == b.row)
					return a.col < b.col;
				return a.row < b.row;
			}
			return a.mov < b.mov;
		});
		int fishRow = fishes[0].row;
		int fishCol = fishes[0].col;
		int fishMov = fishes[0].mov;
		Board[fishRow][fishCol] = 0;
		eatFishCnt++;
		if (eatFishCnt == curSharkSize)
		{
			curSharkSize++;
			eatFishCnt = 0;
		}
		time += fishMov;
		curRow = fishRow;
		curCol = fishCol;

		// for (int i = 0; i < N; i++)
		// {
		// 	for (int j = 0; j < N; j++)
		// 	{
		// 		cout << Board[i][j] << " ";
		// 	}
		// 	cout << endl;
		// }
		// cout << "------" << endl;
	}

	cout << time << endl;
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


