// https://www.acmicpc.net/problem/1552

// # 1번째 풀이 -> 시간 초과
// 1) dfs -> 모든 방문 가능한 경우의 수 조사
    // 이후 N 개를 방문하면, 방문 경우의 수 -> 또 다시 순열을 통해 모든 조합으로 사이클 모두 구하기
    // 그 중에서 최대 사이클 개수를 사이클 개수로 설정
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

// 2번째 풀이 : -> 굳이 지금까지 모아온 경로 정보들을 순열로 만들 필요 x. map  ? 형태로 자료구조 변경
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

		// 지문에서 항상 하나 이상의 사이클이 나온다고 햇다.
		// 사이클이 만들어지지 않을 수도 있는 경우를 대비한다. ? X
		// 어차피 무조건 하나의 사이클은 만들어진다.
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
