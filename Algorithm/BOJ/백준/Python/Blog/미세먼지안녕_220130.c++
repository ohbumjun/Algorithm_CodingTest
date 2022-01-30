#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <functional>
#include<queue>
#include<map>
#include <set>

#define endl "\n"
#define MAX 1000+1
#define INF int(1e9)

using namespace std;

int R, C, T;
std::vector<std::vector<int>> CurrentDust;
std::vector<std::vector<int>> SpreadDust;
std::vector<std::vector<int>> MoveDust;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int AirMoveDirX[4] = {0, -1, 0, 1}; // 세로
int AirMoveDirY[4] = {1, 0, -1, 0};  // 가로 

std::pair<int, int> GetNextPos(int Row, int Col, int& Dir, bool Up)
{
    int NxtRow = Row + AirMoveDirX[Dir];
    int NxtCol  = Col + AirMoveDirY[Dir];

    if (NxtRow >= R || NxtRow < 0 || NxtCol >= C || NxtCol < 0)
    {
        if (Up)
            Dir = (Dir + 1) % 4;
        else
        {
            Dir = (Dir - 1);
            if (Dir < 0)
                Dir = 3;
        }

        NxtRow = Row + AirMoveDirX[Dir];
        NxtCol = Col + AirMoveDirY[Dir];
    }

    return std::make_pair(NxtRow, NxtCol);
}

int CalSum(int& Sum)
{
    for (int row = 0; row < R; row++)
    {
        for (int col = 0; col < C; col++)
        {
            Sum += CurrentDust[row][col];
        }
    }
    return Sum;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    int Time = 0;
    int FAirR = -1, FAirC = -1;
    int SAirR = -1, SAirC = -1;

    cin >> R >> C >> T;
    CurrentDust = std::vector<std::vector<int>>(R, std::vector<int>(C, 0));
    SpreadDust = std::vector<std::vector<int>>(R, std::vector<int>(C, 0));
    MoveDust    = std::vector<std::vector<int>>(R, std::vector<int>(C, 0));

    for (int row = 0; row < R; row++)
    {
	    for (int col = 0; col < C; col++)
	    {
            int N;
            cin >> N;
            CurrentDust[row][col] = N;
	    }
    }

    // 공기 청정기 위치 찾기
    for (int row = 0; row < R; row++)
    {
        for (int col = 0; col < C; col++)
        {
        	if (CurrentDust[row][col] == -1)
        	{
        		if (FAirR == -1)
                    FAirR = row, FAirC = col;
                else
                    SAirR = row, SAirC = col;
        	}
        }
    }

    while (Time < T)
    {
        // 현재 미세먼지 초기화
        for (int row = 0; row < R; row++)
        {
            for (int col = 0; col < C; col++)
            {
                SpreadDust[row][col] = 0;
            }
        }

        // 미세먼저 확산
        for (int row = 0; row < R; row++)
        {
	        for (int col = 0; col < C; col++)
	        {
                if (CurrentDust[row][col] == 0)
                    continue;

                // 공기 청정기 pass 
                if (row == FAirR && col == FAirC)
                    continue;
                if (row == SAirR && col == SAirC)
                    continue;

                int Dust = CurrentDust[row][col];
                int Spread = 0;

		        for (int k = 0; k < 4; k++)
		        {
                    int nRow = row + dx[k];
                    int nCol   = col + dy[k];

                    // 범위
                    if (nRow >= R || nRow < 0 || nCol >= C || nCol < 0)
                        continue;

                    // 공기 청정기 여부
                    if (nRow == FAirR && nCol == FAirC)
                        continue;
                    if (nRow == SAirR && nCol == SAirC)
                        continue;

                    SpreadDust[nRow][nCol] += Dust / 5;
                    Spread += 1;

		        }

                // 해당 칸 미세먼지 감소
                Dust -= (Dust / 5) * Spread;
                SpreadDust[row][col] += Dust;
	        }
        }

        // 공기 청정기 발동
        for (int row = 0; row < R; row++)
        {
            for (int col = 0; col < C; col++)
            {
                MoveDust[row][col] = SpreadDust[row][col];
            }
        }

        // 1) 윗칸 먼저
        int FCurR = FAirR + AirMoveDirX[0];
        int FCurC = FAirC + AirMoveDirY[0];
        int AirMoveDir = 0;

        while (true)
        {
            std::pair<int, int> NxtPos = GetNextPos(FCurR, FCurC, AirMoveDir, true);
            MoveDust[NxtPos.first][NxtPos.second] = SpreadDust[FCurR][FCurC];
            FCurR = NxtPos.first, FCurC = NxtPos.second;

            if (FCurR == FAirR && FCurC == FAirC)
                break;
        }

        // 공기청정기 위치
        MoveDust[FAirR][FAirC] = 0;
        // 공기청정기 다음 위치
        MoveDust[FAirR + AirMoveDirX[0]][FAirC + AirMoveDirY[0]] = 0;

        // 2) 아랫칸 그 다음
        int SCurR = SAirR + AirMoveDirX[0];
        int SCurC = SAirC + AirMoveDirY[0];
        AirMoveDir = 0;

        while (true)
        {
            std::pair<int, int> NxtPos = GetNextPos(SCurR, SCurC, AirMoveDir, false);
            MoveDust[NxtPos.first][NxtPos.second] = SpreadDust[SCurR][SCurC];
            SCurR = NxtPos.first, SCurC = NxtPos.second;

            if (SCurR == SAirR && SCurC == SAirC)
                break;
        }

        // 공기 청정기 위치
        MoveDust[SAirR][SAirC] = 0;
        // 공기청정기 다음 위치
        MoveDust[SAirR + AirMoveDirX[0]][SAirC + AirMoveDirY[0]] = 0;

        // Curret Dust로 복사해주기
        for (int row = 0; row < R; row++)
        {
            for (int col = 0; col < C; col++)
            {
                CurrentDust[row][col] = MoveDust[row][col];
            }
        }

        Time += 1;
    }

    // 남은 먼지양 구하기
    int ANS = 0;
    cout << CalSum(ANS);
   
    return 0;
}


