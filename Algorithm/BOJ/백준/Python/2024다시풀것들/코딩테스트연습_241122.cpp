// https://school.programmers.co.kr/learn/courses/30/lessons/118668

#include <string>
#include <vector>
#define MX 999999999
using namespace std;
// dp의 최대 index 값은 150(req)+30(rwd)이다.
// 150으로 줘서 segmentation fault가 발생했다.
vector<vector<int>> dp(201, vector<int>(201, MX));

int solution(int alp, int cop, vector<vector<int>> problems) 
{
    int answer = 0, alp_mx=0, cop_mx=0;
    
    for(int i=0; i<problems.size(); i++)
    {
        alp_mx=max(alp_mx, problems[i][0]);
        cop_mx=max(cop_mx, problems[i][1]);
    }
    
    // 예외 처리
    alp=min(alp, alp_mx), cop=min(cop, cop_mx);
    dp[alp][cop] = 0;
    int x_idx, y_idx;
    
    for(int i=alp; i<=alp_mx; i++)
    {
        for(int j=cop; j<=cop_mx; j++)
        {
        	// 예외 처리
            x_idx=min(i+1, alp_mx), y_idx=min(j+1, cop_mx);
            
            // CASE 1. 알고력 1 증가
            dp[x_idx][j]=min(dp[x_idx][j], dp[i][j]+1);
            
            // CASE 2. 코딩력 1 증가
            dp[i][y_idx]=min(dp[i][y_idx], dp[i][j]+1);
            
            // CASE 3. 문제 풀이
            // for(int k=0; k<problems.size(); k++){
            for (const vector<int>& prob : problems)
            {
                int alp_req=prob[0], cop_req=prob[1];
                int alp_rwd=prob[2], cop_rwd=prob[3], cost=prob[4];
            
                if(i<alp_req || j<cop_req) continue;
                
                // 예외 처리
                x_idx=min(i+alp_rwd, alp_mx);
                y_idx=min(j+cop_rwd, cop_mx);
                
                dp[x_idx][y_idx]=min(dp[x_idx][y_idx], dp[i][j]+cost);
            }
        }
    }
    return answer=dp[alp_mx][cop_mx];
}