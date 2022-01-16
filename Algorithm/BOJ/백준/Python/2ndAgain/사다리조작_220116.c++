// https://www.acmicpc.net/problem/15684

// 1번째 풀이 : 모든 가능한 조합 구하기 ( 완전 탐색 ) + 각각에서의 시뮬레이션 => 시간 초과
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

int COL, NUM_ROW, ROW; // 

std::vector<std::vector<bool>> m_Maps;
std::vector<pair<int, int>> g_vecAreaIdxs;

int FindPath(int Start, std::vector<std::vector<bool>>& Maps)
{
    // cout << "Start : " << Start + 1 << endl;
    bool WentRight = false;
	for (int row = 0; row < ROW; row++)
	{
        WentRight = false;

		// 해당 Idx 블록이 true 라면, 오른쪽 이동 ( idx ++ )
        if (Start + 1 <= COL)
        {
	        if (m_Maps[row][Start])
	        {
                WentRight = true;
                Start += 1;
               //  cout << "Go Right : " << Start << ", Row : " << row << endl;
	        }
        }

        // 해당 Idx 왼쪽 블록이 true 라면 , 왼쪽 이동
        if (Start - 1 >= 0 && !WentRight)
        {
            if (m_Maps[row][Start - 1])
            {
                Start -= 1;
                // cout << "Go Left : " << Start << ", Row : " << row << endl;
            }
        }
	}
    return Start;
}

void PrintAllMap()
{
    for (int r = 0; r < ROW; r++)
    {
        for (int c = 0; c < COL; c++)
        {
            cout << m_Maps[r][c] << ".";
        }
        cout << endl;
    }

}

// 조합 만들기 : 단, 가로선이 연속이어서는 안된다.
void MakeComb(int Index, int TotalNum, int CurCount, std::vector<pair<int, int>>& AreaIdx)
{
	if (CurCount == TotalNum)
	{
        bool IsContinuous = false;

		// 연속인지 판단
        for (size_t  i = 0; i < AreaIdx.size() - 1; i++)
        {
            int curRow = AreaIdx[i].first;
            int nxtRow = AreaIdx[i+1].first;
            if (curRow == nxtRow)
            {
                IsContinuous = true;
                break;
            }
        }

        if (IsContinuous)
        {
            return;
        }


        // 연속이 아니라면, 해당 idx 들을 m_Maps에서 true로 만들고
        for (size_t i = 0; i < AreaIdx.size(); i++)
        {
            int curRow = AreaIdx[i].first;
            int curCol = AreaIdx[i].second;
            m_Maps[curRow][curCol] = true;
        }

        // 만약 모두 자기에 도달하면 해당 값 출력
        std::vector<int> result;
        result.resize(COL + 1);

        for (int i = 0; i <= COL; i++)
        {
            result[i] = FindPath(i, m_Maps);
        }

        bool IsAllSame = true;
        for (int i = 0; i < result.size(); i++)
        {
	        if (result[i] != i)
	        {
                IsAllSame = false;
                break;
	        }
        }

        // 그리고 시스템 종료
        if (IsAllSame)
        {
            // PrintAllMap();
            cout << TotalNum;
            exit(1);
        }

        // 그게 아니라면 다시 m_Maps 를 false로
        for (size_t i = 0; i < AreaIdx.size(); i++)
        {
            int curRow = AreaIdx[i].first;
            int curCol = AreaIdx[i].second;
            m_Maps[curRow][curCol] = false;
        }
	}

    // 조합 만들기 
    int Size = (int)g_vecAreaIdxs.size();
    for (int i = Index; i < Size; i++)
    {
        AreaIdx.push_back(g_vecAreaIdxs[i]);
        MakeComb(i + 1, TotalNum, CurCount + 1, AreaIdx);
        AreaIdx.pop_back();
    }
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("input_C.txt", "r", stdin); 

    cin >> COL >> NUM_ROW >> ROW; // 세로선 , 가로선, 세로선마다 가로선 놓을 수 있는 위치 개수 

    // 세로선 개수 - 1개의 열
    // 가로선 개수만큼의 행
    m_Maps = std::vector<std::vector<bool>>(ROW, std::vector<bool>(COL, false));

    // 입력 세팅
    int Row = -1, Col = -1;
    for (int i = 0; i < NUM_ROW; i++)
    {
        cin >> Row >> Col;
        Row -= 1; Col -= 1;
        m_Maps[Row][Col] = true;
    }

    // g_vecAreaIdxs 채우기
    g_vecAreaIdxs.reserve(COL * ROW);
    for (int row = 0; row < ROW; row++)
    {
	    for (int col = 0; col < COL; col++)
	    {
            if (m_Maps[row][col])
                continue;
            g_vecAreaIdxs.push_back(make_pair(row, col));
	    }
    }

    // 최초 정보 조사하기
    std::vector<int> result;
    result.resize(COL + 1);

    for (int i = 0; i <= COL; i++)
    {
        result[i] = FindPath(i, m_Maps);
    }

	bool IsAllSame = true;

    for (int i = 0; i < result.size(); i++)
    {
        if (result[i] != i)
        {
            IsAllSame = false;
            break;
        }
    }
    if (IsAllSame)
    {
        cout << 0;
        exit(1);
    }

    for (int TotNum = 1; TotNum <= 3; TotNum++)
    {
        vector<pair<int, int>> vecAreaIdx = {};
        MakeComb(0, TotNum, 0, vecAreaIdx);
    }

    cout << -1;

    return 0;
}



// 2번째 방법 : dfs 활용
// 원ㄹ : 계속 아래로 내려가거나, 계속 오른쪽으로만 가겠다
// 그래서 dfs 안에서 그다음 검사 시작을 넘겨준 인자 부분부터 시작하는 것이다. 

#include<iostream>
#include<algorithm>
using namespace std;
 
int N, M, H;
int map[32][12];
int ans;
 
bool go() {
    for (int X = 1; X <= N; X++) {
        int ch = X;
        for (int Y = 1; Y <= H; Y++) {
            if (map[Y][ch] == 1) {
                ch++;
            }
            else if (map[Y][ch - 1] == 1) {
                ch--;
            }
        }
        if (ch != X) {
            return false;
        }
    }
    return true;
}
 
void dfs(int dep,int x,int y) {
    if (ans <= dep) return;
    if (go()) {
        ans = dep;
        return;
    }
    if (dep == 3) return;
 
    // 아래로 가겠다 !! : row부터 검사 
    for (int Y = y; Y <= H; Y++) {
        for (int X = 0; X <= N; X++) {
            /*
            오른쪽으로 가겠다 ! : col부터 검사
            for (int X = x; X <= N; X++) {
                for (int Y = 0; Y <= H; Y++) {
            */
            if (map[Y][X] == 0 && map[Y][X - 1] == 0 && map[Y][X + 1] == 0) {
                map[Y][X] = 1;
                dfs(dep + 1, X, Y);
                map[Y][X]=0;
            }
        }
        x = 1;
    }
}
 
int main() {
    ans = 10000000;
    cin >> N >> M >> H;
    for (int m = 0; m < M; m++) {
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
    }
    ans = 4;
    dfs(0,1,1);
    if (ans == 4)
        cout << "-1";
    else
        cout << ans;
}
