https://school.programmers.co.kr/learn/courses/30/lessons/43105?language=cpp

#include <string>
#include <vector>
#include <iostream>

using namespace std;

// dp[idx] : idx 번째 칸 까지 거쳐간 최대 숫자값
int dp[500][500];

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    
    for (int level = 0; level < triangle.size(); ++level)
    {
        const vector<int>& nums = triangle[level];
        
        // 각 숫자 기준으로, 자기까지 거쳐온 최대값 ? 을 구해야 하는 건가 ?
        // 그러면 일단 dp 를 2 x 2 배열로 만들어야 겠다.
        for (int idx = 0; idx < nums.size(); ++idx)
        {
            int maxVal = dp[level][idx];
            
            // 가장 첫번째 단계
            if (level == 0)
            {
                dp[level][idx] = nums[idx];
                continue;
            }
            
            if (idx > 0) maxVal = max(maxVal, dp[level - 1][idx - 1] + nums[idx]);
            
            maxVal = max(maxVal, dp[level - 1][idx] + nums[idx]);
            
            dp[level][idx] = maxVal;
            
            if (level == triangle.size() - 1) answer = max(answer, dp[level][idx]);
        }
    }
    
    /*
    for (int level = 0; level < triangle.size(); ++level)
    {
        const vector<int>& nums = triangle[level];
        
        for (int n : nums) cout << n << ".";
        cout << endl;
    }
    */
    
    return answer;
}