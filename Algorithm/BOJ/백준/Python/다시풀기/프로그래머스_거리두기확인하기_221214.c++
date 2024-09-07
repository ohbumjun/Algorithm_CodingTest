#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <iostream>

// 첫번째 풀이  : bfs

#include <string>
#include <vector>
#include <queue>
#include <tuple>
#include <iostream>

using namespace std;

int dRow[4] = {-1, 1, 0,  0};
int dCol[4] = {0 , 0, 1, -1};

vector<int> solution(vector<vector<string>> places) {
    
    // 방문 체크 배열 세팅
    std::vector<std::vector<bool>> vecVisited;
    vecVisited.reserve(5);
    
    for (int i = 0; i < 5; ++i)
    {
        vecVisited.push_back(std::vector<bool>(5, false));        
    }
    
    // 결과 vector
    vector<int> answer(5, 0);
        
    // 1) 각각의 대기실 별로
    for (int i = 0; i < 5; ++i)
    {
        bool pass = true;
        
        // 2) 각 자리에서 bfs 를 실행한다.
        for (int row = 0; row < 5; ++row)
        {
            for (int col = 0; col < 5; ++col)
            {
                // 응시자 자리인 경우만 조사한다.
                if (places[i][row][col] != 'P')
                    continue;
                
                // check 배열 초기화
                for (int vR = 0; vR < 5; ++vR)
                {
                    for (int vC = 0; vC < 5; ++vC)
                    {
                        vecVisited[vR][vC] = false;
                    }
                }
                
                // bfs 를 위한 queue 세팅
                std::queue<std::tuple<int, int, int>> bfsQueue;
                
                bfsQueue.push(std::make_tuple(0, row, col));
                
                vecVisited[row][col] = true;
                
                while (!bfsQueue.empty())
                {
                    std::tuple<int, int, int> curInfo = bfsQueue.front();
                    
                    bfsQueue.pop();
                    
                    int curDist = std::get<0>(curInfo);
                    int curRow = std::get<1>(curInfo);
                    int curCol = std::get<2>(curInfo);
                    
                    // 거리가 2 이라면, break
                    if (curDist >= 2)
                        break;
                    
                    // 4방향 탐색
                    for (int k = 0; k < 4; ++k)
                    {
                        int nRow = curRow + dRow[k];
                        int nCol = curCol + dCol[k];
                        
                        // 범위를 벗어난다면 X
                        if (nRow >= 5 || nRow < 0 || nCol >= 5 || nCol < 0)
                            continue;
                        
                        // 해당 위치가 파티션이면, 조사할 필요없다. 어차피 거리이내 --> 파티션 아닐 때만 dfs 계속 진행
                        if (places[i][nRow][nCol] == 'X')
                            continue;
                        
                        // 이미 방문했다면 X
                        if (vecVisited[nRow][nCol])
                            continue;
                        
                        // 1) 현재 자리가 또 다른 응시자이고
                        // 2) 해당 자리까지 거리가 2 이하 이며
                        // 3) 현재 자리가 파티션이 아닌 경우 --> 허용 X
                        if (places[i][nRow][nCol] == 'P')
                        {
                            pass = false;
                            break;
                        }
                        
                        // 그게 아니라면, 계속 bfs 진행
                        vecVisited[nRow][nCol] = true;
                        
                        bfsQueue.push(std::make_tuple(curDist + 1, nRow, nCol));
                    }
                    if (!pass)
                        break;
                }
                if (!pass)
                    break;
            }
            if (!pass)
                break;
        }

        // 3) 당연히, 방문 여부에 대한 정보를 담은 2차원 배열을, 각 대기실 별로 세팅하고
        answer[i] = pass ? 1 : 0;

    }
    
    return answer;
}

// 2번째 풀이 : 다른 접근 방식

using namespace std;

int dRow[4] = {-1, 1, 0,  0};
int dCol[4] = {0 , 0, 1, -1};

vector<int> solution(vector<vector<string>> places) {
    
    // 방문 체크 배열 세팅
    std::vector<std::vector<int>> vecDist;
    vecDist.reserve(5);
    
    for (int i = 0; i < 5; ++i)
    {
        vecDist.push_back(std::vector<int>(5, 0));        
    }
    
    // 결과 vector
    vector<int> answer(5, 0);
        
    // 1) 각각의 대기실 별로
    for (int i = 0; i < 5; ++i)
    {
        bool pass = true;
        
        // vecVisited 배열 0 값으로 초기화
        for (int row = 0; row < 5; ++row)
        {
            for (int col = 0; col < 5; ++col)
            {
                vecDist[row][col] = 0;
            }
        }
        
        // 순회 
        // 1) 사람 주변 -1
        // 2) 파티션 +10 (꼭 10 일 필요는 없다. +3 이상이면 된다.)
        // vecVisited 배열 0 값으로 초기화
        for (int row = 0; row < 5; ++row)
        {
            for (int col = 0; col < 5; ++col)
            {
                if (places[i][row][col] == 'X')
                    vecDist[row][col] = 10;
                
                if (places[i][row][col] == 'P')
                {
                    vecDist[row][col] -= 1;
                    
                    // 주변 4방향 -1
                    for (int k = 0; k < 4; ++k)
                    {
                        int nRow = row + dRow[k];
                        int nCol = col + dCol[k];
                        
                        if (nRow < 0 || nRow >= 5 || nCol < 0 || nCol >= 5)
                            continue;
                        
                        vecDist[nRow][nCol] -= 1;
                    }
                }
            }
        }
    
        
        
        // 다시 순회 --> -2 이하의 숫자가 하나라도 있다면 안지킨 것
        for (int row = 0; row < 5; ++row)
        {
            for (int col = 0; col < 5; ++col)
            {
                if (vecDist[row][col] <= -2)
                {
                    pass = false;
                    break;
                }
            }
            if (!pass)
                break;
        }
        
        // 3) 당연히, 방문 여부에 대한 정보를 담은 2차원 배열을, 각 대기실 별로 세팅하고
        answer[i] = pass ? 1 : 0;
    }
    
    return answer;
}