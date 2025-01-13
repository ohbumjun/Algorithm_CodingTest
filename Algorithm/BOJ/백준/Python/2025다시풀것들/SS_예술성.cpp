// https://www.codetree.ai/training-field/frequent-problems/problems/artistry?page=2&pageSize=20

// https://www.codetree.ai/training-field/frequent-problems/problems/codetree-tour/description?page=1&pageSize=10

// 1) 시간 초과
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <algorithm>
#include <cassert>
using namespace std;

#define INT_MAX int(1e9)

// #define DEBUG 1

struct GroupInfo
{
    int num;
    vector<pair<int, int>>  poses;
};

int N;
int currentId = 11;
vector < vector<int>> board;
vector < vector<int>> idBoard;
unordered_map<int, GroupInfo> groupInfo; // id, table<key,vec<poses>>
vector <vector<int>> groupScore; // [r][c] : r과 c 숫자를 가진 그룹 조합 점수


int dRow[4] = { 0, 0, 1, -1 };
int dCol[4] = { 1, -1, 0, 0 };
int groupScoreMax = 1;

void Input()
{
    cin >> N;
    groupScoreMax = 2 * N * N + 1;
    board.resize(N, vector<int>(N, 0));
    idBoard.resize(N, vector<int>(N, 0));
    groupScore.resize(groupScoreMax, vector<int>(groupScoreMax, INT_MAX));

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
			cin >> board[i][j];
}

int caclucate()
{
    int totScore = 0;

    groupInfo.clear();
    currentId = 0;

    for (int r = 0; r < groupScoreMax; ++r)
        for (int c = 0; c < groupScoreMax; ++c)
			groupScore[r][c] = INT_MAX;

    // 1) 그룹화 하기
    vector<vector<bool>> check;
    check.resize(N, vector<bool>(N, false));

    for (int r = 0; r < N; ++r)
    {
        for (int c = 0; c < N; ++c)
        {
            if (check[r][c] == true)
				continue;
            vector<pair<int, int>> poses;
            int curNum = board[r][c];
            queue<pair<int, int>> q;
            q.push({ r, c });
            check[r][c] = true;
            while (!q.empty())
            {
                int curRow = q.front().first;
				int curCol = q.front().second;
				q.pop();
                poses.push_back({ curRow, curCol });
                for (int i = 0; i < 4; ++i)
                {
					int nextRow = curRow + dRow[i];
					int nextCol = curCol + dCol[i];
                    if (nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= N)
                        continue;
                    if (check[nextRow][nextCol] == true)
                        continue;
                    if (board[nextRow][nextCol] != curNum)
                        continue;
                    check[nextRow][nextCol] = true;
                    q.push({ nextRow, nextCol });
                }
            }

            for (const pair<int, int>& pos : poses)
                idBoard[pos.first][pos.second] = currentId;

            groupInfo[currentId].num = curNum;
            groupInfo[currentId].poses = std::move(poses);
            currentId += 1;
        }
    }

#ifdef DEBUG
    cout << "----------------------\n";
    cout << "id  Board" << endl;
    for (int r = 0; r < N; ++r)
    {
        for (int c = 0; c < N; ++c)
            cout << idBoard[r][c] << " ";
        cout << endl;
    }
#endif


    // 조합 점수 구하기
    for (const auto& stInfo : groupInfo)
    {
        int currentId = stInfo.first;
        int stNum = stInfo.second.num;
        const vector<pair<int, int>>& stPoses = stInfo.second.poses;
        for (const auto& nxtInfo : groupInfo)
        {
            int nxtId = nxtInfo.first;
            int nxtNum = nxtInfo.second.num;
            const vector<pair<int, int>>& nxtPoses = nxtInfo.second.poses;
            if (currentId == nxtId)
				continue;
            if (groupScore[currentId][nxtId] != INT_MAX)
                continue;
            int curScore = 0;
            int stGroupSize = stPoses.size();
            int nxtGroupSize = nxtPoses.size();
            curScore = stGroupSize + nxtGroupSize;
            curScore *= stNum;
            curScore *= nxtNum;
            // 맞닿은 변을 조사해야 한다.
            // st 기준으로 nxtNum 을 찾을 것이다
            int touchCount = 0;
            for (const pair<int, int>& stpos : stPoses)
            {
                int curRow = stpos.first;
                int curCol  = stpos.second;
                // 현재 기준 4방향 조사 -> nxtNum 찾기
                for (int d = 0; d < 4; ++d)
                {
                    int nxtRow = curRow + dRow[d];
                    int nxtCol = curCol + dCol[d];
                    if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
                        continue;
                    if (idBoard[nxtRow][nxtCol] != nxtId)
                        continue;
                    touchCount++;
                }
            }

            if (touchCount == 0)
            {
                continue;
            }

            curScore *= touchCount;

            // 모두 끝나고
            groupScore[currentId][nxtId] = curScore;
            groupScore[nxtId][currentId] = curScore;

            totScore += curScore;
        }
    }
    
    return totScore;
}

