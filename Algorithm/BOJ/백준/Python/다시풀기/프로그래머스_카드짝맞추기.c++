#include <string>
#include <vector>
#include <unordered_map>
#include <utility>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

#define INF int(1e9)

vector<vector<int>> board;
vector<int> card;
int dRow[] = {-1, 1, 0, 0};
int dCol[] = {0, 0, 1, -1};
int answer = INF;
int r,c;

// 목적지 까지의 최단 거리를 구하기
int bfs(int dest)
{
    bool check[4][4] = {false,};
    
    // 시작점
    queue<pair<pair<int, int>,int>> q;
    q.push({{r,c},0});
    
    check[r][c] = true;
    
    while (!q.empty())
    {
        int row = q.front().first.first;
        int col = q.front().first.second;
        int cnt = q.front().second;
        q.pop();
        
        if (board[row][col] == dest)
        {
            // 뒤집은 카드는, 0 으로 세팅해준다.
            board[row][col] = 0;
            
            // r, c, 정보를 계속 Update 시켜준다.(현재 커서 위치를 전역 변수로 세팅한 것)
            r = row, c = col;
            
            // + 1을 해주는 이유는 Enter 키 포함
            return cnt + 1;
        }
        
        // 4방향 탐색 (그냥 방향키를 누르는 경우)
        for (int i = 0; i < 4; ++i)
        {
            int nRow = row + dRow[i];
            int nCol = col + dCol[i];
            
            // 범위 검사
            if (nRow < 0 || nRow >= 4 || nCol < 0 || nCol >= 4)
                continue;
            if (check[nRow][nCol])
                continue;
            
            check[nRow][nCol] = true;
            q.push({{nRow, nCol}, cnt + 1});
        }
        
        // Ctrl + 방향키. 를 누르는 경우
        for (int i = 0; i < 4; ++i)
        {
            int nRow = row, nCol = col;
            
            // 앞면을 찾을 때 까지 특정 방향으로 계속 나아간다.
            while (nRow + dRow[i] >= 0 && nCol + dCol[i] >= 0 &&
                  nRow + dRow[i] < 4 && nCol + dCol[i] < 4)
            {
                nRow += dRow[i];
                nCol += dCol[i];
                
                if (board[nRow][nCol])
                    break;
            }
            
            // 해당 앞면 방문 고려 
            if (!check[nRow][nCol])
            {
                check[nRow][nCol] = true;
                q.push({{nRow, nCol}, cnt + 1});
            }
        }
    }
}

int solution(vector<vector<int>> Board, int stR, int stC) {

    // 1. 카드의 짝 만큼 순열.을 돌린다.
    // 2. 카드의 조합을 순서대로 찾아가면서, bfs 로 짝을 찾아 카드를 지운다.
    // 3. 최소가 나오는 경우를 찾아야 하므로, 모든 경우를 다 본다.
    
    // ex. 1,2,3 카드가 있다면
    // 순열이 (1,2,3) (1,3,2) (2,1,3) (2,3,1) (3,1,2) (3,2,1) 총 6개
    // 전역변수로, 현재 커서의 위치를 저장하면서, bfs 를 돌리면서
    // 두 카드 중 가까운 카드 > 먼 카드. 순으로 돌면서, 총 몇번의 명령어를 입력했는지 확인한다.
    
    // 카드 종류 최대 6개 (1 ~ 6)
    bool card_check[7] = {false,};
    
    for (int i = 0; i < Board.size(); i++)
    {
        for (int j = 0; j < Board[0].size(); j++)
        {
            // 앞면이라면
            if (Board[i][j])
            {
                // 카드 존재 여부 세팅
                card_check[Board[i][j]] = true;
            }
        }
    }
    
    // 존재하는 카드 목록을 확인한다.
    // 반드시 오름차순 형태로 넣어줘야 한다.
    for (int i = 1; i < 7; ++i)
        if (card_check[i])
            card.push_back(i);
    
    do
    {
        board = Board;
        r = stR, c = stC;
        int tmp = 0;
        for (int i = 0; i < card.size(); ++i)
        {
            // 특정 카드까지의 거리를 구한다.
            tmp += bfs(card[i]);
            tmp += bfs(card[i]);
        }
        answer = min(answer, tmp);
    }while (next_permutation(card.begin(), card.end()));
    
    return answer;
}