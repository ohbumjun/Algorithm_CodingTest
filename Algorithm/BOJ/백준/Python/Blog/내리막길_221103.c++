

// # 1번째 풀이 : 전형적인 Bottom Up 방식 = dp + dfs
#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include<queue>
#include<map>
#include <set>
 
#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int ROW, COL;
std::vector<std::vector<int>> Map;
std::vector<std::vector<int>> Dp;
std::vector<std::vector<bool>> Check;

int dfs(int Row, int Col)
{
    if (Row == ROW - 1 && Col == COL - 1)
    {
        // cout << "here" << endl;
        return 1;
    }

    // cout << "Row : " << Row << ", " << "Col : " << Col << endl;

    if (Dp[Row][Col] > 0)
        return Dp[Row][Col];

    int dp = 0;

	for (int k = 0; k < 4; k++)
	{
        int nRow = Row + dx[k];
        int nCol  = Col + dy[k];
        if (nRow < 0 || nRow >= ROW || nCol < 0 || nCol >= COL)
            continue;
        if (Map[nRow][nCol] >= Map[Row][Col])
            continue;
        dp += dfs(nRow, nCol);
	}
    Dp[Row][Col] = dp;
    // cout << endl;
    return dp;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    // 입력 
    cin >> ROW >> COL;
    Map.resize(ROW);
    for (int i = 0; i< ROW; i++)
    {
        Map[i].resize(COL);
    }

    int point = 0;
    for (int i = 0; i < ROW; i++)
    {
	    for (int j = 0; j < COL; j++)
	    {
            cin >> point;
            Map[i][j] = point ;
	    }
    }


    // DP 초기화
    Dp = std::vector<std::vector<int>>(ROW, std::vector<int>(COL, 0));
    Dp[0][0] = 0;
    Check = std::vector<std::vector<bool>>(ROW, std::vector<bool>(COL, false));

    cout << dfs(0, 0);

    /*
    for (int row = 0; row < ROW; row++)
    {
	    for (int col = 0; col < COL; col++)
	    {
            cout << Dp[row][col] << ". ";
	    }
        cout << endl;
    }
    */

    // cout << Dp[0][0] << endl;


    return 0;
}


// 2번째 풀이 : 시간초과 해결 방법 --> Check 배열을 통한 중복 방문 방지
#include<iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include<queue>
#include<map>
#include <set>
 
#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int ROW, COL;
std::vector<std::vector<int>> Map;
std::vector<std::vector<int>> Dp;
std::vector<std::vector<bool>> Check;

int dfs(int Row, int Col)
{
    if (Row == ROW - 1 && Col == COL - 1)
    {
        // cout << "here" << endl;
        return 1;
    }

    // cout << "Row : " << Row << ", " << "Col : " << Col << endl;

    // if (Dp[Row][Col] > 0)
       // return Dp[Row][Col];
    if (Check[Row][Col])
        return Dp[Row][Col];
    int dp = 0;

	for (int k = 0; k < 4; k++)
	{
        int nRow = Row + dx[k];
        int nCol  = Col + dy[k];
        if (nRow < 0 || nRow >= ROW || nCol < 0 || nCol >= COL)
            continue;
        if (Map[nRow][nCol] >= Map[Row][Col])
            continue;
        dp += dfs(nRow, nCol);
	}
    Dp[Row][Col] = dp;
    Check[Row][Col] = true;
    // cout << endl;
    return dp;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력 
    cin >> ROW >> COL;
    Map.resize(ROW);
    for (int i = 0; i< ROW; i++)
    {
        Map[i].resize(COL);
    }

    int point = 0;
    for (int i = 0; i < ROW; i++)
    {
	    for (int j = 0; j < COL; j++)
	    {
            cin >> point;
            Map[i][j] = point ;
	    }
    }


    // DP 초기화
    Dp = std::vector<std::vector<int>>(ROW, std::vector<int>(COL, 0));
    Dp[0][0] = 0;
    Check = std::vector<std::vector<bool>>(ROW, std::vector<bool>(COL, false));

    cout << dfs(0, 0);

    /*
    for (int row = 0; row < ROW; row++)
    {
	    for (int col = 0; col < COL; col++)
	    {
            cout << Dp[row][col] << ". ";
	    }
        cout << endl;
    }
    */

    // cout << Dp[0][0] << endl;


    return 0;
}


