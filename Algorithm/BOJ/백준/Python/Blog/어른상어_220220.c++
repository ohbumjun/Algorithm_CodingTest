#define _CRT_SECURE_NO_WARNINGS

#include<iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
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

enum Direction {
	Top,
    Bottom,
    Left,
    Right,
    End
};

// 방향 세팅 (1,2,3,4 --> 위, 아래, 왼쪽, 오른쪽)
int Dx[4] = {0, 0, -1, 1};
int Dy[4] = {-1, 1, 0, 0};

// 냄새에 해당하는 구조체
// - 종류, 시간 (초기값은 k로 세팅)
struct Smell {
    int Kind;
    int TimeLeft;
    Smell() :
    Kind(-1),
    TimeLeft(-1){}
};

// 상어에 해당하는 구조체
// - 현재 바라보는 방향
// - 우선순위 -> 각 방향에 따른 우선순위 
// - 자신의 숫자
struct Shark {
    int Row;
    int Col;
    int Dir;
    int Priority[Direction::End][Direction::End];
    int Num;

    bool operator < (const Shark& Sk) const 
    {
        return Num < Sk.Num;
    }
};

int SIZE = -1, TOTALSHARK = 1, K = -1;

// 냄새를 저장하는 2차원 배열
// - 냄새가 존재하지 않는 칸은, 종류, 시간을 -1로 세팅한다.
std::vector<std::vector<Smell>> vecSmell;

// 상어들의 이동 결과를 저장하는 3차원 배열 
std::vector<std::vector<std::vector<int>>> vecPosShark;

