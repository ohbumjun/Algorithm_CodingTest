#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>
#include <string>
#include <cmath>
#include <climits>
#include <bitset>

#define endl "\n"
#define MAX 10000+1
#define INF int(1e9)

using namespace std;

int N;

int dRow[6] = {-1, -1, 0, 1, 1, 0};
int dCol[6]   = {0, 1, 1, 0, -1, -1};

int ColorNum = 0;

std::vector<std::vector<char>> vecMap;
std::vector<std::vector<int>> vecColor;

void Input()
{
    // 육각 보드 만들기
    cin >> N;

    vecMap.reserve(N);
    vecColor.reserve(N);

    for (int i = 0; i < N; ++i)
    {
        vecMap.push_back(std::vector<char>(N, '-'));
        vecColor.push_back(std::vector<int>(N, -1));
    }

    for (int i = 0; i < N; ++i)
    {
        std::string Input;
        cin >> Input;

        for (int j = 0; j < N; ++j)
        {
            vecMap[i][j] = Input[j];
        }
    }
}

void DFS(int row, int col, int color)
{
    // 여기에 들어왔다는 것은, 색칠할 색상이 적어도 1개 있다는 것이다.
    ColorNum = max(ColorNum, color);

    vecColor[row][col] = color;

    // 해당 칸을 중심으로 6칸을 조사한다.
    for (int k = 0; k < 6; ++k)
    {
        int nxtRow = row + dRow[k];
        int nxtCol = col + dCol[k];

        // 범위 조사
        if (nxtRow < 0 || nxtRow >= N || nxtCol < 0 || nxtCol >= N)
            continue;

        if (vecMap[nxtRow][nxtCol] == 'X')
        {
            // 인접한 곳의 색이 아직 칠해지지 않았다면 --> 최소 2개의 색상
            if (vecColor[nxtRow][nxtCol] == -1)
            {
                int nxtColor = color == 1 ? 2 : 1;
                DFS(nxtRow, nxtCol, nxtColor);
                ColorNum = max(ColorNum, 2);
            }
            // 이미 색이 칠해져 있다면, 그리고 자신과 색상이 같다면 --> 최소 3개의 색상
            else if (vecColor[nxtRow][nxtCol] == color)
            {
                /*
                for (int row = 0; row < N; ++row)
                {
	                for (int col = 0; col < N; ++col)
	                {
                        cout << vecColor[row][col] << ".";
	                }
                    cout << endl;
                }
                */


                ColorNum = max(ColorNum, 3);
                vecColor[row][col] = color;
                cout << ColorNum;
                exit(0);
            }
        }
    }
}

void MakeBoard()
{
    // 왼쪽 상단 부터 시작하여, 색칠할 첫번째 칸을 찾는다
    int stRow = -1, stCol = -1;

    for (int row = 0; row < N; ++row)
    {
	    for (int col = 0; col < N; ++col)
	    {
		    if (vecMap[row][col] == 'X')
		    {
                stRow = row;
                stCol = col;
                break;
		    }
	    }
        if (stRow != -1)
            break;
    }

    // 여전히 stRow 가 -1 이라면, 색칠할 곳이 없다라는 의미이므로, 0을 출력하고 끝
    if (stRow == -1)
    {
        cout << 0;
        exit(0);
    }

    // 모든 정점들에 대해서 아래의 DFS 함수를 실행하 것이다.
    for (int row = 0; row < N; ++row)
    {
        for (int col = 0; col < N; ++col)
        {
            if (vecMap[row][col] == 'X' && vecColor[row][col] == -1)
            {
                DFS(row, col, 1);
            }
        }
    }
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // freopen("input_c.txt", "r", stdin);

    Input();

    MakeBoard();

    cout << ColorNum;

    return 0;
}