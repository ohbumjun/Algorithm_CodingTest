// https://www.acmicpc.net/problem/2239

#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <stack>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

std::vector<std::vector<int>> Sudoku;

// 행 검사용 array
std::array<bool, 9> RowCheck;
std::array<bool, 9> ColCheck;
std::array<bool, 9> BoxCheck;

// 행
bool CheckRow (int TrialNum, int Row, std::vector<std::vector<int>>& pSudoku)
{
    // 해당 Row의 모든 Column을 고려한다.
    for (int Col = 0; Col < 9; Col++)
    {
        // 빈 공간이라면 건너뛴다.
        if (pSudoku[Row][Col] == 0)
            continue;

        // 해당 숫자가 이미 존재한다면 false
        if (pSudoku[Row][Col] == TrialNum)
        {
            // cout << "Trial Num : " << TrialNum << endl;
            // cout << "Row : " << Row << endl;
            return false;
        }
    }

    return true;
}

// 열
bool CheckCol(int TrialNum, int Col, std::vector<std::vector<int>>& pSudoku)
{
    // 해당 Col 의 모든 Row을 고려한다.
    for (int Row = 0; Row < 9; Row++)
    {
        // 빈 공간이라면 건너뛴다.
        if (pSudoku[Row][Col] == 0)
            continue;

        // 해당 숫자가 이미 존재한다면 false
        if (pSudoku[Row][Col] == TrialNum)
            return false;
    }

    return true;
}

// 각 영역
bool CheckBox (int TrialNum, int Row, int Col, std::vector<std::vector<int>>& pSudoku)
{
	// 속한 Box 를 구한다.
    int ConvertRow = (Row / 3) * 3;
    int ConvertCol = (Col / 3 ) * 3;

    for (int R = ConvertRow; R < ConvertRow + 3; R++)
    {
	    for (int C = ConvertCol; C < ConvertCol + 3; C++)
	    {
            if (pSudoku[R][C] == TrialNum)
                return false;
	    }
    }

    return true;
}

void MakeSudoku(int Index, std::vector<std::vector<int>>& pSudoku)
{
    int Row = Index / 9;
    int Col = Index % 9;

    // 만일 이미 해당 위치에 숫자가 차있다면 바로 다음으로 진행
    if (pSudoku[Row][Col] != 0)
    {
        if (Index == 80)
        {
            for (int r = 0; r < 9; r++)
            {
                for (int c = 0; c < 9; c++)
                {
                    cout << pSudoku[r][c];
                }
                cout << endl;
            }
            exit(0);
        }

        MakeSudoku(Index + 1, pSudoku);
        return;
    }

    // 0부터 9까지의 모든 숫자를 조사한다
    for (int CurNum = 1; CurNum <= 9; CurNum++)
    {
		// 현재 행, 열, 박스 에서 해당 숫자가 가능한지 판단한
	    if (!CheckRow(CurNum, Row, pSudoku))
	        continue;
	    if (!CheckCol(CurNum, Col, pSudoku))
            continue;
	    if (!CheckBox(CurNum, Row, Col, pSudoku))
            continue;
	    // 해당 위치에 숫자를 세팅한다.
	    pSudoku[Row][Col] = CurNum;

	    // 만약 가장 마지막 Index 라면 해당 Sudoku를 출력하고 종료
        if (Index == 80)
        {
	        for (int r = 0; r < 9; r++)
	        {
		        for (int c = 0; c < 9; c++)
		        {
                    cout << pSudoku[r][c];
		        }
                cout << endl;
	        }
            exit(0);
        }

        // Sudoku를 진행한다.
        MakeSudoku(Index + 1, pSudoku);

	    // 해당 위치에서 숫자를 뺀다
	    pSudoku[Row][Col] = 0;
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // Init 세팅
    Sudoku     = std::vector<std::vector<int>>(9, std::vector<int>(9));

    for (int row = 0; row < 9; row++)
    {
	    for (int col = 0; col < 9; col++)
	    {
            char num;
            cin >> num;
            Sudoku[row][col] = num;
            Sudoku[row][col] -= 48;
	    }
    }

    // dfs 로 들어갈 것이다.
    MakeSudoku(0, Sudoku);

    return 0;
}


