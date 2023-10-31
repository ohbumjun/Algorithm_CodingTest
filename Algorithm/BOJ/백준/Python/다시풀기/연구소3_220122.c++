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

int N, M;
int ANSWER = INF;
int NonVirusNum = 0;
std::vector<std::vector<int>>   Maps; // 원본
std::vector<std::vector<int>>   TestMaps; // 복사본
std::vector<std::vector<bool>> CheckMaps; // 방문 여부
std::vector<std::vector<int>>   DistMaps;  // 각 칸까지의 시간
std::vector<pair<int, int>>        Virus;
std::vector<std::vector<pair<int, int>>> VirusCombination;

// 방향
int dx[4] = { -1, 1, 0, 0};
int dy[4] = { 0, 0, 1, -1};


// 그 다음 BFS 를 통한 최대값 찾기 알고리즘 적용
void MakeVirusSet(int Num)
{
	for (int i = 0; i < (1 << Num); i++)
	{
        int Count = 0;

        for (int j = 0; j < Num; j++)
        {
	        if (i & (1 << j))
                Count += 1;
        }

        if (Count == M)
        {
            std::vector<pair<int, int>> VirusSet;
            for (int j = 0; j < Num; j++)
            {
                if (i & (1 << j))
                    VirusSet.push_back(Virus[j]);
            }
            VirusCombination.push_back(VirusSet);
        }
	}
}

void ResetMaps()
{
	for (int row = 0; row < N; row++)
	{
        for (int col = 0; col < N; col++)
        {
            TestMaps[row][col] = Maps[row][col];
            CheckMaps[row][col] = false;
            DistMaps[row][col] = 0;
        }
	}
}

void SetVirus()
{
	// 모든 바이러스 세트에 대해서
    int Size = (int)VirusCombination.size();

    for (int set = 0; set < Size; set++)
    {
        // 현재 조사하는 Virus 조합
        std::vector<pair<int, int>> CurrentVirus = VirusCombination[set];

        // BFS 용 Queue
        std::queue<pair<int, int>> queue;

        // "비"바이러스 개수
        int CNonVirusNum = NonVirusNum;

        // 바이러스 전체 확산 여부
        bool AllSpread = false;

        // Maps 재세팅
        ResetMaps();

        int CurRow = -1, CurCol = -1;
        int NxtRow = -1, NxtCol = -1;
        pair<int, int> CurSet = {};

        for (int i = 0; i < M; i++)
        {
            queue.push(CurrentVirus[i]);

            // 방문 처리
            int CurRow = CurrentVirus[i].first;
            int CurCol  = CurrentVirus[i].second;
            CheckMaps[CurRow][CurCol] = true;
        }

        while (!queue.empty())
        {
            CurSet = queue.front();
            queue.pop();

            CurRow = CurSet.first;
            CurCol = CurSet.second;

            // 네 방향 조사하기
            for (int k = 0; k < 4; k++)
            {
                NxtRow = CurRow + dx[k];
                NxtCol  = CurCol + dy[k];

                // 범위 검사
                if (NxtRow < 0 || NxtRow >= N || NxtCol < 0 || NxtCol >= N)
                    continue;

                // 벽 검사
                if (TestMaps[NxtRow][NxtCol] == 1)
                    continue;

                // 방문 여부 검사
                if (CheckMaps[NxtRow][NxtCol])
                    continue;

                // 거리 세팅
                DistMaps[NxtRow][NxtCol] = DistMaps[CurRow][CurCol] + 1;

                // 방문 체크
                CheckMaps[NxtRow][NxtCol] = true;


                // 전체 확산 여부 조사
                if (TestMaps[NxtRow][NxtCol] == 0)
                {
                    CNonVirusNum -= 1;

                    TestMaps[NxtRow][NxtCol] = 2;

                    // 바이러스가 모두 퍼지게 된 상황
                    if (CNonVirusNum == 0)
                    {
                        AllSpread = true;
                        break;
                    }
                }

                // 바이러스 세팅
                TestMaps[NxtRow][NxtCol] = 2;

                // 큐에 추가
                queue.push(std::make_pair(NxtRow, NxtCol));
            }

            if (AllSpread)
                break;
        }

        // 전체 퍼지지 않은 경우 세팅 X
        if (!AllSpread)
            continue;

        // 해당 세트에서의 최대 시간 구하기 ( 총 바이러스를 퍼뜨린 시간 )
        int PartMax = 0;

        for (int row = 0; row < N; row++)
        {
	        for (int col = 0; col < N; col++)
	        {
                // 퍼지지 않은 부분이 존재한다는 것
                if (TestMaps[row][col] == 0)
                {
                    AllSpread = false;
                    break;
                }
                if (DistMaps[row][col] > PartMax)
                    PartMax = DistMaps[row][col];
	        }
        }

        // 전체 퍼지지 않은 경우 세팅 X ( 혹시나 해서 )
        if (!AllSpread)
            continue;

        // 전체 최소값과 비교하기
        if (PartMax < ANSWER)
        {
            ANSWER = PartMax;
        }
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    cin >> N >> M;

    // Map 세팅
    Maps = std::vector<std::vector<int>>(N, std::vector<int>(N, 0));
    TestMaps = std::vector<std::vector<int>>(N, std::vector<int>(N, 0));
    CheckMaps = std::vector<std::vector<bool>>(N, std::vector<bool>(N, false));
    DistMaps = std::vector<std::vector<int>>(N, std::vector<int>(N, 0));

    // 입력 세팅
    char Input;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> Input;
            Maps[i][j] = (int)(Input - '0');
        }
    }

    // 바이러스 목록 구하기 + 바이러스 아닌 녀석들 목록 구하기 
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // 바이러스라면 
            if (Maps[i][j] == 2)
                Virus.push_back(std::make_pair(i, j));

            else if (Maps[i][j] == 0) // 벽도 아니고, 바이러스도 아니고
                NonVirusNum += 1;
        }
    }

    // 만약 이미 모두 퍼져있다면
    if (NonVirusNum == 0)
    {
        cout << 0;
        exit(0);
    }

    MakeVirusSet((int)Virus.size());

    SetVirus();

    if (ANSWER == INF)
        cout << -1;
    else
        cout << ANSWER;

    return 0;
}


