// https://school.programmers.co.kr/learn/courses/30/lessons/42891#
// 음식 시간 + 음식 번호 묶어서 정렬 (기준 : 음식 시간 단위)

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(pair<int, int>& p1, pair<int, int>& p2)
{
    return p1.second < p2.second;
}

int solution(vector<int> food_times, long long k) {
    
    // food, idx 정보 기준으로 sort
    vector<pair<int,int>> vecFoodInfo;
    vecFoodInfo.reserve(food_times.size());
    
    int preTime = 0;
    int foodN   = food_times.size();
    
    for (int i = 0; i < food_times.size(); ++i)
        vecFoodInfo.push_back(make_pair(food_times[i], i + 1));
    
    sort(vecFoodInfo.begin(), vecFoodInfo.end());
    
    for (int i = 0; i < vecFoodInfo.size(); ++i, --foodN)
    {
        int curFoodTime = vecFoodInfo[i].first;
        
        if (curFoodTime - preTime == 0)
            continue;
        
        long long decN = (curFoodTime - preTime) * foodN;
        
        // cout << "k - decN : " << k - decN << endl;
        
        if (k - decN >= 0)
        {
            k -= decN;
            preTime = curFoodTime;
            
            /*
            cout << "cur K : " << k << endl;
            cout << endl;
            */
        }
        else 
        {
            k %= foodN;
            
            // 뒷부분 이제 idx 기준으로 정렬하기 
            sort(vecFoodInfo.begin() + i, vecFoodInfo.end(), compare);
            
            /*
            for (int j = i; j < vecFoodInfo.size(); ++j)
                cout << vecFoodInfo[j].second << ".";
            cout << endl;
            
            cout << "i, k : " << i << "," << k << endl;
            cout << endl;
            */
            
            return vecFoodInfo[i + k].second;
        }
    }
    
    int answer = -1;
    
    return answer;
}