vector<vector<int>> spinPart(int size, int stR, int stC)
{
    // size : 각 부분 격자 사이즈 ex) 2x2 라면 size 는 2
     vector<vector<int>> tempBoard;
     vector<vector<int>> returnBoard;
     tempBoard.resize(size, vector<int>(size, 0));
     returnBoard.resize(size, vector<int>(size, 0));

     // stR, stC 을 받고, 거기서 size 만큼 순회
     // 해당 내용을 tempBoard 에 넣기
     for (int r = stR; r < stR + size; ++r)
		 for (int c = stC; c < stC + size; ++c)
			 tempBoard[r - stR][c - stC] = board[r][c];
     
     // 이후 시계 방향 로직을 통해서 새로운 2차원 만들기
     // ex) 0.0 -> 0.1 / 0.1 -> 1.1 / 1.1 -> 1.0 / 1.0 -> 0.0
     // r : c -> r 로 간다
     // c : N - 1 - r
     for (int r = 0; r < size; ++r)
     {
         for (int c = 0; c < size; ++c)
         {
             int nxtRow = c;
			 int nxtCol = size - 1 - r;
             returnBoard[nxtRow][nxtCol] = tempBoard[r][c];
         }
     }

     // 그값을 리턴하기
     return returnBoard;
}

void spin()
{
#ifdef DEBUG
    cout << "----------------------\n";
    cout << "before  L" << endl;
    for (int r = 0; r < N; ++r)
    {
		for (int c = 0; c < N; ++c)
			cout << board[r][c] << " ";
		cout << endl;
	}
#endif

    // 1) 가운데 회전
    // ex) 0.2 -> 2.0 / 2.0 -> 4.2/ 4.2 -> 2.4/ 2.4 -> 0.2
    // c : r -> c 로 간다
    // r : N - 1 - c
    set<pair<int, int>> middles;
    for (int r = 0; r < N; ++r)
        middles.insert({ r, N / 2 });
    for (int c = 0; c < N; ++c)
        middles.insert({ N / 2, c });
    vector < vector<int>> copyBoard = board;
    for (const auto& info : middles)
    {
        int cRow = info.first;
        int cCol = info.second;
        int nxtRow = N - 1 - cCol;
        int nxtCol = cRow;
        copyBoard[nxtRow][nxtCol] = board[cRow][cCol];
    }
    board = copyBoard;

#ifdef DEBUG
    cout << "middle  L" << endl;
    for (int r = 0; r < N; ++r)
    {
        for (int c = 0; c < N; ++c)
            cout << board[r][c] << " ";
        cout << endl;
    }
#endif

    // 2) 각 부분 회전
    int size = N / 2;
    int stRow = 0, stCol = 0; // left top
    vector<vector<int>> spinned = spinPart(size, stRow, stCol);
    for (int r = stRow; r < stRow + size; ++r)
        for (int c = stCol; c < stCol + size; ++c)
			board[r][c] = spinned[r - stRow][c - stCol];

#ifdef DEBUG
	cout << "leftTop  L" << endl;
    for (int r = stRow; r < stRow + size; ++r)
    {
        for (int c = stCol; c < stCol + size; ++c)
            cout << board[r][c] << " ";
        cout << endl;
    }
#endif

	stRow = 0, stCol = N / 2 + 1; // right top
	spinned = spinPart(size, stRow, stCol);
	for (int r = stRow; r < stRow + size; ++r)
		for (int c = stCol; c < stCol + size; ++c)
            board[r][c] = spinned[r - stRow][c - stCol];
#ifdef DEBUG
    cout << "right Top  L" << endl;
    for (int r = stRow; r < stRow + size; ++r)
    {
        for (int c = stCol; c < stCol + size; ++c)
            cout << board[r][c] << " ";
        cout << endl;
    }
#endif
    stRow = N / 2 + 1, stCol = 0; // left bottom
    spinned = spinPart(size, stRow, stCol);
    for (int r = stRow; r < stRow + size; ++r)
		for (int c = stCol; c < stCol + size; ++c)
			board[r][c] = spinned[r - stRow][c - stCol];
#ifdef DEBUG
    cout << "left Bottom  L" << endl;
    for (int r = stRow; r < stRow + size; ++r)
    {
        for (int c = stCol; c < stCol + size; ++c)
            cout << board[r][c] << " ";
        cout << endl;
    }
#endif
    stRow = N / 2 + 1, stCol = N / 2 + 1; // right bottom
	spinned = spinPart(size, stRow, stCol);
	for (int r = stRow; r < stRow + size; ++r)
        for (int c = stCol; c < stCol + size; ++c)
			board[r][c] = spinned[r - stRow][c - stCol];
#ifdef DEBUG
    cout << "right Bottom  L" << endl;
    for (int r = stRow; r < stRow + size; ++r)
    {
        for (int c = stCol; c < stCol + size; ++c)
            cout << board[r][c] << " ";
        cout << endl;
    }
#endif

#ifdef DEBUG
    cout << "after  L" << endl;
    for (int r = 0; r < N; ++r)
    {
        for (int c = 0; c < N; ++c)
            cout << board[r][c] << " ";
        cout << endl;
    }
#endif
}


void Solve()
{
   // 1) 초기 점수 구하기
    // - 각 그룹별로 그룹화 하기
    // - 조합 점수 구하기 : 변 공유 => check 2차원 배열 (각 그룹 기준)
    int initScore = caclucate();

    // 2) 회전
    // - 가운데 십자가 반시계 회전
    // - 그외 부분 시계방향 회전 => (0.0) 으로 옮겨서 회전, 그 이후 값 복사
    // - 이후 예술 점수 구하기
    int firstScore = 0;
    spin();
    firstScore = caclucate();

    int secondScore = 0;
    spin();
    secondScore = caclucate();

    int thirdScore = 0;
    spin();
    thirdScore = caclucate();

    // 3) 초기 + 1+ 2 + 3 => 합 구하기
    cout << initScore + firstScore + secondScore + thirdScore << endl;
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

// 2) 