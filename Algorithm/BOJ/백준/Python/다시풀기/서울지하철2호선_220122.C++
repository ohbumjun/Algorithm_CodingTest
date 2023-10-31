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

int N;
std::vector<std::vector<int>> Graph;
std::vector<bool> Cycle;
std::vector<int> Distance;

int FindCycle(int StNode, int PrevNode, std::vector<bool>& vecCheck, int& CycleNode)
{
	// 싸이클에 해당하는 점을 찾음 (이미 방문한적이 있음)
    if (vecCheck[StNode])
    {
        CycleNode = StNode;

        // 싸이클 포함 시키기
        Cycle[StNode] = true;

        // 거리 0
        Distance[StNode] = 0;

        return 1; // 싸이클 찾았다 !
    }

    // 방문 처리
    vecCheck[StNode] = true;

    // 그 다음 Path 상에서 Cycle을 찾음
    int Size    = Graph[StNode].size();
    int Result = -1, NxtNode = -1;

    for (int i = 0; i < Size; i++)
    {
        NxtNode = Graph[StNode][i];

        if (NxtNode == PrevNode)
            continue;

        Result = FindCycle(Graph[StNode][i], StNode, vecCheck, CycleNode);

        // 싸이클을 찾았다면
        if (Result == 1)
        {
	        // 싸이클의 시작, 끝의 점이라면
	        if (StNode == CycleNode)
                return 2;

            // 그게 아니고, 싸이클 찾은 이후 계속 돌아오고 있다면
            // Cycle 목록에 해당 정점 정보를 추가한다.
            Cycle[StNode] = true;

            // 거리 0
            Distance[StNode] = 0;

            return 1;

        }
        // 싸이클 처리를 끝나고 돌아오는 경우
        if (Result == 2)
            return 2;
    }

    // 방문 해제 
    vecCheck[StNode] = false;

    // 계속 찾고 있다
    return -1;
}

void CalculateDist(int StNode, int PrevNode, int InitNode, int Count)
{
	if (Cycle[StNode])
	{
        if (Distance[InitNode] > Count)
			Distance[InitNode] = Count;
        return;
	}

    int Size = Graph[StNode].size();
    int NxtNode = -1;
    for (int i = 0; i < Size; i++)
    {
        NxtNode = Graph[StNode][i];

        if (NxtNode == PrevNode)
            continue;

        CalculateDist(NxtNode, StNode, InitNode, Count + 1);
    }
    
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin);

    cin >> N;

    // Graph, Cycle 세팅 
    Graph.resize(N+1);

    for (int i = 0; i < N; i++)
        Graph[i].reserve(N);

    Cycle = std::vector<bool>(N + 1, false);
    Distance = std::vector<int>(N + 1, INF);

    // Input 값 세팅
    int St = -1, Ed = -1;
    for (int i = 0; i < N; i++)
    {
        cin >> St >> Ed;
        Graph[St].push_back(Ed);
        Graph[Ed].push_back(St);
    }

    // 싸이클 찾기
    std::vector<bool> vecCheck = std::vector<bool>(N+1, false);
    int CycleNode = -1;

    FindCycle(1, -1, vecCheck, CycleNode);

    // 싸이클 출력
    // for (const auto& elem : Cycle)
    //    cout << elem << ". ";

    // 거리 출력
    for (int i = 1; i <= N; i++)
    {
        if (Cycle[i])
            cout << 0 << " ";
        else
        {
            int StNode = i;
            CalculateDist(StNode, -1, StNode, 0);
            cout << Distance[StNode] << " ";
        }
    }
    
    
    return 0;
}


