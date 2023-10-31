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
#define MAX 100000 + 1
#define INF int(1e9)

using namespace std;

int Dx[6] = {0, 0 ,1, -1, 0, 0};
int Dy[6] = {-1, 1, 0, 0, 0, 0};
int Dz[6] = {0, 0, 0, 0, -1, 1};

struct DistInfo {
    int Height;
	int Row;
	int Col;
	int Dist;
};

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    int COL, ROW, HEIGHT;

    cin >> COL >> ROW >> HEIGHT;

    // M : 열
    // N : 행

    int Input;

    std::vector<std::vector<std::vector<int>>> vecTomatoes(HEIGHT, std::vector<std::vector<int>>(ROW, std::vector<int>(COL)));
    std::vector<std::vector<std::vector<int>>> vecDist(HEIGHT, std::vector<std::vector<int>>(ROW, std::vector<int>(COL, INF)));

    std::queue<DistInfo> Queue;

    bool AllRiped = true;

    for (int h = 0; h < HEIGHT; h++)
    {
    	for (int n = 0; n < ROW; n++)
	    {
			for (int m = 0; m < COL; m++)
            {
                cin >> Input;
                vecTomatoes[h][n][m] = Input;

                // 모든 토마토가 익었는지 판단
                if (Input == 0)
                    AllRiped = false;

                // 익은 토마토 큐에 추가 
                if (Input == 1)
                {
                    DistInfo Info;
                    Info.Height = h; Info.Row = n; Info.Col = m; Info.Dist = 0;
                    Queue.push(Info);
                    vecDist[h][n][m] = 0;
                }
            }
	    }
    }

    // 모든 토마토가 익은 것이라면
    if (AllRiped == true)
    {
        cout << 0;
        exit(0);
    }

    while (!Queue.empty())
    {
        DistInfo Info = Queue.front();
        Queue.pop();

        int CurDist = Info.Dist;

        // 주변 범위 조사하기
        for (int k = 0; k < 6; k++)
        {
            int nCol  = Info.Col + Dx[k];
            int nRow = Info.Row + Dy[k];
            int nH     = Info.Height + Dz[k];

            // 범위 벗어나면 X
            if (nRow < 0 || nRow >= ROW || nCol < 0 || nCol >= COL || nH < 0 || nH >= HEIGHT)
                continue;

            // 토마토가 들어있지 않은 칸이라면
            if (vecTomatoes[nH][nRow][nCol] == -1)
                continue;

            // 이미 최소 거리라면 X
            if (vecDist[nH][nRow][nCol] <= CurDist + 1)
                continue;

            // 거리 표시
            vecDist[nH][nRow][nCol] = CurDist + 1;

            // 익은 것이라고 표시하기
            vecTomatoes[nH][nRow][nCol] = 1;

            // Queue에 추가
            DistInfo Info;
            Info.Height = nH; Info.Row = nRow; Info.Col = nCol; Info.Dist = CurDist + 1;
            Queue.push(Info);
        }
    }

    // 최대 시간 출력하기 ( == 모든 토마토가 익은 시간 )
    int maxTime = 0;

    for (int h = 0; h < HEIGHT; h++)
    {
        for (int n = 0; n < ROW; n++)
        {
            for (int m = 0; m < COL; m++)
            {
                // 익지 않은 것이 하나라도 있다면
                if (vecTomatoes[h][n][m] == 0)
                {
                    cout << -1;
                    exit(0);
                }

                // 최소거리 Update
                if (maxTime < vecDist[h][n][m] && vecDist[h][n][m] != INF)
                    maxTime = vecDist[h][n][m];
            }
        }
    }

    cout << maxTime;

    /*
    for (int h = 0; h < HEIGHT; h++)
    {
        for (int n = 0; n < ROW; n++)
        {
            for (int m = 0; m < COL; m++)
            {
                cout << vecDist[h][n][m] << ".";
            }
            cout << endl;
        }
        cout << endl;
    }
    */
    
    return 0;
}


