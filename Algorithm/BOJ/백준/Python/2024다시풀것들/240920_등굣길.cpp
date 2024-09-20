// https://school.programmers.co.kr/learn/courses/30/lessons/42898

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) 
{
    // m : 열, n : 행
    int answer = 0;
    vector<vector<int>> dps;
    vector<vector<bool>> visit;
    dps.resize(n, vector<int>(m, 0));
    visit.resize(n, vector<bool>(m, true));
    
    for (const vector<int>& puddle : puddles)
    {
        int c = puddle[0] - 1;  // 열
        int r = puddle[1] - 1;  // 행
        
        // 실제 인자로 들어오는 내용은, 행,열 반대
        if (r >= n) continue;
        if (c >= m) continue;
        
        visit[r][c] = false;
    }
    
    dps[0][0] = 1;
    
    for (int r = 0; r < n; ++r)
    {
        for (int c = 0; c < m; ++c)
        {
            if (visit[r][c] == false) continue;
            if (r == 0 && c == 0) continue;
            if (r == 0)
                dps[r][c] = dps[r][c-1]; 
            else if (c == 0)
                dps[r][c] = dps[r-1][c]; 
            else
                dps[r][c] = (dps[r-1][c] + dps[r][c-1]) % 1000000007; 
        }
    }
    
    return dps[n-1][m-1];
}