// https://www.acmicpc.net/problem/15683

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

int dRow[] = { -1, 0, 1, 0 }; // 북, 동, 남, 서
int dCol[] = { 0, 1, 0, -1 };
int N, M;
int ans = 0;
vector<vector<int>> room;

// cctvs[i] : i 번째 cctv
// cctvs[i][j] : i 번째 cctv 의 j 번째 방향들
// ccvs[i][j][k] : i 번째 cctv 의 j 번째 방향 종류에서 k 번째 방향
vector<vector<vector<int>>> cctvs;

struct Site
{
	int row, col, dir;
};

struct Cctv
{
	int row, col, idx;
};

void dfs(int cctvIdx, const vector<Cctv>& originCctvs,
	vector<pair<int,int>>& accCctvDirs) // cctv, cctv 방향 idx
{
	if (cctvIdx == originCctvs.size())
	{
		// 이제 여기서 사각지대를 조사하면 된다.
		int cnt = 0;
		vector<vector<int>> copyRoom = room;
		queue<Site> q;

		for (const pair<int, int>& cctvDirInfo : accCctvDirs)
		{
			int idxInfo		= cctvDirInfo.first;
			int cctvDirIdx = cctvDirInfo.second;
			const Cctv& cctv = originCctvs[idxInfo];
			int cctvIdx = cctv.idx;
			int row = cctv.row;
			int col = cctv.col;

			const vector<int>& cctvDirs = cctvs[cctvIdx][cctvDirIdx];

			for (int i = 0; i < cctvDirs.size(); ++i)
			{
				int curDir = cctvDirs[i];
				int nxtRow = row + dRow[curDir];
				int nxtCol = col + dCol[curDir];

				if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= M)
					continue;
				if (room[nxtRow][nxtCol] == 6)
					continue;
				q.push({ nxtRow, nxtCol, curDir });

				// 검사한 곳은 -1로 표시
				copyRoom[nxtRow][nxtCol] = -1;
			}
		}

		while (!q.empty())
		{
			Site cur = q.front();
			q.pop();

			int row = cur.row;
			int col = cur.col;
			int dir = cur.dir;

			int nxtRow = row + dRow[dir];
			int nxtCol	= col + dCol[dir];

			if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= M)
				continue;
			if (copyRoom[nxtRow][nxtCol] == 6)
				continue;
			copyRoom[nxtRow][nxtCol] = -1;
			q.push({ nxtRow, nxtCol, dir });
		}

		for (int r = 0; r < N; ++r)
			for (int c = 0; c < M; ++c)
				if (copyRoom[r][c] == 0)
					++cnt;

		ans = min(ans, cnt);

		return;
	}

	// 그게 아니라면 현재 cctv 4가지 방향을 모두 dfs 로 진행
	for (int i = 0; i < 4; ++i)
	{
		// 현재 cctv 의 방향을 설정
		accCctvDirs.push_back({ cctvIdx, i });

		// 현재 cctv 의 방향을 설정했으니, 다음 cctv 로 넘어간다.
		dfs(cctvIdx + 1, originCctvs, accCctvDirs);

		// 현재 cctv 의 방향을 다시 원래대로 돌려놓는다.
		accCctvDirs.pop_back();
	}
}

void Input()
{
	cin >> N >> M;

	room.resize(N, vector<int>(M, 0));

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < M; ++c)
			cin >> room[r][c];

	cctvs.resize(5);

	for (int i = 0; i < 5; ++i)
		cctvs[i].resize(4);

	{
		// 1번
		cctvs[0][0].push_back(0);
		cctvs[0][1].push_back(1);
		cctvs[0][2].push_back(2);
		cctvs[0][3].push_back(3);
	}

	{
		// 2번
		cctvs[1][0].push_back(1);
		cctvs[1][0].push_back(3);

		cctvs[1][1].push_back(0);
		cctvs[1][1].push_back(2);

		cctvs[1][2].push_back(1);
		cctvs[1][2].push_back(3);

		cctvs[1][3].push_back(0);
		cctvs[1][3].push_back(2);
	}

	// 3번
	{
		cctvs[2][0].push_back(0); // 북, 동
		cctvs[2][0].push_back(1);

		cctvs[2][1].push_back(1); // 동, 남
		cctvs[2][1].push_back(2);

		cctvs[2][2].push_back(2); // 남, 서
		cctvs[2][2].push_back(3);

		cctvs[2][3].push_back(3); // 서, 북
		cctvs[2][3].push_back(0);
	}

	// 4번
	{
		// 서, 북, 동
		cctvs[3][0].push_back(3);
		cctvs[3][0].push_back(0);
		cctvs[3][0].push_back(1);

		// 북, 동, 남
		cctvs[3][1].push_back(0);
		cctvs[3][1].push_back(1);
		cctvs[3][1].push_back(2);

		// 동, 남, 서
		cctvs[3][2].push_back(1);
		cctvs[3][2].push_back(2);
		cctvs[3][2].push_back(3);

		// 남, 서, 북
		cctvs[3][3].push_back(2);
		cctvs[3][3].push_back(3);
		cctvs[3][3].push_back(0);
	}

	// 5번
	{
		cctvs[4][0].push_back(0);
		cctvs[4][0].push_back(1);
		cctvs[4][0].push_back(2);
		cctvs[4][0].push_back(3);

		cctvs[4][1].push_back(0);
		cctvs[4][1].push_back(1);
		cctvs[4][1].push_back(2);
		cctvs[4][1].push_back(3);

		cctvs[4][2].push_back(0);
		cctvs[4][2].push_back(1);
		cctvs[4][2].push_back(2);
		cctvs[4][2].push_back(3);

		cctvs[4][3].push_back(0);
		cctvs[4][3].push_back(1);
		cctvs[4][3].push_back(2);
		cctvs[4][3].push_back(3);
	}
}

void Solve()
{
	// 90도 회전 -> 
	// 벽 통과는 불가능
	// CCTV 끼리는 가능
	// 일단, room 에 있는 모든 cctv 종류 찾기
	// 각각에 대해서 90도 회전 -> 모든 케이스 bfs
	// 단, 2번은 2개 케이스, 5번은 1개 케이스.
	vector<Cctv> curCctvs;
	vector<pair<int, int>> accCctvDirs;

	ans = N * M;

	for (int r = 0; r < N; ++r)
		for (int c = 0; c < M; ++c)
			if (room[r][c] >= 1 && room[r][c] <= 5)
				curCctvs.push_back({ r, c, room[r][c] - 1 });

	dfs(0, curCctvs, accCctvDirs); // cctv, cctv 방향 idx
	
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


