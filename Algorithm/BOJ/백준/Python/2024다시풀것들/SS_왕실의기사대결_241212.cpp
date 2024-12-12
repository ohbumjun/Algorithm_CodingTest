// https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=2&pageSize=10


#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <tuple>
#include <unordered_map>
#include <cassert>
using namespace std;

// #define DEBUG 1
// #define SINGLE_DEBUG 1

int L, N, Q;

int dRow[] = {-1, 0, 1, 0 }; // 상, 오른쪽, 아래쪽, 왼쪽
int dCol[]  = {0, 1, 0, -1 }; 

struct Knight
{
    int row = -1;
    int col = -1;
    int height;
    int width = 0;
    int health = 0;
};

// 0 : 빈칸
// 1 : 함정
// 2 : 벽
vector<vector<int>> board;
unordered_map<int, Knight> knights;
vector<int> initHealths;

void Input()
{
   cin >> L >> N >> Q;

   board.resize(L + 2, vector<int>(L + 2, 0));
   initHealths.resize(N + 1);

   // ex) L : 4 -> 가로, 세로 총 6
   // 벽 세팅
   for (int r = 0; r < L + 2; ++r)
   {
       board[r][0] = 2;
       board[r][L + 1] = 2;
   }
   for (int c = 0; c < L + 2; ++c)
   {
       board[0][c] = 2;
       board[L + 1][c] = 2;
   }

   // 체스판 정보 받아들이기
   for (int r = 1; r < L + 1; ++r)
       for (int c = 1; c < L + 1; ++c)
		   cin >> board[r][c];

   for (int i = 0; i < N; i++)
   {
       int r, c, h, w, k;
       cin >> r >> c >> h >> w >> k;
       knights[i + 1] = {r, c, h, w, k};
       initHealths[i + 1] = k;
   }
}

void pushKnight(int idx, int dir)
{
    queue<int> knightsQueue; // push 할 knight 들의 목록
    set<int> pushedKnights; // 이미 push 된 knight 들의 목록

    knightsQueue.push(idx);
    pushedKnights.insert(idx);

    vector<int> damanges(N + 1, 0);

    while (!knightsQueue.empty())
    {
        int curKnight = knightsQueue.front();
        knightsQueue.pop();

        // push
        // 단, 벽을 만난다면, 애초에 아무런 처리를 안해줘도 된다.
        // 데미지를 입는다면 -> 이거는 나중에 아래에서 한꺼번에
        int nxtStRow = knights[curKnight].row + dRow[dir];
        int nxtStCol = knights[curKnight].col + dCol[dir];
        int height = knights[curKnight].height;
        int width = knights[curKnight].width;
        int nxtEdRow = nxtStRow + height;
        int nxtEdCol = nxtStCol + width;

        for (int r = nxtStRow; r < nxtEdRow; ++r)
        {
            for (int c = nxtStCol; c < nxtEdCol; ++c)
            {
                // 벽
                if (board[r][c] == 2)
                    return; // 아무것도 안하면 된다.
                // 데미지
                if (board[r][c] == 1)
                    damanges[curKnight]++;
            }
        }

        // 그 다음 knight 찾기
        for (const auto& knightInfo : knights)
        {
            int nxtKnight = knightInfo.first;
            const Knight& knight = knightInfo.second;

            if (pushedKnights.find(nxtKnight) != pushedKnights.end())
                continue;

            int stR = knight.row;
            int stC = knight.col;
            int height = knight.height;
            int width = knight.width;
            int edR = stR + height;
            int edC = stC + width;

            bool contain = false;

            if (nxtStRow <= edR - 1 && nxtStCol <= edC - 1 &&
                nxtEdRow - 1 >= stR && nxtEdCol - 1 >= stC)
                contain = true;
           
            if (contain == false)
                continue;

            knightsQueue.push(nxtKnight);
            pushedKnights.insert(nxtKnight);
        }
    }

    damanges[idx] = 0;
    
    for (const auto& curKnight : pushedKnights)
    {
        // 이동 처리하기
        knights[curKnight].row += dRow[dir];
        knights[curKnight].col += dCol[dir];

        // 데미지 처리하기
        int damange = damanges[curKnight];
        knights[curKnight].health -= damange;
        if (knights[curKnight].health <= 0)
            knights.erase(curKnight);
    }

}

void Solve()
{
    // L * L 크기 배열
    // 기사들은 자신의 마력으로 상대방을 밀칠 수 있다.
    // 각 기사 체력은 k

    // 1) 기사 이동
    // 상하좌우 한칸
    // - 기사에게 명령 가능
    // - 이동 위치에 다른 기사 있으면, 연쇄적으로 밀려남
    // - 단, 이동 방향에 벽이 있으면 이동 불가
    // - 체스판에서 사라진 기사는 이동 x

    // 2) 대결 대미지
    // - 밀려난 기사는 피해
    // - 피해 받은 만큼 체력 감소
    // - 남은 체력 이상 피해의 경우 체스판에서 사라짐
    // - 명령을 받은 기사는 피해 x
    // - 나머지 기사들은 모두 밀리고 나서 대미지
    // - 밀쳐진 위치에 함정 없으면 피해 x
    for (int q = 0; q < Q; q++)
    {
        // i 번 기사에게 방향 d 로 이동
        // i 번 기사는 이미 사라져 있을 수 있다.
        int i, d; 
        cin >> i >> d;

        if (knights[i].health == 0)
			continue;
        pushKnight(i, d);
    }

    int answer = 0;

    for (const auto& knightInfo : knights)
    {
        int nxtKnight = knightInfo.first;
        const Knight& knight = knightInfo.second;

		if (knight.health == 0)
			continue;
		answer += (initHealths[nxtKnight] - knight.health);
	}

    cout << answer << endl;
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
