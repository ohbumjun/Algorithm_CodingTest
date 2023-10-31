// CodingTest.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
#define _CRT_SECURE_NO_WARNINGS

#define MAX 1000001

#include <iostream>
#include <vector>

using namespace std;

int N;
std::vector<bool> col_marked;
std::vector<std::pair<int, int>> cases;

// 이미 마크 ? 표시가 된 

void Input()
{
	cin >> N;

	col_marked.resize(N);

	for (int n = 0; n < N; ++n)
	{
		col_marked[n] = false;
	}
}

void ClearMap()
{
	for (int n = 0; n < N; ++n)
	{
		col_marked[n] = false;
	}

	cases.clear();
}

int DFS(int row, int col)
{
	int cnt		= 0;
	int nxtRow	= row + 1;

	cout << "row, col : " << row << "," << col << endl;

	if (row >= N - 1)
	{
		cout << "end" << endl;
		return 1;
	}

	col_marked[col] = true;
	cases.push_back(std::make_pair(row, col));


	for (int nxtCol = 0; nxtCol < N; ++nxtCol)
	{
		// 같은 열에 있는 대상은 건너뛴다.
		if (col_marked[nxtCol])
		{
			continue;
		}

		bool isDiagonal = false;

		// 대각선을 검사한다.
		for (int idx = 0; idx < cases.size(); ++idx)
		{
			int prevRow = cases[idx].first;
			int prevCol = cases[idx].second;

			// 오른쪽 대각선
			if (nxtRow + nxtCol == prevRow + prevCol)
			{
				isDiagonal = true;
				break;
			}

			// 왼쪽 대각선
			if (prevRow - prevCol == nxtRow - nxtCol)
			{
				isDiagonal = true;
				break;
			}
		}

		if (isDiagonal) continue;

		cnt += DFS(nxtRow, nxtCol);
	}

	// DFS 이후에 다시 빼주는 작업을 해줘야 한다. 
	col_marked[col] = false;
	cases.pop_back();

	return cnt;
}

void Solve()
{
	// 92 이다. 
	int answer = 0;

	for (int col = 0; col < N; ++col)
	{
		ClearMap();
		answer += DFS(0, col);
	}

	cout << answer << endl;
}

int main()
{
	ios::sync_with_stdio(false);

	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input.txt", "r", stdin);

	Input();

	Solve();
}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