// 상어의 종류를 unordered_map
// 자신의 숫자를 key로 하여 저장 --> 이후 삭제의 편리성을 위한 것이다.
std::unordered_map<int, Shark*> mapShark;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    cin >> SIZE >> TOTALSHARK >> K;

    vecSmell = std::vector<std::vector<Smell>>(SIZE, std::vector<Smell>(SIZE));
    vecPosShark = std::vector<std::vector<std::vector<int>>>(SIZE, std::vector<std::vector<int>>(SIZE, std::vector<int>(0)));

    for (int row = 0; row < SIZE; row++)
    {
	    for (int col = 0; col < SIZE; col++)
	    {
            int SharkNum;
            cin >> SharkNum;

            if (SharkNum > 0)
            {
                // 해당 번호의 Shark 구조체 생성
                Shark *NewShark = new Shark;

                // 정보 세팅
                NewShark->Num = SharkNum;
                NewShark->Row = row;
                NewShark->Col = col;

                // Shark 종류에 추가
                mapShark.insert(std::make_pair(SharkNum, NewShark));
                
            }
	    }
    }

    // 각 상어의 방향
    for (int i = 0; i <TOTALSHARK; i++)
    {
        int InputD;

        cin >> InputD;

        // 상어 정보
        Shark *CurShark = mapShark.find(i + 1)->second;

        // 1을 빼서 Index 개념으로 접근할 수 있게 한다.
        CurShark->Dir = InputD - 1;

    }

    // 이후, 각 상어의 우선 순위 방향을 세팅한다.
    for (int i = 0; i < TOTALSHARK; i++)
    {
        // 상어 정보
        Shark *CurShark = mapShark.find(i+1)->second;

        // 우선순위 정보 가져오기
        // 1) 위를 향할 때 우선순위
        // 2) 아래를 향할 때 우선순위
        // 3) 왼쪽을 향할 때 우선순위
        // 4) 오른쪽을 향할 때 우선순위
        for (int p = 0; p < 4; p++)
        {
            int InputP;
            for (int q = 0; q < 4; q++)
            {
                cin >> InputP;
				CurShark->Priority[p][q] = InputP - 1;
            }
        }
    }

    // 0) 맨 처음에는, 자기가 있는 위치에 냄새를 남긴다.
    // - 냄새의 종류
    // - 남은 시간을 기록해야 한다.
    auto iter = mapShark.begin();
    auto iterEnd = mapShark.end();

    for (; iter != iterEnd; ++iter)
    {
        Shark *CurShark = iter->second;

        // 남은 시간 Update
        vecSmell[CurShark->Row][CurShark->Col].TimeLeft = K;

        // 종류 세팅
        vecSmell[CurShark->Row][CurShark->Col].Kind = CurShark->Num;
    }

    // 만약 처음부터 격자에 상어가 한마리라면 0을 출력하고 종료
    if (mapShark.size() == 1)
    {
        cout << 0;
        exit(0);
    }

    // 최대 1000초 까지 진행한다
    for (int CurTime = 1; CurTime < 1001; CurTime++)
    {
        auto iter = mapShark.begin();
        auto iterEnd = mapShark.end();
        

        for (; iter != iterEnd; ++iter)
        {
            Shark *CurShark = iter->second;

            // 1) 방향 판단
			// - 먼저, 인접한 칸 중에서, 아무 냄새가 없는 칸의 방향으로 이동한다.
            int CurRow         = CurShark->Row;
            int CurCol          = CurShark->Col;
            int CurDir           = CurShark->Dir;
            int CurSharkNum = CurShark->Num;
            

            bool NoSmellFound = false;

            int NxtMovedRow = -1, NxtMovedCol = -1, NxtMovedDir = -1;

            // 현재 자신의 방향에 기초하여, 우선순위 방향대로 탐색해야 한다.
            for (int k = 0; k < 4; k++)
            {
                int NxtRowDir = Dy[CurShark->Priority[CurDir][k]];
                int NxtColDir = Dx[CurShark->Priority[CurDir][k]];

                int NxtRow = CurRow + NxtRowDir;
                int NxtCol = CurCol + NxtColDir;

                // 범위 검사
                if (NxtRow < 0 || NxtRow >= SIZE || NxtCol < 0 || NxtCol >= SIZE)
                    continue;

                if (vecSmell[NxtRow][NxtCol].Kind == -1)
                {
                    NoSmellFound = true;
                    NxtMovedRow = NxtRow;
                    NxtMovedCol = NxtCol;
                    NxtMovedDir = CurShark->Priority[CurDir][k];
                    break;
                }
            }

            // 2) 이동
			// - 해당 방향으로 한 칸 이동한다.
			// - 해당 상어의 방향을, 이동한 방향으로 세팅한다.

            // 만약 아무 냄새도 없는 칸을 찾았다면
            if (NoSmellFound)
            {
	            // 해당 방향으로 상어를 이동 시킨다.
                vecPosShark[NxtMovedRow][NxtMovedCol].push_back(CurSharkNum);

                // 이동 방향 Update
                CurShark->Dir = NxtMovedDir;

                // 위치 Update
                CurShark->Row = NxtMovedRow;
                CurShark->Col = NxtMovedCol;
            }
            else
            {
                // - 그러한 칸이 없다면, 자신의 냄새가 있는 칸의 방향을 찾을 것이다
				// 여기서도 자신의 방향 우선순위대로 조사한다.
                for (int k = 0; k < 4; k++)
                {
                    int NxtRowDir = Dy[CurShark->Priority[CurDir][k]];
                    int NxtColDir = Dx[CurShark->Priority[CurDir][k]];

                    int NxtRow = CurRow + NxtRowDir;
                    int NxtCol = CurCol + NxtColDir;

                    // 범위 검사
                    if (NxtRow < 0 || NxtRow >= SIZE || NxtCol < 0 || NxtCol >= SIZE)
                        continue;

                    // 자신의 냄새가 있는 방향을 발견했다면
                    // 해당 방향으로 이동후 break
                    if (vecSmell[NxtRow][NxtCol].Kind == CurSharkNum)
                    {
                        // 이동
                        vecPosShark[NxtRow][NxtCol].push_back(CurSharkNum);

                        // 방향 정보 Update
                        CurShark->Dir = CurShark->Priority[CurDir][k];

                        // 위치 Update
                        CurShark->Row = NxtRow;
                        CurShark->Col = NxtCol;

                        break;
                    }
                }
            }
        }

        // 3) 모든 칸에 남아있는 냄새의 시간을 1 씩 줄이고
        // - 0 이 되는 녀석은 제거한다.
        for (int row = 0; row < SIZE; row++)
        {
            for (int col = 0; col < SIZE; col++)
            {
                if (vecSmell[row][col].Kind != -1)
                {
                    vecSmell[row][col].TimeLeft -= 1;

                    if (vecSmell[row][col].TimeLeft <= 0)
                    {
                        vecSmell[row][col].TimeLeft = -1;
                        vecSmell[row][col].Kind = -1;
                    }
                }
            }
        }


        // 4) 같은 칸에 여러 상어가 있다면,
        // - 가장 작은 숫자의 상어만을 남기고 모두 제거한다.
        // - 그리고 해당 칸에, 남아있는 상어의 냄새를 세팅한다.
        for (int row = 0; row < SIZE; row++)
        {
	        for (int col = 0; col < SIZE; col++)
	        {
                // 맨 처음 원소에 해당하는 Shark 외
                // 모든 Shark 는 mapShark 에서 제외시킨다.
                size_t vecSize = vecPosShark[row][col].size();

		        if (vecSize > 0)
		        {
			        // 정렬을 수행한다.
                    std::sort(vecPosShark[row][col].begin(), vecPosShark[row][col].end());

                    if (vecSize > 1)
                    {
                        for (size_t Index = 1; Index < vecSize; Index++)
                        {
                            auto iter = mapShark.find(vecPosShark[row][col][Index]);

                            // free
                            delete iter->second;

                            mapShark.erase(iter);

                        }
                    }

                    // 해당 칸에 상어의 냄새를 세팅한다.
                    vecSmell[row][col].TimeLeft = K;
                    vecSmell[row][col].Kind = vecPosShark[row][col][0];
		        }
	        }
        }
        

        // 5) vecCurPosShark 를 Update 해준다. ( 다시 모두 비워준다. )
        for (int row = 0; row < SIZE; row++)
        {
            for (int col = 0; col < SIZE; col++)
            {
                vecPosShark[row][col].clear();
            }
        }

        // 현재 1번 상어만 남는 지를 확인한다 ( 사실상 Map 의 Size 만 조사하면 되지 않을까 ?)
        if (mapShark.size() == 1)
        {
            cout << CurTime;
            exit(0);
        }

    }

    cout << -1;
    
    return 0;
}


