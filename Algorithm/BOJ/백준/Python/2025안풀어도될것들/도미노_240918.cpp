// https://www.acmicpc.net/status?user_id=dhsys112&problem_id=1552&from_mine=1

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

//도미노 패가 놓여진 보드의 길이
int gridSize;

//각 도미노 패에 있는 정수
vector<vector<int>> dominoPoints;

// 해당 열을 이미 방문했는가.
vector<bool> colUsed;	   

// 각 행에서 선택한 열의 번호.
vector<int> selectedCols;  

//백트래킹에 사용된 변수: 생성 가능한 점수 중 최대치를 담는 변수
long long maxPoint = (-2147483647L - 1);

//백트래킹에 사용된 변수: 생성 가능한 점수 중 최소치를 담는 변수
long long minPoint = 2147483647L;

long long calculatePoint();

void recursive(int depth) {
	if (depth == gridSize) {
		long long pointCalculated = calculatePoint();
		maxPoint = max(maxPoint, pointCalculated);
		minPoint = min(minPoint, pointCalculated);
		return;
	}

	for (int col = 0; col < gridSize; col++) {
		if (colUsed[col]) continue;
		colUsed[col] = true;

		// 여기서 depth 는 일조의 'row' 라고 생각해도 되는 것일까 ?
		selectedCols[depth] = col;
		recursive(depth + 1);
		colUsed[col] = false;
	}
}

long long calculatePoint() {

	//생성한 그룹의 개수
	int numGroups = 0;

	//그룹 생성에 사용된 패의 개수
	int numUsedTiles = 0;

	//특정 패가 그룹 생성에 사용되었는지 여부: 하나의 패를 여러 번 사용할 수 없다.
	vector<bool> tileUsed(gridSize, false);

	//그룹 생성: 모든 패가 그룹 생성에 사용될 때 까지 반복한다.
	while (numUsedTiles < gridSize) {

		//그룹을 시작하는 패의 왼쪽 suit
		int currentTileNumber = -1;

		//그룹을 시작하는 패의 오른쪽 suit
		int nextTileNumber = -1;

		// "그룹을 시작하는 패를 찾기 위한 loop"
		// 아직 사용되지 않은 도미노패를 찾아 그룹을 완성한다.
		for (int i = 0; i < gridSize; ++i) 
		{
			if (tileUsed[i])
				continue;
			numUsedTiles++;
			tileUsed[i] = true;
			currentTileNumber = i;					// tile row
			nextTileNumber = selectedCols[i];   // tile col (그 다음 tile row)
			break;
		}

		// 0.1, 1.2, 2.4, 3.2, 4.3

		// 하나의 그룹을 완성하려면 맨 왼쪽 suit와 맨 오른쪽 suit가 일치해야 한다.
		// 즉, 그룹을 완성하는 패.
		while (currentTileNumber != nextTileNumber) 
		{
			//그룹이 완성될 때 까지 다른 패를 덧붙여 나간다.
			numUsedTiles++;
			tileUsed[nextTileNumber] = true;
			nextTileNumber = selectedCols[nextTileNumber];
		}

		if (currentTileNumber == nextTileNumber)
			numGroups += 1;

		// numGroups++;
	}

	//선택된 도미노에 있는 정수들의 곱
	long long pointProduct = 1;

	for (int i = 0; i < gridSize; ++i) 
	{
		pointProduct *= dominoPoints[i][selectedCols[i]];
	}

	return (numGroups % 2 == 0) ? -pointProduct : pointProduct;
}


void Input()
{
	cin >> gridSize;
	dominoPoints.resize(gridSize, vector<int>(gridSize));
	for (int i = 0; i < gridSize; ++i) {
		for (int j = 0; j < gridSize; ++j) {
			char c;
			cin >> c;
			dominoPoints[i][j] = (c >= '0' && c <= '9') ? c - '0' : -(c - 'A' + 1);
		}
	}
}

void Solve()
{
	colUsed.resize(gridSize);
	selectedCols.resize(gridSize);

	recursive(0);

	cout << minPoint << endl;
	cout << maxPoint << endl;
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
