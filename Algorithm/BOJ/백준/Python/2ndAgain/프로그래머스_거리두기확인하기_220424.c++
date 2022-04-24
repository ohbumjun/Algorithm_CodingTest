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